"""Alloys: steel, bronze, aluminium and titanium, and why engineers mix metals instead of using them pure."""
CODE = 'engineering2_alloys'
BOOK = {
    "title": 'Alloys: Steel, Bronze, Aluminium and Titanium',
    "subtitle": 'Mixing metals to get what a pure metal cannot give',
    "chapters": [
        ('Why mix metals',
         "Pure metals are often too soft, too weak or too reactive for a job. An alloy is a metal mixed with other elements to "
         "get the properties the job needs. Most structural metals in use are alloys, not pure metal."),
        ('Steel: iron and carbon',
         "Steel is iron with a small amount of carbon, usually well under two per cent. The carbon atoms sit between the iron "
         "atoms and make the metal much stronger than iron alone. Adding chromium and nickel gives stainless steel, which "
         "resists rust. Steel is about 7,850 kg per cubic metre, close to the 7,874 of pure iron in the catalogue."),
        ('Bronze: copper and tin',
         "Bronze is mainly copper, with tin added, often around a tenth of the mix. It is harder than copper, and it casts "
         "well into detailed shapes. That is why people have used it for bells, statues and bearings for thousands of years. "
         "Bronze is about 8,800 kg per cubic metre, a little heavier than copper's 8,960 is not quite true, so treat it as close to that of copper."),
        ('Aluminium alloys',
         "Pure aluminium is soft, so it is mixed with small amounts of copper, magnesium, zinc or silicon to make alloys strong "
         "enough for frames and skins. Aluminium is 2,700 kg per cubic metre, about a third as heavy as steel for the same "
         "volume. That is why aircraft and many spacecraft structures use aluminium alloys."),
        ('Titanium alloys',
         "Titanium is 4,507 kg per cubic metre, a little over half the weight of steel. Its alloys, with small amounts of "
         "aluminium and vanadium, are very strong for their weight, and they keep their strength at higher temperatures than "
         "aluminium does. They resist corrosion, including sea water. Titanium is hard to machine, so its parts cost more to make."),
        ('Choosing an alloy',
         "Write down what the part must do: the load it carries, the weight it may have, the heat it meets, and whether it "
         "is exposed to water or air. Then choose the alloy that does the job at the lowest weight and cost. Work out its "
         "weight from its density before you build, never after."),
    ],
    "test": [
        ("What is an alloy?",
         [('a', 'A metal mixed with other elements to get properties that pure metal lacks'), ('b', 'A pure metal, straight from the ground'), ('c', 'A kind of plastic'), ('d', 'A gas that has been cooled')], 'a'),
        ("What does a small amount of carbon do to iron?",
         [('a', 'It turns the iron into copper'), ('b', 'It makes the iron much stronger, giving steel'), ('c', 'It makes the iron lighter than air'), ('d', 'It makes the iron melt at room temperature')], 'b'),
        ("Bronze is mainly made of which two metals?",
         [('a', 'Iron and nickel'), ('b', 'Aluminium and lithium'), ('c', 'Copper and tin'), ('d', 'Gold and silver')], 'c'),
        ("Why is aluminium alloy chosen where weight matters?",
         [('a', 'It is harder than titanium'), ('b', 'It is magnetic'), ('c', 'It is cheaper than air'), ('d', 'It is about a third as heavy as steel for the same volume')], 'd'),
        ("What property makes titanium alloys useful for demanding parts?",
         [('a', 'They are very soft'), ('b', 'Strength for their weight, and resistance to corrosion'), ('c', 'They conduct heat like copper'), ('d', 'They melt easily')], 'b'),
    ],
}
