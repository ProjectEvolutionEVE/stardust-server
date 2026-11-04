"""Contaminant Transport in Groundwater. How pollutants move, spread, stick to rock and get cleaned up underground."""
CODE = "science5_geo_contaminant"
BOOK = {
    "title": "Contaminant Transport in Groundwater",
    "subtitle": "Where pollution travels underground, and how we track it",
    "chapters": [
        ("Groundwater on the move",
         "Groundwater flows slowly through the pores and fractures of soil and rock. A contaminant dissolved in that water travels with it, and its path depends on the flow and the rock."),
        ("Advection and dispersion",
         "Advection is the movement of a dissolved substance with the flow of water. Dispersion spreads it out as water takes different routes through the rock, so the pollution forms a widening plume."),
        ("Sorption and retardation",
         "Some contaminants stick to mineral and organic surfaces, a process called sorption. Sorption slows the contaminant down, so it moves more slowly than the water that carries it."),
        ("Plume modelling",
         "Plume models use flow data, dispersion and sorption to predict where a contaminant will go and how concentrations will change. The models are checked against samples from wells."),
        ("Remediation methods",
         "Remediation removes or contains contamination. Methods include pumping and treating water, injecting material that breaks down pollutants, and building barriers that keep the plume from spreading."),
        ("Monitoring well design",
         "A monitoring well must be placed and screened at the right depth to sample the plume. Poor placement can miss the contamination completely, so good design is essential."),
    ],
    "test": [
        ("What is advection in groundwater?",
         [("a", "The freezing of water in soil"), ("b", "The growth of plants in sand"), ("c", "The breaking of rock by roots"), ("d", "The movement of a dissolved substance with the flow of water")], "d"),
        ("What does dispersion do to a contaminant plume?",
         [("a", "It stops the plume at once"), ("b", "It spreads the plume as water takes different routes"), ("c", "It turns the plume into rock"), ("d", "It moves the plume upward into the air")], "b"),
        ("What is sorption?",
         [("a", "A type of rain"), ("b", "A fish that lives in aquifers"), ("c", "A contaminant sticking to mineral or organic surfaces"), ("d", "The heating of water")], "c"),
        ("What do plume models use to predict contaminant movement?",
         [("a", "Only the colour of the soil"), ("b", "Flow data, dispersion and sorption"), ("c", "Only the wind speed above the land"), ("d", "Only the age of the trees")], "b"),
        ("Why must monitoring wells be placed and screened carefully?",
         [("a", "Poor placement can miss the contamination completely"), ("b", "Wells must always be the same depth everywhere"), ("c", "Wells cannot sample groundwater"), ("d", "Wells only measure air")], "a"),
    ],
}
