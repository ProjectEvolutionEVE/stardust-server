"""Logic and Decisions: true and false, AND, OR, NOT, if-then-else and loops, the way a program chooses what to do."""
CODE = 'computing1_logic'
BOOK = {
    "title": 'Logic and Decisions',
    "subtitle": 'True and false, AND, OR, NOT, if, then and loops',
    "chapters": [
        ('True and false',
         'Logic is reasoning with statements that are either true or false, with nothing in between. "The hold is full" is either true or false. Computers make every decision by checking statements like this one.'),
        ('AND',
         'AND is true only when both statements are true. "The craft has fuel AND the hatch is closed" is true only when both parts hold. If either part is false, the whole statement is false.'),
        ('OR',
         'OR is true when at least one of the statements is true, and also when both are. "The bank has credit OR the market has a buyer" is true if either part is true, so only a statement with both parts false fails.'),
        ('NOT',
         'NOT turns a statement around. If "the thruster is on" is true, then NOT "the thruster is on" is false. NOT is the simplest of the three, but it is needed everywhere a rule says "unless".'),
        ('If, then and otherwise',
         'A decision is written as: if a condition is true, do this, otherwise do that. A game might say: if a body bar is below 50, the character is impaired; otherwise carry on as normal. Every choice a program makes is built from this.'),
        ('Loops',
         'A loop repeats steps while a condition is true, or a set number of times, or once for each item in a list. A loop must have a way to end. A loop that never ends is called an infinite loop, and it is a common kind of bug.'),
    ],
    "test": [
        ('Which of these is a statement that is either true or false?',
         [('a', 'Open the hatch, please'), ('b', 'How fast is the craft?'), ('c', 'Maybe the Starship is near'), ('d', 'The hold is full')], 'd'),
        ('When is the statement "A AND B" true?',
         [('a', 'When either A or B is true'), ('b', 'When both A and B are true'), ('c', 'When neither is true'), ('d', 'When A is false')], 'b'),
        ('When is the statement "A OR B" true?',
         [('a', 'Only when both are true'), ('b', 'Only when both are false'), ('c', 'When at least one of them is true'), ('d', 'Never')], 'c'),
        ('If "the light is on" is false, what is NOT "the light is on"?',
         [('a', 'True'), ('b', 'False'), ('c', 'Maybe'), ('d', 'Unknown')], 'a'),
        ('What is the danger of a loop that has no way to end?',
         [('a', 'It saves too many files'), ('b', 'It repeats forever, which is called an infinite loop'), ('c', 'It makes the screen brighter'), ('d', 'It clears the memory')], 'b'),
    ],
}
