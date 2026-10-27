"""Bifurcations in Engineering Systems: how a small change in a design parameter can suddenly change a system from stable to unstable, and what that means for design."""
CODE = "engineering5_bifurcation"
BOOK = {
    "title": "Bifurcations in Engineering Systems",
    "subtitle": "Small changes that cause sudden changes in behaviour",
    "chapters": [
        ("Fixed points", "A fixed point is a state where a system stays put once it arrives there. A pendulum hanging straight down is one. Engineers ask whether a fixed point is stable, meaning small disturbances die away."),
        ("Stability change", "As a design parameter changes, a fixed point can lose or gain stability. A bifurcation is the point where this change happens. Just past it, the behaviour can look very different."),
        ("Saddle-node bifurcation", "In a saddle-node bifurcation, two fixed points meet and vanish. This can mean a system that had a steady state no longer has one. Motion then jumps to another behaviour."),
        ("Hopf bifurcation", "In a Hopf bifurcation, a fixed point loses stability and a steady oscillation appears. The size of that oscillation grows smoothly from zero in the simplest case. This is how many machines start to chatter or hum."),
        ("Design implications", "A bifurcation tells you the edge of safe operation. Designers keep parameters well away from the edge with a margin. They also check what happens beyond it, because a jump can be sudden and large."),
        ("Checking with the real machine", "Models predict where bifurcations occur, but measurements confirm them. Engineers sweep a parameter slowly and watch for the change in behaviour. This keeps the design within a safe range."),
    ],
    "test": [
        ("What is a fixed point?", [("a", "A point where a system stays put once it arrives"), ("b", "A welding joint"), ("c", "A measurement of colour"), ("d", "A point on a map of roads")], "a"),
        ("What is a bifurcation?", [("a", "A split in a road"), ("b", "A type of bolt"), ("c", "A fixed length of cable"), ("d", "A point where a change in a parameter alters stability or behaviour")], "d"),
        ("What happens in a saddle-node bifurcation?", [("a", "The system becomes heavier"), ("b", "Two fixed points meet and vanish"), ("c", "A colour changes"), ("d", "The fuel is refilled")], "b"),
        ("What does a Hopf bifurcation produce?", [("a", "A broken window"), ("b", "A change in paint"), ("c", "A fuel leak"), ("d", "A steady oscillation that appears as a fixed point loses stability")], "d"),
        ("What does a good design do near a bifurcation?", [("a", "Operates right at the edge"), ("b", "Ignores the edge"), ("c", "Keeps parameters away from the edge with a safety margin"), ("d", "Changes the parameter as fast as possible")], "c"),
    ],
}
