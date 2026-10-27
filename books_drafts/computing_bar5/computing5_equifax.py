"""The Equifax Breach: an unpatched web framework, data exposure, accountability, patch management, incident response and lessons."""
CODE = 'computing5_equifax'
BOOK = {
    "title": 'The Equifax Breach',
    "subtitle": 'A known fix not applied, and a very large exposure of personal data',
    "chapters": [
        ('An unpatched web framework',
         'In 2017 attackers used a known weakness in a web framework that an online dispute system relied on. A fix for the weakness had been published months earlier. The system had not been updated in time.'),
        ('Data exposure',
         'The attackers were able to reach personal records of about 147 million people, including names, dates of birth and identification numbers. Such records are valuable to criminals for years, because they are hard to change.'),
        ('Accountability',
         'Following the breach there were investigations, public hearings and a large settlement. The company faced intense criticism for how it had handled both security and the response. Accountability for security sits with leaders as well as engineers.'),
        ('Patch management',
         'Patch management means finding every system that needs an update, applying it, and checking that it worked. Gaps often open when no one owns the inventory of what is running. A missed patch can stay open for months.'),
        ('Incident response',
         'A breach needs fast detection, containment, clear communication and honest records of what happened. Delay in finding and reporting the breach made the harm worse for many people.'),
        ('Lessons',
         'Keep an accurate list of systems, apply known fixes promptly, and make someone clearly responsible for each one. Plan the response before the breach happens.'),
    ],
    "test": [
        ('What weakness did the attackers use?',
         [('a', 'A known weakness in an unpatched web framework'), ('b', 'A broken office printer'), ('c', 'A lost paper form'), ('d', 'A weak cup of coffee')], 'a'),
        ('About how many people had personal records exposed?',
         [('a', 'About fifty people'), ('b', 'About one hundred people'), ('c', 'About one hundred and forty-seven million people'), ('d', 'About five people in total')], 'c'),
        ('What does patch management involve?',
         [('a', 'Finding every system that needs an update, applying it, and checking it worked'), ('b', 'Painting the server room'), ('c', 'Turning off email for ever'), ('d', 'Printing all records on paper')], 'a'),
        ('What followed the breach?',
         [('a', 'Investigations, public hearings and a large settlement'), ('b', 'A medal for the company'), ('c', 'Nothing at all'), ('d', 'A new holiday for staff')], 'a'),
        ('What lesson does this case teach?',
         [('a', 'Known fixes can wait for ever'), ('b', 'Keep an accurate list of systems and apply known fixes promptly'), ('c', 'Personal data does not matter'), ('d', 'Breach plans are a waste of time')], 'b'),
    ],
}
