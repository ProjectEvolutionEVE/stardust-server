"""Medicine, bar 2: Milestones in Medicine. Germ theory, anaesthesia, antiseptics and antibiotics, as history."""
CODE = "medicine2_milestones"
BOOK = {
    "title": "Milestones in Medicine",
    "subtitle": "Germs, anaesthesia and antibiotics: how medicine changed in about a century",
    "chapters": [
        ("Before germs were known",
         "For most of history, people believed illness came from bad air, bad smells or an imbalance in the body. Many doctors did not wash their hands between patients, so infections often spread through hospitals."),
        ("Semmelweis and handwashing",
         "In the 1840s the Hungarian doctor Ignaz Semmelweis, working in Vienna, found that washing hands in a disinfectant solution sharply reduced deaths on his clinic. His findings were not quickly accepted, and many doctors resisted them for years."),
        ("Germ theory",
         "In the 1860s and 1870s, Louis Pasteur showed that microbes can cause fermentation and disease. Robert Koch then linked specific bacteria to specific diseases, including tuberculosis in 1882. This germ theory of disease explained infection and pointed the way to prevention."),
        ("Anaesthesia",
         "Surgery was long a terrifying ordeal of pain. In 1846 William Morton publicly demonstrated ether as an anaesthetic in Boston, letting a patient sleep through an operation. Anaesthesia made longer and more careful surgery possible."),
        ("Antiseptics and cleaner surgery",
         "In the 1860s Joseph Lister used carbolic acid to clean wounds and instruments, which helped reduce the deadly infections that often followed surgery. Clean technique became a basic part of surgery."),
        ("Antibiotics",
         "In 1928 Alexander Fleming noticed that a mould, Penicillium, had killed bacteria on a dish he had left out. In the early 1940s Howard Florey and Ernst Chain developed it into a usable medicine. Antibiotics have since saved very many lives, but overuse has led to bacteria that resist them."),
    ],
    "test": [
        ("Which doctor's handwashing rule greatly reduced deaths on his clinic?",
         [("a", "Edward Jenner"), ("b", "Robert Koch"), ("c", "William Morton"), ("d", "Ignaz Semmelweis")], "d"),
        ("What did William Morton demonstrate in 1846?",
         [("a", "Ether as an anaesthetic"), ("b", "Penicillin"), ("c", "The stethoscope"), ("d", "A vaccine for smallpox")], "a"),
        ("What did germ theory show?",
         [("a", "That illness comes from bad smells"), ("b", "That specific microbes cause specific diseases"), ("c", "That bones make blood"), ("d", "That the heart does not beat")], "b"),
        ("Which 1928 discovery began the story of antibiotics?",
         [("a", "The stethoscope"), ("b", "Anaesthesia"), ("c", "A mould that killed bacteria on a dish"), ("d", "Vaccination of cattle")], "c"),
        ("What is the main warning about antibiotics today?",
         [("a", "Overuse can lead to bacteria that resist them"), ("b", "They cure viruses in every case"), ("c", "They have no effect on bacteria"), ("d", "They replace sleep")], "a"),
    ],
}
