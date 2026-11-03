"""How each catalogue material is made, and what it is for (Eric 11-03): the Raw Materials Catalogue's entries.

For every material in materials.json: where it comes from aboard (the debris-field ores that yield its element, with
their real yields by weight from minerals.py, rule 27); how it is refined, in a few true, simple steps; and what it is
used for in the real world. Uses are real-world facts, never game designs: what gets built from these materials aboard
is designed by players as blueprints (rule 11).
"""
import minerals as MN

# the element each single-element material is, so its ores are found from the minerals' yields
ELEMENT = {"mat-iron": "Fe", "mat-nickel": "Ni", "mat-cobalt": "Co", "mat-copper": "Cu", "mat-aluminium": "Al",
           "mat-titanium": "Ti", "mat-magnesium": "Mg", "mat-zinc": "Zn", "mat-tin": "Sn", "mat-lead": "Pb",
           "mat-chromium": "Cr", "mat-manganese": "Mn", "mat-tungsten": "W", "mat-molybdenum": "Mo", "mat-lithium": "Li",
           "mat-silver": "Ag", "mat-gold": "Au", "mat-platinum": "Pt", "mat-palladium": "Pd", "mat-iridium": "Ir",
           "mat-silicon": "Si", "mat-carbon": "C", "mat-sulfur": "S", "mat-phosphorus": "P", "mat-neodymium": "Nd",
           "mat-uranium": "U"}
NOT_A_SOURCE = {"diamond", "lonsdaleite"}      # gems are kept as gems, never burned down for their carbon

NOT_FOUND = "Not found in the debris fields yet."

