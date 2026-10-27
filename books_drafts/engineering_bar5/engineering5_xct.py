"""X-Ray Computed Tomography of Parts: reconstruction, voxel size, porosity mapping, metrology and scan time against sampling."""
CODE = "engineering5_xct"
BOOK = {
    "title": "X-Ray Computed Tomography of Parts",
    "subtitle": "Seeing inside a part without cutting it open",
    "chapters": [
        ("Pictures from every side",
         "A computed tomography scanner takes X-ray images of a part from many angles. A computer combines them into a three-dimensional picture of the inside. The part is never cut, so the same piece can be checked again and again."),
        ("Building the volume",
         "The computer works backward from the many shadows to rebuild the density at each point. This step is called reconstruction. The result is a grid of small cubes, each with its own grey value."),
        ("Voxel size",
         "Each cube in that grid is a voxel, a three-dimensional pixel. A smaller voxel shows finer detail, but the scan takes longer and produces far more data. The right voxel size depends on the smallest feature the engineer must see."),
        ("Mapping pores",
         "Pores and cracks show as dark regions, because they hold less material. Software counts and sizes them, and maps where they sit. This gives a porosity map, which shows whether a casting or a printed part is sound where it matters."),
        ("Measuring by CT",
         "The scan can also measure a part's dimensions, including hidden inner passages that a probe cannot reach. Measurements carry uncertainty, and the engineer must state it. A number without its uncertainty is not a measurement."),
        ("Scan time against sampling",
         "Every extra image, and every finer voxel, adds scan time. Sampling fewer parts is cheaper, but it can miss a bad one. Teams weigh the cost of each scan against the cost of a part that fails in service."),
    ],
    "test": [
        ("What does a CT scanner take pictures from?",
         [("a", "One side only"), ("b", "Below the part only"), ("c", "Many angles"), ("d", "Inside a liquid bath")], "c"),
        ("What is a voxel?",
         [("a", "A type of X-ray tube"), ("b", "A fixture for holding a part"), ("c", "A unit of weight"), ("d", "A three-dimensional pixel")], "d"),
        ("How do pores usually show in a CT picture?",
         [("a", "As dark regions"), ("b", "As bright white rings"), ("c", "As red lines"), ("d", "They do not show")], "a"),
        ("What happens when the voxel size gets smaller?",
         [("a", "The scan gets faster"), ("b", "The scan gets finer detail but takes longer"), ("c", "The part gets heavier"), ("d", "Nothing changes")], "b"),
        ("Why must a CT measurement state its uncertainty?",
         [("a", "Because the X-ray tube needs it"), ("b", "Because the colour must match"), ("c", "Because a number without uncertainty is not a complete measurement"), ("d", "Because the part must be cut")], "c"),
    ],
}
