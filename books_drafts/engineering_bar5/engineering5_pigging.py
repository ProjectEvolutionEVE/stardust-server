"""Pipeline Pigging and Inline Inspection: pig design, tool runs, sensor types, defect sizing and the money side of inspection."""
CODE = "engineering5_pigging"
BOOK = {
    "title": "Pipeline Pigging and Inline Inspection",
    "subtitle": "Pigs, tool runs, sensors and defect sizing",
    "chapters": [
        ("What a pig is",
         "A pig is a device pushed through a pipeline by the flow of the product inside it. Cleaning pigs scrape away wax, sand and scale, and they are sized to fit the pipe."),
        ("Pig design",
         "A pig must fit the pipe closely enough to push the debris ahead of it, but not so tightly that it jams. Designers choose the shape, the seals and the material for the job. Bends, valves and changes in pipe size all make the design harder."),
        ("Tool runs",
         "An inspection pig, sometimes called an intelligent pig, travels the whole line and records what it finds. Each run takes time, needs planning and must be launched and received safely. Operators often run the tool again after repairs to check the work."),
        ("Sensor types",
         "Inspection tools use sensors such as magnetic flux leakage, which picks up changes in the steel, and ultrasound, which measures wall thickness by timing sound echoes. Each sensor is good at finding some kinds of damage and weaker at others."),
        ("Defect sizing",
         "Finding a defect is not enough; the operator must also know how deep and how long it is. Sizing uses calibrated signals and a known accuracy range. A defect deeper than a set share of the wall is repaired or replaced."),
        ("The money side",
         "A tool run costs money, and so does the production that stops while a line is cleaned. Operators compare the cost of cleaning and inspection runs with the cost of a leak. Clean lines also flow better, which saves energy."),
    ],
    "test": [
        ("What does a pig do inside a pipeline?",
         [("a", "It cools the product"), ("b", "It is pushed by the flow to clean or inspect the pipe"), ("c", "It paints the walls"), ("d", "It measures the air outside")], "b"),
        ("Why must a pig fit the pipe closely?",
         [("a", "To push debris ahead without jamming"), ("b", "To make it lighter"), ("c", "To keep it cold"), ("d", "To stop the product flowing")], "a"),
        ("What does an inspection tool record?",
         [("a", "The name of the operator"), ("b", "The weather above"), ("c", "What it finds along the whole line"), ("d", "The price of the product")], "c"),
        ("What does ultrasound do in an inspection tool?",
         [("a", "It measures wall thickness by timing sound echoes"), ("b", "It heats the steel"), ("c", "It seals the joints"), ("d", "It counts the seals")], "a"),
        ("Why must the operator size a defect?",
         [("a", "To know how deep and long it is before deciding on repair"), ("b", "To choose the colour of the pipe"), ("c", "To fix the price of the product"), ("d", "To count the crew")], "a"),
    ],
}
