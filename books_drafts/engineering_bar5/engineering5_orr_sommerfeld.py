"""Flow Stability and the Orr-Sommerfeld Equation: how small disturbances grow or fade in a flow, and what that means for transition."""
CODE = "engineering5_orr_sommerfeld"
BOOK = {
    "title": "Flow Stability and the Orr-Sommerfeld Equation",
    "subtitle": "Small disturbances, growth rates and the onset of transition",
    "chapters": [
        ("Small disturbances", "A flow can be disturbed by small waves or ripples. The question is whether these disturbances grow or fade away over time and distance."),
        ("The Orr-Sommerfeld equation", "The Orr-Sommerfeld equation describes how a small disturbance grows or decays in a parallel shear flow. It is the standard tool for linear stability."),
        ("Growth rates", "If a disturbance grows, the flow can become unstable. The growth rate says how fast the disturbance grows, and it changes with the flow conditions."),
        ("Neutral curves", "A neutral curve marks the edge between growing and decaying disturbances. Conditions on one side are stable, and on the other side they are unstable."),
        ("Transition onset", "The point where disturbances begin to grow strongly marks the start of transition. Downstream of this point the flow can become turbulent."),
        ("Laminar flow control", "Keeping a flow laminar by shaping the surface delays transition. A later transition means less skin friction and less drag."),
    ],
    "test": [
        ("What does the Orr-Sommerfeld equation describe?", [("a", "How paint dries on a surface"), ("b", "How bread rises in an oven"), ("c", "How small disturbances grow or decay in a shear flow"), ("d", "How doors close on their hinges")], "c"),
        ("What is a growth rate?", [("a", "How fast a disturbance grows"), ("b", "The interest rate on a bank loan"), ("c", "The price of paint per litre"), ("d", "The size of a room")], "a"),
        ("What is a neutral curve?", [("a", "A curve in a road"), ("b", "A painted line on a floor"), ("c", "A grade of steel"), ("d", "The edge between growing and decaying disturbances")], "d"),
        ("What does transition onset mark?", [("a", "The start of a holiday"), ("b", "The start of a change from laminar to turbulent flow"), ("c", "The purchase of a boat"), ("d", "The end of a meal")], "b"),
        ("What does laminar flow control do?", [("a", "Adds drag to the body"), ("b", "Stops all flow"), ("c", "Delays transition and cuts drag"), ("d", "Makes the flow chaotic")], "c"),
    ],
}
