"""Drilling Programmes and Hole Design: choosing azimuth, dip, depth and drill method to test a geological hypothesis at a sensible cost."""
CODE = 'mining4_drill_planning'
BOOK = {'title': 'Drilling Programmes and Hole Design',
 'subtitle': 'Designing holes that test a clear idea at a fair cost',
 'chapters': [('Azimuth and dip',
               'The azimuth is the compass direction a hole points, and the dip is its angle below the '
               'horizontal. Together they set the path of the hole. A good design crosses the target at a '
               'sensible angle.'),
              ('Target depth',
               'Each hole is planned to reach a target depth, below which the ore is not expected. The depth '
               'is set by the geological model. Drilling past the target wastes money, and stopping short '
               'can miss the ore.'),
              ('Diamond versus reverse circulation',
               'Diamond drilling brings up solid core, which is very good for logging. Reverse circulation '
               'brings up chips of rock, which is faster and cheaper. The choice depends on what the team '
               'needs to learn.'),
              ('Cost per metre',
               'Drilling is charged by the metre, so the cost per metre matters. Hard rock, deep holes and '
               'difficult ground all raise the cost. A planner estimates the cost of each hole before it '
               'starts.'),
              ('Hole spacing',
               'Holes are spaced to test the target at the scale that matters. Close spacing gives '
               'confidence but costs more. Wide spacing covers ground faster but leaves more uncertainty.'),
              ('Testing hypotheses with drilling',
               'Every hole should test a clear idea, such as whether a fault carries ore or a zone is '
               'altered. A drilling programme is a series of tests. Each result either supports the idea or '
               'changes it.')],
 'test': [('What is the azimuth of a drill hole?',
           [('a', 'The compass direction the hole points'),
            ('b', 'The depth of the hole'),
            ('c', 'The name of the driller'),
            ('d', 'The colour of the core')],
           'a'),
          ('What does diamond drilling bring up?',
           [('a', 'Liquid water only'), ('b', 'Gas only'), ('c', 'Solid core'), ('d', 'Nothing at all')],
           'c'),
          ('What is the cost of drilling usually based on?',
           [('a', 'Cost per kilogram of the drill'),
            ('b', 'Cost per metre drilled'),
            ('c', 'Cost per cloud'),
            ('d', 'Cost per star')],
           'b'),
          ('What does close hole spacing do?',
           [('a', 'Removes all uncertainty for free'),
            ('b', 'Makes the ore disappear'),
            ('c', 'Stops the drill'),
            ('d', 'Gives more confidence but costs more')],
           'd'),
          ('What should every drill hole do?',
           [('a', 'Test a clear geological idea'),
            ('b', 'Be drilled at random'),
            ('c', 'Go as deep as possible always'),
            ('d', 'Avoid the target')],
           'a')]}
