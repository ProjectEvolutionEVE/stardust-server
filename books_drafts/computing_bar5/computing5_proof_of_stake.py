"""Proof-of-Stake Consensus: validators and stake, slashing, finality gadgets, long-range attacks and the trade-off between liveness and safety."""
CODE = 'computing5_proof_of_stake'
BOOK = {'title': 'Proof-of-Stake Consensus',
 'subtitle': 'Agreeing on a ledger by staking value instead of energy',
 'chapters': [('Validators and stake',
               "In proof-of-stake, validators lock up a stake of the network's currency to take part in agreeing on blocks. Their chance to propose or vote depends on their "
               'stake. Honest work is rewarded, and misconduct can cost the stake.'),
              ('Slashing',
               "Slashing destroys part of a validator's stake when it signs conflicting messages or breaks the rules. The penalty makes double-voting costly. Slashing gives the "
               'system an economic way to punish attacks.'),
              ('Finality gadgets',
               'A finality gadget is a mechanism that declares a block final once enough validators have voted for it. Final blocks cannot be reverted without losing a large '
               'amount of stake. Finality gives users a firm point of settlement.'),
              ('Long-range attacks',
               'A long-range attack tries to rebuild history from an old point using keys of validators who have since left. Designs defend against it with checkpoints and by '
               'keeping stake locked for a time. The risk is subtle and needs explicit design.'),
              ('Liveness versus safety',
               'Liveness means the system keeps producing blocks. Safety means it never finalises conflicting blocks. A design that stops when validators disagree protects safety '
               'at the cost of liveness. Designers choose the balance deliberately.'),
              ('Design trade-offs',
               'Proof-of-stake uses much less energy than proof-of-work, but it adds complexity around rewards, penalties and the rules for validators. It also raises questions '
               'about how stake concentrates. Each design makes its own compromises.')],
 'test': [('What do validators lock up in proof-of-stake?',
           [('a', 'A computer in a cupboard'), ('b', 'A paper ledger'), ('c', 'A photo'), ('d', "A stake of the network's currency")],
           'd'),
          ('What does slashing do?',
           [('a', 'Adds coins to every account'), ('b', "Destroys part of a validator's stake for misconduct"), ('c', 'Deletes the blockchain'), ('d', 'Prints a receipt')],
           'b'),
          ('What does a finality gadget declare?',
           [('a', 'That a block is final once enough validators have voted for it'),
            ('b', 'That a block is a picture'),
            ('c', 'That the network is closed'),
            ('d', 'That no one may vote')],
           'a'),
          ('What does a long-range attack try to do?',
           [('a', 'Speed up the clock'),
            ('b', 'Print the ledger'),
            ('c', 'Rebuild history from an old point using keys of validators who have left'),
            ('d', 'Count the validators in a room')],
           'c'),
          ('What is the difference between liveness and safety?',
           [('a', 'Liveness is the colour, safety is the size'),
            ('b', 'Liveness is steady block production, safety is never finalising conflicting blocks'),
            ('c', 'They are the same thing'),
            ('d', 'Safety is a kind of printer')],
           'b')]}
