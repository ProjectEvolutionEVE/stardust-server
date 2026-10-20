"""Engineering & Drafting (10-20): designing things clearly, and the blueprint form."""
import minerals as MN

CODE = "drafting"

BOOK = {
    "title": "Engineering & Drafting",
    "subtitle": "Thinking a design through and writing it down clearly",
    "chapters": [
        ("Start with the problem",
         "Engineering is solving a real problem with things you can build. Good designs start with a clear "
         "question: who needs this, and what goes wrong without it? The blueprint form asks this first."),
        ("Drawings and units",
         "Engineers write designs down so someone else can build them exactly. Use one set of units and stick to it: "
         "metres, kilograms, minutes. Aboard, every amount in the blueprint form is in kilograms."),
        ("Mass, volume and density",
         "Density is mass divided by volume. Turn it round and volume is mass divided by density. That is how the "
         "blueprint form works out a design's size: you never type the weight or size in. 1 kg of aluminium "
         "(2,700 kg/m³) takes almost three times the space of 1 kg of iron (7,874 kg/m³)."),
        ("Choosing materials",
         "Pick each material for its job: light for things that move, strong for things that carry loads, heat-proof "
         "for things that get hot. The form lists the refined or working form of each material, never raw ore."),
        ("Break it into parts",
         "Split a design into parts, and give each part its materials. Number the steps of how it is built. A design "
         "can have up to 30 parts, each with up to 20 materials."),
        ("New, upgrade or newer version",
         "The form asks whether a design is brand new, an upgrade, or a newer version or model. An upgrade or newer "
         "version names what it builds on and says what's different."),
        ("Review and serials",
         "The review team reads every design and can ask a question, ask for changes, approve it or turn it down. "
         "An approved design gets a model code, and every printed copy carries its own serial, so forgeries can't "
         "pass. Players design blueprints; the Starship's team only reviews them."),
    ],
    "test": [
        ("What should a good design start with?",
         [("a", "Its colour"), ("b", "The problem it solves"), ("c", "Its price"), ("d", "Its serial")], "b"),
        ("How is volume worked out from mass?",
         [("a", "Mass divided by density"), ("b", "Mass times ten"), ("c", "You type it in"), ("d", "It can't be")], "a"),
        ("Which takes more space: 1 kg of aluminium or 1 kg of iron?",
         [("a", "Iron"), ("b", "Aluminium"), ("c", "The same"), ("d", "Neither takes space")], "b"),
        ("What must an upgrade name?",
         [("a", "What it builds on, and what's different"), ("b", "The designer's real name"), ("c", "Nothing"), ("d", "A price")], "a"),
        ("Who designs blueprints?",
         [("a", "The Starship's team"), ("b", "Players"), ("c", "The bank"), ("d", "Nobody")], "b"),
    ],
}
