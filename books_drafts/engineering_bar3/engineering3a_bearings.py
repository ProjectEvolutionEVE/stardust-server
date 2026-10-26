"""Bearings: plain and rolling, how a shaft turns on its support, and how the support wears."""
CODE = 'engineering3a_bearings'
BOOK = {
    "title": 'Bearings: Plain and Rolling',
    "subtitle": 'How a shaft turns on its support with little friction, and how the support wears',
    "chapters": [
        ('A bearing carries a turning shaft',
         'A bearing holds a shaft in place while letting it turn. It carries the load from the shaft into the frame. Without one, the shaft would rub hard on the frame and wear through quickly.'),
        ('Plain bearings slide',
         'A plain bearing is a smooth sleeve that the shaft slides on, often made of bronze or a tough polymer. It is simple, cheap and copes well with knocks. It needs a film of oil or grease to keep the surfaces apart.'),
        ('Rolling bearings roll',
         'A rolling bearing places balls or rollers between an inner ring and an outer ring. Rolling makes far less friction than sliding, especially when the shaft starts from rest. It is precise, but it costs more and can be damaged by hard knocks.'),
        ('Lubrication keeps surfaces apart',
         'A good lubricant forms a thin film that stops metal surfaces from touching. Under light, steady loads the film is usually enough. Under heavy loads or at low speed the film can thin out, so the surfaces wear, and the choice of lubricant matters.'),
        ('Load, speed and life',
         "A bearing's life depends on how much load it carries, how fast it turns and how clean it stays. Dirt or water inside the bearing can shorten its life sharply. Makers publish a rated life for each bearing, so replacements can be planned."),
        ('Fitting a bearing',
         'A bearing must fit its shaft and housing to the right tolerance. Too tight, and it cannot turn freely or may crack its ring. Too loose, and the shaft wobbles. Check the fit before fitting, and keep the bearing clean while it goes in.'),
    ],
    "test": [
        ('What does a bearing do?',
         [('a', 'It makes the shaft hotter'), ('b', 'It stores fuel'), ('c', 'It supports a turning shaft and carries its load'), ('d', 'It paints the shaft')], 'c'),
        ('Which of these is a plain bearing?',
         [('a', 'A smooth sleeve that the shaft slides on'), ('b', 'A tight rack of wires'), ('c', 'A ball in a glass tube'), ('d', 'A spring without a shaft')], 'a'),
        ('What is the main advantage of a rolling bearing?',
         [('a', 'It has no friction at all'), ('b', 'It never needs cleaning'), ('c', 'It costs nothing to make'), ('d', 'Much less friction, especially when starting from rest')], 'd'),
        ('What is the main job of a lubricant in a bearing?',
         [('a', 'To make the metal soft'), ('b', 'To keep the metal surfaces apart with a thin film'), ('c', 'To paint the housing'), ('d', 'To heat the shaft')], 'b'),
        ("What shortens a bearing's life sharply?",
         [('a', 'Clean oil kept sealed in'), ('b', 'Turning it slowly with no load'), ('c', 'Dirt or water getting inside it'), ('d', 'A bright finish')], 'c'),
    ],
}
