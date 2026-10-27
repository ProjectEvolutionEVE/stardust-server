"""Sensor Networks for Exploration Camps: remote monitoring of weather, ground and equipment at camps far from the grid."""
CODE = "mining5_sensor_camp"
BOOK = {
    "title": "Sensor Networks for Exploration Camps",
    "subtitle": "Remote monitoring, power, data links and the cost of upkeep",
    "chapters": [
        ("Eyes at a remote camp",
         "An exploration camp may sit far from towns and roads. A sensor network watches weather, ground movement and equipment from the camp desk. It gives early warning and keeps records without a person walking the site every hour."),
        ("Remote monitoring",
         "Sensors send their readings to a central logger. Staff can check the readings from a laptop or phone when they have a signal. Alarms can be set for values that need quick action."),
        ("Power",
         "Sensors often run on batteries charged by solar panels. The system must be sized for the dark, cloudy days of the season. A sensor that runs out of power records nothing, so power planning matters as much as the sensor itself."),
        ("Data links",
         "Data can travel by radio, satellite or cellular links. Each link has its own range, speed and cost. Readings can be stored on the logger and sent in batches when a link is available."),
        ("Environmental sensors",
         "Weather stations, dust monitors and water-level gauges help the camp work safely. They also give a record for regulators and for the environment. Calibrated sensors give readings that can be trusted."),
        ("Maintenance and costs",
         "Sensors need cleaning, checking and replacing. Each maintenance trip costs time and money, so a good plan groups the trips together. The true cost of a network includes its upkeep for many seasons, not just its purchase price."),
    ],
    "test": [
        ("What does a sensor network at a remote camp do?",
         [("a", "It cooks the camp meals"), ("b", "It replaces the camp's staff"), ("c", "It watches weather, ground and equipment from the camp desk"), ("d", "It sells the camp's samples")], "c"),
        ("Why is power planning important for sensors?",
         [("a", "Sensors never need any power"), ("b", "Power makes the rock hotter"), ("c", "Power changes the colour of the logger"), ("d", "A sensor that runs out of power records nothing")], "d"),
        ("What are the common data links for remote sensors?",
         [("a", "Smoke signals only"), ("b", "Radio, satellite or cellular links"), ("c", "Pigeons only"), ("d", "Paper letters only")], "b"),
        ("Why are sensors calibrated?",
         [("a", "So their readings can be trusted"), ("b", "So they look smarter"), ("c", "So they weigh more"), ("d", "So they can be painted")], "a"),
        ("What should a good maintenance plan do?",
         [("a", "Group trips together to save time and money"), ("b", "Visit every sensor every minute"), ("c", "Never check the sensors"), ("d", "Replace all sensors on the first day")], "a"),
    ],
}
