"""Proof Testing and Acceptance Criteria: what a passed load test does and does not prove."""
CODE = "engineering5_proof_test"
BOOK = {
    "title": "Proof Testing and Acceptance Criteria",
    "subtitle": "What a passed load test does and does not prove",
    "chapters": [
        ("Proving a part",
         "A proof test loads a part to a set level above its working load, to show it is free of harmful flaws at that level. It is a go or no-go check, not a measure of strength."),
        ("Proof loads and overload factors",
         "The proof load is the working load multiplied by an overload factor chosen by the design code. The factor depends on the risk and on the type of structure."),
        ("Test to failure",
         "Some tests load a sample until it breaks, to find its real strength. These give strength data, but they use up the sample, so only a few are made."),
        ("Acceptance criteria",
         "Acceptance criteria state in advance which result counts as a pass, such as no visible permanent deformation or no leak. Writing them first prevents arguments afterwards."),
        ("What a passed test proves",
         "A passed proof test shows the part survived that load, which screens out the largest flaws. It does not prove the part will last under any other load or for any longer time."),
        ("Plan the test",
         "Record the load, the hold time and the readings, and keep the test within the part's safe limits. A clear record makes the result useful later."),
    ],
    "test": [
        ("What is a proof test?",
         [("a", "A paint test"), ("b", "A check at a set load above the working load to screen for harmful flaws"), ("c", "A price check"), ("d", "A colour check")], "b"),
        ("What is a proof load?",
         [("a", "The working load times an overload factor"), ("b", "The price"), ("c", "The paint"), ("d", "The age")], "a"),
        ("Why are only a few samples tested to failure?",
         [("a", "They are cheap"), ("b", "They are painted"), ("c", "They are used up in the test"), ("d", "They stretch")], "c"),
        ("What are acceptance criteria?",
         [("a", "The result that counts as a pass, set in advance"), ("b", "The paint colour"), ("c", "The price list"), ("d", "The weather")], "a"),
        ("What does a passed proof test NOT prove?",
         [("a", "That the part will last under any other load or for any longer time"), ("b", "That the part survived that load"), ("c", "That harmful flaws were screened out at that load"), ("d", "That it met the criteria")], "a"),
    ],
}
