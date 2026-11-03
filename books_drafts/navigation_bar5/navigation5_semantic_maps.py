"""Semantic Mapping: maps that record what things are, not only where they are."""
CODE = 'navigation5_semantic_maps'
BOOK = {
    "title": 'Semantic Mapping',
    "subtitle": 'Object labels, scene graphs, uses, uncertainty, updates and planning',
    "chapters": [
        ('Object labels',
         'A semantic map adds a label to each object it sees, such as chair, door or tree. The label tells the robot what the object is. A plain map only shows that something is there.'),
        ('Scene graphs',
         'A scene graph links objects by their relations, such as a cup on a table or a door next to a window. It describes the scene the way people do. This makes the map easier to reason about.'),
        ('Uses',
         'Semantic maps help robots follow instructions such as bring the cup from the kitchen. They also help people find their way in buildings. Knowing what things are makes many tasks simpler.'),
        ('Uncertainty',
         'Labels can be wrong, especially in poor light or from a long way off. Each object is given a confidence score. Low-confidence labels are checked again before they are relied on.'),
        ('Updates',
         'Objects move and scenes change, so the map must be updated. New sightings can confirm, change or remove an object. Old information is dropped when it no longer matches.'),
        ('Planning',
         'A robot plans routes and tasks using the semantic map. It can avoid the things it should not touch and go to the things it needs. Good planning depends on an accurate and up-to-date map.'),
    ],
    "test": [
        ('What is a semantic map?',
         [('a', 'A map that records what objects are, not just where they are'), ('b', 'A map of words'), ('c', 'A map of ocean depths'), ('d', 'A map of time zones')], 'a'),
        ('What is a scene graph?',
         [('a', 'A painted wall'), ('b', 'A line chart'), ('c', 'A shop list'), ('d', 'Objects linked by relations, such as on top of or next to')], 'd'),
        ('Why do semantic maps help planning?',
         [('a', 'They show colours only'), ('b', 'They hide objects'), ('c', 'A robot can plan using what objects are and where they are'), ('d', 'They remove obstacles')], 'c'),
        ('What uncertainty is there in a semantic map?',
         [('a', 'None at all'), ('b', 'Only in the colour'), ('c', 'A label can be wrong, so each object has a confidence'), ('d', 'Only in the size of the paper')], 'c'),
        ('Why must maps be updated?',
         [('a', 'To change the weather'), ('b', 'Because objects move and the scene changes'), ('c', 'To remove the robot'), ('d', 'To delete labels')], 'b'),
    ],
}
