"""Dilution of Precision: how the shape of the satellite sky changes the quality of a fix."""
CODE = "navigation4_dilution_precision"
BOOK = {
    "title": "Dilution of Precision",
    "subtitle": "How the sky's shape affects your fix",
    "chapters": [
        ("Satellite geometry", "The accuracy of a fix depends on the geometry of the satellites. Satellites spread across the sky give a better fix. Satellites bunched together give a poorer one."),
        ("HDOP and VDOP", "HDOP measures how the geometry affects horizontal position. VDOP measures how it affects height. Smaller values mean better geometry."),
        ("Good and bad skies", "A sky with satellites well spread from horizon to horizon is good. A sky with satellites bunched in one area is poor. Planning helps you choose the best time to work."),
        ("Planning observations", "Before surveying, check the predicted DOP for the planned time. Schedule the work when the DOP is low. This helps you avoid wasted time in the field."),
        ("The mask angle", "The mask angle is the lowest elevation at which the receiver uses satellites. Setting a higher mask removes weak, low satellites. This can improve quality, but it may reduce the number of satellites in use."),
        ("Predicting quality", "Predicted DOP values give a useful guide to expected quality. They do not replace measurements or checks. Combine them with field checks for a sound result."),
    ],
    "test": [
        ("What does DOP describe?",
         [("a", "How satellite geometry affects accuracy"), ("b", "The price of the satellite"), ("c", "The colour of the sky"), ("d", "The age of the receiver")], "a"),
        ("What does VDOP measure?",
         [("a", "How geometry affects speed"), ("b", "How geometry affects colour"), ("c", "How geometry affects height"), ("d", "How geometry affects the time of day")], "c"),
        ("Which sky gives a good fix?",
         [("a", "Satellites bunched in one corner"), ("b", "No satellites at all"), ("c", "Clouds only"), ("d", "Satellites spread from horizon to horizon")], "d"),
        ("What is the mask angle?",
         [("a", "The lowest elevation at which satellites are used"), ("b", "The angle of a sail"), ("c", "The tilt of the tripod"), ("d", "The angle of the wind")], "a"),
        ("What happens when you raise the mask angle?",
         [("a", "Every satellite is added"), ("b", "The receiver grows"), ("c", "Low, weak satellites are removed"), ("d", "The sky turns blue")], "c"),
    ],
}
