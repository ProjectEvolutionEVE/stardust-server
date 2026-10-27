"""Graphene and Two-Dimensional Materials: one-atom-thick sheets of carbon, and the other materials built the same way."""
CODE = 'mining4_graphene'
BOOK = {
    "title": 'Graphene and Two-Dimensional Materials',
    "subtitle": 'One-atom-thick sheets, and how they are made',
    "chapters": [
        ('One atom thick',
         'Graphene is a sheet of carbon atoms arranged in a honeycomb pattern. It is only one atom thick. It is the thinnest material that can exist as a stable sheet.'),
        ('Peeling it off',
         'The first graphene was peeled from graphite, the stuff in pencil lead, using sticky tape. Layer by layer the tape thins the graphite until single sheets remain. This is called exfoliation.'),
        ('Growing it',
         'For larger sheets, graphene is grown from a carbon gas on a metal foil, usually copper. The gas breaks down on the hot foil and carbon forms a single layer. This is chemical vapour growth.'),
        ('Strength and conduction',
         'Graphene is very strong for its weight and conducts electricity and heat very well. These properties make it interesting for coatings, electronics and composites.'),
        ('Uses and costs',
         'Graphene is used in some coatings, inks and composite materials. Making high quality sheets in quantity is still costly, so many uses are niche. Costs fall as production methods improve.'),
        ('Other 2D materials',
         'Other materials can also be made as single layers. Hexagonal boron nitride and molybdenum disulfide are examples. Each has its own electrical and optical behaviour, and they can be stacked to build new devices.'),
    ],
    "test": [
        ('How thick is a graphene sheet?',
         [('a', 'One metre thick'), ('b', 'One centimetre thick'), ('c', 'One atom thick'), ('d', 'As thick as a human hair')], 'c'),
        ('What was the first graphene peeled from?',
         [('a', 'Graphite, the material in pencil lead'), ('b', 'Gold leaf'), ('c', 'Ice'), ('d', 'Glass bottles')], 'a'),
        ('What is exfoliation?',
         [('a', 'Melting a metal into a ball'), ('b', 'Painting a surface'), ('c', 'Freezing water into ice'), ('d', 'Peeling layers apart until single sheets remain')], 'd'),
        ('What is graphene grown on in chemical vapour growth?',
         [('a', 'A wooden board'), ('b', 'A metal foil, usually copper'), ('c', 'A bowl of sugar'), ('d', 'A sheet of paper')], 'b'),
        ('What is one reason graphene is interesting?',
         [('a', 'It is a liquid at room temperature'), ('b', 'It tastes sweet'), ('c', 'It is very strong for its weight and conducts well'), ('d', 'It is made of glass')], 'c'),
    ],
}
