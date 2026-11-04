"""Ocean Carbonate Chemistry: how the sea holds dissolved carbon dioxide, why acidification happens, and how scientists measure it."""
CODE = 'science5_chem_ocean_carb'
BOOK = {
    "title": 'Ocean Carbonate Chemistry',
    "subtitle": 'How the sea holds carbon dioxide and keeps its chemistry in balance',
    "chapters": [
        ('Carbon dioxide in seawater',
         'The ocean takes up carbon dioxide from the air. Once dissolved, the gas reacts with water to form carbonic acid, which breaks down into bicarbonate and carbonate ions. These forms are linked, and together they make up the carbonate system.'),
        ('Alkalinity',
         'Alkalinity measures how well seawater can resist a change in acidity. It comes mostly from bicarbonate and carbonate ions. A high alkalinity means the water can absorb more acid before its pH falls.'),
        ('Ocean acidification',
         'As more carbon dioxide dissolves, the ocean gets more acidic, and its pH falls. This process is called ocean acidification. It lowers the amount of carbonate ion in the water.'),
        ('Carbonate saturation',
         'Shell-building animals and corals use carbonate ions to make calcium carbonate. The saturation state tells how easily these minerals form. When saturation falls too low, shells and skeletons become harder to build and can even dissolve.'),
        ('Measuring the system',
         'Scientists measure any two of the carbonate parameters, such as alkalinity and dissolved inorganic carbon, and calculate the rest. Shared reference materials and standard methods keep measurements from different ships and labs comparable.'),
        ('Ocean buffering',
         "The ocean buffers itself on long timescales through the slow weathering of rocks and the burial of carbonate sediments. This buffer works slowly, so today's fast rise in carbon dioxide outpaces it. Careful monitoring of the carbonate system is needed to see the change early."),
    ],
    "test": [
        ('What is formed when carbon dioxide dissolves in seawater and reacts with water?',
         [('a', 'Pure oxygen'), ('b', 'Table salt'), ('c', 'Methane'), ('d', 'Carbonic acid')], 'd'),
        ('What does alkalinity measure?',
         [('a', 'How deep the water is'), ('b', 'How warm the water is'), ('c', 'How well seawater resists a change in acidity'), ('d', 'How much sunlight reaches the surface')], 'c'),
        ('What is ocean acidification?',
         [('a', 'The ocean getting more acidic as it takes up more carbon dioxide'), ('b', 'The ocean getting saltier'), ('c', 'The ocean freezing from the top'), ('d', 'Rivers flowing into the sea')], 'a'),
        ('Why does low carbonate saturation harm shell-building animals?',
         [('a', 'It makes shells harder to build and can cause them to dissolve'), ('b', 'It makes the water too hot'), ('c', 'It makes the animals grow too fast'), ('d', 'It removes all oxygen')], 'a'),
        ('How is the ocean carbonate system usually measured?',
         [('a', 'By measuring any two parameters and calculating the rest'), ('b', 'By weighing a bucket of seawater'), ('c', 'By counting fish'), ('d', 'By listening to waves')], 'a'),
    ],
}
