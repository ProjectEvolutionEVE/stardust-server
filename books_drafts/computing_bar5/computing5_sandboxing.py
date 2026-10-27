"""Sandboxing and Isolation: running untrusted code inside a box with strict limits on what it may touch."""
CODE = 'computing5_sandboxing'
BOOK = {'title': 'Sandboxing and Isolation',
 'subtitle': 'Process and virtual machine boundaries, WebAssembly, capabilities and escapes',
 'chapters': [('Running code you do not trust',
               'A sandbox runs code with strict limits on what it can reach. It lets a program run '
               'safely even when its author cannot be trusted. Sandboxes protect both the user and '
               'the wider system.'),
              ('Process and virtual machine boundaries',
               'Operating systems separate programs into processes that cannot freely touch each '
               'other. Virtual machines go further and separate whole operating systems. Each '
               'boundary must be enforced by the layer below it.'),
              ('WebAssembly sandboxes',
               'WebAssembly runs code inside a memory-safe box in browsers and other hosts. The '
               'code can only use what the host hands it. This design is used to run third-party '
               'modules.'),
              ('Capability restrictions',
               'A sandbox often gives a program only the abilities it needs. Access to files, the '
               'network and devices can be denied by default. Least privilege limits the harm of '
               'any single flaw.'),
              ('Escape history',
               'Sandboxes have been escaped many times over the years, through flaws in the '
               'boundary or in what it exposes. Each escape led to a fix and to tighter design. '
               'History shows that defence in depth is needed.'),
              ('Design trade-offs',
               'Strict sandboxes can make programs harder to write and slower to run. Designers '
               'balance safety with how useful the code must be. The right line depends on how '
               'much the code is trusted.')],
 'test': [('What is a sandbox for?',
           [('a', 'Growing plants'),
            ('b', 'Running code with strict limits on what it can reach'),
            ('c', 'Playing games on a beach'),
            ('d', 'Storing paper')],
           'b'),
          ('What does a virtual machine separate?',
           [('a', 'Paper from ink'),
            ('b', 'Music from silence'),
            ('c', 'Whole operating systems from each other'),
            ('d', 'Rain from sunshine')],
           'c'),
          ('What does a WebAssembly sandbox let code use?',
           [('a', 'Everything on the disk'),
            ('b', 'Every camera in the house'),
            ('c', 'Any secret password'),
            ('d', 'Only what the host hands it')],
           'd'),
          ('What is least privilege?',
           [('a', 'Giving a program only the abilities it needs'),
            ('b', 'Giving every program full power'),
            ('c', 'Removing all programs'),
            ('d', 'Printing the code')],
           'a'),
          ('Why does defence in depth matter for sandboxes?',
           [('a', 'Because sandboxes never fail'),
            ('b', 'Because layers make the code slower to read'),
            ('c', 'Because sandboxes have been escaped before, so more than one layer helps'),
            ('d', 'Because sandboxes need no testing')],
           'c')]}
