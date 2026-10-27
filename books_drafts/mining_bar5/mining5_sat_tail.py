"""Satellite Data for Tailings and Mines: using spectral indices, change detection and radar to watch tailings dams and mine sites from orbit."""
CODE = "mining5_sat_tail"
BOOK = {
    "title": "Satellite Data for Tailings and Mines",
    "subtitle": "Spectral indices, water detection, dam monitoring and revisit times",
    "chapters": [
        ("Watching from orbit",
         "Satellites photograph the same site again and again. Those images show how vegetation, water and bare ground change over time. For a mine, this is a low-cost way to watch large areas."),
        ("Spectral indices",
         "A spectral index combines two or more colour bands into one number. The vegetation index is a well-known example, because healthy plants reflect more near-infrared light. Indices make changes easier to see."),
        ("Water detection",
         "Water absorbs near-infrared light and reflects little of it, so open water shows up dark in those bands. Water indices can map ponds, pools and seepage on a tailings area. Changes in water extent can be an early sign of trouble."),
        ("Change detection and dam monitoring",
         "Comparing images taken at different dates shows where the ground or the water has changed. Radar satellites can also measure tiny movements of a dam wall. These records help engineers spot a problem early."),
        ("Cloud cover",
         "Clouds block optical images, and many sites are cloudy for long periods. Radar can see through cloud, which is why it is useful in wet regions. Planners check cloud records before relying on a satellite."),
        ("Revisit times",
         "A satellite returns to the same spot after a set number of days. Some systems revisit every few days and others less often. A short revisit time gives more chances to see a change as it happens."),
    ],
    "test": [
        ("What does a spectral index do?",
         [("a", "It paints the satellite gold"), ("b", "It combines two or more colour bands into one number"), ("c", "It counts the miners"), ("d", "It replaces the dam")], "b"),
        ("Why does open water look dark in certain satellite bands?",
         [("a", "Water absorbs near-infrared light and reflects little of it"), ("b", "Water is always painted black"), ("c", "Water is too small to see"), ("d", "Water only exists at night")], "a"),
        ("What can radar satellites do that optical images cannot?",
         [("a", "See through cloud cover"), ("b", "Smell the air"), ("c", "Cook food"), ("d", "Print a map on paper")], "a"),
        ("What does change detection compare?",
         [("a", "The colour of two different cars"), ("b", "The weight of two dams"), ("c", "Images taken at different dates to show what has changed"), ("d", "The prices of two metals")], "c"),
        ("What does a short revisit time give?",
         [("a", "A slower view of the site"), ("b", "No images at all"), ("c", "Lower cost for the mine's lunch"), ("d", "More chances to see a change as it happens")], "d"),
    ],
}
