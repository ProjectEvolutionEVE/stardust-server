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
  ('filing_cabinet_m3',  0.15, 'SAMPLE: the filing cabinet in Private Quarters (blueprints and documents), cubic metres'),
  ('bookshelf_m3',        0.3, 'SAMPLE: the bookshelf in Private Quarters (library books checked out), cubic metres'),
  ('bank_bid_gap_pct',     10, 'the bank''s standing bid sits this many percent under the last price')
ON CONFLICT (key) DO NOTHING;

-- v3 (10-11): the game's OWN accounts, no link to Quavara (Eric). `player_key` was `qcid` (the old Quavara id): renamed
-- in place on databases that have it. It is now an internal id; how a player signs in lives in `logins`.
DO $$ BEGIN
  IF EXISTS (SELECT 1 FROM information_schema.columns WHERE table_name='players' AND column_name='qcid') THEN
    ALTER TABLE players RENAME COLUMN qcid TO player_key;
  END IF;
END $$;
CREATE TABLE IF NOT EXISTS players (
  id           BIGSERIAL PRIMARY KEY,
  player_key   TEXT UNIQUE NOT NULL,             -- internal id ('p:<random>'; 'dev:<name>' in local tests)
  display_name TEXT,
  created_at   TIMESTAMPTZ NOT NULL DEFAULT now()
);
-- Who the player is in the game (Eric 10-11): no real names. Rank + a first and last name picked from names.py.
-- Everyone starts at the bottom of the civilian ladder (track 'civilian', step 1 = Trainee); a military track comes later.
ALTER TABLE players ADD COLUMN IF NOT EXISTS first_name TEXT;
ALTER TABLE players ADD COLUMN IF NOT EXISTS last_name  TEXT;
ALTER TABLE players ADD COLUMN IF NOT EXISTS language   TEXT;
ALTER TABLE players ADD COLUMN IF NOT EXISTS track      TEXT NOT NULL DEFAULT 'civilian';
ALTER TABLE players ADD COLUMN IF NOT EXISTS rank_step  INT  NOT NULL DEFAULT 1;
-- The body (Eric 10-11): stamina, energy and focus, 0-100. Awake they drain 2.2 an hour; asleep they refill 35 per 6
-- hours. Stored as the value at `body_at` plus whether the character is asleep; the current value is worked out on read.
ALTER TABLE players ADD COLUMN IF NOT EXISTS stamina NUMERIC(6,3) NOT NULL DEFAULT 100;
ALTER TABLE players ADD COLUMN IF NOT EXISTS energy  NUMERIC(6,3) NOT NULL DEFAULT 100;
ALTER TABLE players ADD COLUMN IF NOT EXISTS focus   NUMERIC(6,3) NOT NULL DEFAULT 100;
ALTER TABLE players ADD COLUMN IF NOT EXISTS body_at TIMESTAMPTZ NOT NULL DEFAULT now();
ALTER TABLE players ADD COLUMN IF NOT EXISTS asleep  BOOLEAN NOT NULL DEFAULT true;     -- a new player starts in bed

