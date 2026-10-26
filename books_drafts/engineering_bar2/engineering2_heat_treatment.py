"""Heat Treatment: heating and cooling metal on purpose, to soften it, harden it or give it toughness."""
CODE = 'engineering2_heat_treatment'
BOOK = {
    "title": 'Heat Treatment',
    "subtitle": 'Heating and cooling metal on purpose, to make it softer, harder or tougher',
    "chapters": [
        ('Heat changes metal',
         "Heating and cooling a metal changes the structure inside it, and that changes how it behaves. The same piece of steel "
         "can be soft enough to file or hard enough to cut other metal, depending on how it is heated and cooled. Heat "
         "treatment is controlled heating and cooling, done for that purpose."),
        ('Annealing: soften it',
         "Annealing heats a metal and then lets it cool slowly. Its internal structure relaxes, and the metal becomes soft and "
         "easy to shape or machine. Metal that has been hammered or bent until it is stiff is often annealed before it is "
         "worked any further."),
        ('Hardening: cool it fast',
         "To harden steel, heat it to a high temperature, then quench it by cooling it quickly in water, oil or air. Fast "
         "cooling traps the carbon in a hard form. Hardened steel cuts well and resists wear, but it is brittle and can crack."),
        ('Tempering: give back toughness',
         "Tempering reheats hardened steel to a lower temperature, holds it there for a time, and then cools it. The part gives "
         "up a little hardness and gains toughness, so it can take a knock without shattering. Engineers choose the temperature "
         "to balance the two."),
        ('Precipitation hardening',
         "Some aluminium and titanium alloys harden in a different way. They are heated so that their alloying elements dissolve, "
         "quenched, and then aged at a lower temperature. Tiny particles form inside the metal and block its internal movement, "
         "which makes it stronger. Many aircraft aluminium alloys are made this way."),
        ('Control and checking',
         "Heat must be controlled and timed. Heated too hot, a metal's structure can be ruined, and a fast quench can warp or "
         "crack a part. Check the hardness after treatment, and test a sample each time the process changes. Write down every "
         "temperature and time."),
    ],
    "test": [
        ("What does annealing do to metal?",
         [('a', 'Makes it harder and more brittle'), ('b', 'Coats it with a shiny layer'), ('c', 'Softens it, so it is easier to shape or machine'), ('d', 'Turns it into a gas')], 'c'),
        ("What is quenching?",
         [('a', 'Cooling hot metal quickly, in water, oil or air'), ('b', 'Melting metal into a mould'), ('c', 'Scraping rust off a part'), ('d', 'Heating metal very slowly over days')], 'a'),
        ("After hardening, what does tempering give back?",
         [('a', 'Shine'), ('b', 'Weight'), ('c', 'Electrical conductivity'), ('d', 'Toughness, so the part does not shatter')], 'd'),
        ("Why is hardened steel often tempered?",
         [('a', 'To make it cheaper'), ('b', 'Because hardened steel can be so brittle that it cracks under a knock'), ('c', 'To make it magnetic'), ('d', 'To make it float')], 'b'),
        ("What forms inside an aluminium alloy during precipitation hardening?",
         [('a', 'Holes'), ('b', 'Liquid pockets'), ('c', 'Tiny particles that block the metal from moving inside'), ('d', 'Coloured crystals on the surface')], 'c'),
    ],
}
