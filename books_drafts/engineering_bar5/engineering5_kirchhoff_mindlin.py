"""Thick and Thin Plate Theories: deciding how much a plate's own shear deformation matters."""
CODE = "engineering5_kirchhoff_mindlin"
BOOK = {
    "title": "Thick and Thin Plate Theories",
    "subtitle": "Choosing how much a plate's own shear matters",
    "chapters": [
        ("What a plate is",
         "A plate is a flat member, much wider than it is thick, that carries loads mainly by bending. How to model it depends largely on how thick it is compared with its span."),
        ("Kirchhoff assumptions",
         "The Kirchhoff theory assumes that straight lines normal to the mid-surface stay straight and normal after bending. It also ignores shear strain through the thickness, which works well for thin plates."),
        ("Shear deformation in Mindlin plates",
         "The Mindlin theory lets the normal rotate separately from the surface, so shear strain through the thickness is included. It suits thicker plates, where shear adds a visible amount of extra deflection."),
        ("Thickness effects",
         "As a plate gets thicker, shear takes a larger share of the deflection. Ignoring it makes the plate look stiffer than it really is."),
        ("Shear locking",
         "A simple finite element based on the Mindlin theory can become too stiff for thin plates, a fault called shear locking. Special formulations or reduced integration avoid it."),
        ("Choosing a theory",
         "Use a thin plate theory for slender plates, and a thicker theory when the span is only a few times the thickness. Checking against a known case is the simplest test of a model."),
    ],
    "test": [
        ("What is a plate?",
         [("a", "A flat member, much wider than it is thick, that bends under load"), ("b", "A type of paint"), ("c", "A long rope"), ("d", "A ceramic bead")], "a"),
        ("What does the Kirchhoff theory ignore?",
         [("a", "Bending"), ("b", "Gravity"), ("c", "The plate's length"), ("d", "Shear strain through the thickness")], "d"),
        ("What does the Mindlin theory add?",
         [("a", "Colour"), ("b", "Heat transfer"), ("c", "Shear deformation through the thickness"), ("d", "A magnetic field")], "c"),
        ("What happens to a thick plate if shear is ignored?",
         [("a", "It looks more flexible than it is"), ("b", "It looks stiffer than it really is"), ("c", "It becomes lighter"), ("d", "Nothing changes")], "b"),
        ("What is shear locking?",
         [("a", "A bolt seizing"), ("b", "A finite element that is too stiff for thin plates"), ("c", "A paint defect"), ("d", "A crane failure")], "b"),
    ],
}
