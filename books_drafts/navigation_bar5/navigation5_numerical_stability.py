"""Numerical Stability in Navigation Software: how rounding and small errors can grow, and how good software keeps answers reliable."""
CODE = 'navigation5_numerical_stability'
BOOK = {
    "title": 'Numerical Stability in Navigation Software',
    "subtitle": 'Floating-point error, cancellation, ill-conditioning, tests and error control',
    "chapters": [
        ('Computers round numbers',
         'Computers store numbers with limited precision, so most results are rounded. The rounding is tiny at each step, but a long calculation can collect many tiny errors. Good software is designed with this in mind.'),
        ('Cancellation',
         'Cancellation happens when two nearly equal numbers are subtracted. Most of the leading digits cancel, and the answer keeps only a few reliable digits. Rearranging the formula can avoid it.'),
        ('Ill-conditioning',
         'A problem is ill-conditioned when small changes in the input cause large changes in the answer. Such problems amplify errors, so even exact arithmetic would give a sensitive result.'),
        ('Testing the software',
         'Tests compare the software against known answers, including tricky cases such as very small or very large values. Testing finds errors that would otherwise surface only in the field.'),
        ('Algorithms that stay stable',
         'Some algorithms are stable and keep errors small. Others can magnify them. Choosing a stable algorithm is one of the most important decisions in navigation software.'),
        ('Error control',
         'Error control means tracking how large the uncertainty is and warning when it becomes too big. Good systems report confidence along with the answer, so a user knows when to doubt it.'),
    ],
    "test": [
        ('Why do computers round numbers?',
         [('a', 'Because numbers are always whole'), ('b', 'Because numbers are painted'), ('c', 'Because they store numbers with limited precision'), ('d', 'Because numbers have no size')], 'c'),
        ('What is cancellation?',
         [('a', 'Stopping a program early'), ('b', 'Deleting a file'), ('c', 'Adding two large numbers'), ('d', 'Subtracting two nearly equal numbers so most leading digits are lost')], 'd'),
        ('What is an ill-conditioned problem?',
         [('a', 'A problem with no answer'), ('b', 'A problem where small input changes cause large output changes'), ('c', 'A problem about colours'), ('d', 'A problem with one number')], 'b'),
        ('Why do tests use tricky cases?',
         [('a', 'To find errors that would otherwise show only in the field'), ('b', 'To make the tests longer'), ('c', 'To avoid any checking'), ('d', 'To change the answer')], 'a'),
        ('What should good navigation software report with its answer?',
         [('a', 'Its colour'), ('b', 'Its confidence, so a user knows when to doubt it'), ('c', 'Its favourite number'), ('d', 'Its price')], 'b'),
    ],
}
