"""Log4Shell: a logging library exploit, the lookup feature, dependency inventory, the patch scramble, supply chain and lessons."""
CODE = 'computing5_log4shell'
BOOK = {
    "title": 'Log4Shell',
    "subtitle": 'One logging library, and a flaw found in thousands of products',
    "chapters": [
        ('A logging library exploit',
         'In December 2021 a serious flaw was found in Log4j, a logging library used in many Java applications. Logging is routine, so the library was present in countless products, often without anyone knowing.'),
        ('The lookup feature',
         'Log4j could look up values from outside sources when a log message contained certain text. An attacker could send a crafted string that made the server fetch and run code from a remote location. That feature is what made the problem so serious.'),
        ('Dependency inventory',
         'Many organisations did not know where Log4j was used, because it was buried inside other products and libraries. Finding every copy took days or weeks. A full list of software dependencies is now widely recommended.'),
        ('The patch scramble',
         'Developers released fixes quickly, but patching meant updating many systems, some of them run by suppliers. Many teams worked through holidays. Some fixes needed follow-up releases because the first one was incomplete.'),
        ('Supply chain',
         'The episode showed how one shared component can carry risk into thousands of products. A flaw in a small, widely reused library can affect everyone who depends on it.'),
        ('Lessons',
         'Know what software you run, keep dependencies updated, and limit what the software is allowed to do. Treat anything that is logged as untrusted input.'),
    ],
    "test": [
        ('What library was at the centre of the problem?',
         [('a', 'A video editor'), ('b', 'A spreadsheet'), ('c', 'A map viewer'), ('d', 'Log4j, a logging library')], 'd'),
        ('Which feature let an attacker make a server fetch and run remote code?',
         [('a', 'The lookup feature'), ('b', 'The printer feature'), ('c', 'The colour setting'), ('d', 'The clock')], 'a'),
        ('Why was it hard to find every copy of Log4j?',
         [('a', 'It was printed on paper'), ('b', 'It was owned by one person'), ('c', 'It was buried inside other products and libraries'), ('d', 'It was used only on paper maps')], 'c'),
        ('What did the patching work involve?',
         [('a', 'Doing nothing for a year'), ('b', 'Updating many systems, some run by suppliers'), ('c', 'Deleting all the logs'), ('d', 'Shutting down the internet in a country')], 'b'),
        ('What does a dependency inventory help a team do?',
         [('a', 'Hide its software'), ('b', 'Forget what it depends on'), ('c', 'Share passwords'), ('d', 'Know where a shared component is used')], 'd'),
    ],
}
