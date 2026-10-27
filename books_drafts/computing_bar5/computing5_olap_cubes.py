"""OLAP cubes: measures and dimensions, roll-up, drill-down, slicing, pre-aggregation and materialised aggregates."""
CODE = 'computing5_olap_cubes'
BOOK = {
    "title": 'OLAP Cubes and Aggregation',
    "subtitle": 'Summary tables that let people slice numbers by time, place and product',
    "chapters": [
        ('Measures and dimensions',
         'A measure is a number you want to add up, such as sales in pounds. A dimension is a way to group it, such as by date, shop or product.'),
        ('Roll-up and drill-down',
         'Rolling up moves from fine detail to a summary, such as from days to months. Drilling down goes the other way, from a total to the parts that make it.'),
        ('Slicing',
         'A slice fixes one dimension, for example one year, and shows the rest. A dice picks a range across several dimensions.'),
        ('Pre-aggregation',
         'Totals for common groupings can be calculated ahead of time and stored. A question about a monthly total can then read one stored number instead of scanning every sale.'),
        ('Materialised aggregates',
         'A materialised view is a stored result that must be refreshed when the data changes. Refreshing takes time, so teams decide how fresh the numbers need to be.'),
        ('Limits',
         'A cube with many dimensions can grow very large, and many of its cells may be empty. Designers choose the groupings people actually need.'),
    ],
    "test": [
        ('What is a measure?',
         [('a', 'A number you want to add up, such as sales'), ('b', 'A type of chair'), ('c', "A user's name"), ('d', 'A list of colours')], 'a'),
        ('What does drill-down do?',
         [('a', 'Deletes the cube'), ('b', 'Adds new users'), ('c', 'Goes from a total to the parts that make it'), ('d', 'Sends an email')], 'c'),
        ('What does a slice do?',
         [('a', 'Fixes one dimension and shows the rest'), ('b', 'Cuts the power'), ('c', 'Splits the data into files'), ('d', 'Renames the dimensions')], 'a'),
        ('Why store pre-aggregated totals?',
         [('a', 'So sales stop'), ('b', 'So a common question reads one number instead of scanning everything'), ('c', 'So the cube gets bigger for fun'), ('d', 'So the chart changes colour')], 'b'),
        ('What must happen to a materialised view when data changes?',
         [('a', 'It must be printed'), ('b', 'It must be deleted every hour'), ('c', 'It must be sent to a manager'), ('d', 'It must be refreshed')], 'd'),
    ],
}
