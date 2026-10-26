"""Entry Corridors: the narrow band of angles a craft must follow to come back through the air safely."""
CODE = 'flight5_a_entry_corridor'
BOOK = {
    "title": 'Entry Corridors',
    "subtitle": 'The narrow band of angles for a safe return',
    "chapters": [
        ('Coming in too steep',
         'If a craft enters the air too steeply, it slows very quickly and the heating and deceleration become extreme. The structure and the crew would be put under dangerous loads. Entry that is too steep is not survivable for people.'),
        ('Coming in too shallow',
         'If the entry angle is too shallow, the craft can bounce off the top of the air, like a stone skipping on water, and head back into space. It may then be lost, or be forced to come down later at a place no one planned.'),
        ('Skip-out',
         'A skip-out is the bounce that happens when a craft enters too shallow. Careful designers avoid it by choosing the right angle. Sometimes a controlled skip is used on purpose to reduce heating or to reach a target.'),
        ('The Apollo corridor',
         'Apollo capsules were built with an uneven weight, so that the air pushed them to one side. This lift let the crew steer within a narrow corridor. The crew could widen or narrow their path to reach the planned landing zone.'),
        ('Lift and control',
         'Lift from the air can be used to steer a returning craft. By turning the capsule, the crew or computer changes the direction of the lift. This keeps the path inside the corridor and within the limits of heat and load.'),
        ('The Shuttle',
         'The Space Shuttle also used lift and a careful path to come back through the air. Its corridor was narrow, and its flight plans were built around it. The corridor is a fact of physics that every returning craft must respect.'),
    ],
    "test": [
        ('What happens to a craft that enters the air too steeply?',
         [('a', 'It becomes a satellite'), ('b', 'It gains fuel'), ('c', 'Heating and deceleration become extreme and dangerous'), ('d', 'It turns into a planet')], 'c'),
        ('What is a skip-out?',
         [('a', 'A jump from a plane'), ('b', 'A type of landing gear'), ('c', 'A fuel leak'), ('d', 'A bounce off the top of the air that happens when entry is too shallow')], 'd'),
        ('How did Apollo capsules steer within the entry corridor?',
         [('a', 'They used their uneven weight so the air pushed them to one side'), ('b', 'They used wings like a bird'), ('c', 'They used sails'), ('d', 'They used a parachute only')], 'a'),
        ('What does lift from the air let a returning craft do?',
         [('a', 'Change the direction of its path by turning'), ('b', 'Fly without any speed'), ('c', 'Go back to the pad'), ('d', 'Stop the Sun')], 'a'),
        ('Why must every returning craft respect the entry corridor?',
         [('a', 'Because the corridor is a painted line'), ('b', 'Because it is a fact of physics that limits heat and load'), ('c', 'Because the air is always hot'), ('d', 'Because the crew asks for it')], 'b'),
    ],
}
