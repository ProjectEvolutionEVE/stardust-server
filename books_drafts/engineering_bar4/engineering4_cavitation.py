"""Cavitation: vapour bubbles that form in liquid and erode metal when they collapse, and how to prevent it in pumps."""
CODE = "engineering4_cavitation"
BOOK = {
    "title": "Cavitation: Bubbles That Bite Metal",
    "subtitle": "Vapour bubbles, collapse, pump damage and prevention",
    "chapters": [
        ("Vapour bubbles",
         "When the pressure in a liquid falls below its vapour pressure, tiny bubbles of vapour form. Pump inlets and sharp valve restrictions are common places for this to happen."),
        ("Collapse and erosion",
         "When the bubbles move into a region of higher pressure, they collapse very quickly. The collapse sends tiny high-speed jets and shock waves at nearby metal. Over time the surface pits and wears away."),
        ("Pump damage",
         "A cavitating pump is noisy, shakes, loses head and wears its impeller fast. The damage often shows as pitting on the vanes near the eye of the impeller."),
        ("Net positive suction head",
         "NPSH is the pressure margin at the pump inlet above the liquid's vapour pressure. A larger margin keeps bubbles from forming. Engineers compare the NPSH available with the NPSH the pump needs."),
        ("Prevention",
         "Keep suction lines short and wide, reduce suction lift, keep the liquid cool, and avoid sharp restrictions on the inlet side. Choose a pump designed for the duty."),
        ("Recognising it early",
         "A crackling, gravel-like noise, rising vibration and a drop in flow are early signs. Stop and check the suction side before the damage spreads."),
    ],
    "test": [
        ("When does cavitation start?",
         [("a", "When pressure drops below the vapour pressure"), ("b", "When pressure rises above 10 bar"), ("c", "When the fluid is cold"), ("d", "When the pump is painted")], "a"),
        ("What happens when cavitation bubbles collapse?",
         [("a", "They freeze"), ("b", "They release shock waves and tiny jets that erode metal"), ("c", "They turn the fluid to glass"), ("d", "They cool the pump")], "b"),
        ("What does NPSH measure?",
         [("a", "The colour of the pump"), ("b", "The weight of the impeller"), ("c", "The pressure margin at the pump inlet above vapour pressure"), ("d", "The speed of the motor")], "c"),
        ("What is an early sign of cavitation?",
         [("a", "Quiet, smooth running"), ("b", "A crackling, gravel-like noise"), ("c", "Lower vibration"), ("d", "Higher flow")], "b"),
        ("Which step helps prevent cavitation?",
         [("a", "Long, narrow suction lines"), ("b", "Short, wide suction lines"), ("c", "Higher suction lift"), ("d", "Hotter liquid")], "b"),
    ],
}
