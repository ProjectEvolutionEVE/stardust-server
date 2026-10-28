"""Multibody Dynamics and Equations of Motion: how a machine made of linked rigid parts moves, and how engineers write and solve the equations for it."""
CODE = "engineering5_multibody"
BOOK = {
    "title": "Multibody Dynamics and Equations of Motion",
    "subtitle": "Linked rigid parts, the constraints between them, and how the motion is computed",
    "chapters": [
        ("What a multibody system is", "A multibody system is a set of rigid parts connected by joints, such as a robot arm, a suspension or a crane. Each part has mass and inertia, and it moves in three dimensions. The aim is to predict how the whole set moves under the forces acting on it."),
        ("Constraints", "A joint is a constraint: it removes some freedom of motion. A pin joint lets a part turn about one axis, while a sliding joint lets it move along one line. The equations must respect every constraint at every moment."),
        ("Writing the equations", "Newton's laws can be applied to each part, with the joint forces added as unknowns. The Lagrange method uses energy instead, and often gives fewer equations. Both lead to a set of equations linking accelerations, forces and constraints."),
        ("Solving in time", "The equations are solved step by step using numerical integration, such as a Runge-Kutta method. The step size must be small enough to follow fast motion. Too large a step gives wrong or unstable results."),
        ("Checking the model", "A model is only useful if it matches reality. Engineers compare its predictions with measured motion from a test rig. They also check that total energy and momentum behave sensibly when no outside forces act."),
        ("Using the results", "The model shows loads in joints, bending in links and the time a motion takes. Designers use these to size bearings, pick motors and avoid parts that hit each other. Good models save many costly prototypes."),
    ],
    "test": [
        ("What is a multibody system?", [("a", "One large part with no joints"), ("b", "A fluid moving through pipes"), ("c", "Rigid parts connected by joints"), ("d", "A single spring and mass")], "c"),
        ("What does a joint do in the equations?", [("a", "It removes some freedom of motion, as a constraint"), ("b", "It adds mass to the part"), ("c", "It changes the colour of the model"), ("d", "It stops all motion")], "a"),
        ("What does the Lagrange method use to write the equations?", [("a", "Only the colour of each part"), ("b", "The weather forecast"), ("c", "The number of bolts"), ("d", "Energy")], "d"),
        ("Why must the step size of a numerical solver be small enough?", [("a", "To make the file smaller"), ("b", "To follow fast motion and keep the result stable"), ("c", "To make the screen brighter"), ("d", "To remove the joints")], "b"),
        ("How is a multibody model checked?", [("a", "By drawing it in a different colour"), ("b", "By doubling every mass"), ("c", "By removing all constraints"), ("d", "By comparing its predictions with measured motion")], "d"),
    ],
}
