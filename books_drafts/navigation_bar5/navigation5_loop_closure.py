"""Loop Closure and Place Recognition: recognising a place seen before and using it to fix the map."""
CODE = 'navigation5_loop_closure'
BOOK = {
    "title": 'Loop Closure and Place Recognition',
    "subtitle": 'Revisited places, bag-of-words, verification, false matches, map correction and robustness',
    "chapters": [
        ('Revisited places',
         'When a robot comes back to a place it has seen before, it can notice the match. This is loop closure. The robot then knows its path has come full circle.'),
        ('Bag-of-words',
         'A bag-of-words method describes each image by counting the visual features it contains, using a stored vocabulary of common features. Two images with similar counts are likely to show the same place. The check is quick, so it can run on every frame.'),
        ('Verification',
         'A candidate match is checked before it is trusted. The points in the two images must agree with a single consistent geometry. A match that fails this check is thrown away.'),
        ('False matches',
         'A false match tells the system that a new place is an old one when it is not. Such a mistake can badly distort the map. Strict checks and careful thresholds keep false matches rare.'),
        ('Map correction',
         'Once a loop is closed, the past poses are adjusted so that the two sightings of the same place agree. The error that built up along the loop is spread back through the path. The map becomes more consistent.'),
        ('Robustness',
         'Loop closure works best when the robot sees varied scenes and uses good checks. Changes in light, season and viewpoint can make places hard to recognise. Good systems combine several cues to stay reliable.'),
    ],
    "test": [
        ('What is loop closure?',
         [('a', 'Recognising a place already visited and correcting the map'), ('b', 'Closing a shop'), ('c', 'Turning off a loop'), ('d', 'Ending a meeting')], 'a'),
        ('What is a bag-of-words approach?',
         [('a', 'A set of shopping bags'), ('b', 'A bag of tools'), ('c', 'Describing images by counts of visual features from a vocabulary'), ('d', 'A sound system')], 'c'),
        ('Why verify a candidate match?',
         [('a', 'To waste memory'), ('b', 'To paint pictures'), ('c', 'To delete the map'), ('d', 'To check it is geometrically consistent and avoid false matches')], 'd'),
        ('What is a false match?',
         [('a', 'A correct match'), ('b', 'Recognising a place as one already seen when it is not'), ('c', 'A missing picture'), ('d', 'A blurred image')], 'b'),
        ('What happens after a loop is closed?',
         [('a', 'The robot forgets its position'), ('b', 'The map is deleted'), ('c', 'All sensors reset'), ('d', 'Past poses are adjusted so the map agrees')], 'd'),
    ],
}
