-- DEBRIS-FIELD GAME — its own database (Eric 2026-10-10: kept separate from Quavara so the game can be sold or
-- licensed later). The ONLY link to Quavara is the player's QCID, carried in a signed game pass (auth_link.py).
-- Nothing here references a Quavara table. Idempotent: safe to run again.
--
-- v2 (2026-10-11, Eric): somewhere to keep everything a player owns (resources, blueprints, ships, ship parts, tools,
-- and kinds still to come), credits with a full paper trail, and the market's orders and trades.
--   · Nothing is unlimited: every place that holds goods has a size.
--   · A place is a row in `locations`, so a colony on the new Earth is just another place (kind 'colony_storage').
--   · Credits exist only inside the game. They never come from real money and never turn into money or Quavara credits.

-- Numbers we can tune while the game is live. Values marked SAMPLE are placeholders until Eric sets them.
CREATE TABLE IF NOT EXISTS settings (
  key   TEXT PRIMARY KEY,
  value NUMERIC NOT NULL,
  note  TEXT
);
INSERT INTO settings(key, value, note) VALUES
  ('start_credits',      5000, 'SAMPLE: credits the Starship bank pays a new player (by career, later)'),
  ('cargo_m3_start',       12, 'SAMPLE: each player''s space in the Starship''s cargo hold, cubic metres (whole hold est. ~34,000 m³)'),
  ('quarters_m3',           4, 'SAMPLE: room for personal possessions in a player''s Private Quarters, cubic metres'),
  ('lockbox_m3',         0.05, 'SAMPLE: the lockbox in the filing drawer, cubic metres'),
  ('hangar_slots_start',    1, 'ships a new player can keep at the Starship'),
  ('bank_bid_gap_pct',     10, 'the bank''s standing bid sits this many percent under the last price')
ON CONFLICT (key) DO NOTHING;

