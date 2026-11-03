"""Traceability in Measurement: how a measurement is linked back to a trusted standard, and why that chain matters."""
CODE = 'navigation5_metrology_traceability'
BOOK = {
    "title": 'Traceability in Measurement',
    "subtitle": 'The calibration chain, uncertainty, standards, accreditation and records',
    "chapters": [
        ('Why measurements need trust',
         'A reading from an instrument is only useful if others can trust it. Traceability means every measurement can be linked back, step by step, to a recognised standard. That link is what makes two results from different places comparable.'),
        ('The calibration chain',
         'Each instrument is compared against a more accurate one, which was itself compared against a better one. The chain ends at a national or international standard. Each step is written down.'),
        ('Uncertainty',
         'No measurement is perfectly exact. An uncertainty is a range that says how far the true value is likely to lie. A result without its uncertainty is incomplete.'),
        ('Standards',
         'Standards are the reference objects, materials or definitions that others measure against. The kilogram and the metre are defined in terms of fixed physical constants. A standard must be stable, well described and available to those who need it.'),
        ('Accreditation and records',
         'Calibration labs can be accredited by an independent body that checks their methods. Good records show who measured what, with which instrument, and when it was last checked.'),
        ('Disputes',
         'When two results disagree, the traceability chain shows where to look. A lab can compare its instrument with a reference, and a dispute can often be settled by checking the chain step by step.'),
    ],
    "test": [
        ('What does traceability mean in measurement?',
         [('a', 'Drawing a line on a graph'), ('b', 'Recording only the highest reading'), ('c', 'Painting an instrument a bright colour'), ('d', 'Linking a measurement back to a recognised standard through a chain of comparisons')], 'd'),
        ('What is an uncertainty?',
         [('a', 'A mistake that has been fixed'), ('b', 'A range that says how far the true value is likely to lie'), ('c', 'The highest value a meter can show'), ('d', 'A kind of cable')], 'b'),
        ('What is a calibration chain?',
         [('a', 'A string of instruments each checked against a more accurate one'), ('b', 'A set of wires joining instruments'), ('c', 'A list of prices for tools'), ('d', 'A list of staff names')], 'a'),
        ('What does accreditation of a calibration lab check?',
         [('a', 'How fast the lab can lift heavy loads'), ('b', 'The colour of its walls'), ('c', 'Whether its methods are sound, by an independent body'), ('d', 'The number of customers it has')], 'c'),
        ('What helps settle a dispute between two results?',
         [('a', 'Ignoring the older result'), ('b', 'Choosing the bigger number'), ('c', 'Taking a vote in the office'), ('d', 'Following the traceability chain step by step')], 'd'),
    ],
}
