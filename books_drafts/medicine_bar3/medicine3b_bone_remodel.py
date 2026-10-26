"""Medicine, bar 3 (Senior Doctor), part B: Bone Remodelling. How bone is constantly rebuilt, the role of calcium and vitamin D, and what low gravity does to the balance."""
CODE = "medicine3b_bone_remodel"
BOOK = {
    "title": "Bone Remodelling: Building and Breaking Down",
    "subtitle": "Bone is rebuilt all the time, and load and calcium keep the balance",
    "chapters": [
        ("Bone is alive",
         "Bone is living tissue that is constantly being rebuilt. Old bone is removed, and new bone is laid down in its place. This ongoing renewal is called remodelling, and it goes on throughout life."),
        ("Two teams",
         "Two kinds of cells do the work. Osteoclasts break down old bone and release its minerals. Osteoblasts build new bone by laying down a framework and filling it with minerals. In a healthy skeleton the two teams stay in balance."),
        ("Calcium and phosphate",
         "Bone is hard because of minerals, mainly calcium and phosphate, set into a flexible framework of protein. The body keeps blood calcium steady, even when food is short, partly by drawing on the calcium stored in bone. Vitamin D helps the gut absorb calcium from food."),
        ("Load tells bone what to do",
         "Bone responds to the forces placed on it. Regular loading, such as walking, running and lifting, signals the bone-building team to strengthen the bone where the load falls. When loading is removed, the balance tips toward breakdown, and bone density starts to fall."),
        ("Bone in low gravity",
         "In low gravity the skeleton carries far less weight. Bone building slows, while breakdown continues at a similar pace, so the balance tips toward loss. Crews tend to lose the most density in the weight-bearing hips and legs, and bone does not always recover fully after a long mission."),
        ("Protecting bone",
         "Strength exercise that loads the bones is the main way to protect them, on Earth or aboard a ship. Enough vitamin D and calcium from food support the minerals in bone. Bone density can be measured to show trends early, and a doctor can help with any worry about bone health."),
    ],
    "test": [
        ("What are osteoclasts?",
         [("a", "Cells that build new bone"), ("b", "Cells that break down old bone"), ("c", "Cells that carry oxygen"), ("d", "Cells that make skin")], "b"),
        ("Which mineral, together with phosphate, gives bone its hardness?",
         [("a", "Iron"), ("b", "Sodium"), ("c", "Calcium"), ("d", "Potassium")], "c"),
        ("What does bone respond to by growing stronger?",
         [("a", "Loads and forces, such as walking, running and lifting"), ("b", "Loud music"), ("c", "Cold air"), ("d", "Sweet drinks")], "a"),
        ("What happens to bone in low gravity when there is little loading?",
         [("a", "Bone building slows while breakdown carries on, so density falls"), ("b", "Bone grows thicker"), ("c", "Bone stops changing altogether"), ("d", "Bone turns into muscle")], "a"),
        ("Which vitamin helps the gut absorb calcium from food?",
         [("a", "Vitamin C"), ("b", "Vitamin B12"), ("c", "Vitamin A"), ("d", "Vitamin D")], "d"),
    ],
}
