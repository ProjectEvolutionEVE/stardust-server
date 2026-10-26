"""Surveying the Land: baselines, angles, levels and traverses, the careful measuring that makes maps and boundaries possible."""
CODE = 'navigation2_surveying'
BOOK = {
    "title": 'Surveying the Land',
    "subtitle": 'Baselines, angles, levels and traverses: how the land is measured',
    "chapters": [
        ('What a survey is for',
         'A survey measures the land exactly, so that boundaries, roads and buildings can be placed correctly. Surveyors use the same ideas as navigators: angles, distances and a fixed starting point. Their results become the maps that everyone else relies on.'),
        ('The baseline',
         'A surveyor starts by measuring one line very carefully. This is the baseline, and every other point is fixed from it using angles and distances. The care taken over the baseline sets the accuracy of the whole survey.'),
        ('The theodolite',
         'A theodolite is a telescope on a stand that measures horizontal and vertical angles very precisely. It is set up over a known point, aimed at another point, and the angle is read. Repeated from several points, these angles tie a whole network of points together.'),
        ('Traverses',
         'A traverse measures a chain of linked lines, each with a length and an angle. If the chain ends back at its starting point, the surveyor can check the closing error and spread it through the work. A gap at the end warns that something has gone wrong.'),
        ('Levelling for height',
         'A level is a telescope set exactly horizontal. The surveyor reads height differences by looking at a measuring staff held upright on two points. Heights are always referred to a benchmark, a marked point whose height is known.'),
        ('Checking the work',
         'Every measurement carries a small error. Surveyors measure again, close their loops, and compare results with points of known position. A survey is trusted only after its checks come out right.'),
    ],
    "test": [
        ('What is a baseline in surveying?',
         [('a', 'A line drawn on a map to mark the coast'), ('b', 'The line of the horizon'), ('c', 'A line measured very carefully, from which other points are fixed'), ('d', 'A pencil mark on a tree')], 'c'),
        ('What does a theodolite measure?',
         [('a', 'Water depth'), ('b', 'The temperature of the ground'), ('c', 'The speed of the wind'), ('d', 'Horizontal and vertical angles, very precisely')], 'd'),
        ('What does it mean when a traverse ends back at its start point but does not match exactly?',
         [('a', 'The survey is finished and correct'), ('b', 'The closing error shows a mistake to check and spread out'), ('c', 'The land has moved overnight'), ('d', 'The traverse must be thrown away at once')], 'b'),
        ('What is a benchmark?',
         [('a', 'A marked point of known height, used as a reference'), ('b', 'A type of compass'), ('c', 'A bench in a park'), ('d', 'A surveying mistake')], 'a'),
        ('Why do careful surveyors check their work?',
         [('a', 'Because the land moves every hour'), ('b', 'Because every measurement carries a small error'), ('c', 'Because the theodolite cannot be read'), ('d', 'Because maps must be coloured')], 'b'),
    ],
}
