"""Allan variance: how sensor noise behaves when averaged, the Allan plot, reading slopes, bias floors and a test plan."""
CODE = "navigation4_allan_variance"
BOOK = {
    "title": "Allan Variance: Measuring Noise",
    "subtitle": "A test plan for the sensor's character",
    "chapters": [
        ("Noise in a sensor", "Every sensor has noise, which is small random change around the true value. Some noise averages away over time, and some builds up. Knowing which is which helps a designer choose a sensor."),
        ("Averaging time", "The Allan variance is computed by averaging the readings over different time spans. Each span gives one point. Plotting these points against averaging time shows how the noise behaves."),
        ("The Allan plot", "The Allan plot is a chart of these results on logarithmic scales. Its slope shows the type of noise at each averaging time. Different noise types show up as different slopes."),
        ("Reading the slope", "A slope that falls steadily as the time grows suggests random noise that averages out. A slope that rises suggests a drift that grows with time. A flat part shows the best achievable stability."),
        ("Identifying bias", "The bottom of the curve shows the smallest noise level the sensor can reach. Bias instability appears as this flat floor. It is a key number on a sensor's data sheet."),
        ("A test plan", "A simple test records a sensor at rest for many hours. The data are then analysed to produce the plot. The plan should be repeatable, with the same conditions each time."),
    ],
    "test": [
        ("What does the Allan variance study?", [("a", "The price of a sensor in different countries"), ("b", "How heavy a sensor is in each season"), ("c", "How sensor noise behaves when readings are averaged over different times"), ("d", "The colour of the sensor board")], "c"),
        ("What does the Allan plot use on its axes?", [("a", "Latitude and longitude"), ("b", "Voltage and temperature only"), ("c", "Date and colour"), ("d", "Averaging time and noise level, on logarithmic scales")], "d"),
        ("A slope that falls steadily as time increases suggests what?", [("a", "A bias that grows"), ("b", "Random noise that averages out"), ("c", "A sensor that is too heavy"), ("d", "A bright light in the room")], "b"),
        ("What does the flat floor at the bottom of the curve show?", [("a", "The best stability the sensor can reach"), ("b", "The colour of the data sheet"), ("c", "The time of day"), ("d", "The number of wires")], "a"),
        ("What is a good feature of a simple Allan test?", [("a", "It needs the sensor to move fast for hours"), ("b", "It can be done only on a moving ship"), ("c", "It is repeatable, with the same conditions each time"), ("d", "It uses no data at all")], "c"),
    ],
}
