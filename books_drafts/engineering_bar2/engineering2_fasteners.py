"""Joints and Fasteners: bolts, washers, rivets and welds, and how to keep a joint held."""
CODE = 'engineering2_fasteners'
BOOK = {
    "title": 'Joints and Fasteners',
    "subtitle": 'Bolts, rivets and welds: how parts are held together, and how to keep them held',
    "chapters": [
        ('Why join things',
         "Parts are joined so that they carry loads together. A joint must hold its load, resist vibration and, if it will be "
         "serviced, come apart without damage. Some joints are meant to be taken apart, and others are meant to be permanent. "
         "Choose the joint for the job."),
        ('Bolts, nuts and washers',
         "A bolt is a threaded rod with a head. As you tighten the nut, the bolt stretches like a spring, and that stretch is "
         "the clamping force holding the parts together. A washer spreads the load under the head or the nut, and protects "
         "the surface from being dented."),
        ('Torque and clamp force',
         "Torque is the twisting effort you apply to a nut or bolt. Much of it goes to friction under the head and in the "
         "threads, and only part becomes clamping force. That is why a torque wrench, set to the figure on the drawing, is the "
         "usual way to get the right tension. Over-tightening can stretch or snap a bolt, and too little lets the joint loosen."),
        ('Locking against vibration',
         "Vibration can work a tight joint loose over time. Lock washers, thread-locking compound and safety wire are common "
         "answers. A witness mark, a line of paint across the nut and the parts, shows at a glance whether anything has moved."),
        ('Rivets and welds',
         "A rivet is a metal pin with a head. It is pushed through matching holes, then a second head is formed on the far "
         "side, which makes a permanent joint that is easy to inspect. A weld fuses the metal of the parts themselves, so a "
         "sound weld is as strong as the metal around it."),
        ('Choosing and checking',
         "Match the fastener's metal to the parts. Mixing metals that are far apart in reactivity can cause galvanic corrosion, "
         "as the Corrosion and Protection book explains. Before you rely on a joint, check that the size is right, that it is "
         "tight, and that its threads are not damaged."),
    ],
    "test": [
        ("What happens to a bolt as you tighten its nut?",
         [('a', 'It melts a little'), ('b', 'It stretches like a spring, and that stretch clamps the parts together'), ('c', 'Its head gets shorter'), ('d', 'It turns into a rivet')], 'b'),
        ("Why is a torque wrench used on a joint?",
         [('a', 'It paints the joint so it can be seen'), ('b', 'It cuts new threads'), ('c', 'It applies the set twist from the drawing, so the joint gets the right tension'), ('d', 'It spins the bolt faster')], 'c'),
        ("What is the main job of a lock washer or thread-locking compound?",
         [('a', 'To stop vibration loosening a tight joint'), ('b', 'To stop the joint being taken apart at all'), ('c', 'To make the bolt heavier'), ('d', 'To make the joint conduct electricity')], 'a'),
        ("How is a rivet fixed in place?",
         [('a', 'By screwing a nut onto its end'), ('b', 'By gluing it into the hole'), ('c', 'By melting its tip into a glass bead'), ('d', 'By forming a second head on the far side, after it passes through the holes')], 'd'),
        ("What is a washer's main job?",
         [('a', 'To store heat'), ('b', 'To spread the load under a bolt head or nut, and protect the surface'), ('c', 'To fill the thread'), ('d', 'To stop the bolt ever rusting')], 'b'),
    ],
}
