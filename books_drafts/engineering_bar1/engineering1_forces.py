"""Forces and Structures: tension, compression, shear and bending, and why a triangle holds its shape."""
CODE = 'engineering1_forces'
BOOK = {
    "title": 'Forces and Structures',
    "subtitle": 'Tension, compression, shear and bending, and why a triangle holds its shape',
    "chapters": [
        ('A force pushes or pulls',
         'A force is a push or a pull. Every structure, from a bicycle frame to a bridge, is built to carry forces without '
         'moving more than it should. Forces are measured in newtons. On Earth, a 1 kg mass pulls down on its support with '
         'about 9.8 newtons.'),
        ('Tension and compression',
         'Tension stretches a member, like a rope or a cable. Compression squeezes it, like a column holding up a roof. Cables '
         'are used where things are pulled, and columns where things are pushed. Stone and concrete are strong in compression '
         'but weak in tension.'),
        ('Shear and bending',
         'Shear is when two parts of a member slide past each other, like the blades of scissors cutting paper. Bending '
         'happens when a beam is loaded across its length: its top is squeezed while its bottom is stretched. A shelf sags '
         'under a row of books for exactly this reason.'),
        ('Why a triangle holds its shape',
         'Three bars joined at their ends form a triangle, and it cannot change shape unless one of its bars changes length. '
         'A four-sided frame can lean over into a diamond with no bar changing length at all. Add one diagonal bar and the '
         'square becomes two triangles, which is why frames are braced that way.'),
        ('Trusses and towers',
         'A truss is a framework of triangles. Each bar carries either tension or compression, and together the bars spread a '
         'heavy load across the whole frame. The Eiffel Tower is an open lattice of wrought iron, and the Forth Bridge in '
         'Scotland, opened in 1890, is a steel truss bridge.'),
        ('Arches and cables',
         'An arch carries its load mostly in compression, pushing the stones together. That is why old stone arch bridges '
         'have lasted for centuries. A suspension bridge hangs its deck from cables in tension. Choose the shape that suits '
         'the forces it must carry.'),
    ],
    "test": [
        ("What does tension do to a cable?",
         [("a", "It squeezes it"), ("b", "It stretches it"), ("c", "It melts it"), ("d", "It bends it into a ring")], "b"),
        ("Which of these is loaded mostly in compression?",
         [("a", "A tow rope"), ("b", "A suspension cable"), ("c", "A hanging chain"), ("d", "A stone arch")], "d"),
        ("What is shear?",
         [("a", "Two parts sliding past each other, like scissors"), ("b", "Heat spreading through metal"), ("c", "A bar being stretched"), ("d", "A sudden fall")], "a"),
        ("Why is a triangle rigid when a square is not?",
         [("a", "Triangles are heavier"), ("b", "Three bars joined at their ends cannot change shape unless a bar changes length"), ("c", "Squares are made of more metal"), ("d", "Triangles float")], "b"),
        ("Which bridge hangs its deck from cables in tension?",
         [("a", "A cantilever bridge"), ("b", "A stone arch"), ("c", "A suspension bridge"), ("d", "A ferry")], "c"),
    ],
}
