"""Data and Graphs: averages, spread, and drawing a graph that tells the truth. Science career, bar 2 (Scientist)."""
CODE = 'science2_data'
BOOK = {
    "title": 'Data and Graphs',
    "subtitle": 'Averages, spread, and drawing a graph that tells the truth',
    "chapters": [
        ('Numbers need a story',
         'Raw numbers are hard to read. A table, a graph or an average can show a pattern, but each one can also hide things. Always ask what was measured, how it was collected, and how many samples there were.'),
        ('Mean, median and mode',
         'The mean is the sum of the values divided by how many there are. The median is the middle value once the numbers are sorted. The mode is the value that appears most often. A few very large numbers pull the mean up, but the median stays where the middle is.'),
        ('Spread',
         'Two sets of data can share the same mean and still look very different. The range is the highest value minus the lowest. Spread measures how far the values typically sit from the middle, and it tells you how much to trust the average.'),
        ('Choosing a graph',
         'Use a line graph to show change over time. Use a bar chart to compare separate groups. Use a scatter plot to see whether two quantities tend to rise or fall together. The wrong graph can make a true result look false.'),
        ('Truthful axes',
         'Start a bar chart\'s vertical axis at zero, or a small difference will look huge. Label both axes with their units, and say where the data came from. A reader should be able to check your graph.'),
        ('Correlation is not cause',
         'Two things can rise together without one causing the other. A scatter plot can show correlation, but only a well-designed experiment can show cause. Always look for a third factor before you claim one thing causes another.'),
    ],
    "test": [
        ('What is the median of 2, 3, 4, 9 and 12?',
         [('a', '4'), ('b', '6'), ('c', '5'), ('d', '9')], 'a'),
        ('Which graph is best for showing change over time?',
         [('a', 'A pie chart'), ('b', 'A bar chart of separate groups'), ('c', 'A line graph'), ('d', 'A table with no axes')], 'c'),
        ('Why should a bar chart\'s vertical axis usually start at zero?',
         [('a', 'Because zero is always the largest value'), ('b', 'To make the bars look shorter'), ('c', 'Because graphs must have ten bars'), ('d', 'So that bar lengths compare honestly')], 'd'),
        ('Which statement about correlation is correct?',
         [('a', 'Two things that rise together must cause each other'), ('b', 'A scatter plot proves cause'), ('c', 'Correlation means nothing at all'), ('d', 'Two things can rise together without one causing the other')], 'd'),
        ('Two data sets have the same mean. What could still be different?',
         [('a', 'Their median is always the same too'), ('b', 'Nothing, the mean fixes everything'), ('c', 'Their spread'), ('d', 'Their units are always the same')], 'c'),
    ],
}