# code: (where it comes from, when it isn't simply the ores of its element; how it is made; what it is for)
REFINING = {
    "mat-iron": ("", "Reduction: the oxide ore is heated with carbon in a furnace; the carbon takes the oxygen away as gas "
                 "and liquid iron is left. Adding back a little carbon makes steel.",
                 "Steel for hulls, frames, beams, tools and machines: the most used metal there is."),
    "mat-nickel": ("", "The sulfide ore is roasted to drive off the sulfur, then smelted; pure nickel is made by "
                   "electrolysis, or by the carbonyl process (nickel joined to carbon monoxide as a gas, then split again).",
                   "Stainless steel and heat-proof alloys for engines; batteries, magnets and plating."),
    "mat-native-iron-nickel": ("Iron-nickel metal pieces from the debris fields: already metal, 90% iron and 10% nickel.",
                               "No smelting needed: the pieces are melted and cast as they are, or refined apart into "
                               "iron and nickel.",
                               "A ready-made steel-like alloy, and a source of both iron and nickel."),
    "mat-cobalt": ("", "Roasted to drive off the sulfur and arsenic, leached with acid, and won from the solution by "
                   "electrolysis.",
                   "Battery cathodes, very strong magnets, and superalloys for turbine blades."),
    "mat-copper": ("", "Chalcopyrite is roasted and smelted to a copper-iron sulfide called matte, blown with air to "
                   "blister copper, then refined pure by electrolysis.",
                   "Wiring, motors, electronics and heat exchangers: the best common conductor of electricity and heat."),
    "mat-aluminium": ("", "Bauxite is dissolved in hot caustic soda to get pure alumina (the Bayer process); then the "
                      "alumina is split by a strong electric current in a bath of molten salt (the Hall-Héroult process).",
                      "Light, rust-proof structures: frames, panels, wiring, and anything that must be light."),
    "mat-titanium": ("", "Ilmenite is turned into titanium tetrachloride with chlorine, which magnesium metal then reduces "
                     "(the Kroll process); the spongy titanium is melted down in a vacuum.",
                     "Strong, light, heat- and corrosion-proof parts for spacecraft, engines and pressure vessels."),
    "mat-magnesium": ("", "Made by electrolysis of molten magnesium chloride, or by heating magnesium oxide with silicon "
                      "in a vacuum (the Pidgeon process).",
                      "The lightest structural metal: light alloys. Also the metal that reduces titanium."),
    "mat-zinc": ("", "Sphalerite is roasted to zinc oxide, leached with acid, and zinc is won from the solution by "
                 "electrolysis.",
                 "Rust protection for steel (galvanizing), brass (with copper), and batteries."),
    "mat-tin": ("", "Cassiterite is reduced with carbon in a furnace, then refined.",
                "Solder for electronics, tin plating, and bronze (with copper)."),
    "mat-lead": ("", "Galena is roasted to lead oxide, which is reduced with carbon in a furnace.",
                 "Radiation shielding, heavy ballast, and batteries."),
    "mat-chromium": ("", "Chromite is reduced with carbon in an electric furnace to ferrochrome, for steelmaking; pure "
                     "chromium is made with aluminium (the thermite reaction) or by electrolysis.",
                     "Stainless steel, and hard, shiny, rust-proof plating."),
    "mat-manganese": ("", "Reduced with carbon in a furnace to ferromanganese, or won pure by electrolysis.",
                      "Strong, tough steels and aluminium alloys; batteries."),
    "mat-tungsten": ("", "Wolframite is turned into tungsten oxide by chemical steps, then reduced with hydrogen to a "
                     "powder that is pressed and sintered (heated until the grains bond).",
                     "The highest melting point of any metal: cutting tools, heat shields, rocket nozzles, and radiation "
                     "shielding."),
    "mat-molybdenum": ("", "Molybdenite is roasted to molybdenum oxide, which is reduced with hydrogen.",
                       "High-strength, heat-resistant steels and alloys. Molybdenite itself is a dry lubricant."),
    "mat-lithium": ("", "Spodumene is heated and leached with acid to lithium salts; lithium metal is won by "
                    "electrolysis of molten lithium chloride.",
                    "Rechargeable batteries, light alloys, and heat-transfer fluids."),
    "mat-silver": ("", "Acanthite (silver sulfide) is smelted, or the silver is dissolved out and recovered; it is "
                   "refined pure by electrolysis.",
                   "The best conductor of all metals: electrical contacts, mirrors, and germ-killing coatings."),
    "mat-gold": ("", "Native gold is already metal: it is melted and refined (with chlorine gas or by electrolysis) to "
                 "remove other metals.",
                 "Corrosion-proof electrical contacts, coatings that reflect heat and radiation, and a store of value."),
    "mat-platinum": ("", "Native platinum is already metal: it is dissolved, separated from its sister metals by "
                     "chemistry, and turned back into metal.",
                     "Catalysts, electrodes, sensors, and heat-proof contacts."),
    "mat-palladium": ("", "Native palladium is already metal: it is separated from platinum and refined by chemistry.",
                      "Catalysts, hydrogen purification (it soaks up hydrogen), and electronics."),
    "mat-iridium": ("", "Native iridium is already metal: it is separated from the other platinum metals by chemistry "
                    "and refined.",
                    "The most corrosion-proof metal: crucibles, spark contacts, and parts that must survive extreme heat."),
    "mat-silicon": ("", "Quartz is reduced with carbon in an electric arc furnace; for electronics and solar cells it is "
                    "purified much further (to 99.9999% or better) and grown into single crystals.",
                    "Solar cells, computer chips, glass, and silicones."),
    "mat-carbon": ("", "Graphite is already nearly pure carbon: it is cleaned of other minerals by flotation and heat.",
                   "Electrodes, the carbon that smelting needs, lubricant, heat shields, and battery anodes."),
    "mat-diamond": ("Industrial diamond pieces from the debris fields. The near-flawless one is its own item, kept "
                    "as a valuable.",
                    "Sorted and graded; no refining.",
                    "The hardest natural material: cutting, drilling and grinding tools, and heat spreaders."),
    "mat-boron": (NOT_FOUND, "Made from borate minerals by chemistry, then reduced with magnesium.",
                  "Neutron shielding and reactor control rods, very hard materials, and heat-proof glass."),
    "mat-sulfur": ("", "Native sulfur is already the element: it is melted and filtered.",
                   "Sulfuric acid, the most used chemical in refining and in batteries."),
    "mat-phosphorus": ("", "Apatite is heated with carbon and sand in an electric furnace; phosphorus comes off as a "
                       "gas and is condensed.",
                       "Fertilizer for growing food, and chemicals."),
    "mat-neodymium": ("", "Monazite is cracked open with acid or alkali, the rare earths are separated from each other "
                      "by many rounds of solvent extraction, and the metal is made by electrolysis.",
                      "The strongest permanent magnets: electric motors and generators."),
    "mat-dysprosium": (NOT_FOUND, "Separated from the other rare earths by solvent extraction, then reduced to metal.",
                       "Added to neodymium magnets so they keep their strength when hot."),
    "mat-water-ice": ("Water ice pieces from the debris fields. The Starship's water plant also makes its own water.",
                      "Melted and filtered.",
                      "Drinking water, the greenhouse, radiation shielding, and a source of hydrogen and oxygen."),
    "mat-hydrogen": ("Split from water ice.",
                     "Water is split by an electric current (electrolysis) into hydrogen and oxygen; the hydrogen is "
                     "dried, then compressed or chilled to a liquid.",
                     "The fuel that runs the small mining craft, and the hydrogen that reduces metal oxides in refining."),
    "mat-oxygen": ("Split from water ice.",
                   "Made together with hydrogen when water is split by electrolysis; dried and stored.",
                   "Air to breathe, and the oxidizer that engines burn their fuel with."),
    "mat-nitrogen": (NOT_FOUND, "Separated from air, or from nitrogen-bearing ices, by cooling and distillation.",
                     "Most of breathable air, fertilizer, and an inert gas for safe storage."),
    "mat-methane": (NOT_FOUND, "Collected from methane ices and purified, or made from carbon dioxide and hydrogen "
                    "(the Sabatier reaction).",
                    "Fuel, and a building block for plastics."),
    "mat-ammonia": (NOT_FOUND, "Made from nitrogen and hydrogen with heat, pressure and a catalyst (the Haber-Bosch "
                    "process), or collected from ammonia ices.",
                    "Fertilizer, and coolant."),
    "mat-carbon-dioxide": (NOT_FOUND, "Captured from air or from dry ice, and purified.",
                           "Food for greenhouse plants, fire suppression, and (with hydrogen) a way to make methane."),
    "mat-helium-3": (NOT_FOUND, "Separated from ordinary helium by cooling it to a few degrees above absolute zero.",
                     "A possible fusion fuel, and ultra-cold cooling."),
    "mat-sand": (NOT_FOUND + " Quartz, its main mineral, is.", "Washed and sieved by grain size.",
                 "Glass, concrete and mortar, and moulds for casting metal."),
    "mat-clay": (NOT_FOUND, "Dug, wetted and kneaded; shaped, dried, and fired hard in a kiln.",
                 "Bricks, pottery, and the first furnaces."),
    "mat-limestone": (NOT_FOUND, "Quarried and crushed; burned in a kiln it becomes lime.",
                      "Cement and mortar, and a flux that carries impurities away as slag when iron is smelted."),
    "mat-basalt": ("Basalt pieces from the debris fields.", "Crushed; or melted and cast; or spun into fibre.",
                   "Building stone, cast stone, and basalt fibre for strong composites."),
    "mat-soil": (NOT_FOUND, "Mixed from crushed rock, compost and water.", "Growing food in the greenhouse."),
    "mat-timber-softwood": ("Grown, not mined.", "Felled, sawn and dried.", "Frames, panels and furniture."),
    "mat-timber-hardwood": ("Grown, not mined.", "Felled, sawn, and dried slowly.",
                            "Strong, hard-wearing beams, floors, tool handles and furniture."),
    "mat-uranium": ("", "Uraninite is leached with acid, the uranium is recovered as an oxide called yellowcake, and "
                    "for most reactors it is enriched.",
                    "Nuclear fuel for power, and dense shielding."),
    "mat-thorium": (NOT_FOUND + " On Earth it comes mostly from monazite.", "Separated from rare-earth ores by chemistry.",
                    "A possible nuclear fuel, and heat-proof ceramics."),
}


def sources(code):
    """'Copper ore (chalcopyrite) CuFeS₂, 34.63%; ...': every debris-field mineral that yields this material's element."""
    el = ELEMENT.get(code)
    if not el:
        return ""
    return "; ".join(f"{m['name']} {m['formula'].split(' (')[0]}, {m['yields'][el]:.2f}%" for c, m in MN.MINERALS.items()
                     if el in m["yields"] and c not in NOT_A_SOURCE)


def entry(code):
    """(where from, how it's made, what it's for) for one material."""
    where, how, uses = REFINING[code]
    found = sources(code)
    return (where or (f"From the debris fields, by weight: {found}." if found else NOT_FOUND)), how, uses
