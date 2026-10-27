"""Domain-Driven Design: ubiquitous language, bounded contexts, aggregates, domain events, context maps, and strategic design choices."""
CODE = "computing4_ddd"
BOOK = {
    "title": "Domain-Driven Design",
    "subtitle": "Building software around the words and rules of the business",
    "chapters": [
        ("Ubiquitous language",
         "Developers and domain experts use the same words for the same things, both in conversation and in the code. Misunderstandings shrink when the words match."),
        ("Bounded contexts",
         "A bounded context is a boundary inside which one model and its terms have one clear meaning. The same word, such as account, can mean different things in different contexts."),
        ("Aggregates",
         "An aggregate is a group of objects that is changed as one unit. The rules inside it stay consistent, and it is changed through a single root object."),
        ("Domain events",
         "A domain event records something important that has happened, such as an order being placed. Other parts of the system can react to it."),
        ("Context maps",
         "A context map shows how the bounded contexts relate. It shows which context supplies data, which depends on which, and where translation between their words happens."),
        ("Strategic design choices",
         "Teams decide where to invest their best effort. Core domains deserve the most care. Supporting parts can use simpler designs or bought solutions."),
    ],
    "test": [
        ("What is ubiquitous language?",
         [("a", "A language for robots"), ("b", "Code only"), ("c", "Shared words that developers and experts use for the same things"), ("d", "A foreign language")], "c"),
        ("What is a bounded context?",
         [("a", "A boundary where one model and its terms have one meaning"), ("b", "A fence"), ("c", "A limit on coffee"), ("d", "A tool")], "a"),
        ("What is an aggregate?",
         [("a", "A group of objects changed as one unit"), ("b", "A pile of rocks"), ("c", "A shop"), ("d", "A quarrel")], "a"),
        ("What is a domain event?",
         [("a", "A party"), ("b", "A sports match"), ("c", "A holiday"), ("d", "A record of something important that has happened")], "d"),
        ("Where should teams invest the most care?",
         [("a", "In core domains"), ("b", "In every part equally"), ("c", "Nowhere"), ("d", "Only in the logo")], "a"),
    ],
}
