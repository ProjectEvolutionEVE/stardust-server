"""InSAR for Ground Movement: using radar from satellites and ground stations to measure how the land moves, a fraction of a centimetre at a time."""
CODE = "mining5_insar"
BOOK = {
    "title": "InSAR for Ground Movement",
    "subtitle": "Radar interferometry, subsidence and watching pit walls",
    "chapters": [
        ("Radar that measures motion",
         "Interferometric synthetic aperture radar, called InSAR, sends radar pulses at the ground and records the returning signal. By comparing two passes over the same area, it can detect tiny changes in distance. It works well over wide areas and from far away."),
        ("Phase",
         "The radar records the phase of each return, which is the position of the wave within its cycle. When the ground moves, the phase shifts. Each full cycle of shift is about half the radar wavelength, so the ground motion is read from these shifts."),
        ("Subsidence",
         "Mining can make the ground sink above workings or over flooded and drained areas. InSAR maps the sinking across a whole district. Maps like this show where the ground is moving and how fast."),
        ("Pit wall monitoring",
         "Ground-based radar can watch an open pit wall around the clock. It sees slow creep days or weeks before a slope fails. Operators use the warning to move people and machines out of danger."),
        ("Noise",
         "The signal can be spoiled. Water vapour in the air bends the radar, and plants or new snow change the surface so the phase no longer matches. Careful processing and a clear view of the target keep the noise low."),
        ("Alerts",
         "Good systems set alert levels in advance. When movement passes a level, people check the site and decide what to do. An alert is a prompt to look closer, and it should be confirmed on the ground."),
    ],
    "test": [
        ("What does InSAR compare to detect ground movement?",
         [("a", "The colour of the soil"), ("b", "The weight of the trucks"), ("c", "Two radar passes over the same area"), ("d", "Rainfall totals alone")], "c"),
        ("What is the phase in a radar signal?",
         [("a", "The name of the satellite"), ("b", "The money spent on the survey"), ("c", "The number of drill holes"), ("d", "The position of the wave within its cycle")], "d"),
        ("What does InSAR help map over a mining district?",
         [("a", "The price of ore"), ("b", "Subsidence, where the ground is sinking"), ("c", "The taste of the water"), ("d", "The speed of the lift")], "b"),
        ("What can a ground-based radar on a pit wall give?",
         [("a", "Warning of slow creep before a slope fails"), ("b", "A map of the stars"), ("c", "Ore grades without sampling"), ("d", "A new kind of fuel")], "a"),
        ("What can spoil an InSAR signal?",
         [("a", "Water vapour in the air and changes to the surface"), ("b", "A clear view of the target"), ("c", "Low alert levels"), ("d", "Careful processing")], "a"),
    ],
}
