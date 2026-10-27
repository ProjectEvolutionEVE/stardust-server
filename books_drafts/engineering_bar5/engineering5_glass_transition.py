"""Glass Transition and Polymer Structure: amorphous and semicrystalline polymers, glass transition temperature, molecular weight and service temperature limits."""
CODE = "engineering5_glass_transition"
BOOK = {
    "title": "Glass Transition and Polymer Structure",
    "subtitle": "Why a plastic goes from hard to soft as it warms",
    "chapters": [
        ("Long chains",
         "A polymer is made of long chains of molecules. How those chains pack together decides how the plastic behaves. Some chains line up in orderly regions, and some stay tangled and random."),
        ("Amorphous and semicrystalline",
         "An amorphous polymer has chains that stay tangled. A semicrystalline polymer has some orderly regions mixed in with the tangled ones. Both kinds have a glass transition, but the semicrystalline kind also has a melting point."),
        ("The glass transition",
         "As an amorphous polymer warms, it changes from hard and glassy to soft and rubbery at a point called the glass transition temperature. Below it, the chains are locked; above it, they can slide. The change is gradual, and the exact point depends on how it is measured."),
        ("Molecular weight",
         "Longer chains, which means higher molecular weight, usually raise the glass transition temperature and improve toughness. Very short chains make a weaker plastic. Suppliers control chain length carefully for that reason."),
        ("Service temperature limits",
         "A plastic should be used well below its glass transition if it must keep its stiffness. Designers allow a margin for heat from the sun, from machines and from the process. Ignoring the margin is a common reason for failure."),
        ("Choosing a polymer",
         "The right polymer balances stiffness, heat, toughness and cost. The cheapest plastic is rarely the best value if it softens in service. Testing the plastic at the real service temperature saves the cost of a failed part."),
    ],
    "test": [
        ("What changes when an amorphous polymer goes through its glass transition?",
         [("a", "It turns into metal"), ("b", "It turns into water"), ("c", "It becomes invisible"), ("d", "It changes from hard and glassy to soft and rubbery")], "d"),
        ("What is the difference in a semicrystalline polymer?",
         [("a", "It has some orderly regions as well as tangled ones"), ("b", "It has no molecules"), ("c", "It is always white"), ("d", "It cannot be heated")], "a"),
        ("How does longer molecular chain length usually affect the glass transition temperature?",
         [("a", "It always lowers it to zero"), ("b", "It usually raises it"), ("c", "It has no effect at all"), ("d", "It makes the plastic melt at room temperature")], "b"),
        ("Why should a plastic be used well below its glass transition?",
         [("a", "To make it lighter"), ("b", "To make it print faster"), ("c", "To keep its stiffness in service"), ("d", "To stop it from being recycled")], "c"),
        ("Why is the cheapest plastic not always the best value?",
         [("a", "It is always heavier"), ("b", "It cannot be bought in bulk"), ("c", "It never changes shape"), ("d", "It may soften in service and fail")], "d"),
    ],
}
