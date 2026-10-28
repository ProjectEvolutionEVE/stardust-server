"""Solid-State Battery Electrolytes: solid materials that carry lithium ions, why interfaces and dendrites are the hard problems, and how cells are built."""
CODE = "mining5_solid_elec"
BOOK = {
    "title": "Solid-State Battery Electrolytes",
    "subtitle": "Solid materials that carry ions, and the problems they must solve",
    "chapters": [
        ("What an electrolyte does", "In a battery, the electrolyte carries ions between the two electrodes. Ordinary batteries use a liquid, which can leak and burn. A solid electrolyte could be safer and allow denser designs."),
        ("Ions moving through solids", "Ions move through a solid by hopping between open sites in the crystal. Ceramics such as garnet-type lithium lanthanum zirconium oxide conduct ions well at room temperature."),
        ("Interfaces", "The contact between the solid electrolyte and the electrode can add resistance. Good cells need the two solids to touch closely, which is hard when both are rigid."),
        ("Dendrites", "Lithium metal can grow thin spikes called dendrites through pores or grain boundaries. Dendrites can short a cell. Makers study dense ceramics and careful pressure to stop them."),
        ("Making a cell", "Thin ceramic layers are pressed and sintered, and the electrodes are bonded on. Each step must be controlled, because small flaws can lead to cracks or poor contact."),
        ("Why the effort", "If the problems are solved, a solid-state cell could hold more energy in the same space and be safer in use. This is why the work continues."),
    ],
    "test": [
        ("What does the electrolyte do in a battery?",
         [("a", "Makes the battery glow"), ("b", "Adds colour to the case"), ("c", "Stores water"), ("d", "Carries ions between the electrodes")], "d"),
        ("How do ions move through a solid electrolyte?",
         [("a", "By swimming in the solid"), ("b", "By hopping between open sites in the crystal"), ("c", "By flying out of the cell"), ("d", "They do not move at all")], "b"),
        ("What is a dendrite?",
         [("a", "A thin spike of lithium that can short a cell"), ("b", "A tree in a forest"), ("c", "A type of fuel"), ("d", "A colour of paint")], "a"),
        ("What is the hard problem at the interface?",
         [("a", "The colour of the solid"), ("b", "The smell of the cell"), ("c", "Contact resistance between two rigid solids"), ("d", "The price of the box")], "c"),
        ("Why might a solid-state cell be attractive?",
         [("a", "It could be safer and hold more energy in the same space"), ("b", "It makes no electricity"), ("c", "It must be filled with water"), ("d", "It only works in the dark")], "a"),
    ],
}
