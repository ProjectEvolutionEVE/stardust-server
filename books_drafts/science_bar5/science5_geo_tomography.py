"""Seismic Tomography: Imaging the Mantle. How earthquake waves reveal the hidden rock inside the Earth."""
CODE = "science5_geo_tomography"
BOOK = {
    "title": "Seismic Tomography: Imaging the Mantle",
    "subtitle": "Using earthquake waves to map the rock inside the Earth",
    "chapters": [
        ("Listening to the Earth",
         "Earthquakes send seismic waves through the whole planet. Seismometers around the world record when each wave arrives. The waves travel at speeds that depend on the rock they pass through, so their arrival times carry a message about what lies below."),
        ("Travel times",
         "Travel-time inversion compares the arrival times we measure with the times a model predicts. Where waves arrive early, the rock is probably faster and colder. Where they arrive late, the rock is probably slower and hotter, or partly melted."),
        ("Ray coverage",
         "Each wave path is a thin line through the Earth, called a ray. A region seen by many crossing rays can be imaged in detail. A region crossed by few rays stays blurred, and scientists must say so."),
        ("Resolution tests",
         "Before trusting an image, researchers build a test model with a known shape and generate synthetic arrival times for it. If the method recovers the test shape, they gain confidence that real features are not artifacts of the way the rays are spread out."),
        ("Imaging slabs",
         "Cold, dense oceanic plates sink into the mantle at subduction zones. Because cold rock is fast for seismic waves, these slabs show up as fast zones that can be followed down hundreds of kilometres."),
        ("Reading the images with care",
         "A tomography image is a model, not a photograph. Scientists report the uncertainty, check features with other methods, and trust a structure most when several independent data sets agree on it."),
    ],
    "test": [
        ("What does seismic tomography use to build images of the Earth's interior?",
         [("a", "Sunlight reflected from the surface"), ("b", "Magnetic records in old lava"), ("c", "The arrival times of seismic waves"), ("d", "Drilling cores from the mantle")], "c"),
        ("Where do cold, dense oceanic plates sink into the mantle?",
         [("a", "Mid-ocean ridges"), ("b", "Subduction zones"), ("c", "Hot spots"), ("d", "Continental rifts")], "b"),
        ("Why does a region crossed by few rays look blurred in a tomography image?",
         [("a", "Few crossing paths give little detail there"), ("b", "The images are always coloured by hand"), ("c", "Few rays means the rock is melted"), ("d", "Few rays means there is no rock")], "a"),
        ("What is a resolution test in tomography?",
         [("a", "A test of the seismometer batteries"), ("b", "A check that the method recovers a model of known shape"), ("c", "A count of earthquakes each year"), ("d", "A measure of wave colour")], "b"),
        ("What do fast zones on a tomography image usually suggest?",
         [("a", "Hot, partly melted rock"), ("b", "Cold, dense rock such as a sinking slab"), ("c", "Empty space"), ("d", "Air trapped in the crust")], "b"),
    ],
}
