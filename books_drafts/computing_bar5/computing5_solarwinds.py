"""The SolarWinds Supply Chain Attack: a trojanised update, build pipeline compromise, detection delay, government response, provenance and lessons."""
CODE = 'computing5_solarwinds'
BOOK = {
    "title": 'The SolarWinds Supply Chain Attack',
    "subtitle": 'When a trusted update carried a hidden intruder',
    "chapters": [
        ('A trojanised update',
         'In 2020 attackers secretly inserted malicious code into an update of Orion, network management software made by SolarWinds. Customers installed the trusted update, and the hidden code came into their networks with it. This kind of attack is called a trojan.'),
        ('Build pipeline compromise',
         'The attackers reached the software build system, so the malicious code was added before the update was signed and released. A normal signature check would show the update as genuine. Protecting the build process is therefore essential.'),
        ('Detection delay',
         'The intrusion went unnoticed for many months. Early signs were missed, and the attackers moved quietly through many networks. The delay gave them time to gain access and gather information.'),
        ('Government response',
         'Government agencies and companies responded with investigations, advisories and new guidance. Many organisations reviewed their use of the software. Officials attributed the attack to a foreign intelligence service.'),
        ('Provenance',
         'Provenance means being able to show where software came from and how it was built. Teams increasingly ask suppliers for records of how each release was produced, often called a software bill of materials.'),
        ('Lessons',
         'Trust in a supplier must be checked, not assumed. Secure the build process, watch for unusual behaviour from trusted tools, and plan for the day a trusted update turns out to be hostile.'),
    ],
    "test": [
        ('What did the attackers insert?',
         [('a', 'Malicious code into an update'), ('b', 'A new keyboard'), ('c', 'Extra colours into a logo'), ('d', 'A recipe for bread')], 'a'),
        ('Which part of the process did the attackers reach?',
         [('a', 'The office kitchen'), ('b', 'The staff lunch room'), ('c', 'The software build system'), ('d', 'The car park')], 'c'),
        ('Why did the intrusion go unnoticed for so long?',
         [('a', 'Early signs were missed'), ('b', 'The attackers were announced on television'), ('c', 'No one used the software'), ('d', 'The network was switched off')], 'a'),
        ('What is provenance?',
         [('a', 'A type of bread'), ('b', 'A record of where software came from and how it was built'), ('c', 'A password reset tool'), ('d', 'A paid advertisement')], 'b'),
        ('What lesson does this case teach about trust?',
         [('a', 'Trust a supplier completely and never check'), ('b', 'Trust must be checked, not assumed'), ('c', 'Updates are always safe'), ('d', 'Build processes never matter')], 'b'),
    ],
}
