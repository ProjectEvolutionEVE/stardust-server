"""Fault Protection and Safe Mode: how a craft notices trouble on its own and falls back to a safe state."""
CODE = "flight4_fault_protection"
BOOK = {
    "title": "Fault Protection and Safe Mode",
    "subtitle": "How a craft protects itself when something goes wrong",
    "chapters": [
        ("Watching for trouble", "Spacecraft run for years with little help from the ground. They watch their own systems and react to faults. This is called fault protection."),
        ("Watchdogs", "A watchdog is a timer that must be reset by the main software at regular intervals. If the software freezes and fails to reset it, the watchdog forces a restart or a switch to a backup."),
        ("Autonomous responses", "The craft can respond on its own to a fault. It may switch to a spare unit, turn off a faulty part or point its antenna in a safe direction. These steps happen without waiting for a command from Earth."),
        ("Safe mode steps", "Safe mode is a simple state with the basics kept alive. The craft points its solar panels at the Sun, keeps its batteries charged, and points a safe antenna toward Earth. Then it waits for the ground to take over."),
        ("Waking from safe mode", "Engineers on the ground study the logs and find the cause. They then bring the craft back to normal, one step at a time, and check each system before moving on."),
        ("False alarms", "Sometimes a sensor reports a fault that is not real. A false alarm can push a craft into safe mode and waste time. Designers try to check each alarm twice before a big response."),
    ],
    "test": [
        ("What is a watchdog timer?", [("a", "A watch you wear on your wrist"), ("b", "A timer that the main software must reset, or a restart is forced"), ("c", "A type of camera"), ("d", "A dog in the crew")], "b"),
        ("What is safe mode?", [("a", "A way to make the craft faster"), ("b", "A paint job"), ("c", "A game for the crew"), ("d", "A simple state that keeps the basics alive while the ground takes over")], "d"),
        ("Where does a craft in safe mode usually point its solar panels?", [("a", "At the Sun"), ("b", "At the floor"), ("c", "Into deep shadow"), ("d", "At the crew cabin")], "a"),
        ("Why must a craft respond on its own to a fault?", [("a", "Earth never sends commands"), ("b", "The craft has no computer"), ("c", "Commands from Earth take time to arrive"), ("d", "Faults are always invisible")], "c"),
        ("What is a risk of a sensor false alarm?", [("a", "It makes the craft invisible"), ("b", "It can push a craft into safe mode and waste time"), ("c", "It changes the colour of the Sun"), ("d", "It turns off gravity")], "b"),
    ],
}
