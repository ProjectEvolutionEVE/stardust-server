"""Wall Functions and Near-Wall Modelling: how a flow simulation treats the thin layer next to a wall, and how the mesh must suit the model."""
CODE = "engineering5_wall_func"
BOOK = {
    "title": "Wall Functions and Near-Wall Modelling",
    "subtitle": "The viscous sublayer, the log law and y-plus targets",
    "chapters": [
        ("Near the surface", "Close to a wall the flow changes very quickly, so the mesh near the wall must capture it or a model must stand in for it. Getting this right matters a great deal for drag and heat transfer."),
        ("The viscous sublayer", "Right at the wall there is a thin sublayer where viscosity dominates. Velocity rises almost in a straight line with distance from the wall here."),
        ("The log law", "Further from the wall, the velocity follows a logarithmic law in the log layer. This is a well-known pattern in turbulent flow near a wall."),
        ("Y-plus targets", "Y-plus measures the distance from the wall in wall units. The mesh is aimed at a y-plus value that suits the chosen wall model."),
        ("Wall function limits", "A wall function skips the sublayer and relies on the log law. This saves cells, but it breaks down in flows with strong pressure gradients or separation."),
        ("Meshing choices", "The height of the first cell is picked to match the chosen wall model. A mismatch between mesh and model gives results that look sound but are wrong."),
    ],
    "test": [
        ("What is the viscous sublayer?", [("a", "A type of jam"), ("b", "A sea creature"), ("c", "A thin layer right at the wall where viscosity dominates"), ("d", "A warm room for testing")], "c"),
        ("What is the log law?", [("a", "A rule that velocity follows a logarithm in the log layer, further from the wall"), ("b", "A rule about cutting trees"), ("c", "A price list for software"), ("d", "A law on paint")], "a"),
        ("What is y-plus?", [("a", "A shop code"), ("b", "Wall distance measured in wall units"), ("c", "A bolt size"), ("d", "A type of plus sign")], "b"),
        ("What do wall functions skip?", [("a", "The computer itself"), ("b", "The whole flow"), ("c", "The viscous sublayer, relying on the log law instead"), ("d", "The mesh entirely")], "c"),
        ("What does the first cell height depend on?", [("a", "The price of the computer"), ("b", "The weather outside"), ("c", "The colour of the screen"), ("d", "The chosen wall model")], "d"),
    ],
}
