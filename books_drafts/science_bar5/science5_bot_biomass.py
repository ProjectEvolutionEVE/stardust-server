"""Forest Inventory and Biomass Estimation. How foresters measure trees, estimate carbon stored in forests, and report the uncertainty."""
CODE = "science5_bot_biomass"
BOOK = {
    "title": "Forest Inventory and Biomass Estimation",
    "subtitle": "Counting the wood and carbon held in forests",
    "chapters": [
        ("Why count trees",
         "Forests store large amounts of carbon in their trunks, branches, roots and soil. To manage forests and track their carbon, scientists must estimate how much biomass is present."),
        ("Plot sampling",
         "Forest inventories measure sample plots spread across a region. Each plot is measured carefully, and the results are scaled up to estimate the whole forest, with a known sampling error."),
        ("Allometric equations",
         "Allometric equations estimate a tree's biomass from easily measured sizes, such as its diameter and height. They are built by harvesting sample trees and weighing their parts, and they are specific to species and region."),
        ("Carbon stocks",
         "Dry biomass is about half carbon by weight, so a tree's carbon stock is roughly half its dry mass. Adding this up across plots gives the carbon stock of the forest."),
        ("Remote sensing of forests",
         "Satellites and airborne lidar cover large areas and measure forest height and structure. Combined with plot data, they make it possible to map biomass across regions that are too large to sample on foot."),
        ("Uncertainty and reporting forest carbon",
         "Every biomass estimate carries uncertainty from sampling, equations and measurement. Good forest carbon reports state these uncertainty ranges clearly, so decisions are based on honest numbers."),
    ],
    "test": [
        ("What are allometric equations used for?",
         [("a", "Painting forest maps"), ("b", "Choosing the colour of leaves"), ("c", "Counting birds in a forest"), ("d", "Estimating tree biomass from easily measured sizes such as diameter")], "d"),
        ("What do sample plots in a forest inventory provide?",
         [("a", "A single tree to weigh"), ("b", "A sample used to estimate the whole forest"), ("c", "A list of tourist paths"), ("d", "A map of the Moon")], "b"),
        ("About what fraction of dry tree biomass is carbon?",
         [("a", "Almost all of it"), ("b", "About one tenth"), ("c", "About half"), ("d", "None of it")], "c"),
        ("What does remote sensing add to forest biomass work?",
         [("a", "Wide coverage of forest height and structure"), ("b", "A taste of the forest soil"), ("c", "The sound of birds"), ("d", "The price of timber")], "a"),
        ("What should a forest carbon report include?",
         [("a", "Uncertainty estimates for its numbers"), ("b", "Only one number with no range"), ("c", "Photographs of the sea"), ("d", "A list of car models")], "a"),
    ],
}
