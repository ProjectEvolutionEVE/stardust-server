"""Maritime Autonomous Surface Ships: Ships that sail with less or no crew on board."""
CODE = 'navigation5_masss'
BOOK = {
    'title': 'Maritime Autonomous Surface Ships',
    'subtitle': 'Ships that sail with less or no crew on board',
    'chapters': [
        ('Ships without crews', 'A maritime autonomous surface ship can sail with a reduced crew or with none on board. It senses the sea and makes decisions with computers.'),
        ('Levels of autonomy', 'Autonomy can range from ships with decision support to fully autonomous ships. Each level gives the crew or the shore team a different role.'),
        ('Remote control', 'Some ships are controlled from shore, with a team watching over them. Remote control needs reliable communications.'),
        ('Regulation', 'Rules for these ships are still being developed. Regulators must decide how existing rules apply and where new ones are needed.'),
        ('Sensor suites', "Radar, cameras, lidar and AIS work together to see the ship's surroundings. Having more than one sensor keeps the picture reliable."),
        ('Safety cases and trials', 'A safety case shows that the risks are managed. Trials test the ship in real conditions before it operates widely.'),
    ],
    'test': [
        ('What is a maritime autonomous surface ship?', [('a', 'A type of fish'), ('b', 'A kind of anchor'), ('c', 'A ship that can sail with reduced or no crew on board'), ('d', 'A lighthouse')], 'c'),
        ('What is remote control?', [('a', 'Using a TV remote on the bridge'), ('b', 'Painting from afar'), ('c', 'Controlling the ship from shore, needing reliable communications'), ('d', 'Mooring by post')], 'c'),
        ('What is a safety case?', [('a', 'A document showing that risks are managed'), ('b', 'A suitcase for the crew'), ('c', 'A paint tin'), ('d', 'A spare anchor')], 'a'),
        ('What do radar, cameras and AIS do together?', [('a', 'Cook meals'), ('b', 'Play music'), ('c', 'Count birds'), ('d', "Work together to see the ship's surroundings")], 'd'),
        ('What do trials do?', [('a', 'Replace the crew'), ('b', 'Test the ship in real conditions before wide use'), ('c', 'Stop all sailing'), ('d', 'Remove regulations')], 'b'),
    ],
}
