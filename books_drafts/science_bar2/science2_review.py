"""Peer Review and Honest Science: how other scientists check a result, and why results must be repeated. Science career, bar 2 (Scientist)."""
CODE = 'science2_review'
BOOK = {
    "title": 'Peer Review and Honest Science',
    "subtitle": 'How other scientists check a result, and why it must be repeated',
    "chapters": [
        ('Publishing a result',
         'A scientist writes up the question, the method, the data and the conclusion, so that others can follow every step. The write-up is then sent to a scientific journal. Publication lets the whole field see the work and test it.'),
        ('What peer review is',
         'Before a paper is published, independent experts in the same field read it. They check whether the method is sound, whether the data support the conclusion, and whether the work is new. Their reports often go back to the author with questions.'),
        ('Peer review is not perfect',
         'Reviewers can miss mistakes, and they can be biased by their own views or by who wrote the paper. Publication is the start of checking, not the end. A paper that passed review can still turn out to be wrong.'),
        ('Replication',
         'Other laboratories repeat the work to see whether they get the same result. Independent replication is one of the strongest tests a claim can face. A result that only one team has ever produced is not yet a settled fact.'),
        ('Negative results',
         'A well-run test that finds nothing is still a result. It shows what does not work and stops others repeating a dead end. Yet negative results are published less often, which can leave the field with a lopsided picture.'),
        ('Honesty and disclosure',
         'Scientists must report who funded their work and any interest that could bias it. Fabricating or altering data is serious misconduct, and it often comes to light when others try to repeat the work and fail.'),
    ],
    "test": [
        ('What does peer review check?',
         [('a', 'Whether the paper is short enough'), ('b', 'Whether the authors are famous'), ('c', 'Whether the method is sound and the conclusion follows from the data'), ('d', 'Whether the paper has pictures')], 'c'),
        ('What is replication?',
         [('a', 'Copying a paper word for word'), ('b', 'Repeating the work independently to see if the same result comes out'), ('c', 'Printing the results twice'), ('d', 'Asking the author for a second opinion')], 'b'),
        ('Why is a negative result valuable?',
         [('a', 'It shows what does not work, so others can avoid the same dead end'), ('b', 'It proves the test was wrong'), ('c', 'It is never worth writing down'), ('d', 'It always means the author failed')], 'a'),
        ('Which statement about peer review is true?',
         [('a', 'It guarantees the paper is correct'), ('b', 'It is never needed'), ('c', 'It is done only after publication'), ('d', 'It can miss mistakes, so it does not guarantee the truth')], 'd'),
        ('What is publication bias?',
         [('a', 'Papers being printed in the wrong colour'), ('b', 'Journals only printing papers by famous authors'), ('c', 'Positive results being published more often than negative ones'), ('d', 'Reviewers reading too quickly')], 'c'),
    ],
}
