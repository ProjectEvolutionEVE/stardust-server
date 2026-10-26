"""Medicine, bar 3 (Senior Doctor), part B: Fresh, Stored and Grown Food. How food changes after harvest, how storage and cooking affect nutrients, and what a grown food supply means aboard a ship."""
CODE = "medicine3b_food_quality"
BOOK = {
    "title": "Fresh, Stored and Grown Food",
    "subtitle": "How food changes after harvest, how storage and cooking affect nutrients, and what a grown food supply means",
    "chapters": [
        ("Quality starts in the field",
         "Food quality begins with how it is grown, how it is picked and how soon it is used. Crops picked ripe and eaten soon usually keep their taste and nutrients best. The clock starts ticking at harvest."),
        ("Nutrients lost in storage",
         "Some vitamins break down over time, especially with heat, light and air. Vitamin C is one of the most easily lost, and leafy greens can lose a good share of it within days if they are stored badly. Cool, humid, dark storage slows the losses, because cold slows the chemical changes."),
        ("Cooking and water",
         "Water-soluble vitamins leach into cooking water, and heat breaks some vitamins down. Steaming and short cooking keep more than long boiling. Using the cooking water in a soup or sauce keeps the nutrients that have dissolved into it."),
        ("Freezing and drying",
         "Freezing soon after harvest keeps many nutrients close to fresh levels, because the cold slows most of the chemistry. Drying removes water, so microbes cannot grow, but it can cost some vitamins. Frozen and tinned vegetables can be nearly as nutritious as fresh ones when they are handled well."),
        ("A grown food supply",
         "A greenhouse aboard a ship can supply fresh food close to the people who eat it. Crops can be picked as they are needed, so food spends little time in storage. Growing food also needs clean water, steady conditions and careful planning, so that the harvest is not wasted."),
        ("Food quality and cost",
         "Spoiled food is money thrown away. Good storage, stock rotation so that the oldest food is used first, and planned meal sizes all cut waste and keep a food budget steady. Recording what is wasted helps a crew see where to save."),
    ],
    "test": [
        ("Which vitamin is one of the most easily lost in storage?",
         [("a", "Vitamin D"), ("b", "Vitamin C"), ("c", "Vitamin K"), ("d", "Iron")], "b"),
        ("Which cooking method keeps more water-soluble vitamins?",
         [("a", "Long boiling in lots of water"), ("b", "Frying in deep oil"), ("c", "Leaving food in hot water for hours"), ("d", "Steaming and short cooking")], "d"),
        ("What does freezing soon after harvest do?",
         [("a", "Destroys most vitamins"), ("b", "Keeps many nutrients close to fresh levels"), ("c", "Adds sugar"), ("d", "Makes food harder to digest")], "b"),
        ("What does drying remove, and why does that help keep food?",
         [("a", "Vitamins, so bacteria cannot grow"), ("b", "Salt, so food tastes better"), ("c", "Water, so microbes cannot grow"), ("d", "Fibre, so food lasts")], "c"),
        ("What helps cut waste in a food supply?",
         [("a", "Stock rotation, first in and first out, and planned meal sizes"), ("b", "Storing everything in the warmest place"), ("c", "Buying more than you need every day"), ("d", "Ignoring what goes off")], "a"),
    ],
}
