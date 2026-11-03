"""Insuring Against Positioning Outages: insurance products, triggers, pricing, claims, exclusions and the risk pool."""
CODE = 'navigation5_outage_insurance'
BOOK = {
    "title": 'Insuring Against Positioning Outages',
    "subtitle": 'How cover can share the cost when positioning fails',
    "chapters": [
        ('Insurance products',
         'Cover can pay for losses caused by a positioning outage. Products differ in what they cover and for how long. Read the wording of each one before you rely on it.'),
        ('Triggers',
         'A policy pays only when a stated trigger occurs, such as an outage lasting longer than a set time. Clear triggers avoid disputes, because both sides know when the policy applies.'),
        ('Pricing',
         'Insurers price cover from the chance of an outage and the size of the likely loss. Better data gives more accurate prices, and a fair price keeps the scheme sustainable.'),
        ('Claims',
         'A claim needs proof that the trigger happened and that the loss followed from it. Good records make claims faster and fairer for everyone.'),
        ('Exclusions',
         'Every policy lists what it does not cover. Exclusions may include losses from poor planning or from faults already known. Read them with care, because they set the real limits of the cover.'),
        ('The risk pool',
         'Insurance works by pooling many risks, so that the losses of a few are shared by many. The pool must be large enough to be stable, or the scheme cannot keep its promises.'),
    ],
    "test": [
        ('What is a trigger in an outage policy?',
         [('a', 'The colour of the policy document'), ('b', 'A stated event that makes the policy pay'), ('c', 'A type of antenna'), ('d', 'The insurer logo')], 'b'),
        ('What does a claim need?',
         [('a', 'Nothing at all'), ('b', 'A guess about the loss'), ('c', 'A new satellite'), ('d', 'Proof that the trigger happened and that the loss followed')], 'd'),
        ('What does pricing depend on?',
         [('a', 'The colour of the insurer office'), ('b', 'The weather alone'), ('c', 'The chance of an outage and the size of the loss'), ('d', 'The name of the client')], 'c'),
        ('What are exclusions?',
         [('a', 'Things the policy does not cover'), ('b', 'The pay of the staff'), ('c', 'The price of the policy'), ('d', 'The name of the satellite')], 'a'),
        ('How does insurance work through a risk pool?',
         [('a', 'Each person pays the full loss alone'), ('b', 'Losses are kept secret'), ('c', 'The pool is never needed'), ('d', 'Many risks are pooled so that a few losses are shared by many')], 'd'),
    ],
}
