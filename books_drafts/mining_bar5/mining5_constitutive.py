"""Constitutive Models for Rock: the rules that describe how rock stretches, yields, cracks and weakens under load, and how they are calibrated."""
CODE = "mining5_constitutive"
BOOK = {
    "title": "Constitutive Models for Rock",
    "subtitle": "Elasticity, plasticity, damage, strain softening and calibration",
    "chapters": [
        ("Rules for how rock responds",
         "A constitutive model is a set of rules that links stress, the load on rock, to strain, how much it changes shape. The model says how rock behaves before and after it breaks. Good models make design calculations trustworthy."),
        ("Elasticity",
         "In the elastic range, rock springs back when the load is removed. The stiffness is described by Young's modulus, and the sideways effect is described by Poisson's ratio. Elastic behaviour is the simplest part of the model."),
        ("Plasticity",
         "Past a yield point, rock deforms permanently. Plasticity describes this permanent change of shape. Models must say where yield begins and how the permanent change grows."),
        ("Damage",
         "Damage means the rock is cracking inside. As microcracks grow, the rock becomes softer and weaker. A damage model follows this loss of stiffness as the load increases."),
        ("Strain softening",
         "Strain softening means the strength falls after the peak is reached. A rock that softens can carry less load as it deforms further. Ignoring softening can make a design look safer than it is."),
        ("Calibration and use in design",
         "Models are calibrated with laboratory tests and field measurements. A model that fits one test may fail on another, so the fit must be checked. Engineers use calibrated models to predict how a pit wall or tunnel will behave."),
    ],
    "test": [
        ("What does a constitutive model link?",
         [("a", "Ore grade and price"), ("b", "Drill bits and boots"), ("c", "Stress and strain"), ("d", "Gold and silver")], "c"),
        ("What does Young's modulus describe?",
         [("a", "The colour of the rock"), ("b", "The weight of the drill"), ("c", "The number of joints"), ("d", "How stiff rock is in the elastic range")], "d"),
        ("What is plasticity?",
         [("a", "Plastic bags around core"), ("b", "Permanent change of shape after the yield point"), ("c", "A type of rock sample"), ("d", "A kind of drill rod")], "b"),
        ("What happens in strain softening?",
         [("a", "The strength falls after the peak is reached"), ("b", "The strength rises forever"), ("c", "The rock turns into water"), ("d", "The rock changes colour")], "a"),
        ("How are models calibrated?",
         [("a", "With laboratory tests and field measurements"), ("b", "By guessing the answer"), ("c", "By using only one test ever"), ("d", "By asking the drill crew to vote")], "a"),
    ],
}
