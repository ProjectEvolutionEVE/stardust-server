"""SMT Solvers: engines that decide whether a set of logical rules can all be true together."""
CODE = 'computing5_smt_solvers'
BOOK = {
    "title": 'SMT Solvers',
    "subtitle": 'Engines that decide whether a set of logical rules can all be true together',
    "chapters": [
        ('Satisfiability', 'A set of rules is satisfiable if some choice of values makes all of them true. A solver is a program that answers that question. Many checks in software, such as whether a path is possible, reduce to exactly this question.'),
        ('Theories', 'Plain logic is not enough for software, so solvers handle theories: the rules of arithmetic, of arrays, and of bit-vectors that model computer numbers. Modern solvers combine several theories in one query.'),
        ('Conflict-driven search', 'Most modern solvers use conflict-driven clause learning. The solver guesses values, and when it hits a contradiction it learns a new rule that rules out that clash, so it does not repeat the same mistake. This idea has made solvers far faster over the last few decades.'),
        ('Encoding problems', 'Users write their problem as a list of rules in a standard format. The skill lies in turning a real question, such as a scheduling clash or a program bug, into rules that are accurate and not too large.'),
        ('Timeouts', 'Some queries take too long, and solvers may give up. A timeout is not an answer, so good tools treat it as unknown and say so. Engineers set time limits and simplify rules to keep queries practical.'),
        ('Verification uses', 'Solvers are used to check hardware designs, to verify parts of operating systems and to find test inputs. They sit behind many tools that prove a program meets a stated rule, within the limits of what was written down.'),
    ],
    "test": [
        ('What does a solver decide?',
         [('a', 'Whether a set of rules can all be true together'), ('b', 'Which colour to paint a screen'), ('c', 'How many users are online'), ('d', 'The weather')], 'a'),
        ('What do theories in a solver cover?',
         [('a', 'Cooking recipes'), ('b', 'Arithmetic, arrays and bit-vectors'), ('c', 'Musical scales'), ('d', 'Sports scores')], 'b'),
        ('What does conflict-driven learning do?',
         [('a', 'Learns a new rule from each clash, so the same mistake is not repeated'), ('b', 'Deletes all rules after each guess'), ('c', 'Asks the user for every answer'), ('d', 'Stops at the first guess')], 'a'),
        ('What should a team treat a solver timeout as?',
         [('a', 'A correct answer of no'), ('b', 'Unknown, not an answer'), ('c', 'A guaranteed yes'), ('d', 'A reason to delete the program')], 'b'),
        ('Which is a common use of SMT solvers?',
         [('a', 'Painting pictures'), ('b', 'Printing paper'), ('c', 'Sending emails'), ('d', 'Checking hardware designs')], 'd'),
    ],
}
