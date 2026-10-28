"""Error-Correcting Codes: adding structured redundancy so that noise on a channel can be found and fixed."""
CODE = 'computing5_error_correcting_codes'
BOOK = {'title': 'Error-Correcting Codes',
 'subtitle': 'Adding just enough redundancy to repair noise',
 'chapters': [('Noise on a channel',
               'Every real channel adds noise: a scratch on a disc, a weak radio signal, a flicker on a cable. Error-correcting codes add extra bits in a planned way, so that the '
               'receiver can spot and repair damage. The extra bits are the price of reliability.'),
              ('Hamming codes',
               'Richard Hamming designed codes that add a few parity bits to each block of data. A standard seven-bit Hamming code corrects any single flipped bit. The parity '
               'bits point to exactly which bit went wrong.'),
              ('Reed-Solomon codes',
               'Reed-Solomon codes treat data as blocks of symbols and add check symbols. They can repair several damaged symbols in one block. They are used in compact discs, '
               'DVDs and QR codes.'),
              ('Minimum distance',
               'The distance between two codewords is the number of positions where they differ. The minimum distance of a code decides how many errors it can correct. A larger '
               'minimum distance means more errors can be repaired, at the cost of more bits.'),
              ('Decoding',
               'Decoding means finding the codeword closest to the received message. For many codes this is done with fast algebra or table lookup. If too many errors occur, the '
               'decoder may fail or report the damage.'),
              ('Codes in the real world',
               'Error-correcting codes protect discs, phone links, QR codes and deep-space links. Signals sent from distant spacecraft travel a long way and get very weak, so '
               'strong codes are essential. Without them, most modern communication would be unreliable.')],
 'test': [('What do error-correcting codes add to data?', [('a', 'Planned extra bits'), ('b', 'Pictures'), ('c', 'Random delays'), ('d', 'Longer file names')], 'a'),
          ('What does a standard seven-bit Hamming code correct?',
           [('a', 'Nothing at all'), ('b', 'All possible errors in any block'), ('c', 'Any single flipped bit'), ('d', 'Only lost files')],
           'c'),
          ('Where are Reed-Solomon codes used?', [('a', 'Paper books only'), ('b', 'Compact discs and QR codes'), ('c', 'Keyboards'), ('d', 'Clocks with hands')], 'b'),
          ('What does the minimum distance of a code tell you?',
           [('a', 'How heavy the code is'), ('b', 'How many people use it'), ('c', 'The colour of the cable'), ('d', 'How many errors it can correct')],
           'd'),
          ('What happens when too many errors occur in a block?',
           [('a', 'The data always repairs itself'), ('b', 'The channel becomes faster'), ('c', 'The decoder may fail or report the damage'), ('d', 'The sender receives a prize')],
           'c')]}
