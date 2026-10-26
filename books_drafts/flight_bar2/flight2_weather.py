"""Weather in Space: the solar wind, solar flares and what they mean for craft and crews."""
CODE = "flight2_weather"
BOOK = {
    "title": "Weather in Space",
    "subtitle": "The solar wind, solar flares, and what they mean for craft and crews",
    "chapters": [
        ("The Sun blows",
         "The Sun gives off a constant stream of charged particles called the solar wind. Near the Earth it usually blows at a few hundred kilometres a second, far faster than any craft flies. It fills the whole solar system."),
        ("Solar flares",
         "Sometimes the Sun releases a sudden burst of energy called a solar flare. A flare can send radiation outward within minutes. It can be followed by a larger cloud of particles called a coronal mass ejection, which travels more slowly."),
        ("Why it matters",
         "Strong solar storms can disturb the electronics on spacecraft and raise the radiation that crews receive. Real missions watch space weather closely, and they can delay work or move crews to better shielding."),
        ("Light that falls off",
         "The Sun's light and heat weaken with the square of the distance, which is a predictable pattern. The game's own sunlight follows the same rule. A pilot near the Sun should expect much stronger light and heat."),
        ("Aurora and the Earth's field",
         "When a solar storm reaches the Earth, it can light up the sky with aurora. The Earth's magnetic field deflects most of the charged particles, which is why people on the ground are mostly protected."),
        ("Planning around the weather",
         "A pilot plans around space weather much as a sailor plans around the wind. Before a long trip, check a space weather forecast, and keep a plan in case the weather turns. Real crews rely on this planning."),
    ],
    "test": [
        ("What is the solar wind?",
         [("a", "A breeze in the Starship's bay"), ("b", "A storm on Jupiter"), ("c", "A type of debris"), ("d", "A constant stream of charged particles from the Sun")], "d"),
        ("About how fast does the solar wind usually blow near the Earth?",
         [("a", "A few hundred kilometres a second"), ("b", "About one metre a second"), ("c", "About the speed of sound on Earth"), ("d", "It does not move at all")], "a"),
        ("What is a solar flare?",
         [("a", "A sudden burst of energy from the Sun"), ("b", "A bright planet"), ("c", "A debris field"), ("d", "A radio on the Starship")], "a"),
        ("Why are strong solar storms a concern for crews and spacecraft?",
         [("a", "They raise radiation and can disturb electronics"), ("b", "They make the bay too bright to see"), ("c", "They fill the hold"), ("d", "They turn the bars gold")], "a"),
        ("What does Earth's magnetic field do for people on the ground?",
         [("a", "Turns off the Sun"), ("b", "Makes the Sun brighter"), ("c", "Brings debris down"), ("d", "Deflects most of the charged particles")], "d"),
    ],
}
