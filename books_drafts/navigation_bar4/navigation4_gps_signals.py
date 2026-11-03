"""GPS Signal Structure: the carrier, the codes and the navigation message inside a GPS signal."""
CODE = "navigation4_gps_signals"
BOOK = {
    "title": "GPS Signal Structure",
    "subtitle": "What is inside the signal from a GPS satellite",
    "chapters": [
        ("The carrier", "Each GPS satellite sends a radio carrier wave. The carrier is a steady signal at a set frequency. Codes and messages are added on top of it."),
        ("Coarse and precise codes", "The coarse acquisition code is easy to find and is used for first contact. The precise code is restricted and used by authorised users. Both help the receiver measure the time the signal has taken to arrive."),
        ("The navigation message", "The navigation message is sent at a low rate. It carries the satellite's orbit data, its clock information and the status of the system. Receivers read it to find the satellite's position."),
        ("The chipping rate", "The chipping rate is how fast the code changes. The coarse code changes about a million times per second. The faster the chips, the finer the timing."),
        ("Broadcast ephemeris", "The broadcast ephemeris is the orbit information sent in the navigation message. It is accurate enough for most users. Precise orbits from other sources can improve results."),
        ("The frequency plan", "GPS uses several frequencies, such as L1 and L2. Using two frequencies helps correct for the ionosphere. The frequency plan serves both civil and military users."),
    ],
    "test": [
        ("What does each GPS satellite send as its base signal?",
         [("a", "A printed map"), ("b", "A piece of music"), ("c", "A tennis ball"), ("d", "A radio carrier wave")], "d"),
        ("What is the coarse code used for?",
         [("a", "First contact and finding the signal"), ("b", "Painting a map"), ("c", "Heating the receiver"), ("d", "Counting the crew")], "a"),
        ("What does the navigation message carry?",
         [("a", "Weather reports"), ("b", "Radio songs"), ("c", "Orbit data, clock information and system status"), ("d", "Recipes")], "c"),
        ("About how fast does the coarse code change?",
         [("a", "Once a day"), ("b", "About a million times per second"), ("c", "Once a year"), ("d", "Never")], "b"),
        ("Why are two frequencies useful?",
         [("a", "To make the satellite brighter"), ("b", "To help correct for the ionosphere"), ("c", "To change the colour of the signal"), ("d", "To shorten the day")], "b"),
    ],
}
