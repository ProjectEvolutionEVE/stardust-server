"""Datalog and Logic Programming: asking questions about facts and rules, and letting the system work out answers."""
CODE = 'computing5_datalog'
BOOK = {
    "title": 'Datalog and Logic Programming',
    "subtitle": 'Asking questions about facts and rules, and letting the system work out the answers',
    "chapters": [
        ('Facts and rules', 'In Datalog you write facts, such as "Ana is a parent of Ben", and rules, such as "a grandparent is a parent of a parent". The program then works out everything that follows from those facts and rules.'),
        ('Recursive queries', 'Rules can refer to themselves. Asking who is an ancestor, for example, can follow parent links as far as they go. Recursion lets short rules answer questions that would otherwise need long loops.'),
        ('Bottom-up evaluation', 'Datalog starts from the known facts and adds new facts as the rules allow, until nothing new appears. This bottom-up approach always finishes, because the set of possible facts is limited.'),
        ('Semi-naive evaluation', 'A simple run keeps re-deriving facts it already has. Semi-naive evaluation only uses the facts that were new in the last round, which saves a great deal of work. It is the standard method in fast Datalog engines.'),
        ('Static analysis in Datalog', 'Many program analysis tools write their rules in Datalog, such as rules about which variables might point to which objects. The engine then computes all the answers for a whole program. This keeps analysis rules short and clear.'),
        ('The history of logic programming', 'Logic programming, where programs are written as logic, grew in the 1970s and 1980s, with Prolog as its best-known language. Datalog keeps the good ideas and limits the rules so that answers always arrive. Teams use it where clear rules matter more than raw speed.'),
    ],
    "test": [
        ('What do you write in Datalog?',
         [('a', 'Facts and rules'), ('b', 'Songs'), ('c', 'Recipes'), ('d', 'Poems')], 'a'),
        ('What does a recursive rule do?',
         [('a', 'It repeats forever with no end'), ('b', 'It refers to itself, so it can follow chains such as ancestors'), ('c', 'It deletes facts'), ('d', 'It runs on paper')], 'b'),
        ('How does bottom-up evaluation stop?',
         [('a', 'When no new facts can be added'), ('b', 'When the user presses a key'), ('c', 'At midnight'), ('d', 'After one second')], 'a'),
        ('What does semi-naive evaluation save?',
         [('a', 'Electricity in the kitchen'), ('b', 'Screen space'), ('c', 'Re-deriving facts already known'), ('d', 'Memory on paper')], 'c'),
        ('What are analysis tools often written in Datalog?',
         [('a', 'Rules about how a program values might relate'), ('b', 'Music tracks'), ('c', 'Shopping lists'), ('d', 'Weather maps')], 'a'),
    ],
}
