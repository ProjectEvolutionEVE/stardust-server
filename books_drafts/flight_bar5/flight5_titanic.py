"""Titanic as a Command Case: speed, ice warnings, lookouts, lifeboats, the Californian and the changes that followed."""
CODE = 'flight5_titanic'
BOOK = {
    "title": 'Titanic as a Command Case',
    "subtitle": 'Decisions at sea in April 1912',
    "chapters": [
        ('Speed',
         'The Titanic was sailing at high speed through an area where ice had been reported. Speed in such waters made it harder to turn and harder to stop in time. The command chose to keep the speed up.'),
        ('Ice warnings',
         'Several ice warnings reached the ship during the day before the sinking. Some were passed to the bridge, but they did not lead to a large change of course or speed. A clear warning system is a key part of command at sea.'),
        ('Lookouts',
         'The lookouts had no binoculars, because the key to the box was missing. They saw the iceberg only at close range, too late to avoid it in full. Simple equipment can decide the outcome of a watch.'),
        ('Lifeboats',
         'The ship carried far fewer lifeboats than were needed for everyone on board. Many boats left only partly full, and many people could not reach a boat at all. The number of boats was set by old rules that did not match the size of the ship.'),
        ('The Californian',
         'A nearby ship, the Californian, saw the lights of the Titanic and stopped for the night. Its radio operator had gone off duty, and no one answered the distress rockets in time. The lesson of that night is that a warning must be heard.'),
        ('Changes',
         'The disaster led to a new international agreement on safety at sea, which required enough lifeboats for everyone aboard. An international ice patrol was set up to watch for icebergs. Round-the-clock radio watch became standard on large ships.'),
    ],
    "test": [
        ('What was the Titanic doing when it struck the iceberg?',
         [('a', 'Anchored in harbour'), ('b', 'Turning back to port'), ('c', 'Being towed'), ('d', 'Sailing at high speed through reported ice')], 'd'),
        ('Why did the lookouts see the iceberg too late?',
         [('a', 'They had no binoculars because the key to the box was missing'), ('b', 'The lookouts were asleep'), ('c', 'The sea was calm and bright'), ('d', 'There was no lookout on duty')], 'a'),
        ('What was the main problem with the lifeboats?',
         [('a', 'They were made of gold'), ('b', 'There were far fewer than needed for everyone aboard'), ('c', 'They were too big to launch'), ('d', 'They were kept in the engine room')], 'b'),
        ("What happened to the Californian's radio operator that night?",
         [('a', 'He was on the Titanic'), ('b', 'He was asleep in a lifeboat'), ('c', 'He had gone off duty'), ('d', 'He was sending a message to the moon')], 'c'),
        ('What change followed the disaster?',
         [('a', 'Ships were banned from the Atlantic'), ('b', 'Radios were banned at sea'), ('c', 'Ice warnings were ended'), ('d', 'A new international agreement requiring enough lifeboats for everyone')], 'd'),
    ],
}
