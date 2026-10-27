"""Laser Welding Keyhole Physics: the narrow vapour cavity that lets a laser weld deep, and how it can go wrong."""
CODE = "engineering5_laser_keyhole"
BOOK = {
    "title": "Laser Welding Keyhole Physics",
    "subtitle": "Keyholes, plasma plumes, pores and watching the weld",
    "chapters": [
        ("A deep, narrow hole", "In deep laser welding, a strong beam boils the metal under it and forms a narrow cavity of vapour called a keyhole. The keyhole lets the beam reach deep into the joint. Its shape decides the shape of the weld."),
        ("The plasma plume", "Metal vapour above the weld can ionise into a plasma plume. The plume can absorb and scatter some of the laser light. Its behaviour changes how much energy reaches the joint."),
        ("Porosity", "Gas can be trapped in molten metal. When the keyhole collapses or the metal freezes, the gas can stay behind as a pore. Pores weaken the joint and can be hard to see from the surface."),
        ("Beam quality", "A beam with better focus puts its energy into a smaller spot. A smaller spot gives a deeper, narrower weld with less heat spread into the part. Beam quality is a key setting for the result."),
        ("Watching the process", "Sensors and cameras can watch the light and heat that come from the weld. Changes in these signals can show a keyhole that is becoming unstable, so a fault can be caught while it forms."),
        ("Putting it together", "A steady keyhole, a controlled plume and good beam quality make sound welds. Monitoring lets an engineer see when one of these starts to drift."),
    ],
    "test": [
        ("What is a keyhole in laser welding?", [("a", "A hole drilled before the weld starts"), ("b", "A narrow cavity of vapour formed by the beam"), ("c", "The clamp that holds the part"), ("d", "A crack that forms in the weld")], "b"),
        ("What can cause porosity?", [("a", "A cold workshop"), ("b", "A very clean surface"), ("c", "Gas trapped in molten metal that forms pores"), ("d", "A bright room")], "c"),
        ("Why does better beam quality help?", [("a", "It focuses energy into a smaller spot, giving a deeper, narrower weld"), ("b", "It makes the metal lighter"), ("c", "It removes the need for shielding gas"), ("d", "It cools the joint quickly")], "a"),
        ("What is the plasma plume?", [("a", "A type of steel used in welding"), ("b", "A coolant pump"), ("c", "A sensor for the clamp"), ("d", "A cloud of vapour above the weld that can scatter laser light")], "d"),
        ("Why watch the process with sensors?", [("a", "To see faults forming during the weld"), ("b", "To make the weld colder"), ("c", "To make the beam longer"), ("d", "To add weight to the part")], "a"),
    ],
}
