"""Software Product Lines: building a family of related products from shared core assets, with managed variation between them."""
CODE = 'computing5_software_product_lines'
BOOK = {
    "title": 'Software Product Lines',
    "subtitle": 'One shared core, many managed variants',
    "chapters": [
        ('What a product line is',
         'A software product line is a family of products built from a common set of core assets. Each product is assembled from those parts with its own selected variations. Reuse is planned, not accidental.'),
        ('Variability models',
         'A variability model records where products may differ and what choices are allowed. It makes the range of variation explicit. Without it, variants drift apart without anyone deciding to.'),
        ('Feature models',
         'A feature model arranges features as a tree, marking which are optional, required or alternatives. Valid products are the combinations the model allows. Feature models help teams check whether a configuration makes sense.'),
        ('Core assets',
         'Core assets include the shared code, designs, tests and documentation used by every product. Their quality determines the quality of every variant. Investment in core assets pays back across the whole family.'),
        ('Configuration',
         'Configuration selects the features for a particular product from the options allowed. Good tools produce the product from its configuration automatically. Hand-made changes after configuration are a common source of error.'),
        ('Governance of variants and scaling reuse',
         'Each new variant needs rules about who approves it and whether it returns to the core. Without governance, variants multiply and maintenance grows painful. Scaling reuse means keeping the core healthy as the family grows.'),
    ],
    "test": [
        ('What is a software product line?',
         [('a', 'A family of products built from a common set of core assets'), ('b', 'A factory for paper cups'), ('c', 'A fishing boat'), ('d', 'A queue at a shop')], 'a'),
        ('What does a variability model record?',
         [('a', 'The office temperature'), ('b', "The employees' lunch orders"), ('c', 'Where products may differ and which choices are allowed'), ('d', 'The number of parking spaces')], 'c'),
        ('What does a feature model show?',
         [('a', 'A map of the planets'), ('b', 'Features arranged as a tree, with optional, required and alternative parts'), ('c', 'A list of prices in a shop'), ('d', 'A calendar of holidays')], 'b'),
        ('Why is the quality of core assets important?',
         [('a', 'They are only used for printing'), ('b', 'They are never shared'), ('c', 'They matter only on Fridays'), ('d', 'Every product in the family depends on them')], 'd'),
        ('What risk comes from hand-made changes after configuration?',
         [('a', 'Errors that are hard to trace and repeat'), ('b', 'Faster products every time'), ('c', 'Automatic colour changes'), ('d', 'Fewer features to test')], 'a'),
    ],
}
