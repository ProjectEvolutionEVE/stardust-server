"""Nutrient Solution Chemistry: ions, pH, electrical conductivity and recipe design for water-grown plants."""
CODE = "science5_bot_nutrient_chem"
BOOK = {
    "title": "Nutrient Solution Chemistry",
    "subtitle": "Ion speciation, pH, conductivity and micronutrient availability",
    "chapters": [
        ("Feeding plants with water", "In water-grown systems, plants take up nutrients as dissolved ions from a solution. The solution must hold every element the crop needs. Its chemistry decides what the roots can actually reach."),
        ("Ion speciation", "Ion speciation is the form in which an element exists in solution. Some forms are easy for roots to take up and others are not. Chemistry decides which form is present at a given pH."),
        ("pH control", "The pH of a nutrient solution affects which nutrients stay soluble. Most water-grown crops do well near a slightly acidic pH. Growers check and adjust pH often, because it drifts as plants take up ions."),
        ("Electrical conductivity", "Electrical conductivity, or EC, is a rough measure of how many dissolved salts a solution holds. Growers use EC to judge the strength of the feed. A solution that is too strong or too weak can stress the crop."),
        ("Micronutrient availability", "Micronutrients such as iron, manganese and zinc are needed in tiny amounts. At high pH they can precipitate and become unavailable. Chelated forms are often used to keep them in solution."),
        ("Recipe design", "A nutrient recipe balances the major elements with the trace elements at the right ratios. Growers adjust the recipe for each crop and growth stage. Records of EC, pH and crop response help improve the recipe over time."),
    ],
    "test": [
        ("How do plants take up most nutrients in a water-grown system?",
         [("a", "As solid lumps of soil"), ("b", "Through their petals only"), ("c", "As dissolved ions from the solution"), ("d", "As gas in the leaves only")], "c"),
        ("What does pH affect in a nutrient solution?",
         [("a", "The colour of the water only"), ("b", "The speed of the sun"), ("c", "The shape of the pot"), ("d", "Which nutrients stay soluble and available")], "d"),
        ("What does electrical conductivity roughly measure?",
         [("a", "How many leaves the plant has"), ("b", "How many dissolved salts the solution holds"), ("c", "How fast the roots grow"), ("d", "The weight of the container")], "b"),
        ("Why are micronutrients sometimes chelated?",
         [("a", "To make them turn into gas"), ("b", "To make them heavier"), ("c", "To stop plants from growing"), ("d", "To keep them soluble and available to roots")], "d"),
        ("What is a nutrient recipe?",
         [("a", "A balance of major and trace elements at set ratios"), ("b", "A dish for the grower's lunch"), ("c", "A rule for pot colour"), ("d", "A list of watering times only")], "a"),
    ],
}
