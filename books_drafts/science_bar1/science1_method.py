"""The Scientific Method: how to find out what is true, one question at a time. Science career, bar 1 (Research Assistant)."""
CODE = 'science1_method'
BOOK = {
    "title": 'The Scientific Method',
    "subtitle": 'How to find out what is true, one question at a time',
    "chapters": [
        ('Start with a question',
         'Every experiment starts with a question you can test. "How much copper does 100 kg of chalcopyrite give?" is a good question, because you can weigh the result. "Is space nice?" is not, because nobody can measure it. A good question has an answer you can check with your hands or your instruments.'),
        ('Make a clear guess',
         'A hypothesis is a clear guess that could turn out to be wrong. Write it down before you test anything, for example: "About a third of the weight of this ore will be copper." Because it can be wrong, a hypothesis is useful. A guess that can never be proved wrong tells you nothing.'),
        ('Test one thing at a time',
         'In an experiment you change one thing and keep everything else the same. The part you keep the same is the control, and it lets you compare. If you change the sample, the furnace and the weight all at once, you will not know which one made the difference.'),
        ('Write down what you see',
         'Observations are what you notice while you work: the numbers on the scale, the colour, the time, the temperature. Write them down as they happen, using the same tool each time. Describe what you saw before you decide what it means.'),
        ('Reach a conclusion',
         'A conclusion says whether the evidence supports your hypothesis. It must match what you measured, no more and no less. If it does not match, the guess was wrong, or the test was poor, and both are worth knowing.'),
        ('Test it again',
         'A result you can repeat is one you can trust. Another scientist, or you tomorrow, should be able to follow the same method and get the same result. A result that cannot be repeated is set aside until someone can show it again.'),
    ],
    "test": [
        ('What makes a good scientific question?',
         [('a', 'Is space nice?'), ('b', 'Which craft is the best?'), ('c', 'How much copper does 100 kg of chalcopyrite give?'), ('d', 'Why do we exist?')], 'c'),
        ('What is the control in an experiment?',
         [('a', 'The part kept the same, so you can compare the change against it'), ('b', 'The final result'), ('c', 'The person who runs the test'), ('d', 'The tool you use to weigh things')], 'a'),
        ('Why do you write down observations as they happen?',
         [('a', 'So you can skip the test'), ('b', 'To make the results look better'), ('c', 'Because notes are never needed'), ('d', 'So your memory does not change the record')], 'd'),
        ('In the Semmelweis story from Vienna, what was tested?',
         [('a', 'Whether the wards were warm'), ('b', 'Whether washing hands in chlorinated lime lowered deaths'), ('c', 'Whether new mothers wanted to leave'), ('d', 'Whether the buildings were tall')], 'b'),
        ('What does repeating a test show?',
         [('a', 'That the test was too easy'), ('b', 'That the scientist is right about everything'), ('c', 'That the result is not a one-off accident and others can check it'), ('d', 'That the test is finished for good')], 'c'),
    ],
}
