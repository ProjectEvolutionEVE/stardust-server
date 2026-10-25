"""Binary and Data: bits, bytes, counting in twos, and how text and pictures become numbers."""
CODE = 'computing1_binary'
BOOK = {
    "title": 'Binary and Data',
    "subtitle": 'Bits, bytes, and how text and pictures become numbers',
    "chapters": [
        ('Two states',
         'A computer\'s memory is made of billions of tiny switches, and each one is either on or off. We write on as 1 and off as 0. One switch holding one of these two values is called a bit.'),
        ('Counting in twos',
         'Binary is counting with only two digits, 0 and 1. Each place is worth double the place to its right: 1, 2, 4, 8, 16 and so on. So binary 101 means 4, plus nothing for the 2, plus 1, which makes 5.'),
        ('Bytes',
         'Eight bits together make one byte. A single byte can hold 256 different values, from 0 up to 255. Bigger amounts are counted in kilobytes, megabytes and gigabytes, each one roughly a thousand times the last.'),
        ('Text as numbers',
         'Every letter is given a number. In the common ASCII code, a capital A is 65, which is 01000001 in binary. Modern text uses a larger system called Unicode, which covers every alphabet and many symbols.'),
        ('Pictures as numbers',
         'A picture is a grid of tiny dots called pixels. Each pixel\'s colour is stored as three numbers, for red, green and blue, and each number runs from 0 to 255. Mixing those three gives about 16 million colours.'),
        ('Why this matters',
         'Everything a computer keeps, from a letter to a price or a receipt code, is kept as numbers in this same way. The machine only ever sees bits. What they mean depends on how the program reads them.'),
    ],
    "test": [
        ('How many bits make up one byte?',
         [('a', '4'), ('b', '8'), ('c', '10'), ('d', '16')], 'b'),
        ('What is the binary number 110 in ordinary numbers?',
         [('a', '3'), ('b', '5'), ('c', '7'), ('d', '6')], 'd'),
        ('How many different values can a single byte hold?',
         [('a', '256'), ('b', '8'), ('c', '100'), ('d', '1024')], 'a'),
        ('In the ASCII code, which number stands for a capital A?',
         [('a', '1'), ('b', '52'), ('c', '65'), ('d', '97')], 'c'),
        ('How is the colour of one pixel usually stored?',
         [('a', 'As one long word for the whole picture'), ('b', 'As three numbers for red, green and blue'), ('c', 'As a list of shapes only'), ('d', 'As a sound file')], 'b'),
    ],
}
