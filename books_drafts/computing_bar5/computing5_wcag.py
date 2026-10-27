"""Accessibility Standards (WCAG): the four principles, success criteria levels, testing with assistive technology, audits, common failures and legal context in general terms."""
CODE = 'computing5_wcag'
BOOK = {'title': 'Accessibility Standards (WCAG)',
 'subtitle': 'The international guidelines for making digital content usable by everyone',
 'chapters': [('The four principles',
               'The Web Content Accessibility Guidelines group their advice under four principles: content '
               'must be perceivable, operable, understandable and robust. Each principle covers ways that '
               'people with different abilities can use the web.'),
              ('Success criteria and levels',
               'Each guideline breaks down into testable success criteria, graded at levels A, AA and AAA. '
               'Level AA is the level most often required by policy and law. Meeting a higher level is good, '
               'but it is not always practical for every page.'),
              ('Testing with assistive technology',
               'Automated checks find some problems but not all. Testing with screen readers, keyboard-only '
               'navigation and magnification shows how real users experience a page. Both automated and '
               'manual testing are needed.'),
              ('Audits',
               'An accessibility audit reviews a product against the standard, lists failures with evidence, '
               'and suggests fixes. Audits work best when they are repeated as the product changes, not only '
               'once at launch.'),
              ('Common failures',
               'Frequent problems include missing text alternatives for images, poor colour contrast, forms '
               'without clear labels, and content that cannot be used from a keyboard. Many of these are '
               'cheap to fix when they are designed in early.'),
              ('Legal context in general terms',
               'In many places, laws and public policies refer to these guidelines when they describe what '
               'accessible digital services must do. The exact duties depend on the country and the '
               'organisation, so specialist advice is needed for any particular case.')],
 'test': [('How many principles do the guidelines group their advice under?',
           [('a', 'Two'), ('b', 'Four'), ('c', 'Three'), ('d', 'Seven')],
           'b'),
          ('Which level is most often required by policy and law?',
           [('a', 'Level A'), ('b', 'Level AAA only'), ('c', 'Level AA'), ('d', 'No level at all')],
           'c'),
          ('What do automated checks alone miss?',
           [('a', 'Nothing at all'),
            ('b', 'All colour problems'),
            ('c', 'Every spelling error'),
            ('d', 'Some problems, so manual testing is also needed')],
           'd'),
          ('Which is a common failure named in the chapter?',
           [('a', 'Images with no text alternatives'),
            ('b', 'Pages that are too bright'),
            ('c', 'Keyboard shortcuts that are too fast'),
            ('d', 'Long words in headlines')],
           'a'),
          ('What does the chapter say about the legal duties?',
           [('a', 'They are the same in every country'),
            ('b', 'They vary, so specialist advice is needed for a particular case'),
            ('c', 'They do not exist'),
            ('d', 'They apply only to paper documents')],
           'b')]}
