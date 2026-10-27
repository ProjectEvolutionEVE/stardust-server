"""Stress Relaxation in Bolted Joints: why the clamp force in a bolt slowly falls, and how to plan for it."""
CODE = "engineering5_bolt_relax"
BOOK = {
    "title": "Stress Relaxation in Bolted Joints",
    "subtitle": "Preload, embedding, thermal cycling and retightening",
    "chapters": [
        ("Clamping force", "A bolt holds parts together by stretching and creating clamping force, called preload. The preload is what keeps a joint tight and sealed."),
        ("Embedding", "When a joint settles, the mating surfaces press slightly into each other. The bolt stretch drops a little, so the preload falls. This is embedding."),
        ("Thermal cycling", "Heating and cooling change the size of parts and bolts. Over repeated cycles, the preload can change each time, sometimes settling lower."),
        ("Gasket creep", "A gasket can slowly flatten under load. As it does, the joint loses clamp, and the preload falls further."),
        ("Preload loss", "These effects combine to reduce the clamp over time. A joint that has lost too much preload may leak or come loose."),
        ("Retightening schedules", "A plan sets when to check and retighten the bolts. The schedule is based on the joint's service conditions and on past experience with similar joints."),
    ],
    "test": [
        ("What is preload?", [("a", "A type of paint for bolts"), ("b", "A kind of gas used in welding"), ("c", "The price of a nut"), ("d", "The clamping force a stretched bolt creates")], "d"),
        ("What is embedding?", [("a", "Surfaces pressing into each other and reducing the preload"), ("b", "Painting the bolt head"), ("c", "Making a hole in a plate"), ("d", "Drilling into a wall")], "a"),
        ("What does thermal cycling do to preload?", [("a", "It removes the bolt"), ("b", "It makes the bolt blue"), ("c", "It can change preload with each heat and cool cycle"), ("d", "It stops the joint for good")], "c"),
        ("What is gasket creep?", [("a", "A gasket that glows in the dark"), ("b", "A gasket slowly flattening under load, which loses preload"), ("c", "A gasket that floats on oil"), ("d", "A gasket that moves fast under load")], "b"),
        ("What does a retightening schedule do?", [("a", "Sets when to check and retighten bolts"), ("b", "Paints the bolts"), ("c", "Sells the bolts"), ("d", "Removes the threads")], "a"),
    ],
}
