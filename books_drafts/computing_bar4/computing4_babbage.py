"""Charles Babbage and the Analytical Engine: the early plans for programmable machines and why they were never finished."""
CODE = 'computing4_babbage'
BOOK = {
    "title": 'Charles Babbage and the Analytical Engine',
    "subtitle": 'Early plans for programmable machines, and why they were never finished',
    "chapters": [
        ('The difference engine',
         'In the 1820s, Charles Babbage designed the Difference Engine, a mechanical machine to calculate and print mathematical tables. Errors in printed tables were a real problem at the time. The machine was meant to remove human mistakes from the work.'),
        ('The analytical engine design',
         'In the 1830s, Babbage turned to a more general design, the Analytical Engine. It had a store for numbers and a mill for calculations, and it could follow different steps depending on results. It is seen as a plan for a general-purpose computer.'),
        ('Punched-card programming',
         'Babbage planned to use punched cards, borrowed from the Jacquard loom, to give the machine its instructions. Cards could also carry numbers. This idea of instructions held outside the machine is one of the important early ideas in computing.'),
        ('Limits of mechanical work',
         'The machines were enormously complex, and the precision needed for their parts was hard to achieve in the workshops of the time. Funding problems and disputes also stopped the work. Babbage never saw a complete Analytical Engine built.'),
        ('Ada Lovelace’s notes',
         'Ada Lovelace translated an article about the Analytical Engine and added long notes of her own. Her notes included a method for calculating Bernoulli numbers, and she wrote about machines handling more than numbers. Her work is often called an early program.'),
        ('Legacy',
         'Babbage’s ideas of stored instructions and general calculation influenced later thinkers. Many historians see his plans as a bridge between mechanical calculation and modern computers. His work reminds us that a good design can come long before the tools to build it.'),
    ],
    "test": [
        ('What did the Difference Engine calculate and print?',
         [('a', 'Paintings'), ('b', 'Railway timetables'), ('c', 'Mathematical tables'), ('d', 'Weather maps')], 'c'),
        ('What was the Analytical Engine?',
         [('a', 'A general-purpose design with a store and a mill'), ('b', 'A steam railway locomotive'), ('c', 'A printing press for newspapers'), ('d', 'A clock for the church tower')], 'a'),
        ('What did Babbage borrow to give instructions to his machine?',
         [('a', 'Paper maps'), ('b', 'Glass lenses'), ('c', 'Radio signals'), ('d', 'Punched cards from the Jacquard loom')], 'd'),
        ('What did Ada Lovelace write about?',
         [('a', 'A guide to growing flowers'), ('b', 'A method for calculating Bernoulli numbers in her notes'), ('c', 'A recipe for bread'), ('d', 'A history of ships')], 'b'),
        ('Why was the Analytical Engine never completed?',
         [('a', 'It was completed and then lost at sea'), ('b', 'It was never designed'), ('c', 'Engineering, funding and disputes stopped the work'), ('d', 'It was banned by the king')], 'c'),
    ],
}
