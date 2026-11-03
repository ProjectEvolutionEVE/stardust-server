"""The Ionospheric Delay: free electrons in the upper air that slow satellite signals."""
CODE = "navigation4_ionosphere_delay"
BOOK = {
    "title": "The Ionospheric Delay",
    "subtitle": "Free electrons that slow the signal",
    "chapters": [
        ("Free electrons", "The ionosphere is a layer of the upper atmosphere with many free electrons. The electrons affect radio signals passing through it. The effect is a delay."),
        ("Delay in the signal", "The ionosphere slows a satellite signal, so the measured distance comes out a little too long. The delay depends on the number of electrons along the path. It changes with the time of day."),
        ("Dual-frequency cancellation", "Two frequencies can be combined to cancel most of the ionospheric delay. The delay depends on frequency, and the combination removes its main part. Dual-frequency receivers use this method."),
        ("The Klobuchar model", "The Klobuchar model is a simple model whose settings are sent in GPS broadcast messages. It estimates the delay for single-frequency users. It removes roughly half of the typical delay."),
        ("Solar activity", "Solar activity changes the number of electrons in the ionosphere. More activity usually means a stronger delay. The effect varies over the solar cycle of about eleven years."),
        ("Storms", "Geomagnetic storms can disturb the ionosphere a great deal. Signals may be delayed more or lose strength. Users may see larger errors during storms."),
    ],
    "test": [
        ("What is the ionosphere?",
         [("a", "A deep sea trench"), ("b", "A type of cloud"), ("c", "A kind of rock"), ("d", "A layer of the upper atmosphere with many free electrons")], "d"),
        ("What does ionospheric delay do to a satellite signal?",
         [("a", "It speeds it up forever"), ("b", "It stops it"), ("c", "It slows it so the distance looks too long"), ("d", "It changes its colour")], "c"),
        ("How does the dual-frequency method work?",
         [("a", "It combines two frequencies to cancel most of the delay"), ("b", "It paints the signal"), ("c", "It adds noise"), ("d", "It doubles the distance")], "a"),
        ("What does the Klobuchar model do?",
         [("a", "Paints the Earth"), ("b", "Estimates the delay for single-frequency users"), ("c", "Counts satellites"), ("d", "Sets the time zone")], "b"),
        ("What does a geomagnetic storm do to the ionosphere?",
         [("a", "It makes it very disturbed"), ("b", "It makes it vanish"), ("c", "It makes it cold"), ("d", "It turns it into ice")], "a"),
    ],
}
