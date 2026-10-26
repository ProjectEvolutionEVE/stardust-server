"""Case Study: MS Estonia. A bow visor failure in a storm, flooding of the car deck, the sinking in the Baltic, the rescue and the changes."""
CODE = 'flight5_estonia'
BOOK = {
    "title": 'Case Study: MS Estonia',
    "subtitle": 'A ferry lost in a Baltic storm, and the rules it changed',
    "chapters": [
        ('A crossing',
         'The ferry Estonia sailed from Tallinn to Stockholm in September 1994. Its route crossed the open Baltic Sea, where storms can build quickly. The ship carried passengers and vehicles on several decks.'),
        ('A bow visor',
         "The bow of a ferry like this has a large door, called a visor, that opens for loading vehicles. The visor's locks had not been properly designed for heavy seas. In a storm the visor was damaged and it was torn away."),
        ('Flooding',
         'Once the visor was lost, water poured into the car deck. The ship lost its balance and began to list. As the water rose, the ship became harder to control and then tipped further.'),
        ('The sinking',
         'The Estonia sank in the early hours of the morning, and most of those aboard died in the cold sea. The disaster was one of the worst peacetime losses at sea in Europe. Lifeboats and rafts were hard to launch in the rough weather.'),
        ('Rescue',
         'Ships and helicopters came to the scene, and some people were rescued from the water. The rescue was made harder by the storm and the cold. Many of the survivors were rescued in the first hours.'),
        ('Changes',
         'Investigators recommended changes to the design of bow doors and visors, and to the way ships are checked and certified. New rules followed to improve stability and flooding protection on ferries. For players, the lesson is that one weak part, if it fails, can bring down the whole ship.'),
    ],
    "test": [
        ('What was the name of the ferry?',
         [('a', 'Titanic'), ('b', 'Estonia'), ('c', 'Bounty'), ('d', 'Victoria')], 'b'),
        ('What part of the ship was torn away in the storm?',
         [('a', 'The funnel'), ('b', 'The radar mast'), ('c', 'The bow visor'), ('d', 'The anchor chain')], 'c'),
        ('Where did the ferry sail?',
         [('a', 'Across the Pacific'), ('b', 'Around Cape Horn'), ('c', 'Across the Sahara'), ('d', 'Between Tallinn and Stockholm, across the Baltic Sea')], 'd'),
        ('What filled the car deck after the visor was lost?',
         [('a', 'Water'), ('b', 'Sand'), ('c', 'Snow only'), ('d', 'Fuel oil only')], 'a'),
        ('What did the changes after the accident focus on?',
         [('a', 'Banning all ferries'), ('b', 'Design of bow doors and stability on ferries'), ('c', 'Removing all lifeboats'), ('d', 'Stopping all storms')], 'b'),
    ],
}
