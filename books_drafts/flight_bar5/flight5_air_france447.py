"""Case Study: Air France 447. Ice in the speed sensors, the autopilot disconnect, a stall, the confusion in the cockpit, the recorders and the lessons."""
CODE = 'flight5_air_france447'
BOOK = {
    "title": 'Case Study: Air France 447',
    "subtitle": 'Speed sensors, a stall and a crew that lost the picture',
    "chapters": [
        ('Pitot ice',
         'Speed on an airliner is measured with small tubes called pitot tubes, which sit outside the plane. In June 2009 ice crystals in high-altitude clouds blocked them. Without reliable speed readings, the automatic systems had to disconnect.'),
        ('Autopilot off',
         'Once the speed readings became unreliable, the autopilot switched off and the plane was handed to the pilots. The pilots had to fly by hand at high altitude. The warnings and the readings were confusing at a time of great stress.'),
        ('The stall',
         'The aircraft pitched up and lost speed, and it entered a stall, where the wings no longer lift well. The crew did not recognise the stall in time, and the plane kept falling. A stall is recovered by lowering the nose and adding power.'),
        ('Confusion',
         'The pilots received conflicting warnings, and they did not clearly agree on what was happening. Some control inputs worked against each other. The crew never fully recognised the stall before the aircraft hit the sea.'),
        ('The recorders',
         'The aircraft was lost in the Atlantic with all on board. The flight data and voice recorders were found years later, after a long search of the deep ocean. Their data showed in detail how the crew responded to the warnings.'),
        ('Lessons',
         'The accident led to clearer instructions on handling unreliable speed readings, and to better training in stall recovery at high altitude. It also showed how automation can hand a crew a hard problem with little warning. For players, the lesson is to know your basic skills well enough to use them when the automatic system steps back.'),
    ],
    "test": [
        ('What did ice block in the Air France 447 flight?',
         [('a', 'The pitot tubes that measure speed'), ('b', 'The fuel tanks'), ('c', 'The cabin doors'), ('d', 'The landing gear')], 'a'),
        ('What happened when the speed readings became unreliable?',
         [('a', 'The engines stopped at once'), ('b', 'The autopilot switched off and the pilots flew by hand'), ('c', 'The plane landed by itself'), ('d', 'The cabin lights went out')], 'b'),
        ('What is a stall?',
         [('a', 'A parked aircraft at the gate'), ('b', 'A fuel leak'), ('c', 'A loss of lift when the wings can no longer support the plane'), ('d', 'A landing on water')], 'c'),
        ('How is a stall usually recovered?',
         [('a', 'By raising the nose sharply'), ('b', 'By turning off all engines'), ('c', 'By opening the cabin door'), ('d', 'By lowering the nose and adding power')], 'd'),
        ('What did the lessons of this accident include?',
         [('a', 'Better training in stall recovery at high altitude'), ('b', 'Removing all autopilots'), ('c', 'Flying only at low altitude'), ('d', 'Banning all pilots from the cockpit')], 'a'),
    ],
}
