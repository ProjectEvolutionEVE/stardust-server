"""The Solow Growth Model: capital and labour, saving and depreciation, the steady state, technology as the residual, convergence and the data."""
CODE = 'business5_solow'
BOOK = {
    "title": 'The Solow Growth Model',
    "subtitle": 'How saving, people and new ideas set the long run',
    "chapters": [
        ('Capital and labour',
         'Robert Solow built a growth model around two inputs, capital such as machines and buildings, and labour, the work of people. Output rises with more of either, but each extra unit adds less than the one before. That is diminishing returns at work.'),
        ('Saving and depreciation',
         'A society that saves a share of its output adds to its stock of capital. Over time, machines wear out, and that loss is called depreciation. Capital grows when saving is larger than depreciation, and it shrinks when the reverse holds.'),
        ('The steady state',
         'Eventually, the capital stock settles where new saving just equals depreciation. This resting point is the steady state. In it, output per worker stops rising, unless something new changes the picture.'),
        ('Technology as the residual',
         'Solow found that capital and labour alone explained only part of the rise in output. The leftover part, now called the Solow residual, was attributed to technology and better ways of working. Technology was the main source of lasting growth in his model.'),
        ('Convergence',
         'In the Solow model, poorer countries with less capital can grow faster, because each new unit of capital adds more. This pull is called convergence. In practice, countries converge only when they share similar saving rates, institutions and technology.'),
        ('The data',
         'Solow won the Nobel Prize in Economics in 1987 for this work. Later studies tested his model with data across countries and over time, and found that it explains much of the pattern. Economists still use it as the starting point for growth theory.'),
    ],
    "test": [
        ('What are the two main inputs in the Solow model?',
         [('a', 'Gold and silver'), ('b', 'Capital and labour'), ('c', 'Sun and moon'), ('d', 'Land and rain')], 'b'),
        ('What is the steady state?',
         [('a', 'A ship that does not move'), ('b', 'A fixed price for gold'), ('c', 'A resting point where new saving just equals depreciation'), ('d', 'A law that stops all trade')], 'c'),
        ('What is the Solow residual?',
         [('a', 'The leftover food'), ('b', 'The last coin in a purse'), ('c', 'The debt of a bank'), ('d', 'The part of growth not explained by capital and labour, linked to technology')], 'd'),
        ('What is convergence in this model?',
         [('a', 'Poorer countries with less capital can grow faster'), ('b', 'All countries become the same size'), ('c', 'Growth always stops'), ('d', 'Capital always grows fastest in rich countries')], 'a'),
        ('In what year did Solow win the Nobel Prize in Economics?',
         [('a', '1776'), ('b', '1987'), ('c', '1933'), ('d', '2020')], 'b'),
    ],
}
