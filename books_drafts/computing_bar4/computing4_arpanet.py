"""ARPANET and Packet Switching: how breaking messages into packets led to a network of networks, and the open choices that followed."""
CODE = 'computing4_arpanet'
BOOK = {
    "title": 'ARPANET and Packet Switching',
    "subtitle": 'How breaking messages into packets led to a network of networks',
    "chapters": [
        ('The packet switching idea',
         'Packet switching breaks a message into small pieces, each sent separately and reassembled at the destination. If one route fails, the pieces can take another path. Researchers such as Paul Baran and Donald Davies developed the idea in the 1960s.'),
        ('The first links',
         'ARPANET was a research network funded by the United States government. Its first message was sent in October 1969, between a computer at UCLA and one at the Stanford Research Institute. The first attempt crashed after only a few letters.'),
        ('Protocol transitions',
         'Early ARPANET used an earlier set of rules for communication. In January 1983, the network moved to the TCP/IP protocols, a change that is often called flag day. TCP/IP later became the basis of the internet.'),
        ('Government funding',
         'The network was funded for research, with a goal of sharing computers across distant sites. Government support paid for the early work and set its direction. Many later networking ideas grew from this research.'),
        ('Open design choices',
         'Many early design choices were made openly, in documents called requests for comments. Anyone could read and respond, which encouraged shared standards. This open process helped the internet grow beyond one organisation.'),
        ('Lessons',
         'ARPANET shows how a simple idea, sending pieces that find their own way, can build something large and resilient. It also shows how open standards let many different systems join together. Its lessons still shape how networks are built.'),
    ],
    "test": [
        ('What does packet switching do with a message?',
         [('a', 'Prints it on paper'), ('b', 'Breaks it into small pieces that are sent separately'), ('c', 'Sends it only by post'), ('d', 'Stores it in a drawer')], 'b'),
        ('Which two places exchanged the first ARPANET message in 1969?',
         [('a', 'Two schools in one town'), ('b', 'A bank and a shop'), ('c', 'A ship and a lighthouse'), ('d', 'UCLA and the Stanford Research Institute')], 'd'),
        ('What set of protocols did ARPANET move to in 1983?',
         [('a', 'TCP/IP'), ('b', 'Morse code'), ('c', 'Post-office rules'), ('d', 'Telegram rules')], 'a'),
        ('What were the early design documents called?',
         [('a', 'Secret orders'), ('b', 'Fashion magazines'), ('c', 'Requests for comments'), ('d', 'Shopping lists')], 'c'),
        ('Why did open design choices help the network grow?',
         [('a', 'They kept all designs secret'), ('b', 'They stopped all new users'), ('c', 'They removed the need for standards'), ('d', 'They let many organisations read, respond and share standards')], 'd'),
    ],
}
