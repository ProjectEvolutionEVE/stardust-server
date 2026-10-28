"""Reference Architectures: reusable, vendor-neutral designs that teams adapt to their own needs and keep under governance."""
CODE = 'computing5_reference_architectures'
BOOK = {
    "title": 'Reference Architectures',
    "subtitle": 'Reusable starting designs, tailored and governed',
    "chapters": [
        ('What a reference architecture is',
         'A reference architecture is a proven pattern for a common kind of system, such as an online shop or a data platform. It shows the main parts and how they fit together. Teams start from it instead of from a blank page.'),
        ('Reusable patterns',
         'Reusable patterns include layers, queues, caches and gateways that solve recurring problems. A reference design gathers them into a sensible arrangement. Each pattern carries known benefits and known costs.'),
        ('Vendor-neutral designs',
         'A vendor-neutral design describes the roles of components without tying them to one product. This keeps options open and makes the design easier to explain. Products are then chosen to fill those roles.'),
        ('Tailoring',
         'No two organisations need exactly the same system. Teams tailor a reference design by removing parts they do not need and adding the rules their business requires. The reference stays the base, and the differences are recorded.'),
        ('Governance',
         'Governance keeps reference designs consistent across teams. Review boards approve changes, and exceptions are recorded with reasons. Good governance guards against each team quietly inventing its own version.'),
        ('Cloud examples and maintenance',
         'Cloud providers publish reference designs that show how the same pattern can be built on their services. Those examples age, so they need regular review. A reference that nobody maintains soon describes a system that no longer exists.'),
    ],
    "test": [
        ('What is a reference architecture?',
         [('a', 'A type of computer monitor'), ('b', 'A bill from a supplier'), ('c', 'A paper for a school test'), ('d', 'A proven pattern for a common kind of system')], 'd'),
        ('What does vendor-neutral mean for a design?',
         [('a', "It is designed by a vendor's own staff"), ('b', 'It describes component roles without tying them to one product'), ('c', 'It cannot be drawn'), ('d', 'It bans all software')], 'b'),
        ('What should a team do when tailoring a reference design?',
         [('a', 'Copy it word for word and tell no one'), ('b', 'Throw it away and start blank'), ('c', 'Remove what is not needed and record the differences'), ('d', 'Print it and hide it')], 'c'),
        ('What is the purpose of governance for reference designs?',
         [('a', 'To keep designs consistent and exceptions recorded'), ('b', 'To stop all changes forever'), ('c', 'To choose the office snacks'), ('d', 'To remove every pattern')], 'a'),
        ('Why does a reference design need regular maintenance?',
         [('a', 'Because paper rots in a week'), ('b', 'Examples and designs age, and an unmaintained one describes a system that no longer exists'), ('c', 'Because designs cannot be read'), ('d', 'Because maintenance is a legal form')], 'b'),
    ],
}
