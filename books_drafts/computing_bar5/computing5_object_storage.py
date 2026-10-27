"""Object Storage Design: keeping huge piles of files safe, findable and cheap to hold."""
CODE = 'computing5_object_storage'
BOOK = {'title': 'Object Storage Design',
 'subtitle': 'Flat namespaces, metadata, durability and lifecycle rules',
 'chapters': [('Files without folders',
               'Object storage keeps data as objects, each with a unique name and no real folder '
               'tree behind it. Folders you see on screen are just names that share a prefix. This '
               'flat design lets a system grow to billions of objects without one giant directory '
               'slowing everything down.'),
              ('Objects and metadata',
               'Each object holds its data and a set of metadata: size, type, date, and any labels '
               'the owner adds. Metadata lets a system search and sort without opening every file. '
               'Keeping metadata small and well chosen is a design decision with real cost.'),
              ('Keeping data safe with erasure coding',
               'Rather than storing three full copies, many systems cut an object into fragments '
               'and add parity fragments. Any set of pieces that is large enough can rebuild the '
               'whole object. This gives strong protection for less extra space than full copies.'),
              ('Durability targets',
               'Designers state a durability target: the chance that an object is lost in a year. '
               'Cloud providers publish very high targets. A target is only as good as the repair '
               'work behind it, so a good design checks and rebuilds lost pieces quickly.'),
              ('Listing takes time',
               'Many systems update data in many places, so a listing of all objects may briefly '
               'miss a new one. This is called eventual consistency. Apps must be built to expect '
               'a short delay between a write and a full listing.'),
              ('Lifecycle rules',
               'A lifecycle rule moves old objects to cheaper, slower storage or deletes them '
               'after a set time. Rules save money without anyone touching each file. Good rules '
               'are written down, tested and reviewed, because a wrong rule can remove data that '
               'someone still needs.')],
 'test': [('What is a flat namespace in object storage?',
           [('a', 'Every object sits in one deep folder tree'),
            ('b', 'Objects have unique names and no real folder tree behind them'),
            ('c', 'Only one object can be stored at a time'),
            ('d', 'Objects are stored only on paper')],
           'b'),
          ('What does metadata describe?',
           [('a', 'The weather near the data centre'),
            ('b', 'The price of the storage plan'),
            ('c', 'The data inside an object, such as its size, type and labels'),
            ('d', 'The name of the data centre engineer')],
           'c'),
          ('What is erasure coding used for?',
           [('a', 'Printing copies of files'),
            ('b', 'Speeding up a single laptop'),
            ('c', 'Hiding file names from users'),
            ('d', 'Splitting data into pieces with parity so the whole can be rebuilt')],
           'd'),
          ('What does eventual consistency mean for a listing?',
           [('a', 'A new object may take a short time to appear in a full listing'),
            ('b', 'Listings never change'),
            ('c', 'Every object is deleted each night'),
            ('d', 'Only the owner can see the list')],
           'a'),
          ('What is the purpose of a lifecycle rule?',
           [('a', 'To make the data centre colder'),
            ('b', 'To rename every object'),
            ('c', 'To move or remove old objects automatically on a set schedule'),
            ('d', 'To stop all writes for ever')],
           'c')]}
