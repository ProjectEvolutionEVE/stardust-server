"""Reading a Blueprint: how a builder reads a design, from its purpose and parts to its weight and its serial number."""
CODE = 'engineering1_blueprint'
BOOK = {
    "title": 'Reading a Blueprint',
    "subtitle": 'How a builder reads a design: its purpose, its parts, its weight and its serial',
    "chapters": [
        ('A blueprint is a plan for building',
         'A blueprint is a written design that someone else can build exactly. Read it the way a builder would: before you '
         'touch a material, check what the design is for, what it needs and what it will weigh. Every approved blueprint has '
         'been through the review team.'),
        ('What it is, and why',
         'Start with the name, the kind (a part, a tool or machine, a ship, or something else) and the problem it solves. '
         'Then check whether it is brand new, an upgrade, or a newer version or model. An upgrade or newer version names what '
         'it builds on and says what is different, so read that line closely.'),
        ('What it does, fits and improves',
         'These answers tell you the job. "Does" lists each thing the design does, in detail. "Fits" says what it attaches to: '
         'a ship, a machine, or nothing at all. "Improves" says what gets better, and by how much.'),
        ('The books it requires',
         'A design lists the library books it needs, so a builder knows what to learn first. Read that list before you start, '
         'and check which books you have already studied. Books are the knowledge behind the steps, not the parts themselves.'),
        ('Weight and size from the materials',
         'Each part lists its materials in kilograms. The weight is the total of those amounts. The space they take up is each '
         'amount divided by its density, added up: 1 kg of aluminium takes about 0.00037 m³, while 1 kg of iron takes about '
         '0.00013 m³. A design can have up to 30 parts, each with up to 20 materials.'),
        ('Steps, time and serial numbers',
         'How it is built gives the tools, skills and numbered steps. Build time is in minutes, hours or days, up to a year, '
         'and builds run in real time. An approved design has a model code, such as BP-K7Q3X. Its original is BP-K7Q3X-ORIGINAL, '
         'and each printed copy carries its run and copy number, such as BP-K7Q3X-R2-0025.'),
    ],
    "test": [
        ("What is the first thing to check on a blueprint?",
         [("a", "Its colour"), ("b", "What it is for and the problem it solves"), ("c", "Its serial number"), ("d", "Its price on the market")], "b"),
        ("How is a blueprint's weight worked out?",
         [("a", "The designer types it in"), ("b", "The review team guesses it"), ("c", "The total of its material amounts, in kilograms"), ("d", "The market price of its parts")], "c"),
        ("Which takes more space: 1 kg of iron or 1 kg of aluminium?",
         [("a", "Iron"), ("b", "The same"), ("c", "Neither takes up space"), ("d", "Aluminium")], "d"),
        ("What does BP-K7Q3X-R2-0025 tell you?",
         [("a", "It is the designer's original"), ("b", "It is copy 25 of run 2 of the design BP-K7Q3X"), ("c", "It is the 25th design the player made"), ("d", "It is a market price code")], "b"),
        ("Can a serial number check tell you who owns a copy?",
         [("a", "Yes, it shows the owner's name"), ("b", "Yes, it shows the price paid"), ("c", "No. It shows what the copy is, its run and copy, and when it was made, but never who owns it"), ("d", "Only the designer can see it")], "c"),
    ],
}
