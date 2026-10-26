"""Corrosion and Protection: how metal rusts and wears away, and how engineers stop it."""
CODE = 'engineering2_corrosion'
BOOK = {
    "title": 'Corrosion and Protection',
    "subtitle": 'How metal rusts and wears away, and how to stop it',
    "chapters": [
        ('Rust is a chemical change',
         "Corrosion is a metal reacting with what surrounds it, usually oxygen and water, to form a new substance. Iron rusts "
         "into iron oxide. Rust is flaky and takes up more space than the metal it came from, so it keeps peeling away and "
         "exposing fresh metal beneath."),
        ('Oxygen, water and salt',
         "Corrosion speeds up with water, salt and heat. Salt water conducts electricity far better than fresh water, and that "
         "speeds up the reaction. Metal in a damp, salty or hot place needs more protection than metal kept dry indoors."),
        ('Galvanic corrosion',
         "When two different metals touch in a wet place, the more reactive one corrodes faster. Zinc protects steel for this "
         "reason, because zinc corrodes first. Keep metals that are far apart in reactivity from touching, or separate them "
         "with an insulating gasket."),
        ('Self-healing skins',
         "Aluminium and titanium form a thin, hard oxide skin that protects the metal beneath. If the skin is scratched, it "
         "rebuilds itself as long as oxygen is present. That is why aluminium holds up well outdoors, even unpainted."),
        ('Coatings and sacrificial metal',
         "Paint, grease and plastic coatings keep water away from the metal. Galvanising coats steel with zinc. A sacrificial "
         "anode is a block of a more reactive metal, fixed to a steel part, which corrodes in the metal's place."),
        ('Checking for corrosion',
         "Look for bubbling paint, flaky rust, pits, and white powder on aluminium. Check joints and crevices, where water "
         "sits and cannot dry out. Clean and recoat early, because a small patch treated today is cheaper than a part "
         "replaced later."),
    ],
    "test": [
        ("What is rust?",
         [('a', 'A coat of paint'), ('b', 'Iron oxide, formed when iron meets oxygen and water'), ('c', 'A copper salt'), ('d', 'A kind of plastic')], 'b'),
        ("Why does salt water speed up corrosion?",
         [('a', 'It conducts electricity better than fresh water'), ('b', 'It is hotter than fresh water'), ('c', 'It contains gold'), ('d', 'It is lighter than fresh water')], 'a'),
        ("Why is zinc used to protect steel?",
         [('a', 'Zinc is cheaper than steel'), ('b', 'Zinc is stronger than steel'), ('c', 'Zinc stops electricity from flowing'), ('d', 'Zinc corrodes first, in place of the steel')], 'd'),
        ("Why does aluminium hold up well outdoors?",
         [('a', 'It is painted gold at the factory'), ('b', 'It cannot react with anything at all'), ('c', 'A thin oxide skin protects it, and rebuilds itself when scratched in air'), ('d', 'It is magnetic')], 'c'),
        ("What is a sacrificial anode?",
         [('a', 'A block of more reactive metal fixed to a part, which corrodes in its place'), ('b', 'A sharp spike that scares off rust'), ('c', 'A type of drill bit'), ('d', 'A fuse for electricity')], 'a'),
    ],
}
