"""Machining chatter and stability lobes: regenerative chatter, stability diagrams, damping, speed selection and listening for chatter."""
CODE = "engineering4_chatter"
BOOK = {
    "title": "Machining Chatter and Stability Lobes",
    "subtitle": "Regenerative chatter, stability diagrams and speed choice",
    "chapters": [
        ("Self-excited vibration",
         "Chatter is a loud, unstable vibration between the cutter and the workpiece. It leaves a rough, wavy surface and can damage the tool. The problem grows when the vibration feeds itself."),
        ("Regenerative chatter",
         "Regenerative chatter happens when each pass of the tool cuts a surface already wavy from the pass before. The wave pattern reinforces itself, and the vibration grows. The effect is a main cause of chatter in milling and turning."),
        ("Stability diagrams",
         "A stability diagram, often called a stability lobe chart, shows which combinations of spindle speed and depth of cut stay stable. Stable regions form lobes with peaks at certain speeds. Choosing a point inside a stable lobe avoids chatter."),
        ("Damping in the machine",
         "Damping absorbs vibration energy in the machine and its structure. A more damped machine tolerates deeper cuts before chatter starts. Stiffer and better-damped tool holders help the same way."),
        ("Speed selection",
         "Machinists work at the lobe peaks, where the stable depth of cut is largest, and avoid the dips between lobes, where the stable depth of cut is smallest. Sometimes a small change in speed moves the cut out of chatter. Charts and test cuts guide the choice."),
        ("Listening for chatter",
         "Experienced machinists can hear chatter as a change in the cutting sound. Sensors can also detect vibration in the spindle. Stopping early when chatter starts protects the tool and the part."),
    ],
    "test": [
        ("What is chatter?", [("a", "A loud, unstable vibration between cutter and workpiece"), ("b", "A quiet hum from a lamp"), ("c", "A type of cutting oil"), ("d", "A paint colour")], "a"),
        ("What does regenerative chatter depend on?", [("a", "The price of the machine"), ("b", "The colour of the workpiece"), ("c", "The weather outside"), ("d", "Each pass cutting a wavy surface left by the pass before")], "d"),
        ("What does a stability diagram show?", [("a", "The number of tools in a shop"), ("b", "Which combinations of spindle speed and depth of cut stay stable"), ("c", "The cost of electricity"), ("d", "The shape of the factory")], "b"),
        ("What does damping do in a machine?", [("a", "Heats the workpiece"), ("b", "Adds vibration to the cut"), ("c", "Absorbs vibration energy so deeper cuts are tolerated"), ("d", "Makes the tool longer")], "c"),
        ("What is one way to avoid chatter?", [("a", "Remove all dampers"), ("b", "Pick a speed in the dip between lobes on purpose"), ("c", "Choose a spindle speed inside a stable lobe"), ("d", "Cut at random speeds with no check")], "c"),
    ],
}
