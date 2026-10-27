"""CRDT Theory: data types that merge safely across copies, without a central referee."""
CODE = 'computing5_crdt_theory'
BOOK = {
    "title": 'CRDT Theory',
    "subtitle": 'Data types that merge safely across copies, without a central referee',
    "chapters": [
        ('Copies that merge', 'A conflict-free replicated data type, or CRDT, is a data structure that can be copied to many machines and changed on each one. When the copies meet again, they merge automatically to the same result, with no central referee.'),
        ('Join semilattices', 'The merge works because the states form a join semilattice: a set with an order in which any two states have a least upper bound. Merging takes the join, the smallest state that includes both. Because joins do not depend on order, the result does not depend on which copy merged first.'),
        ('State-based and operation-based', 'State-based CRDTs send whole states and merge them with the join. Operation-based ones send the individual operations, which need reliable delivery. Shapiro and colleagues described both styles in 2011.'),
        ('Counters and sets', 'A grow-only counter keeps one count per machine, and the total is their sum. Sets can be built so that adds and removes merge safely, with rules that decide the winner when both happen. These small examples show the method.'),
        ('Operation delivery', 'Operation-based types need every operation to arrive, and they must be applied in a way that does not change the result. Systems that send operations must track delivery carefully, so the same operation is not counted twice.'),
        ('Limits of merging', 'A CRDT guarantees that copies converge, but not that the result is what a user intended. Some changes, such as moving the same item in two places, need extra thought. Designers still have to decide what the merged answer should mean.'),
    ],
    "test": [
        ('What does a CRDT allow?',
         [('a', 'Copies changed on many machines and merged automatically'), ('b', 'Only one copy ever'), ('c', 'No changes at all'), ('d', 'Changes made on paper')], 'a'),
        ('What is a join in a semilattice?',
         [('a', 'A kind of bridge'), ('b', 'A cut of bread'), ('c', 'The smallest state that includes both states'), ('d', 'A type of hinge')], 'c'),
        ('What do state-based CRDTs send?',
         [('a', 'Nothing'), ('b', 'Only the time'), ('c', 'Only pictures'), ('d', 'Whole states')], 'd'),
        ('What does a grow-only counter keep?',
         [('a', 'One count per machine, summed for the total'), ('b', 'A single password'), ('c', 'A map of stars'), ('d', 'Only errors')], 'a'),
        ('What does a CRDT not guarantee?',
         [('a', 'That copies converge'), ('b', 'That merging is automatic'), ('c', 'That copies can be stored'), ('d', 'That the merged result is what a user intended')], 'd'),
    ],
}