CREATE TABLE IF NOT EXISTS players (
  id           BIGSERIAL PRIMARY KEY,
  qcid         TEXT UNIQUE NOT NULL,             -- the Quavara account id; a buyer would swap this for their own login
  display_name TEXT,
  created_at   TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Every kind of thing in the game. A new kind of thing is a new row here, not a new table.
--   base_unit 'g'    : kept as an amount (resources), in grams so collected pieces add up exactly
--   base_unit 'each' : counted (blueprint copies)
--   unique_items     : every one is its own row in `items` with its own details (ships, parts, tools)
--   trade_unit       : how many base units make one unit on the market (1000 g = 1 kg)
-- A blueprint design is its own item type; a copy of it is owned forever and builds as many as you like (Eric 10-10).
CREATE TABLE IF NOT EXISTS item_types (
  code           TEXT PRIMARY KEY,
  kind           TEXT NOT NULL CHECK (kind IN ('resource','blueprint','ship','part','tool','other')),
  name           TEXT NOT NULL,
  base_unit      TEXT NOT NULL CHECK (base_unit IN ('g','each')),
  trade_unit     BIGINT NOT NULL DEFAULT 1 CHECK (trade_unit > 0),
  unique_items   BOOLEAN NOT NULL DEFAULT false,
  density_kg_m3  NUMERIC,                         -- resources: real density, for weight and storage space
  volume_m3_each NUMERIC,                         -- counted and unique things: space each one takes in storage
  tradeable      BOOLEAN NOT NULL DEFAULT true,
  designer_id    BIGINT REFERENCES players(id),   -- blueprints: who designed it
  stats          JSONB NOT NULL DEFAULT '{}'::jsonb,  -- what it does, shown as stats (no product art, Eric 10-10)
  created_at     TIMESTAMPTZ NOT NULL DEFAULT now()
);
INSERT INTO item_types(code, kind, name, base_unit, trade_unit, density_kg_m3) VALUES
  ('iron',    'resource', 'Iron ore', 'g', 1000,  5150),
  ('copper',  'resource', 'Copper',   'g', 1000,  8960),
  ('silver',  'resource', 'Silver',   'g', 1000, 10490),
  ('gold',    'resource', 'Gold',     'g', 1000, 19300),
  ('diamond', 'resource', 'Diamond',  'g', 1000,  3510)
ON CONFLICT (code) DO NOTHING;
INSERT INTO item_types(code, kind, name, base_unit, unique_items, tradeable, stats) VALUES
  ('ship-starter', 'ship', 'Starter prospector', 'each', true, false,
   '{"hold_m": [1.6, 1.2, 1.0], "scanner": "Mk I"}'::jsonb)
ON CONFLICT (code) DO NOTHING;

-- Accounts hold credits: one per player, plus the game's own. The mint issues credits (starting credits), so its balance
-- goes below zero by exactly what it has issued; the bank trades; the sink is where spent credits leave the economy.
-- Across every account, credits + held always add up to zero. That is the audit (store.audit()).
CREATE TABLE IF NOT EXISTS accounts (
  id           BIGSERIAL PRIMARY KEY,
  kind         TEXT NOT NULL CHECK (kind IN ('player','bank','mint','sink')),
  player_id    BIGINT UNIQUE REFERENCES players(id) ON DELETE CASCADE,
  credits      BIGINT NOT NULL DEFAULT 0,
  held_credits BIGINT NOT NULL DEFAULT 0 CHECK (held_credits >= 0),   -- set aside for bids waiting on the market
  CHECK (kind = 'mint' OR credits >= 0),
  CHECK ((kind = 'player') = (player_id IS NOT NULL))
);
CREATE UNIQUE INDEX IF NOT EXISTS accounts_one_system ON accounts(kind) WHERE kind <> 'player';
INSERT INTO accounts(kind) VALUES ('bank'), ('mint'), ('sink') ON CONFLICT DO NOTHING;

-- The paper trail: every credit that moves is one row. Append-only.
CREATE TABLE IF NOT EXISTS credit_ledger (
  id           BIGSERIAL PRIMARY KEY,
  at           TIMESTAMPTZ NOT NULL DEFAULT now(),
  from_account BIGINT NOT NULL REFERENCES accounts(id),
  to_account   BIGINT NOT NULL REFERENCES accounts(id),
  amount       BIGINT NOT NULL CHECK (amount > 0),
  reason       TEXT NOT NULL,                     -- 'start', 'trade', 'fuel', 'upgrade', 'blueprint_print', ...
  ref          JSONB NOT NULL DEFAULT '{}'::jsonb,
  CHECK (from_account <> to_account)
);
CREATE INDEX IF NOT EXISTS credit_ledger_from ON credit_ledger(from_account, at DESC);
CREATE INDEX IF NOT EXISTS credit_ledger_to   ON credit_ledger(to_account, at DESC);

-- Ships. Each ship is also a unique item (below), so it can be owned, stored and one day traded like anything else.
CREATE TABLE IF NOT EXISTS ships (
  id         BIGSERIAL PRIMARY KEY,
  player_id  BIGINT NOT NULL REFERENCES players(id) ON DELETE CASCADE,
  hull       TEXT NOT NULL DEFAULT 'starter',
  hold_l     NUMERIC(6,3) NOT NULL DEFAULT 1.6,   -- the hold in real interior metres (Eric 10-10: cubic space, true shapes)
  hold_w     NUMERIC(6,3) NOT NULL DEFAULT 1.2,
  hold_h     NUMERIC(6,3) NOT NULL DEFAULT 1.0,
  active     BOOLEAN NOT NULL DEFAULT true,       -- the ship the player is flying
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE UNIQUE INDEX IF NOT EXISTS ships_one_active ON ships(player_id) WHERE active;

-- Places that hold things. Every one has a size: cubic metres for goods, slots for ships.
--   starship_cargo   : the player's space in the Starship's cargo hold (resources wait here until they sell)
--   private_quarters : a small room of their own for personal possessions (furnished: Eric 10-11)
--   lockbox          : inside the quarters' filing drawer, for valuables
--   colony_storage   : on the new Earth, once the first colony is set up
CREATE TABLE IF NOT EXISTS locations (
  id             BIGSERIAL PRIMARY KEY,
  player_id      BIGINT NOT NULL REFERENCES players(id) ON DELETE CASCADE,
  kind           TEXT NOT NULL CHECK (kind IN ('starship_cargo','private_quarters','lockbox','hangar','ship_hold',
                                                  'colony_storage')),
  ship_id        BIGINT UNIQUE REFERENCES ships(id) ON DELETE CASCADE,   -- for a ship's hold
  parent_id      BIGINT REFERENCES locations(id) ON DELETE CASCADE,      -- a place inside a place (the lockbox in the quarters)
  name           TEXT NOT NULL,
  capacity_m3    NUMERIC(12,4),
  capacity_slots INT,
  created_at     TIMESTAMPTZ NOT NULL DEFAULT now(),
  CHECK (capacity_m3 IS NOT NULL OR capacity_slots IS NOT NULL),
  CHECK ((kind = 'ship_hold') = (ship_id IS NOT NULL))
);
CREATE UNIQUE INDEX IF NOT EXISTS locations_one_starship ON locations(player_id, kind) WHERE kind IN ('starship_cargo','private_quarters','lockbox','hangar');

-- Amounts of one kind of thing in one place (resources in grams, blueprint copies counted).
CREATE TABLE IF NOT EXISTS stacks (
  location_id BIGINT NOT NULL REFERENCES locations(id) ON DELETE CASCADE,
  item_code   TEXT NOT NULL REFERENCES item_types(code),
  qty         BIGINT NOT NULL DEFAULT 0 CHECK (qty >= 0),
  held        BIGINT NOT NULL DEFAULT 0 CHECK (held >= 0),   -- set aside for asks waiting on the market
  PRIMARY KEY (location_id, item_code)
);

-- The furnishings of every Private Quarters (Eric 10-11). Fixed in the room; not traded.
INSERT INTO item_types(code, kind, name, base_unit, unique_items, tradeable) VALUES
  ('furn-bed','other','Bed','each',true,false), ('furn-mirror','other','Mirror','each',true,false),
  ('furn-closet','other','Closet','each',true,false), ('furn-desk','other','Desk','each',true,false),
  ('furn-lamp','other','Lamp','each',true,false), ('furn-chair','other','Chair','each',true,false),
  ('furn-filing-drawer','other','Filing drawer','each',true,false), ('furn-lockbox','other','Lockbox','each',true,false)
ON CONFLICT (code) DO NOTHING;

-- One-of-a-kind things: each ship, each part with its condition or variation, each tool.
CREATE TABLE IF NOT EXISTS items (
  id          BIGSERIAL PRIMARY KEY,
  item_code   TEXT NOT NULL REFERENCES item_types(code),
  owner_id    BIGINT NOT NULL REFERENCES players(id) ON DELETE CASCADE,
  location_id BIGINT REFERENCES locations(id),
  ship_id     BIGINT UNIQUE REFERENCES ships(id) ON DELETE CASCADE,       -- when the item IS a ship
  fitted_to   BIGINT REFERENCES ships(id) ON DELETE SET NULL,             -- a part fitted to a ship
  held        BOOLEAN NOT NULL DEFAULT false,                             -- set aside on the market
  attrs       JSONB NOT NULL DEFAULT '{}'::jsonb,                         -- condition, variation, serial...
  created_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS items_owner ON items(owner_id);

-- Blueprints are open (Eric 10-11): the game does not ship a library of blueprints. This is only the structure a
-- player's design is written into: the design is an item type (designer_id, stats), and its recipe says what goes in,
-- what comes out, and how long it takes. Inputs are used up; the product takes its own (usually smaller) space.
-- Every design must obey the world's rules (real materials, sizes, time); those checks are still to be written.
CREATE TABLE IF NOT EXISTS recipes (
  id             BIGSERIAL PRIMARY KEY,
  blueprint_code TEXT NOT NULL REFERENCES item_types(code),
  output_code    TEXT NOT NULL REFERENCES item_types(code),
  output_qty     BIGINT NOT NULL CHECK (output_qty > 0),   -- base units (grams or count)
  minutes        INT NOT NULL CHECK (minutes > 0),         -- builds take time (Eric 10-10)
  created_at     TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE TABLE IF NOT EXISTS recipe_inputs (
  recipe_id BIGINT NOT NULL REFERENCES recipes(id) ON DELETE CASCADE,
  item_code TEXT NOT NULL REFERENCES item_types(code),
  qty       BIGINT NOT NULL CHECK (qty > 0),               -- base units used up
  PRIMARY KEY (recipe_id, item_code)
);

-- A play session. The server issues the seed, so later it can regenerate the same universe to check harvests.
CREATE TABLE IF NOT EXISTS sessions (
  id              UUID PRIMARY KEY,
  player_id       BIGINT NOT NULL REFERENCES players(id) ON DELETE CASCADE,
  seed            BIGINT NOT NULL,
  started_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
  last_collect_at TIMESTAMPTZ
);
CREATE INDEX IF NOT EXISTS sessions_player ON sessions(player_id, started_at DESC);

-- Every piece collected into a ship's hold, with its true shape. Mass comes from the material's real density on the
-- server, never from the client. When the ship unloads at the Starship, the piece becomes grams in storage.
CREATE TABLE IF NOT EXISTS cargo (
  id           BIGSERIAL PRIMARY KEY,
  player_id    BIGINT NOT NULL REFERENCES players(id) ON DELETE CASCADE,
  ship_id      BIGINT NOT NULL REFERENCES ships(id) ON DELETE CASCADE,
  session_id   UUID REFERENCES sessions(id) ON DELETE SET NULL,
  material     TEXT NOT NULL REFERENCES item_types(code),
  dim_a        NUMERIC(8,4) NOT NULL, dim_b NUMERIC(8,4) NOT NULL, dim_c NUMERIC(8,4) NOT NULL,
  volume_m3    NUMERIC(10,6) NOT NULL,
  box_m3       NUMERIC(10,6) NOT NULL,
  mass_kg      NUMERIC(12,3) NOT NULL,
  collected_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  unloaded_at  TIMESTAMPTZ                        -- NULL = still in the hold
);
CREATE INDEX IF NOT EXISTS cargo_aboard ON cargo(ship_id) WHERE unloaded_at IS NULL;

-- The market (spec §7): a live order book per item, open 24/7. Orders wait here; every trade is final and kept.
CREATE TABLE IF NOT EXISTS orders (
  id         BIGSERIAL PRIMARY KEY,
  account_id BIGINT NOT NULL REFERENCES accounts(id),
  item_code  TEXT NOT NULL REFERENCES item_types(code),
  side       TEXT NOT NULL CHECK (side IN ('buy','sell')),
  type       TEXT NOT NULL CHECK (type IN ('limit','instant')),
  price      BIGINT CHECK (price > 0),            -- credits per trade unit; NULL for instant orders
  qty        BIGINT NOT NULL CHECK (qty > 0),     -- in trade units (kg, copies)
  remaining  BIGINT NOT NULL CHECK (remaining >= 0),
  status     TEXT NOT NULL CHECK (status IN ('open','filled','partial','unfilled','cancelled')),
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  closed_at  TIMESTAMPTZ,
  CHECK (type = 'instant' OR price IS NOT NULL)
);
CREATE INDEX IF NOT EXISTS orders_book ON orders(item_code, side, price, id) WHERE status = 'open';
CREATE INDEX IF NOT EXISTS orders_account ON orders(account_id, created_at DESC);

CREATE TABLE IF NOT EXISTS trades (
  id         BIGSERIAL PRIMARY KEY,
  item_code  TEXT NOT NULL REFERENCES item_types(code),
  price      BIGINT NOT NULL CHECK (price > 0),
  qty        BIGINT NOT NULL CHECK (qty > 0),
  buy_order  BIGINT NOT NULL REFERENCES orders(id),
  sell_order BIGINT NOT NULL REFERENCES orders(id),
  buyer      BIGINT NOT NULL REFERENCES accounts(id),
  seller     BIGINT NOT NULL REFERENCES accounts(id),
  aggressor  TEXT NOT NULL CHECK (aggressor IN ('buy','sell')),
  at         TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS trades_item ON trades(item_code, at DESC);

-- Append-only record of everything else that changes a player's holdings (collecting, unloading, building...).
CREATE TABLE IF NOT EXISTS ledger (
  id        BIGSERIAL PRIMARY KEY,
  player_id BIGINT NOT NULL REFERENCES players(id) ON DELETE CASCADE,
  kind      TEXT NOT NULL,                        -- 'collect', 'unload', ...
  detail    JSONB NOT NULL DEFAULT '{}'::jsonb,
  at        TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS ledger_player ON ledger(player_id, at DESC);

-- Blueprint review (Eric 10-11). Players design; the game's team reviews. A designer fills in the blueprint form and
-- submits it. Reviewers can ask questions or request changes; the designer answers or changes it and resubmits; the
-- team approves or turns it down. Every submitted version is kept. Only approval turns a design into something that
-- can be built and sold.
CREATE TABLE IF NOT EXISTS blueprint_submissions (
  id          BIGSERIAL PRIMARY KEY,
  designer_id BIGINT NOT NULL REFERENCES players(id) ON DELETE CASCADE,
  title       TEXT NOT NULL,
  status      TEXT NOT NULL CHECK (status IN ('draft','submitted','changes_requested','approved','rejected','withdrawn')),
  form        JSONB NOT NULL,                     -- the designer's answers, latest version
  version     INT NOT NULL DEFAULT 0,             -- how many times it has been submitted
  item_code   TEXT REFERENCES item_types(code),   -- set on approval: the design that can now be built
  created_at  TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS blueprint_submissions_queue ON blueprint_submissions(status, updated_at);

CREATE TABLE IF NOT EXISTS blueprint_versions (
  submission_id BIGINT NOT NULL REFERENCES blueprint_submissions(id) ON DELETE CASCADE,
  version       INT NOT NULL,
  form          JSONB NOT NULL,
  submitted_at  TIMESTAMPTZ NOT NULL DEFAULT now(),
  PRIMARY KEY (submission_id, version)
);

-- The conversation between reviewers and the designer about one submission.
CREATE TABLE IF NOT EXISTS blueprint_messages (
  id            BIGSERIAL PRIMARY KEY,
  submission_id BIGINT NOT NULL REFERENCES blueprint_submissions(id) ON DELETE CASCADE,
  from_reviewer TEXT,                             -- the reviewer's name; NULL when the designer wrote it
  kind          TEXT NOT NULL CHECK (kind IN ('question','change_request','reply','decision')),
  body          TEXT NOT NULL,
  version       INT NOT NULL,                     -- which version it was about
  at            TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS blueprint_messages_sub ON blueprint_messages(submission_id, at);
