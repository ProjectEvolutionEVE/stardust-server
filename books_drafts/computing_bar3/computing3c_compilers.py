"""Compilers and Interpreters: how the words you write become instructions the processor can run."""
CODE = "computing3c_compilers"
BOOK = {
    "title": "Compilers and Interpreters",
    "subtitle": "How the words you write become instructions the processor can run",
    "chapters": [
        ("From words to instructions",
         "A processor understands only its own simple instructions, which are written as numbers. Programmers write in languages such as Python or C, because words are easier to read. Something must translate those words into instructions, and that is the job of a compiler or an interpreter."),
        ("Compilers",
         "A compiler reads the whole program first and turns it into machine code. That machine code can then run again and again without translating it each time. Mistakes in the wording can often be caught before the program starts."),
        ("Interpreters",
         "An interpreter reads the program and carries out each step as it goes, without saving a separate machine-code file. Changes take effect at once, which is handy when learning. The translating work happens again every time the program runs."),
        ("Many tools use both",
         "Some tools first turn a program into a middle form called bytecode, then run that bytecode on a virtual machine. Python, for example, turns your code into bytecode and runs it on its own virtual machine. The line between compiling and interpreting is less sharp than it looks."),
        ("Making code faster",
         "A compiler can rearrange and simplify instructions so the program runs faster. Good optimisation takes extra time up front, and then the faster program saves processor time every time it runs. The gain is only worth it when the program runs often."),
        ("Choosing a tool",
         "Each choice trades off speed of running, speed of changing the code, and how easily errors are caught. Know that trade-off before you pick a language for a large job. Simple tools are often the right start."),
    ],
    "test": [
        ("What does a processor understand?",
         [("a", "English sentences"), ("b", "Pictures of code"), ("c", "Its own simple instructions, written as numbers"), ("d", "Only spoken words")], "c"),
        ("What is the main job of a compiler?",
         [("a", "To translate the whole program into machine code before it runs"), ("b", "To print the program on paper"), ("c", "To delete the program after it runs"), ("d", "To play music")], "a"),
        ("How does an interpreter work?",
         [("a", "It makes one machine-code file and stops"), ("b", "It carries out each step as it reads, without saving a separate machine-code file"), ("c", "It sends the program to another player"), ("d", "It does nothing until the program is finished")], "b"),
        ("What is bytecode?",
         [("a", "A middle form that a virtual machine can run"), ("b", "A kind of paper"), ("c", "A safety lock"), ("d", "A picture of a ship")], "a"),
        ("Why might a compiler catch errors before a program starts?",
         [("a", "Because errors are always hidden"), ("b", "Because the program runs twice"), ("c", "Because the program is printed"), ("d", "Because it reads the whole program before making machine code")], "d"),
    ],
}
