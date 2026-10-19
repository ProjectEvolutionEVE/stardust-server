"""What debris fields hold (Eric 10-19: "Go."): about thirty real minerals in three tiers, so every metal in the
raw-materials catalogue (materials.json) can actually be mined. This file is the ONE list: game.py takes its densities
from here, the library books take their text from here, test_server.py checks schema.sql and static/debris-flight.js
against it.

  · Real minerals, real formulas, real densities (kg/m³, webmineral / mindat values; pure-mineral values where a range
    is published). Every piece is pure ore mineral (rule 27), so smelting yields each element's share by weight,
    worked out here from the formula. Mixed sites like (Fe,Ni) are taken as half and half to keep it simple.
  · Tier 1 COMMON: most of every field by count. Tier 2 ORES: one or more per catalogue metal. Tier 3 SHOCK MINERALS:
    real minerals that on Earth form only under extreme shock pressure or heat. Their text states only that fact,
    never a cause (canon: nobody knows what destroyed the planets).
  · Rarity is a handful of bands that roughly follow real abundance; the client rolls pieces from these bands
    (static/debris-flight.js, BANDS and MIX).
  · Prices are whole credits per LOT (rule 21), Eric delegated the numbers on 10-19 ("prices will self adjust");
    every floor is half the start. Lots: bulk 100 kg, valuable 10 kg, precious 1 kg. Full table: docs/minerals-price-list.md.
"""

ATOMIC = {"H": 1.008, "C": 12.011, "O": 15.999, "F": 18.998, "Li": 6.94, "Mg": 24.305, "Al": 26.982, "Si": 28.085,
          "P": 30.974, "S": 32.06, "Ca": 40.078, "Ti": 47.867, "Cr": 51.996, "Mn": 54.938, "Fe": 55.845, "Co": 58.933,
          "Ni": 58.693, "Cu": 63.546, "Zn": 65.38, "As": 74.922, "Mo": 95.95, "Pd": 106.42, "Ag": 107.868,
          "Sn": 118.71, "La": 138.905, "Ce": 140.116, "Nd": 144.242, "W": 183.84, "Ir": 192.217, "Pt": 195.084,
          "Au": 196.967, "Pb": 207.2, "U": 238.029, "Na": 22.990}

# Rarity bands, commonest first. The client's MIX gives each band its share of pieces per field size.
BANDS = ("common", "plentiful", "ore", "scarce", "rare", "shock", "shock-rare", "lonsdaleite", "brownleeite")
LOT_G = {"bulk": 100_000, "valuable": 10_000, "precious": 1_000}

