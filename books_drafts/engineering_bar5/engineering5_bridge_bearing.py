"""Bridge Bearings and Expansion Joints: how a bridge is allowed to move with heat, load and time while it still carries its weight."""
CODE = "engineering5_bridge_bearing"
BOOK = {
    "title": "Bridge Bearings and Expansion Joints",
    "subtitle": "How bridges move, turn and carry their loads safely",
    "chapters": [
        ("Why bridges must move", "A bridge grows and shrinks as its temperature changes. Traffic, wind and the slow creep of concrete also cause movement. If the bridge were fixed rigidly, these movements would crack it, so it is built to move in controlled ways."),
        ("The job of a bearing", "A bearing sits between the deck and the pier or abutment. It carries the vertical load safely into the support. It also lets the deck slide or turn in the directions it must move."),
        ("Elastomeric bearings", "An elastomeric bearing is a block of rubber layered with thin steel plates. The rubber flexes to allow movement and rotation, and the steel plates stop the rubber from bulging out under load. These bearings are simple, quiet and need little upkeep."),
        ("Expansion joints", "An expansion joint is a gap across the deck that lets the two sides move apart and together. It must be sealed so that water and salt do not reach the structure below. Traffic passes over the joint, so it must also be smooth and strong."),
        ("Designing for movement", "Engineers calculate the largest movement expected in each direction, from temperature range, traffic and time. The bearing and joint are then chosen to allow that full movement with a safety margin. A design that ignores movement will fail early."),
        ("Keeping access for care", "Bearings and joints wear, so they must be easy to inspect and replace. Jacking points and access space are planned at the design stage. Regular inspection finds cracks, leaks and stiff parts before they cause damage."),
    ],
    "test": [
        ("Why does a bridge need to move in controlled ways?", [("a", "To look more modern"), ("b", "To make traffic go faster"), ("c", "To remove the need for piers"), ("d", "To avoid cracks from temperature and load changes")], "d"),
        ("What is the main job of a bearing?", [("a", "To store rainwater"), ("b", "To light the road at night"), ("c", "To carry the vertical load and allow controlled movement"), ("d", "To measure traffic speed")], "c"),
        ("What are the steel plates inside an elastomeric bearing for?", [("a", "To stop the rubber bulging out under load"), ("b", "To make the bearing heavier"), ("c", "To carry electricity"), ("d", "To paint the bearing")], "a"),
        ("What does an expansion joint allow?", [("a", "Water to pool on the deck"), ("b", "The bridge to stop moving"), ("c", "Cars to skip the road surface"), ("d", "The two sides of the deck to move apart and together")], "d"),
        ("How is the movement a bearing must allow chosen?", [("a", "By guessing from the colour of the deck"), ("b", "By calculating the largest expected movement plus a safety margin"), ("c", "By copying the last bridge built"), ("d", "By waiting to see what happens")], "b"),
    ],
}
