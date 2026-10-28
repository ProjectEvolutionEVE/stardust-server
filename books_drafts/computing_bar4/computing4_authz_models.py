"""Authorisation: RBAC and ABAC: roles, attributes and policies, least privilege, policy engines, separation of duties, and reviewing access over time."""
CODE = "computing4_authz_models"
BOOK = {
    "title": "Authorisation: RBAC and ABAC",
    "subtitle": "Deciding who may do what, and keeping that decision right over time",
    "chapters": [
        ("Roles",
         "Role-based access control gives permissions to roles, and users are given roles. It is easy to understand, but it can become messy as the number of roles grows."),
        ("Attributes and policies",
         "Attribute-based access control decides access from attributes of the user, the resource and the situation, such as department or time of day. The rules are written as policies."),
        ("Least privilege",
         "Every user and every service should have only the access the job needs, and no more. Narrow access limits the damage from a mistake or a stolen login."),
        ("Policy engines",
         "A policy engine evaluates the rules in one place, so the same policy applies across many services. Testing policies before they go live prevents surprises."),
        ("Separation of duties",
         "Critical actions should need two people. For example, one person requests a payment and another approves it. This makes fraud harder to commit."),
        ("Reviewing access over time",
         "People change roles and leave the organisation. Regular access reviews remove access that is no longer needed."),
    ],
    "test": [
        ("What does RBAC give permissions to?",
         [("a", "Colours"), ("b", "Clouds"), ("c", "Fish"), ("d", "Roles")], "d"),
        ("What does ABAC decide from?",
         [("a", "Attributes of the user, the resource and the situation"), ("b", "Coin flips"), ("c", "Weather only"), ("d", "Paper")], "a"),
        ("What is least privilege?",
         [("a", "Giving only the access the job needs"), ("b", "Giving everyone admin rights"), ("c", "Removing all access"), ("d", "Sharing one account")], "a"),
        ("What is separation of duties?",
         [("a", "Requiring two people for critical actions"), ("b", "Splitting the office"), ("c", "One person does everything"), ("d", "Sharing keys")], "a"),
        ("Why review access over time?",
         [("a", "Reviews are fun"), ("b", "Access never changes"), ("c", "People change roles and leave, so old access must be removed"), ("d", "It saves paper")], "c"),
    ],
}
