"""Medicine, bar 3 (Senior Doctor), part A: Blood and Its Parts. Plasma, red cells, white cells and platelets, and what each one carries or does."""
CODE = "medicine3a_blood"
BOOK = {
    "title": "Blood and Its Parts",
    "subtitle": "Plasma, red cells, white cells and platelets, and what each one does",
    "chapters": [
        ("A liquid tissue",
         "Blood is a liquid tissue that travels through the whole body. About half of its volume is a pale fluid called plasma, and the rest is made of cells and cell fragments. Blood carries nutrients, wastes, hormones, oxygen and heat."),
        ("Plasma: the carrier",
         "Plasma is mostly water, with dissolved salts, sugars, proteins, hormones and wastes. Some of its proteins help with clotting and immunity. Plasma is the route along which everything else in the blood is moved."),
        ("Red cells: the oxygen carriers",
         "Red blood cells are packed with haemoglobin, a protein that binds oxygen in the lungs and releases it in the tissues. Mature red cells have no nucleus, which leaves more room for haemoglobin. They live for around four months before they are replaced."),
        ("White cells: the defenders",
         "White blood cells are the body's defenders, and there are several kinds with different jobs. They travel in the blood and move into tissues when they are needed. The immune system book covers how these cells work together."),
        ("Platelets: the plug",
         "Platelets are small cell fragments that gather at a damaged blood vessel. They stick together to form a plug, and a set of clotting proteins then builds a mesh that holds it in place. Clotting is a normal, life-saving process that stops bleeding."),
        ("Making new blood",
         "Blood cells are made all the time in the bone marrow, inside the bones, and old cells are removed and replaced. The marrow needs good nutrition, including iron, to make healthy red cells. Blood production is a steady process rather than a one-off event."),
    ],
    "test": [
        ("What is the liquid part of blood called?",
         [("a", "Plasma"), ("b", "Marrow"), ("c", "Bile"), ("d", "Lymph")], "a"),
        ("What do red blood cells mainly carry?",
         [("a", "Bones"), ("b", "Germs"), ("c", "Oxygen, using haemoglobin"), ("d", "Hormones only")], "c"),
        ("Why do mature red blood cells have no nucleus?",
         [("a", "Because they are dead cells that cannot be used"), ("b", "To make them heavier"), ("c", "To carry bacteria"), ("d", "To make room for haemoglobin")], "d"),
        ("What do platelets help to do?",
         [("a", "Digest food"), ("b", "Form a plug at a damaged blood vessel and start clotting"), ("c", "Filter the urine"), ("d", "Make hormones")], "b"),
        ("Where are new blood cells made?",
         [("a", "In the bone marrow inside the bones"), ("b", "In the stomach"), ("c", "In the heart valves"), ("d", "On the surface of the skin")], "a"),
    ],
}
