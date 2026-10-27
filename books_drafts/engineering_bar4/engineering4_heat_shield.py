"""Heat Shields and Ablation: re-entry heating, ablative materials, char layers, reusable tiles and arc-heater testing."""
CODE = "engineering4_heat_shield"
BOOK = {
    "title": "Heat Shields and Ablation",
    "subtitle": "Re-entry heating, ablators, char layers and reusable tiles",
    "chapters": [
        ("Re-entry heating",
         "A craft coming back through the air is slowed by that air, and the slowing turns energy into heat. The surface can reach extreme temperatures in a short time."),
        ("Ablative materials",
         "An ablative shield is made of material that burns or erodes in a controlled way. As it wears away, it carries heat off with it and protects the structure beneath."),
        ("The char layer",
         "Many ablators form a char, a black carbon layer that insulates the material below. The char and the gases escaping from it both help block the heat."),
        ("Reusable tiles",
         "Reusable heat tiles are light, porous ceramic panels that insulate without burning away. They can be flown again, but each one needs careful inspection and repair."),
        ("Testing in arc heaters",
         "Arc heaters make hot gas flows that match re-entry conditions in a test. Engineers test samples to see how much material is lost and how the char forms."),
        ("Designing the thickness",
         "The shield must be thick enough to last the whole heating pulse. Extra thickness adds weight, so the choice is always a balance."),
    ],
    "test": [
        ("What causes the heating in re-entry?",
         [("a", "The air slowing the craft and turning energy into heat"), ("b", "The engines"), ("c", "Sunlight"), ("d", "Radio signals")], "a"),
        ("What does an ablative material do?",
         [("a", "Freezes"), ("b", "Burns or erodes in a controlled way, carrying heat away"), ("c", "Melts into water"), ("d", "Glows")], "b"),
        ("What is a char layer?",
         [("a", "Paint"), ("b", "Fuel"), ("c", "Ice"), ("d", "A black carbon layer that insulates the material below")], "d"),
        ("What are reusable tiles?",
         [("a", "Heavy steel blocks"), ("b", "Glass windows"), ("c", "Light, porous ceramic panels that insulate"), ("d", "Fuel cells")], "c"),
        ("What is the trade-off in shield thickness?",
         [("a", "More weight against lasting the whole heating pulse"), ("b", "More colour against sound"), ("c", "More sound against light"), ("d", "More crew against space")], "a"),
    ],
}
