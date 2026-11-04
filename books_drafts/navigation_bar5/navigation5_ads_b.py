"""ADS-B Surveillance: Aircraft that tell others where they are."""
CODE = 'navigation5_ads_b'
BOOK = {
    'title': 'ADS-B Surveillance',
    'subtitle': 'Aircraft that tell others where they are',
    'chapters': [
        ('Broadcasting position', 'ADS-B lets an aircraft broadcast its own position, height and speed. Other aircraft and ground stations can receive these messages.'),
        ('The GNSS source', "The position comes from the aircraft's satellite navigation system. Accurate satellite data is what makes the broadcasts useful."),
        ('The message', 'Each message carries an identity code, position, height and other data. The format is standard so that many different receivers can read it.'),
        ('Coverage', 'Coverage depends on receivers on the ground and in other aircraft. Remote areas are harder to cover unless more receivers are added.'),
        ('Security', 'ADS-B messages are not encrypted. That makes them open to spoofing and to errors, so systems must check them carefully.'),
        ('Separation', 'Controllers and pilots use ADS-B to keep safe distances between aircraft. It supports better awareness, especially where radar is limited.'),
    ],
    'test': [
        ('What does ADS-B broadcast?', [('a', 'Music'), ('b', 'Weather jokes'), ('c', 'The menu of the cabin'), ('d', "An aircraft's position, height and speed")], 'd'),
        ('Where does ADS-B position data usually come from?', [('a', 'A satellite navigation system on the aircraft'), ('b', 'A paper chart'), ('c', 'A radio station only'), ('d', "Passengers' phones")], 'a'),
        ('Why is ADS-B coverage harder in remote areas?', [('a', 'The sun is too bright'), ('b', 'Remote areas have no aircraft'), ('c', 'Fewer receivers are available on the ground and in other aircraft'), ('d', 'Radios are banned')], 'c'),
        ('Why are ADS-B messages a security concern?', [('a', 'They are not encrypted, so they can be spoofed'), ('b', 'They are too heavy'), ('c', 'They use paper'), ('d', 'They cannot be received')], 'a'),
        ('What is ADS-B used for?', [('a', 'Printing tickets'), ('b', 'Mixing drinks'), ('c', 'Growing crops'), ('d', 'Keeping safe separation between aircraft')], 'd'),
    ],
}
