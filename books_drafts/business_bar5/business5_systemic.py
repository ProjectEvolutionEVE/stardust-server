"""Systemic Risk and Financial Networks: banks linked by debt, contagion, too connected to fail, stress that spreads, and designing safer networks."""
CODE = "business5_systemic"
BOOK = {
    "title": "Systemic Risk and Financial Networks",
    "subtitle": "Banks linked by debt, contagion, and designing safer networks",
    "chapters": [
        ("Linked by debt", "Banks and firms lend to each other and hold each other's debts. This web of links brings benefits in good times and risks in bad times. One failure can reach others through those links."),
        ("Contagion", "Contagion means trouble spreading from one institution to others. When a bank fails, the firms that lent to it may be hurt, and they may fail too. The chain can spread quickly if people panic."),
        ("Too connected to fail", "Some firms are so central that their failure would cause severe damage across the system. This is often called too connected to fail, or too big to fail. The idea shapes rules for banks and regulators."),
        ("Stress that spreads", "Stress in one part of a network can spread through shared exposures to the same assets. Many institutions can be hit at once if they hold similar assets. Diversity can help, but correlated holdings can undo it."),
        ("The Haldane view", "Andrew Haldane of the Bank of England has written about how financial networks behave. He has argued that tight links can make a whole system fragile. His work helped bring network thinking into central banking."),
        ("Designing safer networks", "Safer networks hold more capital, limit large exposures, and test how shocks would spread. Rules can require firms to plan for their own failure. The goal is a system that bends under stress instead of breaking."),
    ],
    "test": [
        ("What is contagion?",
         [("a", "A cold"), ("b", "A type of loan"), ("c", "Trouble spreading from one institution to others"), ("d", "A bank holiday")], "c"),
        ("What does too connected to fail mean?",
         [("a", "Firms that never lend"), ("b", "Firms with no links"), ("c", "Firms that are too small"), ("d", "Firms so central that their failure would cause severe damage")], "d"),
        ("Who at the Bank of England has written about financial networks?",
         [("a", "Andrew Haldane"), ("b", "Edward Tufte"), ("c", "Samuel Insull"), ("d", "Theodore Vail")], "a"),
        ("What can make stress spread through a network?",
         [("a", "Diverse holdings only"), ("b", "Shared exposures to the same assets"), ("c", "Calm markets"), ("d", "Lower debt")], "b"),
        ("What helps make a financial network safer?",
         [("a", "Hiding exposures"), ("b", "Ignoring shocks"), ("c", "Removing all capital"), ("d", "Holding more capital and limiting large exposures")], "d"),
    ],
}
