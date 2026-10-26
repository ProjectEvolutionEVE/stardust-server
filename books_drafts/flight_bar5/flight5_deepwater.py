"""Case Study: Deepwater Horizon. A cement job, a pressure test misread, a kick, the blowout, the failed blowout preventer and the findings."""
CODE = 'flight5_deepwater'
BOOK = {
    "title": 'Case Study: Deepwater Horizon',
    "subtitle": 'A well blowout in the Gulf of Mexico in 2010',
    "chapters": [
        ('The cement job',
         'Deepwater Horizon was a drilling rig in the Gulf of Mexico. Near the end of drilling, a cement job was used to seal the well. A cement job that fails can let oil and gas flow up the well, so its quality must be tested with care.'),
        ('Pressure tests',
         'A negative pressure test was run to check that the well was sealed. The result was read in a way that suggested the well was safe, when the signs showed otherwise. The misreading was missed by the people in charge that day.'),
        ('The kick',
         'Oil and gas began to flow into the well, a warning called a kick. The crew did not stop the flow in time, and the mixture rose to the rig. Early signs were not recognised as the emergency they were.'),
        ('The blowout',
         'Gas reached the rig and ignited, causing explosions and a fire. Eleven workers were killed, and the rig was lost. Oil then flowed from the well into the Gulf for months.'),
        ('The blowout preventer',
         'A blowout preventer is a huge valve on the seabed meant to seal the well in an emergency. On this rig it failed to close fully. A backup that does not work is no backup, so its design and testing matter greatly.'),
        ('Findings',
         'Investigators found many failures in design, testing, communication and management. They called for stronger well control, better decisions on pressure tests and clearer roles for each company on the job. For players, the lesson is that every safety test must be read honestly, even when it is inconvenient.'),
    ],
    "test": [
        ('Where was Deepwater Horizon working?',
         [('a', 'The Sahara'), ('b', 'The Alps'), ('c', 'The Atlantic off Tenerife'), ('d', 'The Gulf of Mexico')], 'd'),
        ('What is a kick in drilling?',
         [('a', 'Oil and gas beginning to flow into the well, a warning sign'), ('b', 'A sports game on the rig'), ('c', 'A type of drill bit'), ('d', 'A new name for the crew')], 'a'),
        ('What is a blowout preventer?',
         [('a', 'A lifeboat'), ('b', 'A huge valve on the seabed meant to seal the well in an emergency'), ('c', 'A kind of helicopter'), ('d', 'A radio mast')], 'b'),
        ('How many workers were killed in the explosions?',
         [('a', 'None'), ('b', 'About 110'), ('c', 'About 11'), ('d', 'About 1,100')], 'c'),
        ('What did the findings say about the pressure test?',
         [('a', 'It was perfectly read'), ('b', 'It was never run'), ('c', "It was run by the crew's pets"), ('d', 'It was read in a way that missed clear signs of danger')], 'd'),
    ],
}
