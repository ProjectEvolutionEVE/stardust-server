"""MEMS Gyroscope Bias Instability: flicker noise, temperature effects, stability tests and drift control."""
CODE = "navigation5_mems_bias"
BOOK = {
    "title": "MEMS Gyroscope Bias Instability",
    "subtitle": "Why tiny gyroscopes drift, and how drift is controlled",
    "chapters": [
        ("Tiny gyroscopes", "MEMS gyroscopes are tiny silicon devices, used in phones and cars. They are cheap, but their bias errors are larger than those of big precision gyroscopes."),
        ("Bias instability", "Bias instability is the slow wandering of a gyro's zero reading. It limits how long a gyro can work on its own."),
        ("Flicker noise", "Flicker noise, also called 1/f noise, is a common cause of bias instability. Its power grows at low frequencies."),
        ("Temperature", "Changes in temperature shift a MEMS gyro's bias. Good designs measure the temperature and correct for it."),
        ("Stability tests", "A stability test runs the gyro for a long time at a steady temperature and records the bias. The result is often shown as an Allan variance curve."),
        ("Drift control", "Engineers control drift with calibration, temperature models and filters that combine the gyro with other sensors. Phones use these methods every day."),
    ],
    "test": [
        ("Where are MEMS gyroscopes commonly used?",
         [("a", "In a deep mine"), ("b", "In phones and cars"), ("c", "Under the sea"), ("d", "On mountains")], "b"),
        ("What is bias instability?",
         [("a", "The slow wandering of a gyro's zero reading"), ("b", "A loud noise"), ("c", "A flower"), ("d", "A map")], "a"),
        ("What is flicker noise also called?",
         [("a", "White noise"), ("b", "Brown noise"), ("c", "1/f noise"), ("d", "Silent noise")], "c"),
        ("What changes a MEMS gyro's bias?",
         [("a", "Paint colour"), ("b", "A song"), ("c", "A fruit"), ("d", "Temperature changes")], "d"),
        ("What does a stability test record?",
         [("a", "The bias over a long period at a steady temperature"), ("b", "The price"), ("c", "A dance"), ("d", "A map")], "a"),
    ],
}