# code: (tier, band, name, mineral, formula shown, atoms {element: count}, density, metals yielded, lot, start price,
#        bank_lot, note).  The first five codes are the original items and keep their codes.
_M = [
    # ---- tier 1: common ----
    ("basalt", 1, "common", "Basalt", "basalt (rock)", "rock: mostly plagioclase and pyroxene", None, 2900, [], "bulk", 50, 4,
     "Dark volcanic rock, the commonest rock of rocky planets' crusts. A building stone; it can be melted and cast or spun into fibre."),
    ("iron-nickel", 1, "common", "Iron-nickel metal", "kamacite and taenite", "Fe,Ni (taken as 90% iron, 10% nickel)",
     {"Fe": 0.90 / 55.845, "Ni": 0.10 / 58.693}, 7900, ["Fe", "Ni"], "bulk", 400, 4,
     "Native metal: iron with some nickel, already metal. On Earth it is found in metallic meteorites; planetary cores are "
     "thought to be made mostly of it."),
    ("water-ice", 1, "common", "Water ice", "ice", "H₂O", {"H": 2, "O": 1}, 917, [], "bulk", 40, 4,
     "Frozen water. The Starship makes its own water, so ice is cheap aboard."),
    # ---- tier 2: ores ----
    ("iron", 2, "plentiful", "Iron ore (hematite)", "hematite", "Fe₂O₃", {"Fe": 2, "O": 3}, 5300, ["Fe"], "bulk", 200, 4,
     "The commonest iron ore."),
    ("magnetite", 2, "plentiful", "Iron ore (magnetite)", "magnetite", "Fe₃O₄", {"Fe": 3, "O": 4}, 5150, ["Fe"], "bulk", 220, 4,
     "A black iron ore, the most iron-rich one, and magnetic."),
    ("bauxite", 2, "plentiful", "Aluminium ore (bauxite)", "gibbsite", "Al(OH)₃", {"Al": 1, "O": 3, "H": 3}, 2400, ["Al"],
     "bulk", 300, 3, "Bauxite is the ore of aluminium; here every piece is its main mineral, gibbsite."),
    ("olivine", 2, "plentiful", "Magnesium ore (olivine)", "forsterite olivine", "Mg₂SiO₄", {"Mg": 2, "Si": 1, "O": 4}, 3270,
     ["Mg"], "bulk", 150, 3, "Green olivine, the main mineral of the rock under a planet's crust."),
    ("quartz", 2, "plentiful", "Quartz", "quartz", "SiO₂", {"Si": 1, "O": 2}, 2650, ["Si"], "bulk", 100, 3,
     "Silica, the source of silicon and of glass."),
    ("copper", 2, "ore", "Copper ore (chalcopyrite)", "chalcopyrite", "CuFeS₂", {"Cu": 1, "Fe": 1, "S": 2}, 4190, ["Cu", "Fe"],
     "bulk", 600, 2, "The commonest copper ore, brassy yellow."),
    ("ilmenite", 2, "ore", "Titanium ore (ilmenite)", "ilmenite", "FeTiO₃", {"Fe": 1, "Ti": 1, "O": 3}, 4720, ["Ti", "Fe"],
     "bulk", 500, 2, "The main ore of titanium."),
    ("pentlandite", 2, "ore", "Nickel ore (pentlandite)", "pentlandite", "(Fe,Ni)₉S₈ (taken as Fe₄.₅Ni₄.₅S₈)",
     {"Fe": 4.5, "Ni": 4.5, "S": 8}, 4800, ["Ni", "Fe"], "bulk", 900, 2, "The main ore of nickel."),
    ("sphalerite", 2, "ore", "Zinc ore (sphalerite)", "sphalerite", "ZnS", {"Zn": 1, "S": 1}, 4050, ["Zn"], "bulk", 400, 2,
     "The main ore of zinc."),
    ("galena", 2, "ore", "Lead ore (galena)", "galena", "PbS", {"Pb": 1, "S": 1}, 7600, ["Pb"], "bulk", 400, 2,
     "Heavy grey cubes: the main ore of lead."),
    ("chromite", 2, "ore", "Chromium ore (chromite)", "chromite", "FeCr₂O₄", {"Fe": 1, "Cr": 2, "O": 4}, 4790, ["Cr", "Fe"],
     "bulk", 400, 2, "The only important ore of chromium."),
    ("pyrolusite", 2, "ore", "Manganese ore (pyrolusite)", "pyrolusite", "MnO₂", {"Mn": 1, "O": 2}, 5060, ["Mn"], "bulk", 300, 2,
     "The main ore of manganese."),
    ("apatite", 2, "ore", "Phosphate (apatite)", "fluorapatite", "Ca₅(PO₄)₃F", {"Ca": 5, "P": 3, "O": 12, "F": 1}, 3190, ["P"],
     "bulk", 300, 2, "The source of phosphorus, for fertiliser in the greenhouse."),
    ("graphite", 2, "ore", "Graphite", "graphite", "C", {"C": 1}, 2250, ["C"], "bulk", 300, 2,
     "Soft black carbon."),
    ("sulfur", 2, "ore", "Native sulfur", "sulfur", "S", {"S": 1}, 2070, ["S"], "bulk", 150, 2,
     "Yellow sulfur, found as the element itself."),
    ("spodumene", 2, "ore", "Lithium ore (spodumene)", "spodumene", "LiAlSi₂O₆", {"Li": 1, "Al": 1, "Si": 2, "O": 6}, 3150,
     ["Li", "Al"], "bulk", 1000, 2, "The main ore of lithium."),
    ("silver", 2, "scarce", "Silver ore (acanthite)", "acanthite", "Ag₂S", {"Ag": 2, "S": 1}, 7300, ["Ag"], "valuable", 300, 2,
     "The main ore of silver."),
    ("cobaltite", 2, "scarce", "Cobalt ore (cobaltite)", "cobaltite", "CoAsS", {"Co": 1, "As": 1, "S": 1}, 6300, ["Co"],
     "valuable", 200, 2, "A silvery ore of cobalt. It contains arsenic."),
    ("cassiterite", 2, "scarce", "Tin ore (cassiterite)", "cassiterite", "SnO₂", {"Sn": 1, "O": 2}, 6990, ["Sn"], "valuable",
     160, 2, "The main ore of tin."),
    ("wolframite", 2, "scarce", "Tungsten ore (wolframite)", "wolframite", "(Fe,Mn)WO₄ (taken as Fe₀.₅Mn₀.₅WO₄)",
     {"Fe": 0.5, "Mn": 0.5, "W": 1, "O": 4}, 7300, ["W"], "valuable", 200, 2, "A heavy ore of tungsten."),
    ("molybdenite", 2, "scarce", "Molybdenum ore (molybdenite)", "molybdenite", "MoS₂", {"Mo": 1, "S": 2}, 4730, ["Mo"],
     "valuable", 240, 2, "Soft and greasy like graphite: the main ore of molybdenum."),
    ("monazite", 2, "scarce", "Rare-earth ore (monazite)", "monazite", "(Ce,La,Nd)PO₄ (taken as Ce₀.₅La₀.₂₅Nd₀.₂₅PO₄)",
     {"Ce": 0.5, "La": 0.25, "Nd": 0.25, "P": 1, "O": 4}, 5150, ["Nd", "Ce", "La"], "valuable", 300, 2,
     "A rare-earth phosphate: a source of neodymium for magnets."),
    ("uraninite", 2, "scarce", "Uranium ore (uraninite)", "uraninite", "UO₂", {"U": 1, "O": 2}, 10950, ["U"], "valuable", 500, 2,
     "Black and very heavy: the main ore of uranium. Radioactive."),
    ("gold", 2, "scarce", "Native gold", "gold", "Au", {"Au": 1}, 19300, ["Au"], "precious", 200, 3,
     "Gold as it is found in nature: already metal."),
    ("diamond", 2, "scarce", "Industrial diamond", "diamond", "C", {"C": 1}, 3510, ["C"], "precious", 100, 5,
     "Pure carbon, the hardest natural material. One in 100,000 is near-flawless."),
    ("platinum", 2, "rare", "Native platinum", "platinum", "Pt", {"Pt": 1}, 21450, ["Pt"], "precious", 300, 3,
     "Platinum as it is found in nature: already metal."),
    ("palladium", 2, "rare", "Native palladium", "palladium", "Pd", {"Pd": 1}, 12020, ["Pd"], "precious", 300, 3,
     "Palladium as it is found in nature: already metal."),
    ("iridium", 2, "rare", "Native iridium", "iridium", "Ir", {"Ir": 1}, 22560, ["Ir"], "precious", 400, 3,
     "Iridium as it is found in nature: already metal, and the densest piece in the fields."),
    # ---- tier 3: shock minerals (facts only, no cause, ever) ----
    ("shocked-quartz", 3, "shock", "Shocked quartz", "quartz with shock lamellae", "SiO₂", {"Si": 1, "O": 2}, 2650, ["Si"],
     "valuable", 200, 2,
     "Quartz crossed by fine parallel planes. On Earth these form only under extreme shock pressure."),
    ("impact-glass", 3, "shock", "Impact glass", "silica glass (lechatelierite)", "SiO₂", {"Si": 1, "O": 2}, 2200, ["Si"],
     "valuable", 200, 2, "Natural glass of almost pure silica. On Earth it forms only when rock is melted at extreme temperatures."),
    ("maskelynite", 3, "shock", "Maskelynite", "feldspar glass", "NaAlSi₃O₈–CaAl₂Si₂O₈ glass (taken as albite)",
     {"Na": 1, "Al": 1, "Si": 3, "O": 8}, 2550, ["Al", "Si"], "valuable", 300, 2,
     "Feldspar turned to glass while staying solid, keeping its crystal's shape. On Earth it forms only under extreme shock pressure."),
    ("coesite", 3, "shock", "Coesite", "coesite", "SiO₂", {"Si": 1, "O": 2}, 2920, ["Si"], "valuable", 400, 2,
     "A dense form of silica. On Earth it forms only under extreme pressure."),
    ("stishovite", 3, "shock-rare", "Stishovite", "stishovite", "SiO₂", {"Si": 1, "O": 2}, 4290, ["Si"], "precious", 100, 3,
     "The densest form of silica. On Earth it forms only under extreme pressure."),
    ("ringwoodite", 3, "shock-rare", "Ringwoodite", "ringwoodite", "Mg₂SiO₄", {"Mg": 2, "Si": 1, "O": 4}, 3900, ["Mg"],
     "precious", 100, 3,
     "Olivine squeezed into a denser crystal. On Earth it forms only under extreme pressure, hundreds of kilometres down."),
    ("lonsdaleite", 3, "lonsdaleite", "Lonsdaleite", "lonsdaleite (hexagonal diamond)", "C", {"C": 1}, 3520, ["C"],
     "precious", 2000, 3,
     "Carbon in a hexagonal diamond crystal. It is not ordinary diamond. On Earth it forms only under extreme pressure and heat."),
    # Eric 10-19: one ultra-rare find known from comets, never found naturally on Earth. Real facts only in "note";
    # its game role (a required material for advanced technologies aboard) is GAME_ROLE, always shown apart.
    ("brownleeite", 3, "brownleeite", "Brownleeite", "brownleeite", "MnSi", {"Mn": 1, "Si": 1}, 5820, ["Mn", "Si"],
     "precious", 20000, 1,
     "Manganese silicide, a semiconductor. First identified in an interplanetary dust particle that likely came from comet "
     "26P/Grigg-Skjellerup (Nakamura-Messenger and others, American Mineralogist, 2010). Approved by the International "
     "Mineralogical Association and named for the astronomer Donald Brownlee, who later led NASA's Stardust comet mission. "
     "It has never been found naturally on Earth; it can be made in a laboratory."),
]

