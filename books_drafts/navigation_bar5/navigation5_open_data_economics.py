"""The Economics of Open Geospatial Data: public goods, reuse value, costs of release, pricing choices, evidence and policy."""
CODE = 'navigation5_open_data_economics'
BOOK = {
    "title": 'The Economics of Open Geospatial Data',
    "subtitle": 'Who pays for maps and positions, and who gains from free access',
    "chapters": [
        ('Public goods',
         'A public good can be used by many people at once, and one person using it does not stop others. Many geospatial datasets have this quality. That is why free access to them can be a sound choice.'),
        ('The value of reuse',
         'Once a dataset exists, it can be reused again and again: by farmers, builders, shipping firms and schools. The total value of these many uses is often much larger than the cost of making the data in the first place.'),
        ('The costs of release',
         'Releasing data is not free. Someone must check it, document it, host it, and answer questions about it. These costs are real, and they should be counted honestly when a decision is made.'),
        ('Pricing choices',
         'An agency can charge for data, release it free, or choose something in between. Each choice affects who uses the data, how much they use it, and how the agency is paid. There is no single right answer for every dataset.'),
        ('Evidence',
         'Good decisions rest on evidence. Track who uses open data, what they do with it, and what it saves them. Simple surveys and usage counts are often enough to show the value.'),
        ('Policy',
         'Governments set the rules for open data. A clear policy explains what is released, under what terms, and who pays for it. Good policy protects privacy and security while still letting the public benefit.'),
    ],
    "test": [
        ('What makes something a public good?',
         [('a', 'Only one person can use it at a time'), ('b', 'It can only be sold once'), ('c', 'It is always physical'), ('d', 'Many people can use it, and one person using it does not stop others')], 'd'),
        ('What is reuse value?',
         [('a', 'The price of a used map'), ('b', 'The value of a dataset used many times by different people'), ('c', 'The cost of printing a map twice'), ('d', 'The fee for a single search')], 'b'),
        ('Which is a real cost of releasing data?',
         [('a', 'Making the data free of all errors by magic'), ('b', 'Paying nothing to anyone, ever'), ('c', 'Checking, documenting and hosting the data'), ('d', 'Losing all the value of the data')], 'c'),
        ('What does a pricing choice decide?',
         [('a', 'Who uses the data, how much, and how the agency is paid'), ('b', 'The colour of the data files'), ('c', 'The height of the satellite'), ('d', 'The language of the map legend')], 'a'),
        ('What is good evidence for an open data decision?',
         [('a', 'Guesses made in a meeting'), ('b', 'The colour of the agency logo'), ('c', 'The number of staff who attended the launch'), ('d', 'Usage counts and simple surveys that show what the data is used for')], 'd'),
    ],
}
