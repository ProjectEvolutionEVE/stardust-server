"""Medicine, bar 3 (Senior Doctor), part A: Oxygen Transport. How haemoglobin loads, releases and carries oxygen, and how carbon dioxide is carried home."""
CODE = "medicine3a_oxygen"
BOOK = {
    "title": "Oxygen Transport: The Journey of a Breath",
    "subtitle": "Haemoglobin, the oxygen grip and the way carbon dioxide returns",
    "chapters": [
        ("From air to tissue",
         "Oxygen enters the blood in the lungs and is carried by red cells to the tissues. Most of it rides on haemoglobin inside the red cells, not dissolved in the plasma. Carbon dioxide travels back the other way, from the tissues to the lungs."),
        ("Haemoglobin binds and lets go",
         "Each haemoglobin molecule can hold four oxygen molecules. It takes oxygen up where the level is high, as in the lungs, and releases it where the level is low, as in active muscle. This switching is what makes haemoglobin so useful."),
        ("The grip that changes",
         "The strength of haemoglobin's grip depends on conditions. Acid, higher temperature and more carbon dioxide make it let go of oxygen more easily. This helps working muscle receive oxygen just when it needs most during hard effort."),
        ("Carbon dioxide's ride home",
         "Carbon dioxide is carried in three ways: dissolved in the plasma, bound to haemoglobin, and as bicarbonate in the plasma. Most of it is converted into bicarbonate, a safe and efficient way to carry it back to the lungs."),
        ("Why iron matters",
         "Haemoglobin contains iron, and the iron is what lets it bind oxygen. Too little iron means fewer working red cells and less haemoglobin, so less oxygen can be carried. People then often feel tired or short of breath during effort."),
        ("One chain, many links",
         "Breathing, the lungs, the blood, the heart and the tissues form one oxygen chain. If any link is weaker, the whole supply falls. This is why fitness, rest and clean air all help the body meet its oxygen needs."),
    ],
    "test": [
        ("Where does most of the oxygen travel in the blood?",
         [("a", "Dissolved in the plasma only"), ("b", "On haemoglobin inside red cells"), ("c", "In the white cells"), ("d", "In the platelets")], "b"),
        ("What happens to haemoglobin's grip on oxygen in active muscle?",
         [("a", "It grips more tightly"), ("b", "It stops working entirely"), ("c", "It turns into plasma"), ("d", "It lets go more easily")], "d"),
        ("What element sits at the heart of haemoglobin's ability to bind oxygen?",
         [("a", "Iron"), ("b", "Calcium"), ("c", "Sodium"), ("d", "Gold")], "a"),
        ("What is the most common way carbon dioxide is carried in the blood?",
         [("a", "As pure gas bubbles"), ("b", "Inside platelets"), ("c", "As bicarbonate in the plasma"), ("d", "Bound to bones")], "c"),
        ("Which condition means the blood carries less oxygen than normal?",
         [("a", "Extra white cells"), ("b", "Fewer working red cells or less haemoglobin"), ("c", "Too many platelets"), ("d", "Lots of plasma")], "b"),
    ],
}
