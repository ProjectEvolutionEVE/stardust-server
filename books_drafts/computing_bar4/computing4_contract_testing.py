"""Contract Testing: checking that a service and the services that call it still agree on the shape of their messages."""
CODE = 'computing4_contract_testing'
BOOK = {
    "title": 'Contract Testing',
    "subtitle": 'Checking that services still agree on the shape of their messages',
    "chapters": [
        ('Consumer-driven contracts',
         'A consumer-driven contract is written by the service that calls an interface, describing the requests it sends and the answers it needs. The provider then checks that it can meet every such contract. The consumer leads the design of what matters to it.'),
        ('Provider verification',
         'The provider runs each consumer contract against its own code, without needing the consumer to be running. A failure tells the provider exactly which consumer would break. This catches breaking changes before deployment.'),
        ('Schema checks',
         'A schema check confirms that messages have the expected fields and types. It is a simple and fast check that catches many mistakes. A schema alone cannot show that the behaviour is correct, so it is one tool among several.'),
        ('Versioning',
         'When a provider must change its interface, it can add new fields without breaking old callers. Removing or renaming a field needs a new version and a period when both versions run. Contract tests help a team see when old callers still depend on something.'),
        ('Broker workflows',
         'A contract broker stores the contracts and shows which versions have been verified. Before a release, a team checks that every consumer and provider pair is compatible. The broker turns a web of promises into a visible list.'),
        ('Limits',
         'Contract tests cannot prove that a service works end to end, and they do not replace broader tests. They check agreement on messages, not the whole business process. Use them to catch the cheap, common breakages early, and keep other tests for the rest.'),
    ],
    "test": [
        ('Who writes a consumer-driven contract?',
         [('a', 'The company accountant'), ('b', 'The office cleaner'), ('c', 'The service that calls the interface'), ('d', 'The customer on the phone')], 'c'),
        ('What does provider verification check?',
         [('a', 'That the provider can meet every consumer contract'), ('b', 'The colour of the provider logo'), ('c', 'The price of the cloud server'), ('d', 'The number of staff lunches')], 'a'),
        ('What does a schema check confirm?',
         [('a', 'That the office is clean'), ('b', 'That users are happy'), ('c', 'That the moon is full'), ('d', 'That messages have the expected fields and types')], 'd'),
        ('Why is adding a new field usually safer than removing one?',
         [('a', 'Removing a field is never possible'), ('b', 'Old callers that ignore the new field keep working'), ('c', 'New fields are always private'), ('d', 'New fields make the system run backwards')], 'b'),
        ('What is a limit of contract testing?',
         [('a', 'It can prove everything about the system'), ('b', 'It cannot check any messages'), ('c', 'It cannot prove the whole business process works end to end'), ('d', 'It needs a paper form')], 'c'),
    ],
}
