"""Thermochronology: Cooling Histories. How dated minerals reveal when rocks cooled as they rose toward the surface."""
CODE = "science5_geo_thermochron"
BOOK = {
    "title": "Thermochronology: Cooling Histories",
    "subtitle": "Reading the temperature history of rocks from their dated minerals",
    "chapters": [
        ("Rocks that cool",
         "Rocks deep in the crust are hot, and as mountains rise and erosion removes the rock above, they cool. Thermochronology uses dated minerals to reconstruct how fast and when that cooling happened."),
        ("Closure temperature",
         "The closure temperature of a mineral is the temperature below which a radiometric clock in it stops losing its daughter products. Each mineral and system has its own closure temperature, which sets the thermal window it can record."),
        ("Apatite fission tracks",
         "Apatite can hold tiny damage trails left by fission of uranium atoms. The number and length of these tracks change with temperature, so they record the cooling of the rock in the upper crust."),
        ("Helium dating",
         "Helium is produced in minerals such as apatite and zircon by the decay of uranium and thorium. Measuring the helium that remains gives a date that depends on the rock's temperature history."),
        ("Exhumation rates",
         "Exhumation is the removal of rock above a sample as it reaches the surface. Combining cooling ages with a known or assumed geothermal gradient gives an exhumation rate, which tells how fast mountains were uncovered."),
        ("Thermal models and sample selection",
         "Thermal models simulate how rock temperature changes through time, and they are compared with measured ages. Good studies choose samples from several elevations in a vertical profile, so the cooling path can be read."),
    ],
    "test": [
        ("What is a closure temperature?",
         [("a", "The temperature at which rock melts"), ("b", "The temperature of the air above a mountain"), ("c", "The temperature below which a mineral stops losing its daughter products"), ("d", "The temperature of the sea floor")], "c"),
        ("What do apatite fission tracks record?",
         [("a", "The cooling of rock in the upper crust"), ("b", "The taste of groundwater"), ("c", "The number of birds that nest in a cliff"), ("d", "The speed of ocean currents")], "a"),
        ("What does exhumation mean?",
         [("a", "The burial of rock under new sediment"), ("b", "The melting of rock into magma"), ("c", "The growth of a glacier"), ("d", "The removal of rock above a sample as it reaches the surface")], "d"),
        ("What is helium produced by in minerals such as zircon?",
         [("a", "The decay of uranium and thorium"), ("b", "The burning of coal"), ("c", "The melting of ice"), ("d", "The growth of plants")], "a"),
        ("Why are samples taken from several elevations in a vertical profile?",
         [("a", "To make the rock look taller"), ("b", "To count the number of trees"), ("c", "To read the cooling path through the rock"), ("d", "To find oil in the sea")], "c"),
    ],
}
