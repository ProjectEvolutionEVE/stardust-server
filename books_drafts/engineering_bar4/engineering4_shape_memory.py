"""Shape memory alloys and superelasticity: nickel-titanium, transformation temperatures, superelastic behaviour, actuators and fatigue."""
CODE = "engineering4_shape_memory"
BOOK = {
    "title": "Shape Memory Alloys and Superelasticity",
    "subtitle": "Nickel-titanium, transformation and actuators",
    "chapters": [
        ("Metals that remember a shape",
         "A shape memory alloy can be bent out of shape and then return to its original form when heated. The effect comes from a change in the metal's crystal structure. Nickel-titanium alloys, often called nitinol, are the best known example."),
        ("Transformation temperatures",
         "The change in structure happens over a range of temperatures set by the alloy's composition and processing. Engineers choose the transformation temperatures to suit the job. Small changes in composition shift these temperatures."),
        ("Superelastic behaviour",
         "Some alloys can be stretched a long way and spring back with little permanent change. This is superelasticity, and it happens at a temperature above the transformation range. It is used in springy parts that must not stay bent."),
        ("Actuators",
         "A shape memory wire can act as a compact actuator that moves when heated. It is quiet and light, but slower than many motors. Designers use it where a small, simple movement is needed."),
        ("Fatigue of the material",
         "Repeated cycling of a shape memory alloy can cause fatigue and change its behaviour over time. The useful life depends on the strain and the number of cycles. Testing under realistic cycles is needed before a design is trusted."),
        ("Choosing the alloy",
         "Engineers choose the alloy by the transformation temperature, the strain needed, the cycle life and the cost. A good choice gives reliable movement for the whole life of the product. Each application is tested with its own loads."),
    ],
    "test": [
        ("What can a shape memory alloy do?", [("a", "Stay bent forever"), ("b", "Melt on contact with air"), ("c", "Return to its original shape when heated"), ("d", "Turn into wood")], "c"),
        ("What is nitinol?", [("a", "A nickel-titanium shape memory alloy"), ("b", "A type of glass"), ("c", "A plastic bag"), ("d", "A paint brand")], "a"),
        ("What is superelasticity?", [("a", "Melting at room temperature"), ("b", "Being very hard and brittle"), ("c", "Glowing in the dark"), ("d", "Stretching a long way and springing back with little permanent change")], "d"),
        ("What is a common use for shape memory wire?", [("a", "A cooking pan"), ("b", "A compact actuator that moves when heated"), ("c", "A window pane"), ("d", "A pipe for water")], "b"),
        ("Why must fatigue be tested for shape memory alloys?", [("a", "They are always made of rubber"), ("b", "They never cycle"), ("c", "Repeated cycling can change their behaviour over time"), ("d", "Fatigue is a colour")], "c"),
    ],
}
