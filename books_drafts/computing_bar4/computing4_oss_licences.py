"""Open-Source Licences: what permissive and copyleft licences allow, what they require, and how they fit together."""
CODE = 'computing4_oss_licences'
BOOK = {
    "title": 'Open-Source Licences',
    "subtitle": 'What permissive and copyleft licences allow, require and forbid',
    "chapters": [
        ('Why licences matter',
         'Software is protected by copyright, so nobody may copy or change it without permission. An open-source licence is the written permission that the owner gives to everyone, on stated terms. Reading the licence is part of using the code properly.'),
        ('Permissive licences',
         'Permissive licences, such as the MIT licence and the Apache 2.0 licence, let you use, change and sell the software with few conditions. Usually you must keep the copyright notice and the licence text. Apache 2.0 also covers patents, which matters to large companies.'),
        ('Copyleft licences',
         'Copyleft licences, such as the GNU General Public License, require that changed versions you distribute carry the same freedoms. This keeps the code open for everyone who receives it. The exact trigger, such as distribution or network use, depends on the licence.'),
        ('Obligations and compatibility',
         'Mixing code from different licences can create conflicts. Some licences cannot be combined in one product that is distributed. Check the compatibility of each licence before combining code, and keep a record of what was used.'),
        ('Licence scanning',
         'Automatic licence scanners read the dependencies of a project and list their licences. They help teams catch surprises early, such as a copyleft library hidden deep in the tree. A scanner finds clues, and a person still needs to make the final call.'),
        ('Dual licensing and contribution policies',
         'Some companies offer the same code under two licences, one free and one paid, which is called dual licensing. Contribution policies decide how outside code enters a project, often by requiring the contributor to agree to the licence. Clear policies protect both the project and its users.'),
    ],
    "test": [
        ('What does an open-source licence give you?',
         [('a', 'The owner’s house'), ('b', 'Written permission to use the software on stated terms'), ('c', 'Ownership of every future version'), ('d', 'A free office')], 'b'),
        ('Which licence is a common permissive one?',
         [('a', 'Gnu General Public License'), ('b', 'Copyleft only'), ('c', 'Trade secret'), ('d', 'MIT')], 'd'),
        ('What do copyleft licences require?',
         [('a', 'That changed versions you distribute keep the same freedoms'), ('b', 'That no one may ever read the code'), ('c', 'That the code is printed on paper'), ('d', 'That the author receives no credit')], 'a'),
        ('Why check licence compatibility before combining code?',
         [('a', 'Compatible licences cost more'), ('b', 'Licences expire at lunchtime'), ('c', 'Some licences cannot be combined in one distributed product'), ('d', 'Compatibility is never a concern')], 'c'),
        ('What is a licence scanner for?',
         [('a', 'Painting the office walls'), ('b', 'Writing new code automatically'), ('c', 'Sending invoices to customers'), ('d', 'Finding licence conflicts and surprises among dependencies')], 'd'),
    ],
}
