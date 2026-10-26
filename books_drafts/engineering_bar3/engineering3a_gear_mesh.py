"""Gear Teeth: module, pitch and mesh, so that two wheels turn together smoothly."""
CODE = 'engineering3a_gear_mesh'
BOOK = {
    "title": 'Gear Teeth: Module, Pitch and Mesh',
    "subtitle": 'How gear teeth are sized so that two wheels turn together smoothly',
    "chapters": [
        ('Teeth that fit',
         'Two gears mesh only if their teeth match in size. The most common measure is the module, which is the pitch diameter divided by the number of teeth. Gears with the same module, cut to the same tooth shape, mesh together.'),
        ('The pitch circle',
         'The pitch circle is the imaginary circle on which two meshing gears roll against each other. Its diameter is set by the module and the number of teeth. For two external gears, the distance between their centres equals the sum of their pitch radii.'),
        ('The involute curve',
         'Most gear teeth have an involute profile, a curve that keeps the turning ratio steady as the teeth push each other round. The ratio stays steady even when the centres move slightly apart, which makes involute gears forgiving to build. Their profiles can be checked with a gauge.'),
        ('Spur and helical',
         'Spur gears have straight teeth parallel to the shaft. Helical gears have angled teeth that engage gradually, so they run quieter and smoother. The angled teeth also push the shafts sideways, so the bearings must take that thrust.'),
        ('Backlash',
         'Backlash is the small gap between meshing teeth, left on purpose so the teeth do not jam as they heat and expand. Too much backlash makes a machine sloppy when it reverses. Too little causes binding and wear.'),
        ('Checking a gear train',
         'Before cutting a gear train, check that every pair shares the same module and pressure angle. Work out each ratio and the centre distance, and leave the backlash. Note the speed at each stage on the drawing so a builder can check it.'),
    ],
    "test": [
        ("What is a gear's module?",
         [('a', 'The number of teeth multiplied by the weight'), ('b', 'The pitch diameter divided by the number of teeth'), ('c', 'The speed of the gear'), ('d', 'The colour of the gear')], 'b'),
        ('When do two gears mesh well together?',
         [('a', 'When one is painted'), ('b', 'When one has twice the weight'), ('c', 'When they are made of different sizes of paper'), ('d', 'When they share the same module')], 'd'),
        ('What does an involute tooth profile help keep steady?',
         [('a', 'The colour of the teeth'), ('b', 'The temperature of the gear'), ('c', 'The turning ratio'), ('d', 'The weight of the shaft')], 'c'),
        ('Why are helical gears quieter than straight-toothed spur gears?',
         [('a', 'Their angled teeth engage gradually'), ('b', 'They have no teeth'), ('c', 'They are always made of wood'), ('d', 'They turn more slowly')], 'a'),
        ('What is backlash?',
         [('a', 'A broken tooth'), ('b', 'The colour of a gear case'), ('c', 'A type of bearing'), ('d', 'A small gap between meshing teeth, left on purpose')], 'd'),
    ],
}
