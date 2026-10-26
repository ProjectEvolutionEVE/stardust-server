"""Medicine, bar 3 (Senior Doctor), part A: The Kidneys. How the kidneys filter the blood, sort what to keep and adjust water and salt."""
CODE = "medicine3a_kidneys"
BOOK = {
    "title": "The Kidneys: Filtering the Blood",
    "subtitle": "Filters, tubes and careful sorting that keep water and salts in balance",
    "chapters": [
        ("Two kidneys, a lot of filtering",
         "The kidneys sit at the back of the abdomen, one on each side. Together they filter all of the blood in the body many times a day. Their job is to clean the blood and keep its water and salt content in balance."),
        ("The filter",
         "Each kidney holds about a million tiny filtering units called nephrons. Blood pressure pushes water and small dissolved substances out of the blood and into a tube. Large things, such as blood cells and most proteins, stay in the blood."),
        ("Sorting what is kept",
         "As the filtered fluid flows along the tubes, the body takes back what it needs, such as glucose, salts and most of the water. What is not needed, such as urea from the breakdown of protein, leaves the body in urine."),
        ("Adjusting on the way",
         "The amount of water and salt taken back is adjusted by hormones. The kidneys hold on to water when the body is short of it, and let it go when there is plenty. This fine tuning is one of the clearest examples of homeostasis at work."),
        ("Waste and the liver",
         "The liver turns protein breakdown into urea, and the kidneys remove it. The kidneys also help control acid and salt levels in the blood. When they stop working well, wastes build up, which is why kidney health matters so much."),
        ("Looking after your kidneys",
         "Drinking enough fluid for your activity, eating a balanced diet, and keeping blood pressure and blood sugar in healthy ranges all help protect the kidneys. Early signs are easy to miss, so a regular health check is a good habit."),
    ],
    "test": [
        ("What are the tiny filtering units of the kidney called?",
         [("a", "Alveoli"), ("b", "Nephrons"), ("c", "Villi"), ("d", "Neurons")], "b"),
        ("What is the main thing the kidneys do?",
         [("a", "Pump blood around the body"), ("b", "Make red blood cells"), ("c", "Digest fat"), ("d", "Filter the blood and keep water and salts in balance")], "d"),
        ("Which of these is normally kept in the blood rather than filtered out into urine?",
         [("a", "Urea"), ("b", "Extra water"), ("c", "Blood cells"), ("d", "Excess salts")], "c"),
        ("What is urea?",
         [("a", "A waste product from the breakdown of protein, removed by the kidneys"), ("b", "A type of vitamin"), ("c", "A hormone made in the lungs"), ("d", "A mineral found in bones")], "a"),
        ("How does the body keep water when it is short of it?",
         [("a", "Hormones make the kidneys take back more water"), ("b", "The kidneys stop working"), ("c", "Water is made in the skin"), ("d", "The lungs turn gas into water")], "a"),
    ],
}
