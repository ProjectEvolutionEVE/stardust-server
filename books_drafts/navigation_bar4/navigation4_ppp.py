"""Precise Point Positioning: single-receiver precise positioning using orbit and clock corrections, float solutions and convergence."""
CODE = "navigation4_ppp"
BOOK = {
    "title": "Precise Point Positioning",
    "subtitle": "One receiver, very good corrections, and patience",
    "chapters": [
        ("Precise positioning from one receiver", "Precise Point Positioning uses one receiver and very accurate satellite orbit and clock data from outside. Standard relative positioning compares signals with a nearby base station, but PPP does not need one. The idea is to make a single receiver as precise as possible on its own."),
        ("Orbits and clocks", "Global networks estimate the satellites' exact positions and clock errors, and these corrections are supplied to the receiver. With them, the receiver removes errors that a standard fix would leave in. The quality of the answer depends on how good the corrections are."),
        ("The float solution", "At first the receiver gives a float solution, where some whole-number ambiguities in the carrier signal are not yet fixed. The position is useful but not yet at its best. Holding the solution for longer improves it."),
        ("Convergence time", "A PPP receiver needs time to settle before its answer is fully precise. This settling is called convergence, and it can often take tens of minutes. Interruptions to the signal can slow it down."),
        ("Corrections in real time", "Corrections can be applied after the fact in a processing step, or sent live over a link. Live corrections give a fix as you go, which suits moving vehicles. Both methods rest on the same physics."),
        ("How accurate it gets", "Once converged, PPP can reach centimetre-level accuracy in good conditions. Its accuracy depends on the receiver, the sky view and the quality of the corrections. It is widely used in surveying and precise machine guidance."),
    ],
    "test": [
        ("What does Precise Point Positioning use instead of a nearby base station?", [("a", "A radio mast on the coast"), ("b", "A second satellite dish in the same field"), ("c", "A map of the local streets"), ("d", "Precise satellite orbit and clock corrections")], "d"),
        ("What is the float solution?", [("a", "A position estimate in which some carrier ambiguities are not yet fixed"), ("b", "A position taken from a paper map"), ("c", "A signal that has bounced off a wall"), ("d", "The time shown on a wristwatch")], "a"),
        ("What is convergence in PPP?", [("a", "The moment a satellite comes over the horizon"), ("b", "The point where two receivers meet"), ("c", "The settling time before the answer becomes fully precise"), ("d", "The process of charging the battery")], "c"),
        ("What accuracy can a converged PPP solution reach in good conditions?", [("a", "Several kilometres"), ("b", "Centimetre-level"), ("c", "Hundreds of metres"), ("d", "Tens of kilometres")], "b"),
        ("What makes live corrections useful for a moving vehicle?", [("a", "They give a fix as the vehicle moves"), ("b", "The vehicle must stop for a whole day"), ("c", "They only work at night"), ("d", "The vehicle must carry a second receiver on its roof")], "a"),
    ],
}
