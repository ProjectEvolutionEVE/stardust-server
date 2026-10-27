"""Heartbleed: the TLS heartbeat bug, buffer over-read, scale of exposure, response, open-source funding and code review lessons."""
CODE = 'computing5_heartbleed'
BOOK = {
    "title": 'Heartbleed',
    "subtitle": 'A small check that was missing, and the lesson for widely shared code',
    "chapters": [
        ('The TLS heartbeat bug',
         'In April 2014 a serious flaw was disclosed in OpenSSL, a widely used library that encrypts traffic for many websites. The flaw lay in the heartbeat feature, a simple message that keeps a secure connection alive.'),
        ('Buffer over-read',
         'The code trusted a length value sent by the client without checking it against the real size of the message. A crafted request could make the server return a piece of its memory, which might hold private data such as keys or passwords. This is called a buffer over-read.'),
        ('Scale of exposure',
         'Because OpenSSL was so common, a large share of secure web servers were affected. Many organisations had to renew certificates and reset credentials after patching. How far the flaw had been misused before disclosure was never fully known.'),
        ('The response',
         'A fixed version was released quickly, and many operators patched their servers in a rush. Teams checked their logs, replaced keys, and told users to change passwords where needed.'),
        ('Open-source funding',
         'The episode drew attention to how critical open-source software was maintained with very little funding. Afterwards, companies and foundations gave more support to security reviews of core libraries.'),
        ('Code review lessons',
         'Careful checking of inputs, bounds checks and independent testing help prevent flaws like this one. Widely used code deserves widely shared attention.'),
    ],
    "test": [
        ('Where was the Heartbleed flaw found?',
         [('a', 'In a game console'), ('b', 'In a printer driver'), ('c', 'In the heartbeat feature of OpenSSL'), ('d', 'In a word processor')], 'c'),
        ('What could attackers do with the flaw?',
         [('a', 'Print documents for free'), ('b', 'Read chunks of server memory that could hold private data'), ('c', 'Change the colour of websites'), ('d', 'Turn off whole computers')], 'b'),
        ('Why was the scale of exposure large?',
         [('a', 'OpenSSL was widely used by secure web servers'), ('b', 'Only one computer was ever affected'), ('c', 'No websites used encryption'), ('d', 'Passwords were printed on posters')], 'a'),
        ('What did operators often have to do after patching?',
         [('a', 'Delete all their websites'), ('b', 'Stop using the internet forever'), ('c', 'Give up their domain names'), ('d', 'Renew certificates and reset credentials')], 'd'),
        ('What did the episode draw attention to?',
         [('a', 'That open-source code needs little care'), ('b', 'That only expensive software has bugs'), ('c', 'That critical open-source software was often under-funded'), ('d', 'That encryption should be abandoned')], 'c'),
    ],
}
