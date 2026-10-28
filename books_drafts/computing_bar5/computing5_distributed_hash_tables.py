"""Distributed Hash Tables: finding data by key across many peers, with no central index."""
CODE = 'computing5_distributed_hash_tables'
BOOK = {
    "title": 'Distributed Hash Tables',
    "subtitle": 'Finding data by key across many peers, with no central index',
    "chapters": [
        ('Finding data without a directory', 'In a peer-to-peer network there is no central list of who holds what. A distributed hash table lets any peer find the owner of a key, by a rule that maps each key to a place in a shared space. Every peer knows a little, and together they can find anything.'),
        ('The Chord ring', 'In Chord, peers and keys are placed on a ring of numbers, and each key belongs to the next peer around the ring. Chord was introduced in 2001 by Stoica and colleagues. A lookup moves around the ring until it reaches the peer that holds the key.'),
        ('Finger tables', 'To speed up lookup, each peer keeps a finger table of shortcuts to peers at growing distances around the ring. Each hop roughly halves the remaining distance, so a lookup takes about log n steps among n peers.'),
        ('Churn', 'Churn is the constant arrival and leaving of peers. A DHT must keep working as members come and go, by repairing the links that break. Good designs keep the system usable even when many peers are changing at once.'),
        ('Kademlia', 'Kademlia uses a different distance rule, based on the XOR of peer IDs, and each peer uses its routing table to find close peers quickly. The design is used in several popular peer-to-peer networks.'),
        ('Lookup costs', 'Each lookup needs several messages across the network, and each hop may take time. In peer-to-peer systems that cost is the price of having no central server. The design works well when lookups are common and peers are stable enough.'),
    ],
    "test": [
        ('What does a DHT let a peer do?',
         [('a', 'Find the owner of a key without a central list'), ('b', 'Paint the peer'), ('c', 'Count the stars'), ('d', 'Sell cars')], 'a'),
        ('What shape is the Chord space?',
         [('a', 'A square box'), ('b', 'A triangle of coins'), ('c', 'A ring'), ('d', 'A bicycle')], 'c'),
        ('What is a finger table?',
         [('a', 'A list of shortcuts to peers at growing distances'), ('b', 'A glove'), ('c', 'A list of errors'), ('d', 'A keyboard map')], 'a'),
        ('What is churn?',
         [('a', 'A kind of butter'), ('b', 'A clock error'), ('c', 'A broken cable'), ('d', 'The constant arrival and leaving of peers')], 'd'),
        ('Roughly how many steps does a Chord lookup take among n peers?',
         [('a', 'About log n steps'), ('b', 'Exactly one step'), ('c', 'About n squared steps'), ('d', 'No steps')], 'a'),
    ],
}
