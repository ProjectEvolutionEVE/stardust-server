"""Progressive Collapse and Structural Robustness: how a structure should still stand when one part is lost, using alternative load paths, tie forces and retrofit."""
CODE = "engineering5_progressive_collapse"
BOOK = {
    "title": "Progressive Collapse and Structural Robustness",
    "subtitle": "Designing a building to survive the loss of one part",
    "chapters": [
        ("What progressive collapse is", "Progressive collapse is when the failure of one part spreads and brings down much more of the building. A gas explosion or a vehicle impact can remove a column. Robust design aims to stop that spread."),
        ("Alternative load paths", "An alternative load path is a second way for the loads to reach the ground if one member is lost. Beams, slabs and floors can bridge over a gap. The structure is designed so that these routes exist."),
        ("Notional member removal", "A common check removes one key column or wall in a model, in turn. The structure must then still carry the loads around the gap within set limits. This test shows whether the alternative paths really work."),
        ("Tie forces", "Ties are continuous steel or reinforcement that holds the parts of a structure together. They let the floors hang or span across a lost support. Adequate ties are a key part of robust design."),
        ("Robustness requirements", "Design codes and government guidance set out requirements for robustness, based on the importance and use of the building. Higher-risk buildings need stronger measures. The requirements are written as checks the design must pass."),
        ("Retrofit", "Existing buildings can be strengthened by adding ties, columns or steel bracing. The work starts with a check of the weak points. The fix is designed so that it does not change the building's use."),
    ],
    "test": [
        ("What is progressive collapse?", [("a", "A paint that peels slowly"), ("b", "A type of door"), ("c", "A rise in the price of steel"), ("d", "When the failure of one part spreads to bring down more of the building")], "d"),
        ("What is an alternative load path?", [("a", "A road for trucks"), ("b", "A pipe for water"), ("c", "A second way for loads to reach the ground if one member is lost"), ("d", "A colour for the walls")], "c"),
        ("What does notional member removal test?", [("a", "Whether the structure still carries loads around a removed key member"), ("b", "Whether the paint is dry"), ("c", "Whether the lift works"), ("d", "Whether the windows are clean")], "a"),
        ("What do ties do?", [("a", "Hold the paint on the wall"), ("b", "Make the building lighter"), ("c", "Remove the floors"), ("d", "Hold the parts of a structure together and help span a lost support")], "d"),
        ("How is an existing building made more robust?", [("a", "By painting it a stronger colour"), ("b", "By adding ties, columns or bracing after checking its weak points"), ("c", "By removing all supports"), ("d", "By doing nothing at all")], "b"),
    ],
}
