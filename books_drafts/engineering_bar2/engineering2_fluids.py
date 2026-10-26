"""Fluids, Pumps and Valves: pressure in liquids and gases, and the pumps and valves that move and control them."""
CODE = 'engineering2_fluids'
BOOK = {
    "title": 'Fluids, Pumps and Valves',
    "subtitle": 'Pressure in liquids and gases, and the pumps and valves that move and control them',
    "chapters": [
        ('Pressure',
         "Pressure is force spread over an area: force divided by area. In a sealed fluid, pressure is passed on equally in every "
         "direction, which is Pascal's principle. A small push on a small piston can move a large piston, as long as the fluid is "
         "sealed in. One pascal is one newton per square metre."),
        ('Hydraulics',
         "A hydraulic system uses a sealed liquid to carry force from one place to another. Oil is used because liquids barely "
         "compress, so the push arrives firmly and at once. Hydraulic presses and brakes work this way. Air can be compressed, so "
         "systems that use air feel springy, while hydraulic systems feel firm."),
        ('Fluids in motion',
         "A fluid flows from high pressure to low. In a pipe, a narrow section makes the fluid speed up, and its pressure drops "
         "there. The flow rate equals the area times the speed, so the same flow through a narrower pipe moves faster."),
        ('Pumps',
         "A pump raises pressure to move a fluid. Positive displacement pumps trap a fixed volume and push it along. Centrifugal "
         "pumps spin the fluid outward and turn that speed into pressure. A pump must suit its fluid and pipe, or it wastes power, "
         "or cavitation, bubbles that form and collapse, damages it."),
        ('Valves',
         "A valve opens, closes or throttles a flow. A gate valve is either fully open or shut. A globe valve controls flow in "
         "steps. A check valve lets fluid through one way only. A relief valve opens when pressure gets too high, to protect the "
         "system."),
        ('Checking a fluid system',
         "Look for leaks first: a drop of oil or water shows a fault. Check seals, hoses and fittings for cracks and wear, and keep "
         "the fluid clean. Test relief valves so you know they open at the set pressure."),
    ],
    "test": [
        ("What is pressure?",
         [('a', 'Force multiplied by area'), ('b', 'Mass divided by volume'), ('c', 'Force divided by area'), ('d', 'Speed times time')], 'c'),
        ("What does a check valve do?",
         [('a', 'Lets fluid pass one way only'), ('b', 'Stops all flow for ever'), ('c', 'Measures the temperature'), ('d', 'Adds pressure to the system')], 'a'),
        ("Why is oil used in hydraulic systems rather than air?",
         [('a', 'Oil is cheaper'), ('b', 'Oil is lighter'), ('c', 'Oil is magnetic'), ('d', 'Liquids barely compress, so the push passes on firmly and at once')], 'd'),
        ("What happens to a fluid as it passes through a narrow section of pipe?",
         [('a', 'It slows down and its pressure rises'), ('b', 'It speeds up and its pressure drops'), ('c', 'It stops'), ('d', 'It turns solid')], 'b'),
        ("What does a relief valve do?",
         [('a', 'Opens when pressure gets too high, to protect the system'), ('b', 'Keeps the pressure at zero'), ('c', 'Fills the pipe with air'), ('d', 'Shuts a pump off for good')], 'a'),
    ],
}
