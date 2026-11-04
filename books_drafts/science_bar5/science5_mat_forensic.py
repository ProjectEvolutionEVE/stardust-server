"""Failure Analysis and Forensic Materials Science: reading a broken part to find out how and why it failed."""
CODE = "science5_mat_forensic"
BOOK = {
    "title": "Failure Analysis and Forensic Materials Science",
    "subtitle": "Fracture surfaces, fractography, root cause, evidence handling, reporting and case studies",
    "chapters": [
        ("Fracture surfaces", "A broken part keeps a record of how it failed. The surface of a fracture carries marks that show where the crack began and how it moved. Reading those marks is the first clue in any failure investigation."),
        ("Fractography", "Fractography is the close study of fracture surfaces, usually with a microscope. Its patterns can show whether a part broke suddenly under overload, slowly through fatigue, or through corrosion. The method turns a broken piece into evidence."),
        ("Root cause", "A root cause is the underlying reason a failure happened, not just the last event before it. Analysts work back through the chain of events, asking what made each step possible. Fixing only the last step often lets the failure return."),
        ("Evidence handling", "Samples must be kept exactly as they were found, with a clear record of who handled them and when. Careful handling keeps the surfaces from being damaged and keeps the record unbroken. Without that record, a finding cannot be checked or trusted."),
        ("Reporting", "A good failure report sets out the evidence, the tests that were run, the reasoning from data to conclusion, and the limits of what is known. It should be clear enough for an engineer who was not there to follow it. Honest uncertainty is part of a sound report."),
        ("Case studies", "Case studies show how these methods solved real problems, from bridge and aircraft incidents to pipeline and component failures. Each case teaches a pattern: small defects, poor design choices or unexpected loads can lead to large failures. Studying old cases helps prevent new ones."),
    ],
    "test": [
        ("What does a fracture surface often reveal about how a part failed?",
         [("a", "The pattern of marks shows where the crack started and how it grew"), ("b", "The price of the metal"), ("c", "The date the part was made"), ("d", "Nothing, since all fracture surfaces look the same")], "a"),
        ("What is fractography?",
         [("a", "Painting cracks on samples to make them visible"), ("b", "Writing the final report for a client"), ("c", "The close study of fracture surfaces to learn how and why a material broke"), ("d", "Drawing maps of mines")], "c"),
        ("What is root cause analysis?",
         [("a", "Guessing the cause as quickly as possible"), ("b", "Working back through the chain of events to the underlying cause"), ("c", "Blaming the last person who handled the part"), ("d", "Cutting the part open before any other test")], "b"),
        ("Why does evidence handling matter?",
         [("a", "It makes the samples lighter to carry"), ("b", "It speeds up the laboratory"), ("c", "It hides damage from the owner"), ("d", "It keeps a clear, unbroken record so the findings can be checked and trusted")], "d"),
        ("What should a failure report include?",
         [("a", "Only the final answer"), ("b", "Opinions without data"), ("c", "The evidence, the tests, the reasoning and the limits of the conclusion"), ("d", "The names of the people who used the part")], "c"),
    ],
}
