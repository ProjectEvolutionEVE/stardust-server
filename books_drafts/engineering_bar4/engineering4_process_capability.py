"""Process Capability: Cp and Cpk. Checking whether a process can hold the limits the drawing asks for."""
CODE = 'engineering4_process_capability'
BOOK = {
    "title": "Process Capability: Cp and Cpk",
    "subtitle": "Checking whether a process can hold the limits the drawing asks for",
    "chapters": [
        ("Specification limits",
         "The drawing sets an upper and a lower limit for a size. Parts outside those limits are scrap or rework. The limits come from what the part must do, not from what is easy to make."),
        ("Process spread",
         "Every process makes parts that vary a little. The spread is the range the output covers, usually measured as a standard deviation. A tight spread is the goal of process control."),
        ("Capability indices",
         "Cp compares the width allowed by the limits with the spread of the process. Cpk also checks whether the process is centred between the limits, so it is the stricter measure."),
        ("Reading the numbers",
         "A Cpk of 1.33 or more is a common target in many industries. The lower the value, the more parts are likely to fall outside the limits."),
        ("Off-centre processes",
         "A process can be tight but off-centre. Such a process can have a fine Cp and a poor Cpk. Moving the centre back to the middle of the limits often helps quickly."),
        ("The cost of scrap",
         "At low capability, a larger share of parts is scrapped or reworked, and that cost adds up fast. Improving capability usually pays back through less waste."),
    ],
    "test": [
        ("What are specification limits?",
         [("a", "The upper and lower limits a size may take"), ("b", "The number of workers on a shift"), ("c", "The speed of the machine"), ("d", "The colour of the part")], "a"),
        ("What does Cp compare?",
         [("a", "The price with the colour"), ("b", "The allowed width with the process spread"), ("c", "The wages with the hours"), ("d", "The number of lights")], "b"),
        ("What does Cpk add to Cp?",
         [("a", "A bigger drawing"), ("b", "A faster machine"), ("c", "A paint check"), ("d", "A check that the process is centred between the limits")], "d"),
        ("A Cpk of 1.33 or more is:",
         [("a", "Never acceptable"), ("b", "A sign of a broken gauge"), ("c", "A common target in many industries"), ("d", "The price of steel")], "c"),
        ("Why does low capability cost money?",
         [("a", "More parts fall outside the limits and are scrapped or reworked"), ("b", "The machine uses less power"), ("c", "The workers are paid less"), ("d", "The drawing is cheaper")], "a"),
    ],
}
