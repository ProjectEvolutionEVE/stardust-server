"""Change Control: recording every design change, checking what it touches and keeping the records straight."""
CODE = 'engineering3c_change_control'
BOOK = {
    "title": 'Change Control: Revising a Design Safely',
    "subtitle": 'Recording every change, checking what it touches and keeping the records straight',
    "chapters": [
        ('Designs change',
         "A design is revised many times, before and after it is built. Each change is a risk, because one edit can break a part that was working. Change control is the set of rules that keeps changes safe."),
        ('Revision letters',
         "Each approved version of a drawing carries a revision mark, such as A, B or C. Builders always work from the latest approved revision. A part built to an old revision can look right and still be wrong."),
        ('Writing the change',
         "A change request says what is changing, why it is changing and what it affects. Writing the reason matters as much as the change itself. A future engineer will need to know why the part looks the way it does."),
        ('Checking what it touches',
         "Before a change is approved, list every part, drawing, test and supplier it touches. A change to one bracket can move a bolt, shift a load and invalidate a test. Follow the links before you agree."),
        ('Testing again',
         "After a change, repeat the tests that the change could affect, not only the test for the new part. A small edit can change a result somewhere else. Record the new results against the new revision."),
        ('The cost of a late change',
         "A change caught on paper costs little. The same change found on the finished build can cost many times more. Put the review early and keep it sharp. Good change control saves money by catching errors when they are cheap to fix."),
    ],
    "test": [
        ('Why is change control needed?',
         [('a', 'To make designs heavier'), ('b', 'To stop drawings being printed'), ('c', 'Because every change is a risk, since one edit can break a part that was working'), ('d', 'To remove revision marks')], 'c'),
        ('What does a revision mark, such as B or C, tell a builder?',
         [('a', 'Which approved version of the drawing to work from'), ('b', 'The colour of the part'), ('c', 'The price of the part'), ('d', 'The date of lunch')], 'a'),
        ('What should a change request say?',
         [('a', 'Only the new price'), ('b', 'Only the name of the person who asked'), ('c', 'Nothing, if the change is small'), ('d', 'What is changing, why, and what it affects')], 'd'),
        ('After a change, which tests should be repeated?',
         [('a', 'None, since only the new part matters'), ('b', 'Those the change could affect, not only the test for the new part'), ('c', 'Only the paint test'), ('d', 'Tests from ten years ago')], 'b'),
        ('Why is an early review of a change worth more?',
         [('a', 'Because late reviews are never allowed'), ('b', 'Because it makes a longer drawing'), ('c', 'Because a change caught on paper costs little, while one found on the finished build can cost many times more'), ('d', 'Because paper is cheaper')], 'c'),
    ],
}