-- How a player signs in: a phone number or an email address. The ONLY personal information the game keeps.
CREATE TABLE IF NOT EXISTS logins (
  id         BIGSERIAL PRIMARY KEY,
  player_id  BIGINT NOT NULL REFERENCES players(id) ON DELETE CASCADE,
  channel    TEXT NOT NULL CHECK (channel IN ('sms','email')),
  address    TEXT NOT NULL,                       -- +<digits> or a lower-case email
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE (channel, address)
);
-- Codes the server makes itself (email; and phone in local tests). Only a hash is kept.
CREATE TABLE IF NOT EXISTS login_codes (
  id         BIGSERIAL PRIMARY KEY,
  channel    TEXT NOT NULL,
  address    TEXT NOT NULL,
  code_hash  TEXT NOT NULL,
  tries      INT NOT NULL DEFAULT 0,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  expires_at TIMESTAMPTZ NOT NULL,
  used_at    TIMESTAMPTZ
);
CREATE INDEX IF NOT EXISTS login_codes_addr ON login_codes(address, id DESC);
-- Every code requested, for the per-hour limits.
CREATE TABLE IF NOT EXISTS login_attempts (
  id      BIGSERIAL PRIMARY KEY,
  channel TEXT NOT NULL,
  address TEXT NOT NULL,
  ip      TEXT NOT NULL DEFAULT '',
  at      TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS login_attempts_addr ON login_attempts(address, at);
CREATE INDEX IF NOT EXISTS login_attempts_ip   ON login_attempts(ip, at);
-- Signed-in devices. Only a hash of each token is kept.
CREATE TABLE IF NOT EXISTS auth_tokens (
  token_hash   TEXT PRIMARY KEY,
  player_id    BIGINT NOT NULL REFERENCES players(id) ON DELETE CASCADE,
  created_at   TIMESTAMPTZ NOT NULL DEFAULT now(),
  last_seen_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  revoked_at   TIMESTAMPTZ
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
  ('iron',    'resource', 'Iron ore', 'g', 1000,  5300),
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

-- Receipts (Eric 10-11): what a player owns sits in the Starship's hands, so every transfer gives them a receipt with a
-- code, like a warehouse receipt. The code is random and unguessable, and only this database can say it is real: anyone
-- can check a code against the server, so a made-up code or an edited receipt doesn't match. Never edited or deleted.
CREATE TABLE IF NOT EXISTS receipts (
  id        BIGSERIAL PRIMARY KEY,
  code      TEXT NOT NULL UNIQUE,                 -- e.g. WSC-7K3F-92QD
  player_id BIGINT NOT NULL REFERENCES players(id) ON DELETE CASCADE,
  kind      TEXT NOT NULL,                        -- 'unload' (later: sale, move to quarters, ...)
  ledger_id BIGINT REFERENCES ledger(id),         -- the history row this receipt is the player's copy of
  detail    JSONB NOT NULL,
  at        TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS receipts_player ON receipts(player_id, at DESC);

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

-- v4 (10-11): where things are kept inside Private Quarters (Eric). The filing cabinet holds every blueprint and,
-- inside it, the lockbox for small personal effects and valuables; the bookshelf holds library books checked out.
-- Raw materials stay in the Starship's cargo hold. Existing players get the new places, and their lockbox moves
-- into the filing cabinet.
DO $$ BEGIN
  ALTER TABLE locations DROP CONSTRAINT IF EXISTS locations_kind_check;
  ALTER TABLE locations ADD CONSTRAINT locations_kind_check CHECK (kind IN ('starship_cargo','private_quarters','lockbox',
    'hangar','ship_hold','colony_storage','filing_cabinet','bookshelf'));
END $$;
CREATE UNIQUE INDEX IF NOT EXISTS locations_one_in_quarters ON locations(player_id, kind) WHERE kind IN ('filing_cabinet','bookshelf');
INSERT INTO locations(player_id, kind, name, capacity_m3, parent_id)
  SELECT q.player_id, 'filing_cabinet', 'Filing cabinet', (SELECT value FROM settings WHERE key='filing_cabinet_m3'), q.id
  FROM locations q WHERE q.kind='private_quarters'
  AND NOT EXISTS (SELECT 1 FROM locations f WHERE f.player_id=q.player_id AND f.kind='filing_cabinet');
INSERT INTO locations(player_id, kind, name, capacity_m3, parent_id)
  SELECT q.player_id, 'bookshelf', 'Bookshelf', (SELECT value FROM settings WHERE key='bookshelf_m3'), q.id
  FROM locations q WHERE q.kind='private_quarters'
  AND NOT EXISTS (SELECT 1 FROM locations b WHERE b.player_id=q.player_id AND b.kind='bookshelf');
UPDATE locations l SET parent_id=f.id, name='Lockbox'
  FROM locations f WHERE l.kind='lockbox' AND f.kind='filing_cabinet' AND f.player_id=l.player_id
  AND l.parent_id IS DISTINCT FROM f.id;

-- v5 (10-11): iron ore is hematite, 5,300 kg/m³ (webmineral; the raw-materials catalogue). It was 5,150 by mistake.
UPDATE item_types SET density_kg_m3 = 5300 WHERE code = 'iron' AND density_kg_m3 = 5150;

-- v6 (10-11): debris fields hold ORES (Eric, rule 25). Item codes stay the same; they now name the ore as found.
-- Every piece is pure ore mineral (rule 27). Smelted metals will get codes of their own (e.g. copper-metal).
UPDATE item_types SET name='Iron ore (hematite)'                         WHERE code='iron';
UPDATE item_types SET name='Copper ore (chalcopyrite)', density_kg_m3=4190 WHERE code='copper';
UPDATE item_types SET name='Silver ore (acanthite)',    density_kg_m3=7300 WHERE code='silver';
UPDATE item_types SET name='Native gold'                                 WHERE code='gold';
UPDATE item_types SET name='Industrial diamond'                          WHERE code='diamond';
-- The near-flawless diamond (Eric, rule 26): one in 100,000 diamond pieces, rolled by the server when collected.
-- Each one is its own item, never mixed in with industrial diamond, kept as a valuable.
INSERT INTO item_types(code, kind, name, base_unit, unique_items, tradeable) VALUES
  ('diamond-flawless', 'resource', 'Near-flawless diamond', 'each', true, true)
ON CONFLICT (code) DO NOTHING;
ALTER TABLE cargo ADD COLUMN IF NOT EXISTS flawless BOOLEAN NOT NULL DEFAULT false;

-- v7 (10-11): the market (Eric, rules 12, 20, 21). Each traded item's starting price (used until its first trade), its
-- floor (nothing trades below it), the reference price the bank leans prices back toward, and the bank's lot size.
-- Prices are whole credits per kg. Eric's draft list of 10-11; any number may change (he approves the list).
CREATE TABLE IF NOT EXISTS item_prices (
  item_code   TEXT PRIMARY KEY REFERENCES item_types(code),
  start_price BIGINT NOT NULL CHECK (start_price > 0),
  floor_price BIGINT NOT NULL CHECK (floor_price > 0),
  ref_price   BIGINT NOT NULL CHECK (ref_price > 0),
  bank_lot_kg BIGINT NOT NULL DEFAULT 0,          -- 0 = the bank doesn't trade it
  listed      BOOLEAN NOT NULL DEFAULT true,
  sort        INT NOT NULL DEFAULT 0
);
INSERT INTO item_prices(item_code, start_price, floor_price, ref_price, bank_lot_kg, sort) VALUES
  ('iron',     2,   1,   2, 400, 1),
  ('copper',   6,   3,   6, 150, 2),
  ('silver',  30,  15,  30,  20, 3),
  ('gold',   200, 100, 200,   3, 4),
  ('diamond',100,  50, 100,   5, 5)
ON CONFLICT (item_code) DO NOTHING;
INSERT INTO settings(key, value, note) VALUES
  ('bank_tick_s',       20, 'about how often the bank desks trade, seconds (Eric 10-11: the bank keeps the market moving)'),
  ('bank_vol_pct',     1.5, 'how far each bank trade nudges the price at random, percent'),
  ('bank_pull_pct',     10, 'how strongly prices lean back toward the reference price, percent per trade'),
  ('bank_bid_qty_kg', 2000, 'size of the bank''s standing bid (the instant sale to the bank), kg'),
  ('bank_ask_gap_pct',   10, 'the bank''s standing ask sits this many percent over the last price (the instant purchase from the bank)')
ON CONFLICT (key) DO NOTHING;

-- v8 (10-11): minimum orders (Eric: "a set minimum order for things with wide price swings, so there are no really small
-- orders"). Each item trades in LOTS, and its price is per lot: iron and copper ore in 100 kg lots, silver ore in 10 kg,
-- gold and diamond in 1 kg. One lot is the smallest order. Per-kg prices stay the same (iron 200 per 100 kg = 2 per kg);
-- a one-credit step is now 0.5% on iron instead of 50%. The market's history restarts at the switch (`since`): older
-- trades stay in the table but no longer set prices or draw candles. Open orders in the old units are given back first.
ALTER TABLE item_prices ADD COLUMN IF NOT EXISTS since    TIMESTAMPTZ NOT NULL DEFAULT now();
ALTER TABLE item_prices ADD COLUMN IF NOT EXISTS bank_lot BIGINT NOT NULL DEFAULT 0;   -- the bank's trade size, in lots
DO $$ BEGIN
  IF (SELECT trade_unit FROM item_types WHERE code='iron') = 1000 THEN
    UPDATE accounts a SET held_credits = a.held_credits - x.amt, credits = a.credits + x.amt
      FROM (SELECT account_id, sum(price * remaining) amt FROM orders
            WHERE status='open' AND side='buy' AND item_code IN ('iron','copper','silver','gold','diamond') GROUP BY account_id) x
      WHERE a.id = x.account_id;
    UPDATE stacks s SET held = s.held - x.g, qty = s.qty + x.g
      FROM (SELECT l.id AS loc, o.item_code, sum(o.remaining * t.trade_unit) AS g FROM orders o
            JOIN accounts a ON a.id = o.account_id
            JOIN locations l ON l.player_id = a.player_id AND l.kind = 'starship_cargo'
            JOIN item_types t ON t.code = o.item_code
            WHERE o.status='open' AND o.side='sell' AND o.item_code IN ('iron','copper','silver','gold','diamond')
            GROUP BY 1, 2) x
      WHERE s.location_id = x.loc AND s.item_code = x.item_code;
    UPDATE orders SET status='cancelled', closed_at=now()
      WHERE status='open' AND item_code IN ('iron','copper','silver','gold','diamond');
    UPDATE item_types SET trade_unit = 100000 WHERE code IN ('iron','copper');   -- 100 kg lots
    UPDATE item_types SET trade_unit = 10000  WHERE code = 'silver';             -- 10 kg lots
    UPDATE item_prices SET start_price=200, floor_price=100, ref_price=200, bank_lot=4, since=now() WHERE item_code='iron';
    UPDATE item_prices SET start_price=600, floor_price=300, ref_price=600, bank_lot=2, since=now() WHERE item_code='copper';
    UPDATE item_prices SET start_price=300, floor_price=150, ref_price=300, bank_lot=2, since=now() WHERE item_code='silver';
    UPDATE item_prices SET bank_lot=3, since=now() WHERE item_code='gold';
    UPDATE item_prices SET bank_lot=5, since=now() WHERE item_code='diamond';
  END IF;
END $$;

-- v9 (10-11): serial numbers (Eric). Every approved design gets a MODEL code. The designer's original and every copy
-- printed from it carry their own SERIAL: the model, the run, and the copy's number in that run, e.g. BP-K7Q3X-R2-0025.
-- Run numbers only go up and every serial is unique, so no run ever repeats a code from an earlier one. Anyone can check
-- a serial (GET /api/dfg/serial/{code}), as with receipts. Built things will use the same tables (kind 'build').
ALTER TABLE item_types ADD COLUMN IF NOT EXISTS model_code TEXT UNIQUE;
CREATE TABLE IF NOT EXISTS production_runs (
  id             BIGSERIAL PRIMARY KEY,
  blueprint_code TEXT NOT NULL REFERENCES item_types(code),
  kind           TEXT NOT NULL CHECK (kind IN ('original','print','build')),
  run_no         INT NOT NULL CHECK (run_no >= 0),
  qty            INT NOT NULL CHECK (qty > 0),
  player_id      BIGINT REFERENCES players(id) ON DELETE SET NULL,
  at             TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE (blueprint_code, kind, run_no)
);
CREATE TABLE IF NOT EXISTS serials (
  code     TEXT PRIMARY KEY,
  item_id  BIGINT UNIQUE REFERENCES items(id) ON DELETE SET NULL,
  run_id   BIGINT NOT NULL REFERENCES production_runs(id),
  copy_no  INT NOT NULL CHECK (copy_no > 0),
  at       TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE (run_id, copy_no)
);
INSERT INTO settings(key, value, note) VALUES
  ('blueprint_copy_m3', 0.0005, 'SAMPLE: space one blueprint copy takes in a filing cabinet (a folded drawing set), cubic metres'),
  ('print_run_max', 500, 'SAMPLE: most copies in one print run')
ON CONFLICT (key) DO NOTHING;
-- v10 (10-11): printing prices (Eric). A premium for registering, serial-tagging and protecting a design: a one-time
-- setup fee with a design's first print run, plus a price per copy. 25 copies on the first run = 100 + 250 = 350.
INSERT INTO settings(key, value, note) VALUES
  ('blueprint_setup_fee', 100, 'Eric 10-11: one-time setup fee for a new design, paid with its first print run, credits'),
  ('blueprint_copy_cost',  10, 'Eric 10-11: price of each printed blueprint copy, credits')
ON CONFLICT (key) DO NOTHING;

-- v11 (10-12): blueprint auctions (Eric). Copies are sold by auction in the Market terminal. The designer picks a start
-- date and time and a floor; copies go up one at a time; each closes 5 minutes after its last top bid (a copy also
-- waits 5 minutes for its first bid); the top bid wins, plus a 2.5% Starship fee on top that goes to the WSC. No bid at
-- or above the floor stops the auction and holds it. Bids set credits aside until outbid. Bidders are never named.
ALTER TABLE production_runs ADD COLUMN IF NOT EXISTS credits BIGINT NOT NULL DEFAULT 0;   -- what the run cost its designer
CREATE TABLE IF NOT EXISTS auctions (
  id             BIGSERIAL PRIMARY KEY,
  designer_id    BIGINT NOT NULL REFERENCES players(id) ON DELETE CASCADE,
  blueprint_code TEXT NOT NULL REFERENCES item_types(code),
  floor          BIGINT NOT NULL CHECK (floor > 0),
  start_at       TIMESTAMPTZ NOT NULL,
  status         TEXT NOT NULL CHECK (status IN ('scheduled','running','held','done','cancelled')),
  below_cost_ack BOOLEAN NOT NULL DEFAULT false,
  created_at     TIMESTAMPTZ NOT NULL DEFAULT now(),
  ended_at       TIMESTAMPTZ
);
CREATE INDEX IF NOT EXISTS auctions_status ON auctions(status, start_at);
CREATE TABLE IF NOT EXISTS auction_lots (
  id          BIGSERIAL PRIMARY KEY,
  auction_id  BIGINT NOT NULL REFERENCES auctions(id) ON DELETE CASCADE,
  lot_no      INT NOT NULL,
  item_id     BIGINT NOT NULL REFERENCES items(id),
  status      TEXT NOT NULL CHECK (status IN ('waiting','open','sold','unsold')),
  opened_at   TIMESTAMPTZ,
  closes_at   TIMESTAMPTZ,
  top_bid     BIGINT,
  top_fee     BIGINT,
  top_bidder  BIGINT REFERENCES players(id),
  closed_at   TIMESTAMPTZ,
  UNIQUE (auction_id, lot_no)
);
CREATE INDEX IF NOT EXISTS auction_lots_open ON auction_lots(status, closes_at);
CREATE TABLE IF NOT EXISTS auction_bids (
  id        BIGSERIAL PRIMARY KEY,
  lot_id    BIGINT NOT NULL REFERENCES auction_lots(id) ON DELETE CASCADE,
  bidder_id BIGINT NOT NULL REFERENCES players(id) ON DELETE CASCADE,
  amount    BIGINT NOT NULL CHECK (amount > 0),
  fee       BIGINT NOT NULL CHECK (fee >= 0),
  at        TIMESTAMPTZ NOT NULL DEFAULT now()
);
INSERT INTO settings(key, value, note) VALUES
  ('auction_window_s', 300, 'Eric 10-12: a copy closes this many seconds after its last top bid (and waits this long for a first bid)'),
  ('auction_fee_pct',  2.5, 'Eric 10-12: the Starship''s fee on top of each winning bid, percent, paid to the WSC (rounded up to whole credits)'),
  ('auction_raise',      1, 'Eric 10-12: the smallest raise over the current top bid, credits'),
  ('auction_max_days',  30, 'SAMPLE: how far ahead an auction can be scheduled, days')
ON CONFLICT (key) DO NOTHING;
