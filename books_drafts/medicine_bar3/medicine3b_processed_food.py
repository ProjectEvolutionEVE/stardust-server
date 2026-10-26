"""Medicine, bar 3 (Senior Doctor), part B: Food Processing and Labels. The NOVA grouping of food, what ultra-processed food tends to be, and how to read ingredient and nutrition labels."""
CODE = "medicine3b_processed_food"
BOOK = {
    "title": "Food Processing and Labels",
    "subtitle": "From whole ingredients to ultra-processed food: how to read a label and judge food quality",
    "chapters": [
        ("Processing is not always bad",
         "Food processing covers everything done to food before it is eaten, including washing, freezing, drying, cooking and mixing. Some processing keeps food safe and lasting. The useful questions are how much processing has happened, and what has been added."),
        ("Four groups",
         "One well-known way to group food is the NOVA system, which has four groups. Unprocessed and minimally processed foods, such as fresh vegetables, plain grains and eggs, come first. Processed culinary ingredients, such as oils, butter and salt, are used in cooking. Processed foods combine a few ingredients, as tinned beans do. Ultra-processed foods are ready to eat and made mostly from industrial ingredients and additives."),
        ("What ultra-processed food tends to be",
         "Ultra-processed foods are often high in sugar, salt and fat, and low in fibre. They are designed to be convenient and tasty. Large studies link diets rich in them with poorer health, although researchers are still working out the causes. Eating them now and then is part of many everyday diets."),
        ("Reading the ingredient list",
         "Ingredients are listed from the largest amount to the smallest. If sugar or fat appears near the top, the product is mostly that. Sugar has many names, such as sucrose, glucose syrup and dextrose, so several of them in one product add up."),
        ("Reading the nutrition panel",
         "The panel shows energy, fat, saturated fat, carbohydrate, sugars, protein and salt, usually per 100 grams and per serving. Compare products on the same basis. Check the serving size, because a small-looking pack can hold several servings."),
        ("Cost per serving",
         "Price per serving is often a better guide than price per pack. Cheap processed food can look economical, but a simple meal from staples often gives more nutrition for the money. Keeping a shopping list and the receipts shows where the money goes."),
    ],
    "test": [
        ("How many groups does the NOVA system use?",
         [("a", "Two"), ("b", "Four"), ("c", "Ten"), ("d", "One")], "b"),
        ("In an ingredient list, in what order are the ingredients given?",
         [("a", "Alphabetical"), ("b", "Smallest amount first"), ("c", "Largest amount first"), ("d", "Random")], "c"),
        ("Which is another name for sugar that may appear on a label?",
         [("a", "Vitamin A"), ("b", "Potassium"), ("c", "Calcium carbonate"), ("d", "Dextrose")], "d"),
        ("Why check the serving size on a label?",
         [("a", "A pack may hold several servings"), ("b", "Every pack is one serving"), ("c", "Serving size does not matter"), ("d", "Serving size equals the price")], "a"),
        ("What is often a better guide to value than the price per pack?",
         [("a", "The colour of the pack"), ("b", "Price per serving"), ("c", "The size of the logo"), ("d", "The date on the receipt")], "b"),
    ],
}