MINERALS = {}
for code, tier, band, name, mineral, formula, atoms, density, metals, lot, price, bank_lot, note in _M:
    shares = {}
    if atoms:
        tot = sum(ATOMIC[e] * n for e, n in atoms.items())
        shares = {e: ATOMIC[e] * n / tot for e, n in atoms.items()}
    MINERALS[code] = {"code": code, "tier": tier, "band": band, "name": name, "mineral": mineral, "formula": formula,
                      "density": density, "yields": {e: round(shares[e] * 100, 2) for e in metals if e in shares},
                      "lot": lot, "lot_g": LOT_G[lot], "price": price, "floor": price // 2, "bank_lot": bank_lot,
                      "note": note}
    assert price % 2 == 0, code

ORIGINAL = ("iron", "copper", "silver", "gold", "diamond")
SHOCK = [c for c, m in MINERALS.items() if m["tier"] == 3]
NOTICED = {"lonsdaleite", "brownleeite"}          # gets its own alert when collected, like the near-flawless diamond (it is NOT that diamond)
ELEMENT_NAMES = {"Fe": "iron", "Ni": "nickel", "Al": "aluminium", "Mg": "magnesium", "Si": "silicon", "Cu": "copper",
                 "Ti": "titanium", "Zn": "zinc", "Pb": "lead", "Cr": "chromium", "Mn": "manganese", "P": "phosphorus",
                 "C": "carbon", "S": "sulfur", "Li": "lithium", "Ag": "silver", "Co": "cobalt", "Sn": "tin",
                 "W": "tungsten", "Mo": "molybdenum", "Nd": "neodymium", "Ce": "cerium", "La": "lanthanum",
                 "U": "uranium", "Au": "gold", "Pt": "platinum", "Pd": "palladium", "Ir": "iridium"}


# How a mineral is used aboard: the GAME's rule, not a real-world claim (Eric 10-19), always shown apart from the facts.
GAME_ROLE = {"brownleeite": "Aboard the Starship, brownleeite is a required material for advanced technologies."}


def yield_text(m):
    """'34.63% copper, 30.43% iron' (rule 27: share by weight from the formula)."""
    return ", ".join(f"{v:.2f}% {ELEMENT_NAMES[e]}" for e, v in m["yields"].items())


def lot_kg(m):
    return m["lot_g"] // 1000


if __name__ == "__main__":
    for m in MINERALS.values():
        print(f"{m['tier']} {m['band']:<11} {m['code']:<15} {m['density']:>6} {m['formula']:<28} {lot_kg(m):>4} kg "
              f"{m['price']:>5}/{m['floor']:<5} {yield_text(m)}")
