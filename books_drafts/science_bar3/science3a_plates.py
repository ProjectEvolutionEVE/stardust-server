"""Plate Tectonics: how a planet's outer shell breaks into plates that move, and what the edges do."""
CODE = 'science3a_plates'
BOOK = {
    "title": 'Plate Tectonics',
    "subtitle": 'How the outer shell breaks into plates that move, and what happens at their edges',
    "chapters": [
        ("A broken shell",
         "Earth's rigid outer shell, the lithosphere, is cut into seven large plates and many smaller ones. Each plate carries continents, oceans or both. The plates fit together like a broken puzzle."),
        ("Plates move slowly",
         "The plates move a few centimetres each year, about as fast as a fingernail grows. Over millions of years that adds up to whole oceans opening and closing."),
        ("What drives them",
         "Heat from deep inside the planet makes the mantle rock flow in slow loops, called convection. The plates ride on top of this flow. A plate that sinks at its edge also pulls the rest of the plate down with it."),
        ("Three kinds of edge",
         "Where plates pull apart, as at the Mid-Atlantic Ridge, new rock rises and fills the gap. Where they push together, one plate can sink under the other, making deep trenches and volcanic mountains. Where they slide past each other, as on the San Andreas Fault, earthquakes are common."),
        ("Mountains and oceans",
         "The Himalayas rose where the Indian plate pushed into Asia. The Atlantic Ocean widens a little each year as the plates on either side move apart. Both are slow, steady results of the same process."),
        ("Why Earth's surface is young",
         "Plate tectonics recycles the crust. Old seafloor sinks back into the mantle at the edges of plates, so almost all of the seafloor is less than about 200 million years old. The continents are much older, but their surfaces keep changing."),
    ],
    "test": [
        ("What is the rigid outer shell of a planet called?",
         [('a', 'The mantle'), ('b', 'The lithosphere'), ('c', 'The core'), ('d', 'The corona')], 'b'),
        ("About how fast do Earth's plates move?",
         [('a', 'A few centimetres a year'), ('b', 'A few kilometres a day'), ('c', 'Several metres a second'), ('d', 'Not at all')], 'a'),
        ("What kind of plate boundary is the Mid-Atlantic Ridge?",
         [('a', 'Convergent'), ('b', 'Transform'), ('c', 'Divergent'), ('d', 'Dormant')], 'c'),
        ("What mainly drives the motion of the plates?",
         [('a', 'The tides of the Moon'), ('b', 'Wind blowing across the surface'), ('c', 'Rain falling into the oceans'), ('d', 'Heat-driven flow in the mantle')], 'd'),
        ("Why is most of Earth's seafloor young?",
         [('a', 'Old seafloor sinks back into the mantle at plate edges'), ('b', 'The seafloor is made fresh every day'), ('c', 'Seawater dissolves the rock'), ('d', 'Only the continents have ever been old')], 'a'),
    ],
}
