"""Cellular Metabolism and Energy Pathways: glycolysis, the citric acid cycle, ATP and electron transport, oxidative phosphorylation, metabolic regulation and energy yields."""
CODE = "science4_bio_metabolism"
BOOK = {
    "title": "Cellular Metabolism and Energy Pathways",
    "subtitle": "Glycolysis, the citric acid cycle and ATP",
    "chapters": [
        ("Glycolysis", "Glycolysis breaks one glucose molecule into two molecules of pyruvate, making a small amount of ATP. It takes place in the cytoplasm and does not need oxygen."),
        ("The citric acid cycle", "In a cell with oxygen, pyruvate enters the mitochondria, where the citric acid cycle releases carbon dioxide. The cycle produces electron carriers that feed the next stage."),
        ("ATP and electron transport", "Electron carriers pass electrons along a chain of proteins in the inner mitochondrial membrane. The energy released pumps protons across that membrane."),
        ("Oxidative phosphorylation", "The proton gradient drives ATP synthase, which makes large amounts of ATP. This process is called oxidative phosphorylation, and oxygen is the final electron acceptor."),
        ("Metabolic regulation", "Cells control these pathways by sensing their energy state. High levels of ATP slow the pathways down, and low levels speed them up."),
        ("Energy yields", "Burning glucose fully yields far more ATP through the whole pathway than glycolysis alone. The exact yields vary between cell types and conditions."),
    ],
    "test": [
        ("What does glycolysis start with?",
         [("a", "Oxygen"), ("b", "Glucose"), ("c", "Water"), ("d", "Salt")], "b"),
        ("Where does glycolysis take place?",
         [("a", "In the cytoplasm"), ("b", "In the nucleus"), ("c", "In the cell wall"), ("d", "In the membrane")], "a"),
        ("What is the final electron acceptor in aerobic respiration?",
         [("a", "Carbon dioxide"), ("b", "Nitrogen"), ("c", "Oxygen"), ("d", "Iron")], "c"),
        ("What does ATP synthase do?",
         [("a", "It breaks down proteins"), ("b", "It moves water out of cells"), ("c", "It stores light"), ("d", "It makes ATP using a proton gradient")], "d"),
        ("What happens when a cell has high levels of ATP?",
         [("a", "Pathways speed up"), ("b", "Pathways slow down"), ("c", "The cell grows wings"), ("d", "The cell divides at once")], "b"),
    ],
}
