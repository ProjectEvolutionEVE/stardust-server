"""Methane and Cryogenic Engines: why some engines burn very cold methane, and what that asks of the people who build them."""
CODE = "flight5_s_methane"
BOOK = {
    "title": "Methane and Cryogenic Engines",
    "subtitle": "Why some engines burn methane, and why the fuel has to be kept cold",
    "chapters": [
        ("Cold fuels",
         "Methane, liquid oxygen and liquid hydrogen are liquids only when kept very cold. Such fuels are called cryogenic propellants. They pack a lot of energy into their weight."),
        ("Why methane",
         "Methane burns cleanly and leaves less soot than some other fuels, which helps an engine stay clean between uses. It is also easier to handle than liquid hydrogen, which is far colder."),
        ("Storage and boil-off",
         "Cold fuel slowly warms and turns to gas, a problem called boil-off. Tanks must be insulated, and the gas has to be vented or managed."),
        ("Built for reuse",
         "A reusable rocket needs engines that can be checked, cleaned and fired again many times. A clean burn helps make that practical."),
        ("Mars and its air",
         "Methane could be made on Mars from carbon dioxide in the air and hydrogen from water, through a chemical process called the Sabatier reaction. Some people see this as a way to refuel a rocket for the trip home."),
        ("A trade-off",
         "Cryogenic engines bring power and a clean burn, but they need careful insulation and frequent checks. Engineers weigh each choice against the job."),
    ],
    "test": [
        ("What is a cryogenic propellant?",
         [("a", "A fuel kept very cold so it stays liquid"), ("b", "A fuel that glows"), ("c", "A solid powder"), ("d", "Plain water in a tank")], "a"),
        ("What is boil-off?",
         [("a", "A fuel being burned"), ("b", "An engine cooling down"), ("c", "Radio noise"), ("d", "Cold fuel warming up and turning into gas")], "d"),
        ("Why is methane attractive for reusable engines?",
         [("a", "It needs no tank at all"), ("b", "It burns cleanly and leaves less soot"), ("c", "It freezes at room temperature"), ("d", "It works without air")], "b"),
        ("What is the Sabatier reaction used to make?",
         [("a", "Hydrogen from sunlight"), ("b", "Oxygen from rock"), ("c", "Methane from carbon dioxide and hydrogen"), ("d", "Steel from ice")], "c"),
        ("What must the storage tanks for cold fuel have?",
         [("a", "Insulation"), ("b", "Paint only"), ("c", "Open lids"), ("d", "Wooden walls")], "a"),
    ],
}
