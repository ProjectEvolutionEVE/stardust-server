"""Dams and spillways: gravity, arch and earth dams, uplift pressure, spillway capacity, seepage and lessons from failures."""
CODE = "engineering4_dams"
BOOK = {
    "title": "Dams and Spillways",
    "subtitle": "Dam types, uplift, spillways, seepage and the lessons of failure",
    "chapters": [
        ("Three main dam types",
         "A gravity dam holds back water by its own great weight. An arch dam pushes its load into the valley walls through its curve. An earth dam is built from compacted soil and rock, and relies on its width and its core to keep water in."),
        ("Uplift pressure",
         "Water under a concrete dam pushes upward on its base. This uplift reduces the weight that keeps the dam stable. Designers add drains and grout curtains to lower the uplift pressure."),
        ("Spillway capacity",
         "A spillway lets flood water pass the dam safely. It must carry the largest flood the design expects, so that the water never flows over the top of the dam uncontrolled. Spillways are sized for a chosen flood level."),
        ("Seepage control",
         "Water seeps slowly through the foundation and the body of every dam. Too much seepage can carry soil away and cause a failure called piping. Cutoff walls, filters and drains keep seepage under control."),
        ("Monitoring the dam",
         "Engineers fit instruments to read pressure, movement and seepage over time. Regular inspections spot cracks, wet patches and changes early. A dam is watched for its whole working life."),
        ("Lessons from failures",
         "Past dam failures taught engineers to study geology, check spillways carefully and design for extreme floods. Many failures came from foundation problems, overtopping or seepage that was not noticed in time. Each lesson is now part of dam design rules."),
    ],
    "test": [
        ("How does a gravity dam hold back water?", [("a", "By floating on the reservoir"), ("b", "By paint on the surface"), ("c", "By a thin sheet of glass"), ("d", "By its own great weight")], "d"),
        ("What is uplift pressure?", [("a", "A type of crane"), ("b", "Water pushing upward on the base of a dam, which reduces stability"), ("c", "The speed of the wind"), ("d", "Rain falling on the crest")], "b"),
        ("What must a spillway be able to carry?", [("a", "Only a small trickle"), ("b", "Traffic across the dam"), ("c", "The largest flood the design expects, so the water passes safely"), ("d", "Nothing at all")], "c"),
        ("What is piping?", [("a", "A water pipe running along the top of a dam"), ("b", "A type of spillway gate"), ("c", "A failure where seepage carries soil away"), ("d", "A painting method")], "c"),
        ("What do past dam failures mainly teach engineers?", [("a", "To design for extreme floods and check foundations and seepage carefully"), ("b", "To stop studying geology"), ("c", "To build dams without spillways"), ("d", "To avoid all monitoring")], "a"),
    ],
}
