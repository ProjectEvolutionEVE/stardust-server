"""Metal Hydrides for Hydrogen Storage: metals that soak up hydrogen like a sponge, and why the cost and weight still limit them."""
CODE = "mining5_metal_hydride"
BOOK = {
    "title": "Metal Hydrides for Hydrogen Storage",
    "subtitle": "Storing hydrogen inside metal, safely and in a small space",
    "chapters": [
        ("Hydrogen held in metal", "Some metals absorb hydrogen atoms into the gaps in their crystal structure. The result is a metal hydride. Hydrogen stored this way is held more safely than as a high pressure gas."),
        ("Interstitial hydrides", "The hydrogen sits in small spaces between the metal atoms. This is why these compounds are called interstitial hydrides. Many transition metals and rare earths form them."),
        ("Plateau pressure", "At a given temperature, a metal absorbs hydrogen over a flat pressure range called the plateau. The plateau pressure sets how easily the metal fills and releases hydrogen."),
        ("Absorbing and releasing", "Absorbing hydrogen releases heat, and releasing it takes heat in. Filling and emptying a tank therefore involve managing temperature. Repeated cycles can also crack or slowly damage the metal."),
        ("Kinetics", "The speed of filling and emptying depends on the metal surface and its particle size. Engineers add catalysts and make fine powders to speed up the reaction."),
        ("The trade-offs", "Many useful hydride metals are heavy or costly, so the amount of hydrogen per kilogram can be low. The storage is safe and compact, but the overall weight and price are the challenges."),
    ],
    "test": [
        ("What is a metal hydride?",
         [("a", "A metal that has been painted"), ("b", "A metal that has been frozen"), ("c", "A metal that has absorbed hydrogen"), ("d", "A metal that has been sewn")], "c"),
        ("Where do hydrogen atoms sit in an interstitial hydride?",
         [("a", "In the gaps between metal atoms"), ("b", "On the moon"), ("c", "Outside the container"), ("d", "In the packaging only")], "a"),
        ("What happens to heat when a metal absorbs hydrogen?",
         [("a", "Heat is always absorbed from the room"), ("b", "Heat turns into light"), ("c", "Heat stops the reaction forever"), ("d", "Heat is released")], "d"),
        ("What is the plateau in a hydride?",
         [("a", "A mountain"), ("b", "A flat pressure range where absorption happens"), ("c", "A type of fuel"), ("d", "A kind of paint")], "b"),
        ("What is a main challenge of metal hydride storage?",
         [("a", "It is too light to hold"), ("b", "It cannot be stored in a tank"), ("c", "It only works on paper"), ("d", "Often heavy or costly per kilogram of hydrogen")], "d"),
    ],
}
