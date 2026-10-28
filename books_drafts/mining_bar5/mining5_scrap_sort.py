"""Sorting Metal Scrap by Alloy: how scrap yards tell one metal grade from another."""
CODE = 'mining5_scrap_sort'
BOOK = {
    "title": 'Sorting Metal Scrap by Alloy',
    "subtitle": 'Telling one metal grade from another before it is melted',
    "chapters": [
        ('Why sorting matters', 'Scrap metal is worth more when it is sorted by alloy, because melting mixed scrap gives a poor product. A batch of steel with the wrong element in it can fail its job. Good sorting protects both quality and price.'),
        ('Spectrometers', "Handheld X-ray fluorescence and optical emission spectrometers measure the elements in a piece of metal in seconds. The instrument reads the light or X-rays given off by the sample. It shows the alloy's chemistry on a screen."),
        ('Lasers', 'Laser-induced breakdown spectroscopy fires a short laser pulse at the metal. The tiny spark it makes gives off light that shows which elements are present. It can sort small pieces quickly, even on a moving belt.'),
        ('Labels', "Sorted scrap is kept in labelled bins, each with its grade and its test record. Clear labels let buyers trust the material without testing it all again. Labels and records are part of the product's value."),
        ('Quality', 'Scrap quality depends on how clean the pieces are and how well they match their grade. Oil, paint and coatings can spoil a melt if they are not removed. Careful preparation raises the price a buyer will pay.'),
        ('Mixing errors', 'A single wrong piece can add an unwanted element to a whole melt. Copper in steel, for example, can cause cracks during later rolling. Preventing mixing is cheaper than fixing it after melting.'),
    ],
    "test": [
        ('Why is sorted scrap worth more?', [('a', 'It is lighter to carry'), ('b', 'It makes the yard quieter'), ('c', 'It changes the weather'), ('d', 'Melting mixed scrap gives a poor product')], 'd'),
        ('What can a handheld spectrometer do in seconds?', [('a', 'Cook a meal'), ('b', 'Measure the elements in a piece of metal'), ('c', 'Print a receipt'), ('d', 'Measure the height of a building')], 'b'),
        ('How does laser-induced breakdown spectroscopy identify elements?', [('a', 'The laser melts the metal into water'), ('b', 'The laser paints a label'), ('c', 'A laser spark gives off light that shows which elements are present'), ('d', 'The laser counts the pieces')], 'c'),
        ('Why are scrap bins labelled with their grade and test record?', [('a', 'So buyers can trust the material without testing it all again'), ('b', 'So the bins can be painted'), ('c', 'So the scrap becomes lighter'), ('d', 'So the bins stay empty')], 'a'),
        ('Why can copper in steel be a problem?', [('a', 'It makes the steel invisible'), ('b', 'It can cause cracks during later rolling'), ('c', 'It makes steel float'), ('d', 'It turns steel into wood')], 'b'),
    ],
}
