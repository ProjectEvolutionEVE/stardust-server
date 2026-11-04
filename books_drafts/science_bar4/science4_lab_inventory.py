"""Lab Inventory and Chemical Tracking: stock records, hazard labels, expiry dates, storage and audits."""
CODE = "science4_lab_inventory"
BOOK = {
    "title": "Lab Inventory and Chemical Tracking",
    "subtitle": "Knowing what is on the shelf, where it is and when it expires",
    "chapters": [
        ("Stock records", "A stock record lists each item, how much is held, where it is stored and when it was received. Keeping it current stops duplicate buying and lost items. A simple, shared system works best."),
        ("Hazard labelling", "Chemicals carry hazard labels, usually following the Globally Harmonized System, with pictograms and warning words. Labels must be clear and kept intact. Staff should know what each symbol means."),
        ("Expiry tracking", "Many chemicals and reagents have an expiry or retest date. Tracking these dates prevents the use of degraded stock. Expired items are removed through the correct waste route."),
        ("Chemical inventories", "A chemical inventory lists every hazardous substance in a building, with quantities. Emergency services and safety officers may need this list. Keep it accurate, because a wrong list can slow a response."),
        ("Storage compatibility", "Some chemicals react dangerously when stored together, such as acids and bases, or oxidisers and flammable materials. Storage plans keep incompatible chemicals apart. Check the safety data sheet before storing a new substance."),
        ("Audits", "Regular audits compare the records with what is on the shelves. They find missing items, expired stock and labels that have worn off. Audit findings lead to fixes, and the results are kept on file."),
    ],
    "test": [
        ("What is a stock record for?",
         [("a", "Listing staff holidays"), ("b", "Recording lab furniture colours"), ("c", "Listing each item, how much is held, where it is stored and when it was received"), ("d", "Choosing paint")], "c"),
        ("What do hazard labels show?",
         [("a", "The price of a chemical"), ("b", "Hazards, using pictograms and warning words"), ("c", "The name of the buyer"), ("d", "The weight of a box")], "b"),
        ("Why track expiry dates?",
         [("a", "To prevent use of degraded stock"), ("b", "To count the number of staff"), ("c", "To change the room temperature"), ("d", "To give prizes")], "a"),
        ("What is a chemical inventory?",
         [("a", "A list of library books"), ("b", "A menu"), ("c", "A holiday roster"), ("d", "A list of every hazardous substance in a building, with quantities")], "d"),
        ("Why must incompatible chemicals be stored apart?",
         [("a", "To save space"), ("b", "Because some react dangerously when stored together"), ("c", "To make them look neater"), ("d", "Because they are all the same colour")], "b"),
    ],
}
