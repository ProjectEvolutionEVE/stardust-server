"""Secrets Management and Key Rotation: where secrets live, vaults, short-lived credentials, rotation schedules, leak response, and keeping secrets out of code."""
CODE = "computing4_secrets_management"
BOOK = {
    "title": "Secrets Management and Key Rotation",
    "subtitle": "Keeping passwords and keys safe, changing them on time, and responding fast when one leaks",
    "chapters": [
        ("Where secrets live",
         "Secrets such as passwords, keys and tokens belong in a dedicated store. They should not sit in code, in widely shared settings files, or in chat logs."),
        ("Vaults",
         "A vault stores secrets encrypted, controls who may read each one, and records each access. Teams can then see what happened to a secret."),
        ("Short-lived credentials",
         "A credential that expires quickly limits the damage if it leaks. A system can request a fresh one when it needs it."),
        ("Rotation schedules",
         "Secrets should change on a schedule, and at once after any suspected leak. Rotation needs a plan so that services keep working during the change."),
        ("Leak response",
         "When a secret leaks, revoke it at once and issue a new one. Check the logs for misuse, and write down what was learned."),
        ("Keeping secrets out of code",
         "Code repositories and build logs must not hold secrets. Automated scanners can catch them before they are pushed."),
    ],
    "test": [
        ("Which is the right place to keep a secret?",
         [("a", "In a dedicated vault"), ("b", "In a shared chat log"), ("c", "In source code"), ("d", "Posted in a public forum")], "a"),
        ("What does a vault do?",
         [("a", "Sells keys"), ("b", "Stores secrets encrypted, with access control and logs"), ("c", "Prints receipts"), ("d", "Plays music")], "b"),
        ("Why use short-lived credentials?",
         [("a", "They never expire"), ("b", "They cost more"), ("c", "They limit damage if they leak"), ("d", "They are paper")], "c"),
        ("What should happen first when a secret leaks?",
         [("a", "Revoke the secret at once"), ("b", "Post it online"), ("c", "Ignore it"), ("d", "Print it")], "a"),
        ("What do secret scanners do?",
         [("a", "Cook meals"), ("b", "Paint"), ("c", "Catch secrets before they are pushed"), ("d", "Count stars")], "c"),
    ],
}
