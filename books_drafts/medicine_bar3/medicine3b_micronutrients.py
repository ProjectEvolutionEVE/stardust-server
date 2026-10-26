"""Medicine, bar 3 (Senior Doctor), part B: Micronutrients in Depth. Vitamins and minerals in detail: what each does, and why a varied diet covers most needs."""
CODE = "medicine3b_micronutrients"
BOOK = {
    "title": "Micronutrients in Depth",
    "subtitle": "Vitamins and minerals in detail: what each one does, and what happens when one runs short",
    "chapters": [
        ("Small amounts, large jobs",
         "Vitamins and minerals are needed in small amounts, but each has a job that few other nutrients can do. Vitamins are organic compounds, and minerals are elements such as iron and calcium. The body cannot make most of them, so food must supply them."),
        ("Fat-soluble vitamins",
         "Vitamins A, D, E and K dissolve in fat and are stored in the body's fat and liver. Vitamin A supports sight. Vitamin D helps the gut take in calcium. Vitamin K helps the blood clot. Because they are stored, very large amounts over a long time can build up and cause harm."),
        ("Water-soluble vitamins",
         "The B vitamins and vitamin C dissolve in water and are not stored for long, so a regular supply matters. Vitamin B12 helps the nerves and red blood cells work. Vitamin C is needed to make collagen, a protein in skin, gums and bone. A long shortage of vitamin C causes scurvy."),
        ("Iron and the blood",
         "Iron is part of haemoglobin, the protein that carries oxygen in red blood cells. Too little iron makes it harder to carry oxygen, and a person can feel tired and short of breath. Iron comes from both meat and plant foods, and vitamin C eaten in the same meal helps the body take up iron from plants."),
        ("Calcium, iodine and zinc",
         "Calcium builds bone and helps muscles and nerves work. Iodine is needed by the thyroid gland to make hormones that set the pace of the body's chemistry. Zinc is part of many enzymes and supports healing and the immune system."),
        ("Variety covers most needs",
         "A varied diet of vegetables, fruit, whole grains, pulses, dairy or other calcium sources, and protein covers most micronutrient needs. If a shortage is suspected, a doctor can check and advise. Too much of some vitamins and minerals can also be harmful."),
    ],
    "test": [
        ("Which vitamin is needed to make collagen?",
         [("a", "Vitamin A"), ("b", "Vitamin C"), ("c", "Vitamin D"), ("d", "Vitamin K")], "b"),
        ("Which mineral is part of haemoglobin?",
         [("a", "Calcium"), ("b", "Iodine"), ("c", "Iron"), ("d", "Zinc")], "c"),
        ("What is iodine needed for in the body?",
         [("a", "Helping the thyroid gland make hormones"), ("b", "Carrying oxygen in the blood"), ("c", "Helping the blood clot"), ("d", "Making vitamin D in the skin")], "a"),
        ("Which condition is caused by a long shortage of vitamin C?",
         [("a", "Night blindness"), ("b", "Goitre"), ("c", "Scurvy"), ("d", "Anaemia from a lack of iron")], "c"),
        ("Which fat-soluble vitamin helps the blood clot?",
         [("a", "Vitamin B12"), ("b", "Vitamin C"), ("c", "Vitamin E"), ("d", "Vitamin K")], "d"),
    ],
}
