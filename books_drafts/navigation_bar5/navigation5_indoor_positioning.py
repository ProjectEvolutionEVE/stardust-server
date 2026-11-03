"""Indoor Positioning and Wayfinding: how signals inside buildings are used to locate people, and the practical limits of doing so."""
CODE = 'navigation5_indoor_positioning'
BOOK = {
    "title": 'Indoor Positioning and Wayfinding',
    "subtitle": 'Wi-Fi fingerprinting, beacons, building models, errors, privacy and deployment',
    "chapters": [
        ('Why indoors is hard',
         'GNSS signals from satellites are weak inside buildings, so they often cannot give a position indoors. Other signals must be used to find a person inside a large building.'),
        ('Wi-Fi fingerprinting',
         'Wi-Fi fingerprinting records the signal strength from nearby access points at many known spots. A device then matches its current readings to the recorded ones to estimate where it is.'),
        ('Beacons',
         'Small beacons placed around a building send out short radio signals. A device that hears several beacons can estimate its place by the strength of each. Beacons are simple to add to a building.'),
        ('Building models',
         'A building model is a map that shows walls, doors and floors. Positioning is more accurate when the estimate is kept inside the walkable spaces of the model.'),
        ('Errors',
         'Walls, people and furniture change the signals, so positions can jump or drift. Filters smooth out these jumps. Results are usually good to a few metres, not to the centimetre.'),
        ('Privacy and deployment',
         'Location data inside a building is personal. Systems should collect only what they need, store it briefly and explain how it is used. Deployment also needs maintenance, as beacons and access points must be kept working.'),
    ],
    "test": [
        ('Why is GNSS often weak inside buildings?',
         [('a', 'Buildings give off heat'), ('b', 'Buildings are always made of glass'), ('c', 'Its satellite signals are weakened by the building'), ('d', 'Buildings have no roofs')], 'c'),
        ('What does Wi-Fi fingerprinting match?',
         [('a', 'Colours of walls'), ('b', 'Current signal readings to readings recorded at known spots'), ('c', 'Sounds in the street'), ('d', 'Names of rooms only')], 'b'),
        ('How do beacons help find a device?',
         [('a', 'By their colour'), ('b', 'By their weight'), ('c', 'By their age'), ('d', 'By the strength of the signals heard from several beacons')], 'd'),
        ('Why do building models help positioning?',
         [('a', 'They keep the estimate inside walkable spaces'), ('b', 'They make walls disappear'), ('c', 'They stop all signals'), ('d', 'They count the people')], 'a'),
        ('What should a system do with indoor location data?',
         [('a', 'Share it with everyone'), ('b', 'Keep it forever'), ('c', 'Print it on walls'), ('d', 'Collect only what it needs and store it briefly')], 'd'),
    ],
}
