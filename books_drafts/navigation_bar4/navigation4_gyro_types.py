"""Gyroscope types: spinning mechanical gyros, ring laser gyros and fibre-optic gyros, with drift and cost."""
CODE = "navigation4_gyro_types"
BOOK = {
    "title": "Gyroscopes: Spinning, Ring and Fibre",
    "subtitle": "Three ways to sense turning",
    "chapters": [
        ("Keeping a direction", "A gyroscope keeps pointing the same way unless a turning force acts on it. This lets a navigation system sense rotation. Early ships and aircraft relied on gyros for steady headings."),
        ("The spinning gyro", "A mechanical gyro is a heavy wheel spinning on bearings. Its spin axis stays fixed in space while the case turns around it. Friction in the bearings causes drift, which limits accuracy."),
        ("The ring laser gyro", "A ring laser gyro sends two laser beams round a closed loop in opposite directions. When the device turns, the beams take slightly different times, and the difference shows the rotation. It has no spinning parts."),
        ("The fibre-optic gyro", "A fibre-optic gyro works on the same principle, with light sent through a long coil of optical fibre. It has no moving parts and is robust. It is common in modern aircraft and vehicles."),
        ("Drift", "Every gyro drifts, meaning its reading slowly changes even when it is still. Drift is often measured in degrees per hour. Lower drift costs more, so the choice depends on the job."),
        ("Cost and use", "Spinning gyros are now mostly found in older or special equipment. Ring laser and fibre-optic gyros suit aircraft, ships and spacecraft. The cheapest sensors are small silicon devices, and they have larger drift."),
    ],
    "test": [
        ("What keeps a mechanical gyroscope pointing the same way?", [("a", "Its spinning mass and its fixed spin axis"), ("b", "Strong magnets in the case"), ("c", "Air pumped through a tube"), ("d", "A battery in every corner")], "a"),
        ("How does a ring laser gyro sense rotation?", [("a", "The beam bends when it hits the ground"), ("b", "Beams travelling round a loop in opposite directions take slightly different times"), ("c", "The laser gets brighter when the craft is still"), ("d", "A sound wave is picked up by a microphone")], "b"),
        ("What is drift in a gyro?", [("a", "A change of colour in the case"), ("b", "The noise made by the bearings only"), ("c", "The gyro flying off its mount"), ("d", "A slow change in its reading even when it is still")], "d"),
        ("What is a key advantage of a fibre-optic gyro?", [("a", "It never drifts at all"), ("b", "It needs no power"), ("c", "It has no moving parts"), ("d", "It spins faster than a ring laser")], "c"),
        ("Which unit is commonly used to measure gyro drift?", [("a", "Degrees per hour"), ("b", "Litres per second"), ("c", "Kilograms per metre"), ("d", "Volts per amp")], "a"),
    ],
}
