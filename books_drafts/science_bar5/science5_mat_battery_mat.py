"""Battery Cathode and Electrolyte Materials: how ions move in and out of battery electrodes, and why batteries wear down."""
CODE = "science5_mat_battery_mat"
BOOK = {
    "title": "Battery Cathode and Electrolyte Materials",
    "subtitle": "What happens inside a battery when it charges and discharges",
    "chapters": [
        ("Intercalation", "Intercalation is the movement of ions in and out of the layers of a host crystal. In lithium-ion batteries, lithium ions slip between the layers as the battery charges and discharges. The host structure stays largely intact."),
        ("Capacity", "Capacity is how much charge a material can store for each gram. A higher capacity lets a battery hold more energy for its weight. Engineers balance capacity against other properties."),
        ("Voltage", "The voltage of a cell depends on the difference in energy between the two electrode materials. Choosing materials with the right energies sets the voltage. Voltage and capacity together set the stored energy."),
        ("Electrolyte chemistry", "The electrolyte carries ions between the electrodes. It must conduct ions well and must not conduct electrons. If it conducted electrons, the battery would short out."),
        ("Interfaces", "The boundary between an electrode and the electrolyte matters a great deal. A protective layer called the SEI often forms there. A good SEI keeps the cell stable, and a poor one wastes charge."),
        ("Degradation", "Repeated cycles of charge and discharge slowly wear the materials down. Cracks, side reactions and lost contact all reduce capacity over time. Designers work to slow each of these."),
    ],
    "test": [
        ("What is intercalation?",
         [("a", "Freezing"), ("b", "Ions moving in and out of a host crystal's layers"), ("c", "Burning"), ("d", "Melting")], "b"),
        ("What is the capacity of a battery material?",
         [("a", "How much charge it can store"), ("b", "How heavy it is"), ("c", "How much it costs"), ("d", "Its colour")], "a"),
        ("What must an electrolyte do?",
         [("a", "Conduct electrons quickly"), ("b", "Be a metal"), ("c", "Glow"), ("d", "Carry ions between the electrodes without conducting electrons")], "d"),
        ("What is the SEI in a battery?",
         [("a", "A kind of battery case"), ("b", "A brand name"), ("c", "A thin protective layer that forms at the electrode and electrolyte boundary"), ("d", "A type of wire")], "c"),
        ("What slowly wears battery materials down?",
         [("a", "Repeated charge and discharge cycles"), ("b", "Silence"), ("c", "Sunlight alone"), ("d", "A smell")], "a"),
    ],
}
