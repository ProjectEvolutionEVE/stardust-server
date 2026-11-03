"""Communicating Scientific Uncertainty: uncertainty language, probability statements, risk framing, visual uncertainty, audience testing and corrections."""
CODE = "science5_method_uncertainty_comm"
BOOK = {
    "title": "Communicating Scientific Uncertainty",
    "subtitle": "Saying how sure we are, clearly and honestly",
    "chapters": [
        ("Why uncertainty is part of the message",
         "Every scientific estimate has some uncertainty. Leaving it out makes a result look firmer than it is. Including it well helps people make better choices, and builds trust when results change."),
        ("Uncertainty language",
         "Words such as likely, possible and unlikely can mean different things to different readers. Pair a word with a range or a number where you can. State the level of confidence in the range, so the reader knows what it means."),
        ("Probability statements",
         "A probability statement gives the chance of an event under stated conditions. Say what the chance is over, and over what period. A bare number without a basis is easy to misread."),
        ("Risk framing",
         "Risk framing is the way a risk is presented, such as as a chance of gain or loss, or as a number of people affected. The same facts can lead to different reactions. Present the frame openly and check that it does not mislead."),
        ("Visual uncertainty",
         "Charts can show uncertainty with error bars, shaded ranges or sets of possible outcomes. Label the axes and explain the bars in the caption. A chart with no sign of spread can suggest false precision."),
        ("Audience testing and corrections",
         "Test the message with people from the audience before publishing. Check that they understand it as intended. When an error is found, publish a clear correction that states what changed and why."),
    ],
    "test": [
        ("What makes an uncertainty statement useful?",
         [("a", "Using vague words only"), ("b", "Saying the range and the level of confidence in it"), ("c", "Hiding the numbers"), ("d", "Avoiding all probabilities")], "b"),
        ("What is risk framing?",
         [("a", "The way a risk is presented, which can change how people react"), ("b", "A picture frame for the lab wall"), ("c", "A grant rule"), ("d", "A loan rule")], "a"),
        ("What is visual uncertainty?",
         [("a", "A blurry photo"), ("b", "A coloured sticker"), ("c", "Showing the spread of possible values in a chart"), ("d", "A graph with no axes")], "c"),
        ("Why test a message with the audience?",
         [("a", "To make slides shorter"), ("b", "To sell more copies"), ("c", "To check that people understand the message as intended"), ("d", "To avoid corrections")], "c"),
        ("Why publish a correction when an error is found?",
         [("a", "To hide the error"), ("b", "To lengthen the paper"), ("c", "To change the data"), ("d", "To keep the record accurate")], "d"),
    ],
}
