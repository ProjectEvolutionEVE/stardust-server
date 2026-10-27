"""Compressible Flow and Nozzles: when gas speeds up near the speed of sound, and how a nozzle shapes it."""
CODE = 'engineering4_nozzles'
BOOK = {
    "title": "Compressible Flow and Nozzles",
    "subtitle": "When gas speeds up near the speed of sound, and how a nozzle shapes it",
    "chapters": [
        ("Mach number",
         "The Mach number is the flow speed divided by the speed of sound in the gas. Above Mach 1 the flow is supersonic."),
        ("Choked flow",
         "In a nozzle, the flow can reach the speed of sound at the throat. Beyond that point the flow rate cannot rise further for the same upstream pressure. This is choked flow."),
        ("Isentropic relations",
         "For smooth, reversible flow, pressure, temperature and density are linked by isentropic relations. They let engineers calculate the flow through a nozzle."),
        ("Convergent-divergent nozzles",
         "A convergent nozzle narrows, and a divergent part widens after the throat. Together they can speed a gas up to supersonic speed."),
        ("Shock formation",
         "A shock is a thin layer where pressure and speed change very suddenly. Shocks form in supersonic flow and waste energy."),
        ("Why it matters",
         "These ideas set the performance of jet engines and rockets. Designing for the right flow avoids losses."),
    ],
    "test": [
        ("What is the Mach number?",
         [("a", "The paint colour"), ("b", "Flow speed divided by the speed of sound in the gas"), ("c", "The nozzle's weight"), ("d", "The room temperature")], "b"),
        ("What is choked flow?",
         [("a", "A clogged pipe"), ("b", "A paint stripe"), ("c", "A broken valve"), ("d", "Flow reaching the speed of sound at the throat, so it cannot rise further")], "d"),
        ("Where do convergent-divergent nozzles speed the flow to supersonic?",
         [("a", "The divergent part after the throat"), ("b", "The inlet"), ("c", "The painted wall"), ("d", "The outlet pipe only")], "a"),
        ("What is a shock?",
         [("a", "A loud noise only"), ("b", "A bump in the road"), ("c", "A thin layer where pressure and speed change very suddenly"), ("d", "A light")], "c"),
        ("Isentropic relations apply to which kind of flow?",
         [("a", "Smooth, reversible flow"), ("b", "Painted walls"), ("c", "People"), ("d", "Lights")], "a"),
    ],
}
