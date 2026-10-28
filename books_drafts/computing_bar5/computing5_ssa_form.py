"""Static Single Assignment Form: a way of writing a program so every value is set in exactly one place."""
CODE = 'computing5_ssa_form'
BOOK = {
    "title": 'Static Single Assignment Form',
    "subtitle": 'A way of writing a program so every value has exactly one place it is set',
    "chapters": [
        ('One definition per name', 'In static single assignment form, each variable is assigned exactly once. When the original program changes a value, the compiler gives the new value a new name. This makes it clear where every value came from.'),
        ('Phi functions', 'Where two paths of the program meet, a value may come from either path. A phi function chooses the right one, depending on which path was taken. It is a small marker that joins the two versions of a value.'),
        ('Dominance frontiers', 'A node dominates another if every route to that node passes through it. Dominance frontiers tell the compiler where phi functions are needed, which lets the form be built efficiently without guessing.'),
        ('Optimisations on SSA', 'Many useful optimisations become simpler in this form, such as spotting constant values and removing unused work. Because each name has one definition, a tool can follow a value without checking every change.'),
        ('Converting back', 'Before a program is run, the phi functions must be removed and replaced by plain moves between registers or memory. This step is called out-of-SSA conversion, and it needs care so that values are not mixed up.'),
        ('Compiler infrastructure', 'Ron Cytron and his co-authors described an efficient way to build this form in 1991. Today it is central to many compilers, including LLVM, which uses it as the core of its optimisation passes.'),
    ],
    "test": [
        ('How often is each variable assigned in SSA form?',
         [('a', 'Once'), ('b', 'Never'), ('c', 'Every second'), ('d', 'A hundred times')], 'a'),
        ('What does a phi function do?',
         [('a', 'Paints the screen'), ('b', 'Deletes loops'), ('c', 'Chooses the right version of a value where paths meet'), ('d', 'Prints numbers')], 'c'),
        ('What does a node dominate?',
         [('a', 'Another node, if every route to that node passes through the first'), ('b', 'The printer'), ('c', 'The next day'), ('d', 'The list of colours')], 'a'),
        ('Why is converting back out of SSA needed?',
         [('a', 'The program must be printed'), ('b', 'Values must be stored in colours'), ('c', 'The compiler must sleep'), ('d', 'Phi functions must be replaced by plain moves before running')], 'd'),
        ('Which major compiler project uses SSA at its core?',
         [('a', 'LLVM'), ('b', 'A card game'), ('c', 'A spreadsheet app'), ('d', 'A photo editor')], 'a'),
    ],
}
