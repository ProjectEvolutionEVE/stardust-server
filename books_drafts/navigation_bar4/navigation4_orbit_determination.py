"""Orbit determination from tracking data: range and Doppler, filters, fitting, covariance and updates."""
CODE = "navigation4_orbit_determination"
BOOK = {
    "title": "Orbit Determination from Tracking",
    "subtitle": "Turning measurements into a best estimate",
    "chapters": [
        ("Finding an orbit from data", "Orbit determination uses tracking data to estimate where a spacecraft really is and how it moves. The data come from ground stations. The answer is a best estimate, not a certainty."),
        ("Range and Doppler", "Range is the distance from a station to the craft, found from the time a signal takes to travel. Doppler is the shift in frequency caused by motion toward or away from the station. Both give information about the orbit."),
        ("The filter", "A filter combines new data with the previous estimate to produce a new one. It weighs new data against what is already known. Filters keep the estimate up to date."),
        ("The fit", "A fit adjusts the orbit model to match many measurements. The best fit is the one with the smallest total error. Checking the fit shows whether the model is good."),
        ("The covariance", "The covariance describes how uncertain the estimate is. It shows the size and shape of the error. Mission planners use it to judge risk."),
        ("Updates", "New tracking data arrive regularly and update the estimate. An orbit is refined over time as more data come in. Quiet periods let the uncertainty grow."),
    ],
    "test": [
        ("What does orbit determination use?", [("a", "Weather reports from the sea"), ("b", "Photographs of the crew"), ("c", "Tracking data from ground stations"), ("d", "Sound from a distant city")], "c"),
        ("What is Doppler in tracking?", [("a", "A dent in the craft's hull"), ("b", "A frequency shift caused by motion toward or away from the station"), ("c", "A command sent by the crew"), ("d", "The colour of the radio signal")], "b"),
        ("What does a filter do?", [("a", "Combines new data with the previous estimate"), ("b", "Turns the data into music"), ("c", "Deletes all old data at once"), ("d", "Sends the data to a printer")], "a"),
        ("What does a good fit achieve?", [("a", "The largest error possible"), ("b", "The shortest trip for the crew"), ("c", "A new colour for the model"), ("d", "The smallest total error between model and measurements")], "d"),
        ("What does the covariance describe?", [("a", "How heavy the spacecraft is"), ("b", "How uncertain the estimate is"), ("c", "The number of ground stations"), ("d", "The time of the next lunch")], "b"),
    ],
}
