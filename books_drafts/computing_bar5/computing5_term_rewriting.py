"""Term Rewriting: simplifying expressions by repeatedly applying fixed rewrite rules."""
CODE = 'computing5_term_rewriting'
BOOK = {
    "title": 'Term Rewriting',
    "subtitle": 'Simplifying expressions by repeatedly applying fixed rewrite rules',
    "chapters": [
        ('Rewriting expressions', 'A rewrite rule replaces one pattern with another, such as turning "x plus zero" into "x". Applying rules over and over simplifies an expression step by step. Term rewriting is the study of such systems.'),
        ('Confluence', 'A system is confluent if, however you order the rewrites, you end at the same answer. Confluence means a result is not a matter of luck. Checking it is a key step in trusting a set of rules.'),
        ('Termination', 'A system terminates if the rewriting always stops. A rule that makes an expression grow forever would never reach an answer. Termination proofs often use an ordering that gets smaller at each step.'),
        ('Knuth-Bendix completion', 'Donald Knuth and Peter Bendix showed in 1970 how to add new rules to make a system confluent. The method, called completion, looks at pairs of rules that overlap and adds what is missing. It is a powerful but sometimes unsteady process.'),
        ('Simplifiers and proof tools', 'Computer algebra systems, compilers and proof assistants use rewriting to simplify expressions and to check that two forms match. The same rules can be applied quickly and in a known order.'),
        ('Normal forms', 'A normal form is an expression that no rule can change further. If a system is confluent and terminating, every expression has exactly one normal form, which makes equality easy to check.'),
    ],
    "test": [
        ('What does a rewrite rule do?',
         [('a', 'Paints a picture'), ('b', 'Sends an email'), ('c', 'Replaces one pattern with another'), ('d', 'Sorts a shelf')], 'c'),
        ('What does confluence mean?',
         [('a', 'Rewrites that never stop'), ('b', 'A very long expression'), ('c', 'A broken printer'), ('d', 'The same final answer whatever order the rewrites follow')], 'd'),
        ('What does termination mean here?',
         [('a', 'The rewriting always stops'), ('b', 'The program prints a line'), ('c', 'The user goes home'), ('d', 'The screen goes dark')], 'a'),
        ('Who gave the completion method in 1970?',
         [('a', 'Donald Knuth and Peter Bendix'), ('b', 'Ada and Alan'), ('c', 'Grace and Linus'), ('d', 'Niklaus and Edsger')], 'a'),
        ('What is a normal form?',
         [('a', 'An expression no rule can change further'), ('b', 'A standard size of paper'), ('c', 'A kind of friendship'), ('d', 'A bank form')], 'a'),
    ],
}
