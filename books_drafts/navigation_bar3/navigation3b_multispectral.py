"""Bands of Light: Multispectral Imaging. Seeing colours the eye cannot see, and reading plant health from them."""
CODE = 'navigation3b_multispectral'
BOOK = {
    "title": "Bands of Light: Multispectral Imaging",
    "subtitle": "Seeing colours the eye cannot see, and reading plant health from them",
    "chapters": [
        ("More than colours",
         "A normal camera records red, green and blue. A multispectral sensor records several narrow bands of light, some of which the eye cannot see, such as near-infrared. Each band tells a different story about the ground."),
        ("What plants reflect",
         "Leaves absorb most red light, because chlorophyll uses red light to make food. They reflect a great deal of near-infrared light, which they do not use. So healthy plants look dark in red and bright in near-infrared."),
        ("A vegetation index",
         "Analysts combine two bands in a formula. The best known is NDVI, the normalised difference vegetation index. It is near-infrared minus red, divided by near-infrared plus red. It gives values from minus one to plus one, and high values mean dense, healthy cover."),
        ("Reading the numbers",
         "Values near zero suggest bare soil or rock. Values below zero often mean water or cloud. A value that falls over a season can point to drought, disease or a crop that has been cut. The index is a guide, not a diagnosis."),
        ("Choosing the bands",
         "Water mapping often uses green and near-infrared bands, because water absorbs near-infrared light strongly. Rock mapping uses bands further into the infrared. The best set of bands depends on what you need to tell apart."),
        ("Money in the field",
         "A farm that checks its crops from space each month can see where water or feed is needed, and send help to those fields only. Spotting a drop early often costs less than repairing a late loss."),
    ],
    "test": [
        ("What does multispectral mean?",
         [("a", "Many bands of light, some beyond what the eye can see"), ("b", "Many people looking at one picture"), ("c", "Many maps stored in one drawer"), ("d", "Many satellites in one orbit")], "a"),
        ("Which light do healthy leaves absorb most strongly, to make food?",
         [("a", "Near-infrared"), ("b", "Green"), ("c", "Red"), ("d", "White")], "c"),
        ("What is NDVI?",
         [("a", "A kind of sensor"), ("b", "A vegetation index that compares near-infrared with red"), ("c", "A map projection"), ("d", "A rain gauge")], "b"),
        ("What does an NDVI value near zero most likely suggest?",
         [("a", "Dense forest"), ("b", "Bare soil or rock"), ("c", "Deep water"), ("d", "A busy road")], "b"),
        ("Why might a farm watch NDVI month by month?",
         [("a", "To spot a drop in plant health early, when a fix often costs less"), ("b", "To count the birds"), ("c", "To set the price of land"), ("d", "To measure the depth of wells")], "a"),
    ],
}
