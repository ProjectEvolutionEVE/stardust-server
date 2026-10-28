"""Compiler Correctness and Verified Compilers: proving that compiled output means what the source meant."""
CODE = 'computing5_compiler_correctness'
BOOK = {
    "title": 'Compiler Correctness and Verified Compilers',
    "subtitle": 'Proving that a compiler output means what the source program meant',
    "chapters": [
        ('What a compiler does', 'A compiler turns the code a programmer writes into the instructions a computer runs. If the compiler goes wrong, a correct program can become a broken one, even though nobody changed the code.'),
        ('Correctness theorems', 'A verified compiler comes with a mathematical proof that its output behaves the same as the source. The theorem says that every behaviour of the compiled program is a behaviour the source allowed.'),
        ('CompCert', 'CompCert is a C compiler whose main parts were proved correct in the Coq proof assistant, led by Xavier Leroy and his team. It suits places where wrong code could be dangerous, and it trades some speed for that assurance.'),
        ('Translation validation', 'Translation validation checks each run of a normal compiler instead of proving the compiler itself. After compiling, a second tool checks that the output matches the input. It is a lighter route that catches problems one program at a time.'),
        ('Miscompilation bugs', 'Studies of compilers have found miscompilation bugs, where correct code is turned into wrong code. Testing with randomly generated programs has been one way to find them. These bugs are rare, but they can be hard to track down.'),
        ('The trusted base and cost', 'A proof is only as good as its assumptions. The parts that are trusted without proof form the trusted base. Verification takes large effort and time, so teams weigh it against the risk of a silent error.'),
    ],
    "test": [
        ('What does a compiler turn code into?',
         [('a', 'Instructions a computer runs'), ('b', 'A song'), ('c', 'A paper map'), ('d', 'A photo')], 'a'),
        ('What does a correctness theorem say about compiled output?',
         [('a', 'It is always faster'), ('b', 'It has no bugs at all'), ('c', 'It behaves only in ways the source allowed'), ('d', 'It is shorter')], 'c'),
        ('Which proof assistant were the main parts of CompCert proved in?',
         [('a', 'Excel'), ('b', 'Notepad'), ('c', 'Coq'), ('d', 'Photoshop')], 'c'),
        ('What is a miscompilation bug?',
         [('a', 'A typing mistake in a comment'), ('b', 'Correct code turned into wrong code by the compiler'), ('c', 'A slow printer'), ('d', 'An empty file')], 'b'),
        ('What is the trusted base?',
         [('a', 'The parts accepted without proof'), ('b', 'The team favourite food'), ('c', 'The list of users'), ('d', 'The hardware warranty')], 'a'),
    ],
}
