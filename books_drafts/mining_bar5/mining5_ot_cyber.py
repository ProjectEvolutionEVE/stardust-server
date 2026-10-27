"""Cybersecurity for Control Systems: industrial networks, segmentation, threat models, incident response, patching and training."""
CODE = 'mining5_ot_cyber'
BOOK = {
    "title": "Cybersecurity for Control Systems",
    "subtitle": "Industrial networks, segmentation, threat models and patching",
    "chapters": [
        ("Control systems are a target",
         "The machines that run a mine or plant are controlled by networked systems. Attacks on these systems can stop production or endanger people. Security for control systems must put safety first."),
        ("Industrial networks",
         "Industrial networks link sensors, controllers and operator screens. Many were built long before security was a concern. Know every connection, including the ones nobody remembers adding."),
        ("Segmentation",
         "Network segmentation splits a network into zones, with controls between them. If an attacker breaks into one zone, the damage stays contained. Careful zones are one of the strongest defences."),
        ("Threat models",
         "A threat model lists how an attacker could reach a system, and what the impact would be. It guides where to spend effort first. Revisit the model when the network changes."),
        ("Incident response and patching",
         "Incident response starts with detecting and containing the threat, then restoring safe operation. Patching fixes known weaknesses, but plants often cannot stop, so patches must be planned into maintenance windows. Test before you patch."),
        ("Training",
         "Staff are the first line of defence. Training helps people spot and report suspicious activity. A simple, fast reporting route matters more than a long manual."),
    ],
    "test": [
        ("What does network segmentation do?",
         [("a", "Joins every control system to the internet"), ("b", "Removes all firewalls"), ("c", "Splits networks into zones so a breach stays contained"), ("d", "Gives every device the same password")], "c"),
        ("What is the first step of an incident response?",
         [("a", "Detect and contain the threat"), ("b", "Post the news on social media"), ("c", "Delete the logs"), ("d", "Turn off every backup")], "a"),
        ("Why is patching control systems hard?",
         [("a", "Patches are never needed"), ("b", "Systems can be left unpatched for years with no harm"), ("c", "Patches always break the plant at once"), ("d", "Plants often cannot stop, so patches must be planned into maintenance windows")], "d"),
        ("What does a threat model identify?",
         [("a", "The menu for the canteen"), ("b", "How an attacker could reach a system and what the impact would be"), ("c", "The staff holiday plan"), ("d", "The price of software")], "b"),
        ("Why train staff in cybersecurity?",
         [("a", "So they can open every email"), ("b", "So staff spot and report suspicious activity"), ("c", "So IT is no longer needed"), ("d", "So systems never need updates")], "b"),
    ],
}
