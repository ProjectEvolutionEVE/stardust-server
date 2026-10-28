"""Gravity Gradiometry Surveys: measuring how gravity changes from place to place, which shows dense ore and rock hiding below."""
CODE = "mining5_grav_grad"
BOOK = {
    "title": "Gravity Gradiometry Surveys",
    "subtitle": "Gradient tensors, instruments, ore density and airborne surveys",
    "chapters": [
        ("Gravity that changes",
         "Gravity is not exactly the same everywhere. Dense rock pulls a little harder than light rock, and that difference is tiny. A gradiometer measures how gravity changes from one point to the next, which is easier to read than the total."),
        ("Gradient tensors",
         "The change in gravity is described by a tensor, a set of values for the change in each direction. A symmetric tensor has five independent values, so a full survey gives a rich set of data. These values point toward the edges of dense bodies."),
        ("Instrument design",
         "Modern gradiometers use pairs of sensitive accelerometers, often spinning or rotating, to cancel out movement. The instrument must hold very steady, and its design decides how small a change it can detect."),
        ("Ore density",
         "Dense ore such as iron-rich rock or massive sulphides gives a strong gradient signal. A survey works only where the ore is denser than the rock around it. Density measurements on samples are needed to read the results."),
        ("Airborne surveys",
         "Gradiometers can fly in aircraft over a large area. The aircraft is always moving, so the data must be corrected for its motion. Flying lines are close together to cover the ground well."),
        ("Noise and interpretation",
         "Vibration, turbulence and aircraft manoeuvres add noise. Many different shapes can give the same gravity signal, so interpretation needs geology and drill results. The map suggests where to look, and drilling confirms what is there."),
    ],
    "test": [
        ("What does a gravity gradiometer measure?",
         [("a", "The total weight of the rock"), ("b", "The temperature of the air"), ("c", "How gravity changes from one point to the next"), ("d", "The colour of the soil")], "c"),
        ("Why are gradient data easier to read than total gravity?",
         [("a", "They are always larger in size"), ("b", "They do not need any instrument"), ("c", "They ignore all rock"), ("d", "They show sharper changes that point to the edges of dense bodies")], "d"),
        ("What helps a gradiometer cancel unwanted movement?",
         [("a", "Loud music"), ("b", "Pairs of sensitive accelerometers, often rotating"), ("c", "A bigger hole"), ("d", "Less sunlight")], "b"),
        ("When does a gravity survey work best?",
         [("a", "Where the ore is denser than the rock around it"), ("b", "Where all rock has the same density"), ("c", "Where the air is empty"), ("d", "Where there is no rock at all")], "a"),
        ("Why is drilling still needed after a gravity survey?",
         [("a", "Because many shapes can give the same signal, so drilling confirms what is there"), ("b", "Because gravity survey maps are never useful"), ("c", "Because drilling makes gravity stronger"), ("d", "Because the aircraft needs fuel")], "a"),
    ],
}
