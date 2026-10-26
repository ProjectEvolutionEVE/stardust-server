"""Brazing, soldering and adhesives: joining metals without melting them, and joining materials that cannot be welded at all."""
CODE = 'engineering3b_brazing_soldering'
BOOK = {
    "title": 'Brazing, Soldering and Adhesives',
    "subtitle": 'Joining metals without melting them, and joining materials that cannot be welded at all',
    "chapters": [
        ('Filler does the joining',
         'Brazing and soldering join metal parts by melting a filler metal into the gap between them. The base metal stays solid. The filler flows into the joint by capillary action, drawn into the narrow gap the way water climbs a thin tube.'),
        ('Soldering: low heat, small joints',
         'Soldering uses a filler that melts below about 450 degrees Celsius. Electronics use tin-based solder to join wires and components to circuit boards. A soldered joint is weak under heavy load, so soldering suits electrical joints and light parts.'),
        ('Brazing: stronger joints',
         'Brazing uses a filler that melts above about 450 degrees Celsius, and it makes much stronger joints. Brass and silver-based fillers are common. Bicycle frames, pipes and tools are often brazed, because the joint is strong and the base metal never melts.'),
        ('Flux and clean surfaces',
         'Both processes need clean metal, because the oxide on a surface stops the filler from wetting it. Flux is a chemical paste or powder that removes oxide and keeps air away while the joint heats. Without flux, most joints fail to fill or to hold.'),
        ('Adhesives join what cannot be welded',
         'Adhesives such as epoxy join metal to plastic, ceramic or wood, and parts that could never be melted together. An epoxy is a two-part resin that hardens when the parts are mixed. The surfaces must be clean and rough enough for the glue to grip.'),
        ('Choosing the joint',
         'A bonded joint spreads the load over a wide area and adds no heat to the parts. But an adhesive loses strength when it gets hot, and it can peel if pulled at the edge. A brazed joint is strong and sealed, and a soldered joint is quick and tidy for wiring. Pick the joint by the load, the heat, and how the part must be taken apart later.'),
    ],
    "test": [
        ('How does the filler reach into a brazed or soldered joint?',
         [('a', 'It is drawn into the narrow gap by capillary action'), ('b', 'It is pumped in by a machine'), ('c', 'It is poured in from above'), ('d', 'It is blown in by air')], 'a'),
        ('Above about what temperature is a filler called brazing rather than soldering?',
         [('a', '50 degrees Celsius'), ('b', '100 degrees Celsius'), ('c', '450 degrees Celsius'), ('d', '4,500 degrees Celsius')], 'c'),
        ('Why does a surface need to be clean before soldering or brazing?',
         [('a', 'So the filler will change colour'), ('b', 'Because oxide on the surface stops the filler from wetting it'), ('c', 'So the flux can be painted on'), ('d', 'So the metal will not conduct')], 'b'),
        ('What is flux?',
         [('a', 'A type of steel'), ('b', 'A sharp cutting tool'), ('c', 'A kind of solder wire'), ('d', 'A chemical paste that removes oxide and keeps air off the joint')], 'd'),
        ('Which of these is a two-part resin that hardens when mixed?',
         [('a', 'Brass'), ('b', 'Tin'), ('c', 'Epoxy'), ('d', 'Flux')], 'c'),
    ],
}
