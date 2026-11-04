"""Surface Chemistry and Adsorption Isotherms: how molecules stick to surfaces and how that is measured."""
CODE = "science5_chem_adsorption"
BOOK = {
    "title": "Surface Chemistry and Adsorption Isotherms",
    "subtitle": "Adsorption sites, Langmuir and BET isotherms, and surface area",
    "chapters": [
        ("Molecules on surfaces", "Adsorption is the sticking of molecules to a surface. It happens on everything from catalysts to soil particles. The surface offers sites where molecules can settle."),
        ("Adsorption sites", "Adsorption sites are the places on a surface where molecules can bind. Some sites are stronger than others. The number and strength of sites decide how much can be adsorbed."),
        ("Langmuir and BET isotherms", "An adsorption isotherm shows how much gas or liquid is taken up at different pressures or concentrations. The Langmuir model assumes a single layer of molecules on identical sites. The BET model allows several layers and is used to measure surface area."),
        ("Surface area measurement", "The BET method measures surface area by measuring how much gas, often nitrogen, is adsorbed at very low temperature. The data are fitted to the BET equation. The result gives the area per gram of material."),
        ("Catalytic surfaces", "Catalysts work on surfaces, so a large surface area often means more active sites. Porous materials can pack a huge area into a small volume. Adsorption studies help chemists design better catalysts."),
        ("Physisorption and chemisorption", "Physisorption is weak adsorption held by van der Waals forces. Chemisorption forms chemical bonds with the surface and is much stronger. The two types behave very differently in an isotherm and in practice."),
    ],
    "test": [
        ("What is adsorption?",
         [("a", "Molecules sticking to a surface"), ("b", "Molecules dissolving completely in the gas"), ("c", "Molecules turning into light"), ("d", "Molecules freezing in a bag")], "a"),
        ("What does the Langmuir model assume?",
         [("a", "An infinite number of layers at once"), ("b", "No sites at all"), ("c", "A single layer of molecules on identical sites"), ("d", "Only sites in the middle of a sphere")], "c"),
        ("Which gas is often used for BET surface area measurement?",
         [("a", "Nitrogen"), ("b", "Chlorine gas"), ("c", "Neon gas"), ("d", "Methane from a bottle")], "a"),
        ("What is the difference between physisorption and chemisorption?",
         [("a", "Physisorption is weak van der Waals attraction; chemisorption forms chemical bonds"), ("b", "Physisorption forms bonds; chemisorption is weak"), ("c", "They are the same process"), ("d", "They only happen in water")], "a"),
        ("Why does a large surface area help a catalyst?",
         [("a", "It makes the catalyst heavier"), ("b", "It stops reactions completely"), ("c", "It changes the colour of the room"), ("d", "It gives more active sites for reaction")], "d"),
    ],
}
