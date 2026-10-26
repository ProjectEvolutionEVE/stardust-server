"""Impact Craters: how a strike from space carves a crater, and why some worlds keep theirs."""
CODE = 'science3a_craters'
BOOK = {
    "title": 'Impact Craters',
    "subtitle": 'How a strike from space carves a crater, and why some worlds keep theirs',
    "chapters": [
        ("A hit at speed",
         "A rock from space can strike the ground at many kilometres per second. The energy is released in a fraction of a second, which digs out a hole far bigger than the rock itself."),
        ("A simple crater",
         "A small impact makes a bowl-shaped crater. The rock thrown out piles up around the edge and forms a rim. Simple craters are often many times wider than the rock that made them."),
        ("Complex craters",
         "A large impact can cause the floor to rebound, and a central peak rises in the middle of the crater. Wider craters often have terraced walls, where the slumping ground forms steps."),
        ("Ejecta and rays",
         "The rock thrown out by an impact is called ejecta. It falls back around the crater. On the Moon, bright rays of ejecta can stretch across great distances from some young craters."),
        ("Erosion and keeping craters",
         "On Earth, wind, water, and moving plates wear craters away, so many old ones have vanished. The Moon and Mercury keep their craters for billions of years, because they have little weather and no moving plates."),
        ("Chicxulub",
         "The Chicxulub crater, buried under the Yucatan Peninsula in Mexico, is about 180 kilometres across. It formed about 66 million years ago, and many scientists link it to the mass extinction that ended the non-avian dinosaurs."),
    ],
    "test": [
        ("What shape is a simple crater?",
         [('a', 'A tall spike'), ('b', 'A flat plain'), ('c', 'A bowl'), ('d', 'A long trench')], 'c'),
        ("What is a central peak?",
         [('a', 'The highest point on a planet'), ('b', 'A rise in the middle of a large crater, formed by the floor rebounding'), ('c', 'A volcano in a crater'), ('d', 'A moon that orbits a crater')], 'b'),
        ("Why do craters last longer on the Moon than on Earth?",
         [('a', 'The Moon is closer to the Sun'), ('b', 'The Moon has little erosion from wind, water and moving plates'), ('c', 'Moon rock is softer than Earth rock'), ('d', 'Craters on the Moon fill with ice')], 'b'),
        ("About how wide is the Chicxulub crater?",
         [('a', 'About 18 kilometres'), ('b', 'About 180 kilometres'), ('c', 'About 1,800 kilometres'), ('d', 'About 1.8 kilometres')], 'b'),
        ("What is ejecta?",
         [('a', 'Rock thrown out by an impact'), ('b', 'Ice inside a crater'), ('c', 'A type of meteorite'), ('d', 'Lava that cools in a crater')], 'a'),
    ],
}
