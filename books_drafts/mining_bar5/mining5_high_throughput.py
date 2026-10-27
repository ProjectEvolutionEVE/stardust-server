"""High-Throughput Experiments: making and testing many material samples at once."""
CODE = 'mining5_high_throughput'
BOOK = {
    "title": 'High-Throughput Experiments',
    "subtitle": 'Making and testing hundreds of samples at once',
    "chapters": [
        ('Combinatorial libraries', 'A combinatorial library is a set of samples that vary in composition, often laid out on one plate or wafer. Each spot holds a slightly different mix. One run can therefore test many recipes side by side.'),
        ('Robotics', 'Robots mix powders, deposit thin films and move samples between stations. They work steadily through the night and do not tire. Their precision keeps the samples comparable with one another.'),
        ('Data', "Each test produces a large amount of data, which must be recorded with the sample's position and recipe. Good labels and databases let researchers match each result to its sample. Without careful records, the data loses its value."),
        ('Rapid testing', 'Fast tools measure properties such as electrical conduction, colour or hardness for each spot. Some tools scan a whole plate in minutes. Speed lets the team learn from many failures quickly.'),
        ('Analysis', 'Analysis looks for trends across the library, such as which mix gives the best result. Statistical checks help separate real effects from noise. Results are often checked again with larger, slower tests.'),
        ('Lessons', 'Most samples in a high-throughput run will not be useful, and that is expected. The method is valuable because it shows the way forward quickly. Repeating good results in a second, independent test is always needed before trusting them.'),
    ],
    "test": [
        ('What is a combinatorial library?', [('a', 'A set of samples that vary in composition, often on one plate'), ('b', 'A book of chemistry rules'), ('c', 'A list of metal prices'), ('d', 'A storage room for coal')], 'a'),
        ('What is the main advantage of high-throughput experiments?', [('a', 'They need no records'), ('b', 'They make only one sample'), ('c', 'They test many recipes in one run'), ('d', 'They avoid all measurement')], 'c'),
        ('Why must each test result be linked to its sample?', [('a', 'So the sample can be eaten'), ('b', 'So the robot can change colour'), ('c', 'So the plate becomes heavier'), ('d', 'So the data can be matched to the right recipe')], 'd'),
        ('What does statistical analysis help a team do?', [('a', 'Paint the samples'), ('b', 'Separate real effects from random noise'), ('c', 'Stop the robots'), ('d', 'Measure the weight of the room')], 'b'),
        ('Why is a good result repeated in a second test?', [('a', "To use up the robot's battery"), ('b', 'To make the data larger on purpose'), ('c', 'To confirm it is not a chance effect'), ('d', 'Because the first test is always wrong')], 'c'),
    ],
}
