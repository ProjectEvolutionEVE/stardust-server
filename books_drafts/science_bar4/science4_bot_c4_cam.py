"""C3, C4 and CAM Photosynthesis: three ways plants fix carbon from the air, and why some grow better in hot, dry places."""
CODE = "science4_bot_c4_cam"
BOOK = {
    "title": "C3, C4 and CAM Photosynthesis",
    "subtitle": "Three routes for capturing carbon, and where each one thrives",
    "chapters": [
        ("Carbon fixation pathways",
         "Plants capture carbon dioxide from the air and fix it into sugars. Most plants use the C3 pathway, where the first stable product has three carbon atoms. C4 and CAM plants add extra steps that concentrate carbon dioxide before the main reaction."),
        ("Rubisco and its limits",
         "Rubisco is the enzyme that fixes carbon dioxide in all three pathways. It is slow, and it can also react with oxygen, which wastes energy. The C4 and CAM pathways are partly ways to reduce this wasteful reaction."),
        ("Water-use efficiency",
         "C4 and CAM plants lose less water for each unit of carbon they fix. C4 plants open their stomata less often in hot weather, and CAM plants open them only at night, when the air is cooler and water loss is lower. This is why they suit dry places."),
        ("Grasses and the spread of C4",
         "Many tropical and warm-season grasses use the C4 pathway. The C4 pathway evolved about 30 million years ago, and C4 grasses spread across many warm, dry regions mainly in the last 8 million years or so. Their spread changed the grasslands and the animals that graze them."),
        ("CAM plants of dry places",
         "Cactus, agave and many succulents use CAM. They take in carbon dioxide at night and store it as acid, then release it in daylight to make sugar. This timing keeps water losses very low in deserts."),
        ("Implications for crops",
         "Choosing and breeding crops depends on which pathway they use. C4 crops such as maize and sugar cane often do well in hot sun with good light. C3 crops such as wheat and rice do better in cooler, wetter conditions. Knowing the pathway guides where a crop will grow best."),
    ],
    "test": [
        ("Which pathway does most plants use?",
         [("a", "CAM"), ("b", "C4"), ("c", "C3"), ("d", "C5")], "c"),
        ("What is the main problem with the enzyme Rubisco?",
         [("a", "It is slow, and it can react with oxygen"), ("b", "It is too fast"), ("c", "It cannot fix carbon at all"), ("d", "It only works in the dark")], "a"),
        ("When do CAM plants open their stomata?",
         [("a", "Only in the middle of the day"), ("b", "Mainly at night"), ("c", "Only in winter"), ("d", "Only when it is raining")], "b"),
        ("Which crop is a C4 crop?",
         [("a", "Wheat"), ("b", "Rice"), ("c", "Maize"), ("d", "Barley")], "c"),
        ("What do CAM plants store as acid during the night?",
         [("a", "Water"), ("b", "Oxygen"), ("c", "Carbon dioxide"), ("d", "Salt")], "c"),
    ],
}
