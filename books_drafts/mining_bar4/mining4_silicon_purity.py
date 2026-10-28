"""Silicon for Chips and Solar: how silicon is purified to near perfection for electronics and solar cells."""
CODE = 'mining4_silicon_purity'
BOOK = {
    "title": 'Silicon for Chips and Solar',
    "subtitle": 'Purifying silicon for electronics and solar cells',
    "chapters": [
        ('Metallurgical silicon',
         'Silicon is made first from quartz sand in an electric furnace, at a purity of around 98 to 99 per cent. That is not nearly good enough for chips, so it goes through more steps.'),
        ('Zone refining',
         'In zone refining, a narrow molten band is moved slowly along a silicon bar. Impurities collect in the melt and are carried off the end of the bar. Repeating the pass removes more.'),
        ('Growing a crystal',
         'In the Czochralski method, a seed crystal is dipped into molten silicon and slowly pulled up as it turns. A large single crystal grows from the melt. The crystal is then sliced into thin wafers.'),
        ('Purity in nines',
         'Chip makers talk about purity in nines. Nine nines means 99.9999999 per cent pure. Each extra nine is a much harder step to reach, and it sets how well a chip works.'),
        ('Polysilicon and solar cells',
         'Polysilicon is silicon made of many small crystals. It is cheaper and is widely used to make solar cells, which need purity but not the perfection of a chip wafer.'),
        ('Recycling silicon',
         'Offcuts from wafer cutting and old solar panels can be recovered. Recycling saves the energy and cost of making new silicon, though the recovered material must be checked for purity before reuse.'),
    ],
    "test": [
        ('What is the usual purity of metallurgical silicon from the furnace?',
         [('a', 'Around 10 per cent'), ('b', 'Exactly 100 per cent'), ('c', 'Around 98 to 99 per cent'), ('d', 'Around 50 per cent')], 'c'),
        ('What does zone refining do?',
         [('a', 'Carries impurities off the end of the bar with a moving molten band'), ('b', 'Melts the whole bar at once'), ('c', 'Cools the silicon to ice'), ('d', 'Paints the bar')], 'a'),
        ('What does nine nines purity mean?',
         [('a', 'Nine per cent pure'), ('b', 'Nine kilograms of silicon'), ('c', 'Nine wafers'), ('d', '99.9999999 per cent pure')], 'd'),
        ('What is polysilicon?',
         [('a', 'A single crystal of silicon'), ('b', 'Silicon made of many small crystals'), ('c', 'A glass lens'), ('d', 'A copper wire')], 'b'),
        ('What is Czochralski growth used for?',
         [('a', 'Melting sand into glass'), ('b', 'Making paper'), ('c', 'Pulling a large single silicon crystal from a melt'), ('d', 'Sealing pipes')], 'c'),
    ],
}
