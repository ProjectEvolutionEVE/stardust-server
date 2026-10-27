"""Software Escrow and Continuity Agreements: how a customer protects itself if a software supplier fails."""
CODE = "computing5_software_escrow"
BOOK = {
    "title": "Software Escrow and Continuity Agreements",
    "subtitle": "How a customer keeps working if its software supplier fails",
    "chapters": [
        ("Source code deposits",
         "In an escrow agreement, the supplier deposits a copy of its source code with a neutral third party. The customer gets a route to the code if the supplier can no longer support it. The deposit must be kept up to date."),
        ("Release triggers",
         "A release trigger is an event that allows the code to be released, such as the supplier going bankrupt or ending support. The triggers must be written clearly. Vague triggers lead to arguments when they matter most."),
        ("Verification",
         "A deposit is only useful if it builds and works. Verification tests check that the code can be compiled and that the documents are complete. Schedule these tests, not just the first one."),
        ("Costs",
         "Escrow has costs: fees for the third party, the work of keeping the deposit current, and the testing. Weigh these against the cost of losing the software. Set who pays before the agreement is signed."),
        ("Vendor failure",
         "A supplier may fail through money trouble, takeover or a change of plan. A continuity agreement can also cover hosting and support during a transition. Plan for the day the supplier is no longer there."),
        ("Testing",
         "Test the release process on a regular basis, as a real rehearsal. Check that the team can use the code and documents without the supplier's help. Record the results and fix gaps quickly."),
    ],
    "test": [
        ("What does an escrow deposit usually contain?",
         [("a", "A customer's bank password"), ("b", "A copy of the source code held by a neutral third party"), ("c", "A box of printer paper"), ("d", "A staff holiday rota")], "b"),
        ("What is a release trigger?",
         [("a", "A type of computer mouse"), ("b", "A staff meeting schedule"), ("c", "A warranty on hardware"), ("d", "An event that allows the code to be released to the customer")], "d"),
        ("Why test the deposit?",
         [("a", "A deposit is only useful if it builds and works"), ("b", "Testing wastes time on purpose"), ("c", "Testing is required only once in history"), ("d", "Testing removes the code")], "a"),
        ("What should be settled before an escrow agreement is signed?",
         [("a", "The colour of the agreement"), ("b", "The weather on the signing day"), ("c", "Who pays the costs"), ("d", "The name of the lawyer's dog")], "c"),
        ("Why rehearse the release process?",
         [("a", "To delete the deposit"), ("b", "To check the team can use the code and documents without the supplier"), ("c", "To stop all support"), ("d", "To avoid writing records")], "b"),
    ],
}
