"""Noise Exposure Limits and Dosimetry: equal-energy rules, dose calculation, measurement practice, controls and hearing conservation."""
CODE = "engineering5_noise_exposure"
BOOK = {
    "title": "Noise Exposure Limits and Dosimetry",
    "subtitle": "Measuring how much noise a worker takes in, and keeping it within limits",
    "chapters": [
        ("Why noise is measured",
         "Loud noise at work can damage hearing over time. Engineers measure the noise a worker is exposed to, compare it with set limits, and act where the limit is exceeded. Measurement comes before any control."),
        ("The equal-energy rule",
         "The equal-energy rule says that the sound energy is what counts. Each rise of 3 decibels in the level halves the time a worker can safely spend at that level. This rule is used in the widely followed NIOSH and ISO approaches."),
        ("Dose calculation",
         "A noise dose is the share of the allowed exposure that a worker has received in a day. If a worker uses up the full allowance, the dose is one hundred percent. Doses from different noise levels are added together to give the total."),
        ("Measurement practice",
         "Exposure is measured with a calibrated sound level meter or a personal dosimeter worn by the worker. Measurements should cover typical work, including the loud and quiet periods. Results are checked and recorded so they can be compared over time."),
        ("Controls",
         "Noise is best reduced at its source, such as by buying quieter machines or fitting enclosures and dampers. Where that is not enough, the path of the sound can be blocked or the worker can be moved away from it. Personal protection is the last line of defence."),
        ("Hearing conservation programmes",
         "A hearing conservation programme combines monitoring, controls, training and regular hearing checks. It aims to protect workers before damage occurs. The programme is reviewed as the workplace and its machines change."),
    ],
    "test": [
        ("What does the equal-energy rule say?",
         [("a", "Each rise of 3 decibels halves the allowed exposure time"), ("b", "Each rise of 10 decibels doubles it"), ("c", "Time does not matter"), ("d", "Noise only matters at night")], "a"),
        ("What is a noise dose?",
         [("a", "A pill for hearing"), ("b", "A paint sample"), ("c", "The share of the allowed exposure that a worker has received"), ("d", "A shouting contest")], "c"),
        ("What is a key part of good measurement practice for noise?",
         [("a", "Guessing the levels"), ("b", "Using a calibrated sound level meter or a dosimeter"), ("c", "Asking the crew"), ("d", "Using a ruler")], "b"),
        ("What is a hearing conservation programme?",
         [("a", "A radio station"), ("b", "A paint plan"), ("c", "A sale of earplugs only"), ("d", "A set of measures, including monitoring, controls and checks, that protects workers' hearing")], "d"),
        ("Which is an example of a noise control?",
         [("a", "Reducing noise at its source, such as with enclosures or quieter machines"), ("b", "Turning up the music"), ("c", "Painting the walls bright"), ("d", "Removing the windows")], "a"),
    ],
}
