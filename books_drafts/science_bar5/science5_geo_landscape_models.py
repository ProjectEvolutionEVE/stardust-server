"""Landscape Evolution Modelling. How scientists model hills, rivers and valleys as they change over time."""
CODE = "science5_geo_landscape_models"
BOOK = {
    "title": "Landscape Evolution Modelling",
    "subtitle": "Computer models of how valleys and hills change over time",
    "chapters": [
        ("Landscapes that change",
         "Landscapes are shaped by uplift that raises the land and erosion that wears it down. Landscape evolution models represent these processes in equations, so a computer can run the shape of a region forward through time."),
        ("The stream power law",
         "The stream power law says that a river erodes faster where water flow is greater and the channel is steeper. Its parameters, such as erodibility, are calibrated against field data, and the law is a common core of these models."),
        ("Hillslope diffusion",
         "Hillslopes soften through creep and slow soil movement, which a diffusion equation describes. Hillslope diffusion smooths sharp edges and links ridges to the rivers below them."),
        ("Uplift and erosion",
         "When uplift speeds up, rivers cut deeper and the landscape responds. The balance between uplift and erosion sets the average height and relief of a mountain range."),
        ("Transient landscapes",
         "A landscape that has not yet adjusted to a change is called transient. A knickpoint, a sharp step in a river profile, can travel upstream and show that the uplift began recently."),
        ("Testing models against the field",
         "A model is only useful if its predictions match real measurements, such as river profiles, erosion rates and dated surfaces. Scientists test several models and admit when a model fails to fit."),
    ],
    "test": [
        ("What two processes shape a landscape in these models?",
         [("a", "Snowfall and sunlight"), ("b", "Uplift and erosion"), ("c", "Ocean tides and moon phases"), ("d", "Volcanic ash and lightning")], "b"),
        ("What does the stream power law describe?",
         [("a", "How a river erodes, faster with more flow and steeper slope"), ("b", "How fast leaves fall in autumn"), ("c", "How deep the sea is"), ("d", "How clouds form")], "a"),
        ("What does hillslope diffusion do to a landscape?",
         [("a", "It smooths sharp edges over time"), ("b", "It makes cliffs taller"), ("c", "It creates ice sheets"), ("d", "It removes all rivers")], "a"),
        ("What is a transient landscape?",
         [("a", "A landscape that has finished adjusting to all changes"), ("b", "A landscape made of ice only"), ("c", "A landscape that has not yet adjusted to a change"), ("d", "A landscape under the sea")], "c"),
        ("What must a useful landscape model do?",
         [("a", "Match real measurements such as river profiles and erosion rates"), ("b", "Ignore all field data"), ("c", "Predict only the weather"), ("d", "Always give the same answer whatever the data")], "a"),
    ],
}
