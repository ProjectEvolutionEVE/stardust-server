"""Medicine, bar 3 (Senior Doctor), part A: The Immune Response in Depth. Antigens, helper cells, signals, clonal selection and how the response is switched off."""
CODE = "medicine3a_immune_depth"
BOOK = {
    "title": "The Immune Response in Depth",
    "subtitle": "Antigens, helper cells, signals and selection: how the response is organised",
    "chapters": [
        ("What the immune system recognises",
         "The immune system recognises antigens, which are molecular shapes found on germs and on abnormal cells. Specialist cells pick up pieces of antigen and display them on their surface. They carry this evidence to the places where the specialist lymphocytes are kept."),
        ("Helper T cells: the coordinators",
         "Helper T cells do not destroy germs themselves. They read the evidence on the antigen-displaying cells and release chemical signals that guide other cells. Their signals help decide whether the response leans toward killer cells, antibodies or inflammation."),
        ("Cytokines: the messages",
         "Cytokines are chemical messengers that tell cells what to do. Some call more defenders to a site, some turn inflammation up or down, and some tell cells to switch on their defences. Together they work like a switchboard, with many signals connected at once."),
        ("Selection of the best fit",
         "Before any infection, the body holds a huge range of B and T cells, each able to recognise a slightly different antigen. When one meets its match and is activated, it multiplies into many copies. This process, called clonal selection, is how the response grows around the right specialist."),
        ("Fever and inflammation",
         "Fever is a raised body temperature that many germs dislike and that helps immune cells work faster. Inflammation brings blood and defenders to an area. Both are useful in the right amount, but very strong or long-lasting responses can also harm healthy tissue."),
        ("Switching the response off",
         "A healthy response ends once the threat has gone. Regulatory cells and calming signals stop the response from running on after the job is done. Balance matters as much as strength, because an overactive response can do its own damage."),
    ],
    "test": [
        ("What is an antigen?",
         [("a", "A molecular shape that the immune system can recognise"), ("b", "A red blood cell"), ("c", "A type of vitamin"), ("d", "A bone")], "a"),
        ("What is the main job of helper T cells?",
         [("a", "To carry oxygen"), ("b", "To make bones"), ("c", "To coordinate the response by releasing signals that guide other cells"), ("d", "To digest food")], "c"),
        ("What are cytokines?",
         [("a", "Solid bones"), ("b", "Blood vessels"), ("c", "Hormones made only in the skin"), ("d", "Chemical messengers that tell cells what to do")], "d"),
        ("What is clonal selection?",
         [("a", "The random loss of white cells"), ("b", "A type of blood test"), ("c", "The clotting of platelets"), ("d", "The multiplication of a matching specialist cell once it is activated")], "d"),
        ("Why does a healthy immune response switch itself off?",
         [("a", "So that defences do not keep attacking healthy tissue after the threat is gone"), ("b", "To save oxygen for the brain"), ("c", "Because blood stops flowing"), ("d", "To make new bones")], "a"),
    ],
}
