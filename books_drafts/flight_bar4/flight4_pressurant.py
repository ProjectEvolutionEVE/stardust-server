"""Tanks and Pressurisation: how propellant is pushed to the engines, the helium that does the pushing, and the problems of liquids in motion."""
CODE = "flight4_pressurant"
BOOK = {
    "title": "Tanks and Pressurisation",
    "subtitle": "Pushing fuel to the engines, and keeping it steady",
    "chapters": [
        ("Getting fuel to the engine", "An engine needs propellant at a steady pressure and flow. Designers use one of two main ways to deliver it: pressure-fed or pump-fed."),
        ("Pressure-fed and pump-fed", "In a pressure-fed system, a gas pushes the propellant out of the tanks. In a pump-fed system, pumps move the propellant. Pressure feeds are simpler, while pumps can carry more power and are used on the largest engines."),
        ("Helium as the pusher", "Helium is often used as the pressurant, the gas that pushes. It is light, it does not react with most propellants, and it stays a gas at low temperatures."),
        ("Tank shapes", "Tanks are usually round or rounded, because curved walls hold pressure well with little metal. Inside, baffles and vanes help the liquid settle and stay where the engine can reach it."),
        ("Sloshing", "Liquid moving in a tank can push back on the craft and shake it. This is called sloshing. Designers add baffles, and they plan control gains so the craft does not fight the slosh."),
        ("Propellant management and leaks", "Propellant management keeps the liquid at the outlet, even in zero gravity. Leaks of gas or fuel can waste fuel and be dangerous, so every joint is checked before flight."),
    ],
    "test": [
        ("What is a pressurant?", [("a", "A gas that pushes propellant out of the tank"), ("b", "A type of crew food"), ("c", "A kind of paint"), ("d", "The name of a rocket")], "a"),
        ("Why is helium a common pressurant?", [("a", "It is heavy and sticky"), ("b", "It burns very well in tanks"), ("c", "It is light and does not react with most propellants"), ("d", "It has a strong smell")], "c"),
        ("What is sloshing?", [("a", "Washing the tank with soap"), ("b", "Liquid moving in a tank that can shake the craft"), ("c", "Cooling the tank with ice"), ("d", "Painting the outside")], "b"),
        ("What do baffles do inside a tank?", [("a", "Make the tank taller"), ("b", "Heat the fuel"), ("c", "Make a noise"), ("d", "Help the liquid settle where the engine can reach it")], "d"),
        ("What is the main difference between pressure-fed and pump-fed?", [("a", "One uses paint and the other uses water"), ("b", "One is in space and one is on the ground only"), ("c", "A gas pushes in one; pumps move the propellant in the other"), ("d", "There is no difference")], "c"),
    ],
}
