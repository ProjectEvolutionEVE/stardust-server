"""Proximity Operations Rules: the careful discipline of flying close to another craft, and the Mir collision."""
CODE = 'flight5_a_prox_ops'
BOOK = {
    "title": 'Proximity Operations Rules',
    "subtitle": 'Flying close to another craft with discipline',
    "chapters": [
        ('Approach ellipsoids',
         'When a craft approaches a station, it follows a defined approach zone, often drawn as an ellipsoid around the target. Staying inside the zone keeps the approach safe. Leaving it triggers a review.'),
        ('Hold points',
         'Hold points are planned stops during an approach, where the craft stops and checks itself before going on. They give the team time to read the data and decide. A hold is cheap insurance.'),
        ('Keep-out zones',
         'A keep-out zone is a volume that a craft must not enter, usually around a station or a sensitive part. Planners set these zones so that a small error cannot cause contact. Their limits are written into the approach plan.'),
        ('Abort corridors',
         'An abort corridor is a safe path a craft can take to pull away quickly. It is planned in advance and rehearsed. When something goes wrong, the craft follows the corridor away from the target.'),
        ('The Mir collision',
         'In 1997 a Progress cargo craft hit the Mir space station during a manual docking test, damaging a solar array and the module it struck. The crew survived and the station was repaired. The accident taught hard lessons about discipline and rehearsal.'),
        ('Discipline',
         'The lesson of close approaches is simple: follow the plan, respect the zones, and stop when unsure. Each rule exists because someone was once hurt or nearly hurt. Good teams keep those lessons alive.'),
    ],
    "test": [
        ('What is an approach ellipsoid?',
         [('a', 'A type of bread'), ('b', 'A drink for the crew'), ('c', 'A kind of rocket fuel'), ('d', 'A zone that a craft follows during a safe approach to a target')], 'd'),
        ('What is a hold point?',
         [('a', 'A planned stop during an approach to check and decide'), ('b', 'A hole in a wall'), ('c', 'A place to store food'), ('d', 'A part of the paint')], 'a'),
        ('What is a keep-out zone?',
         [('a', 'A volume that a craft must not enter'), ('b', 'A park for the crew'), ('c', 'A parking lot for cars'), ('d', 'A fuel tank')], 'a'),
        ('What happened when a Progress craft hit Mir in 1997?',
         [('a', 'It landed on the Moon'), ('b', 'It damaged the station during a manual docking test, and the crew survived'), ('c', 'It sank in a lake'), ('d', 'It turned into a planet')], 'b'),
        ('What is an abort corridor?',
         [('a', 'A hallway full of tools'), ('b', 'A sealed tunnel for cargo'), ('c', 'A safe path a craft can take to pull away quickly'), ('d', 'A line painted on a road')], 'c'),
    ],
}
