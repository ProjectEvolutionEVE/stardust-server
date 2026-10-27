"""Prestressed Concrete Design: tendon profiles, prestress losses, post-tensioning, cracking limits and load balancing."""
CODE = "engineering5_prestress"
BOOK = {
    "title": "Prestressed Concrete Design",
    "subtitle": "Building in squeeze so concrete can carry more load",
    "chapters": [
        ("Squeeze before the load",
         "Concrete is strong in squeeze but weak in pull. Prestressed concrete puts steel tendons under tension and anchors them in the concrete, so the concrete is squeezed before any load arrives. The squeeze helps it resist cracking."),
        ("Tendon profiles",
         "The tendon is not always straight. Its path, called the profile, follows the bending moments of the beam. A curved profile pushes up on the beam and can carry much of its own weight."),
        ("Prestress losses",
         "Some of the squeeze is lost over time. Friction in the duct, shrinkage and creep of the concrete, and slip at the anchors all reduce it. Engineers add up these losses to be sure enough squeeze remains."),
        ("Pre-tensioning and post-tensioning",
         "In pre-tensioning, tendons are stretched before the concrete is cast. In post-tensioning, the concrete is cast first and the tendons are stretched afterward against the hardened concrete. Each method suits different jobs."),
        ("Cracking limits",
         "Design codes limit how much tension the concrete may carry at service loads. Keeping the section within these limits controls cracks and protects the steel from rust. The check is part of every design."),
        ("Load balancing",
         "Load balancing is a design method. Engineers choose a tendon profile that pushes up with a force equal to the loads on the beam. The beam then feels little bending from those loads, which makes design simpler and cheaper."),
    ],
    "test": [
        ("What does prestressing do to concrete?",
         [("a", "It makes it lighter than air"), ("b", "It melts the surface"), ("c", "It puts it under compression before the load arrives"), ("d", "It dissolves the cement")], "c"),
        ("What are prestress losses?",
         [("a", "Loss of money on a job"), ("b", "Loss of workers"), ("c", "Loss of paint"), ("d", "Loss of squeeze from friction, shrinkage, creep and anchor slip")], "d"),
        ("How is post-tensioning done?",
         [("a", "The concrete is cast first, then the tendons are stretched against it"), ("b", "The tendons are painted before casting"), ("c", "The concrete is frozen first"), ("d", "The tendons are never stretched")], "a"),
        ("Why do cracking limits matter?",
         [("a", "They make the beam heavier"), ("b", "They control cracks and protect the steel from rust"), ("c", "They change the beam's colour"), ("d", "They remove the need for steel")], "b"),
        ("What is load balancing in prestressed design?",
         [("a", "Weighing the concrete on a scale"), ("b", "Painting the beam in stripes"), ("c", "Choosing a tendon profile whose upward push balances the loads"), ("d", "Removing all the tendons")], "c"),
    ],
}
