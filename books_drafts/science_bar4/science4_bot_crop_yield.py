"""Crop Physiology and Yield Components: how light, stress and growth stages build the yield a farmer harvests."""
CODE = "science4_bot_crop_yield"
BOOK = {
    "title": "Crop Physiology and Yield Components",
    "subtitle": "Light, stress, growth stages and the harvest that results",
    "chapters": [
        ("Canopy light interception",
         "A crop canopy catches sunlight, and the share it catches drives how much carbon the plants can fix. When leaves cover the ground early, more light is captured. Dense, well-placed leaves usually mean higher yield."),
        ("Yield components",
         "Yield is built from parts: the number of plants, the number of grains or fruits per plant, and the weight of each grain or fruit. Each part is set at a different stage of growth. Knowing them helps explain why yields differ."),
        ("Harvest index",
         "Harvest index is the share of the total plant dry matter that ends up in the harvested part. A high harvest index means more of the plant’s growth goes into grain or fruit. Breeders have raised it in many crops."),
        ("Heat and drought stress",
         "Heat and drought at key stages, such as flowering or grain filling, can cut yield sharply. Stress can stop pollen working or shorten the time for filling grain. The same stress at a quieter stage may do much less harm."),
        ("Growth stages",
         "Crops pass through defined stages, from germination to maturity. Each stage has a sensitive period when stress matters most. Farmers time irrigation and fertilizer to protect the stages that set yield."),
        ("Field trial measurements",
         "To learn how a crop performs, researchers measure canopy cover, biomass, grain number and final yield on small plots. Repeated trials across seasons show how yield responds to weather, soil and management."),
    ],
    "test": [
        ("What does canopy light interception affect?",
         [("a", "How much carbon the plants can fix"), ("b", "The colour of the soil"), ("c", "The weight of the tractor"), ("d", "The number of farmers")], "a"),
        ("Which of these is a yield component?",
         [("a", "The price at the market"), ("b", "The number of grains or fruits per plant"), ("c", "The name of the farm"), ("d", "The colour of the fence")], "b"),
        ("What does a high harvest index mean?",
         [("a", "The plant has no leaves"), ("b", "The plant is not growing"), ("c", "The soil is very dry"), ("d", "More of the plant’s dry matter goes into the harvested part")], "d"),
        ("Why does stress at flowering matter so much?",
         [("a", "Because flowers do not need water"), ("b", "Because flowers make the soil colder"), ("c", "Because stress can stop pollen working and cut yield"), ("d", "Because flowering never affects yield")], "c"),
        ("What is the main purpose of field trial measurements?",
         [("a", "To paint the field"), ("b", "To count the birds"), ("c", "To learn how a crop performs under real conditions"), ("d", "To remove the roots")], "c"),
    ],
}
