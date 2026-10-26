"""Medicine, bar 3 (Senior Doctor), part B: Muscle Fibres. Slow and fast fibres, how muscle is rebuilt, and why use keeps muscle while disuse wastes it."""
CODE = "medicine3b_muscle_fibres"
BOOK = {
    "title": "Muscle Fibres: Use It or Lose It",
    "subtitle": "Two kinds of muscle fibre, how muscle grows and shrinks, and why load keeps it",
    "chapters": [
        ("Muscle is built from fibres",
         "Each muscle is a bundle of long cells called fibres. A nerve signal makes the fibres contract, and the whole muscle pulls on the bone it is joined to through a tendon. Many bundles together make one muscle."),
        ("Slow and fast fibres",
         "Some fibres work slowly and tire slowly, which suits steady work such as holding posture. Others work quickly and powerfully, but tire sooner. Most muscles contain a mix of both, and the mix differs from person to person."),
        ("Protein keeps the machinery",
         "Muscle is rebuilt all the time. The body joins amino acids from food into new muscle proteins, a process called muscle protein synthesis, and it also breaks old proteins down. When building outweighs breakdown, muscle grows, and when breakdown wins, it shrinks."),
        ("Use it or lose it",
         "Muscle that is used regularly keeps its size and strength. Muscle that is not loaded begins to shrink. In spaceflight the postural muscles that normally fight gravity, such as those in the calf, are affected most, because they have so little to do."),
        ("Satellite cells",
         "Satellite cells sit beside muscle fibres. When a muscle is worked hard, these cells can become active and help repair the fibres and add to them. Their activity depends on rest, good food and the load placed on the muscle."),
        ("Keeping muscle strong",
         "Regular strength work, which pushes the muscles against a load, is the strongest signal to keep or build muscle. Enough protein across the day supports the rebuilding. Rest between hard sessions is part of the plan, because muscle is rebuilt while the body recovers."),
    ],
    "test": [
        ("What is a muscle made of?",
         [("a", "Bundles of long fibres"), ("b", "Small bones"), ("c", "Blood only"), ("d", "Sheets of skin")], "a"),
        ("Which type of muscle fibre tends to tire slowly and suits steady holding of posture?",
         [("a", "Fast fibres"), ("b", "Slow fibres"), ("c", "Nerve fibres"), ("d", "Bone fibres")], "b"),
        ("What happens when muscle breakdown is greater than muscle building?",
         [("a", "Muscle grows"), ("b", "Muscle turns into bone"), ("c", "Nothing changes"), ("d", "Muscle shrinks")], "d"),
        ("In low gravity, which muscles are affected most?",
         [("a", "The muscles of the face"), ("b", "Muscles used only for speaking"), ("c", "Postural muscles, such as the calf"), ("d", "The muscles of the hands only")], "c"),
        ("What gives the strongest signal to keep or build muscle?",
         [("a", "Sitting still all day"), ("b", "Regular strength work against a load"), ("c", "Sleeping less"), ("d", "Skipping meals")], "b"),
    ],
}
