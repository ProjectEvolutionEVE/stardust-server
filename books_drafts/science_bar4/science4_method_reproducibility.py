"""Reproducibility and Preregistration: writing the plan first, replication, reporting standards and the replication crisis."""
CODE = "science4_method_reproducibility"
BOOK = {
    "title": "Reproducibility and Preregistration",
    "subtitle": "Writing the plan first, and making results checkable",
    "chapters": [
        ("What reproducibility means", "Reproducibility means another team, using the same data and methods, gets the same result. It is a basic check that a finding is solid. Many fields have found that repeating studies is harder than expected."),
        ("Preregistration", "Preregistration means writing down the question, design and analysis plan before the data are collected. A public record shows what was planned. This makes it harder to change the test after seeing the results."),
        ("Replication studies", "A replication study repeats an earlier study with new data, often to test whether a finding holds. Successful replications add confidence, and failed ones prompt questions. Both outcomes are useful to science."),
        ("Analysis plans and reproducible code", "An analysis plan lists how data will be cleaned, tested and reported. Reproducible code lets others run the same steps and check the numbers. Keeping code and data together helps this work."),
        ("Reporting standards", "Reporting standards are checklists that ask researchers to report key details, such as sample sizes, methods and limits. Using them makes papers easier to assess and repeat. Many journals and funders now ask for them."),
        ("The replication crisis", "In several fields, many published results have failed to replicate. The problem has many causes, including small samples and flexible analysis. The response has been better planning, openness and more replication."),
    ],
    "test": [
        ("What does reproducibility mean?",
         [("a", "Making the paper longer"), ("b", "Another team, using the same data and methods, gets the same result"), ("c", "Printing the results twice"), ("d", "Using a different colour for graphs")], "b"),
        ("What is preregistration?",
         [("a", "Writing down the question and analysis plan before collecting data"), ("b", "Registering a car"), ("c", "Booking a conference room"), ("d", "Signing a lab coat")], "a"),
        ("What is a replication study?",
         [("a", "A study that copies a paper's cover"), ("b", "A study with no data"), ("c", "A repeat of an earlier study with new data to test a finding"), ("d", "A list of journal names")], "c"),
        ("What does reproducible code allow?",
         [("a", "Hiding the steps"), ("b", "Others to run the same steps and check the numbers"), ("c", "Faster printing"), ("d", "Changing the data in secret")], "b"),
        ("What is the replication crisis?",
         [("a", "A shortage of lab coats"), ("b", "A rule for funding"), ("c", "A plan to stop all research"), ("d", "A situation where many published results failed to replicate")], "d"),
    ],
}
