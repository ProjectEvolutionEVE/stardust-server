"""Mandelbrot and Wild Randomness: cotton prices, self-similarity, fat tails, why the bell curve fails, and what it means for risk."""
CODE = "business5_fractal"
BOOK = {
    "title": "Mandelbrot and Wild Randomness",
    "subtitle": "Cotton prices, self-similarity, fat tails, and what the bell curve misses",
    "chapters": [
        ("Benoit Mandelbrot", "Benoit Mandelbrot was a mathematician who studied patterns that repeat at every scale. He is known for the idea of fractals, shapes that look similar when you zoom in. His work also changed how people thought about prices."),
        ("Cotton prices", "In the early 1960s Mandelbrot studied the price of cotton over many years. He found that the changes did not follow the smooth bell curve often assumed. Large swings came more often than the usual models predicted."),
        ("Self-similarity", "Self-similarity means a pattern looks alike at different scales. Price charts over a day, a month, or a year can look similar in their roughness. This hints that the same kind of randomness runs through markets at many time scales."),
        ("Fat tails", "Fat tails mean extreme moves are far more common than a normal distribution would predict. A few very large moves can dominate the total change. Models that ignore them tend to underestimate risk."),
        ("Why the Gaussian fails", "The Gaussian, or normal, distribution is the bell curve that many models use. It assumes that big surprises are very rare. When that assumption fails, risk models can give a false sense of safety."),
        ("Implications for risk", "Mandelbrot and Richard Hudson wrote The (Mis)Behavior of Markets, published in 2004, arguing that markets are wilder than the standard models admit. The lesson is to plan for extremes, keep reserves, and not assume the normal curve will hold. Respect for wild randomness is good sense."),
    ],
    "test": [
        ("What is a fractal?",
         [("a", "A shape that looks similar at different scales"), ("b", "A type of coin"), ("c", "A kind of ship"), ("d", "A tax code")], "a"),
        ("What did Mandelbrot study in the early 1960s?",
         [("a", "Coffee"), ("b", "Oil"), ("c", "Gold"), ("d", "Cotton prices")], "d"),
        ("What are fat tails?",
         [("a", "Thick hair"), ("b", "Extreme moves that are more common than a normal curve predicts"), ("c", "Short prices"), ("d", "Rounded numbers")], "b"),
        ("What does the Gaussian curve assume about big surprises?",
         [("a", "They are common"), ("b", "They are the most common outcome"), ("c", "They are very rare"), ("d", "They always happen on a Monday")], "c"),
        ("What is the main lesson of Mandelbrot's work for risk?",
         [("a", "Plan for extremes and do not assume the normal curve holds"), ("b", "Ignore all extremes"), ("c", "Markets are always calm"), ("d", "Risk does not exist")], "a"),
    ],
}
