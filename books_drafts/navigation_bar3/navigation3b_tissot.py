"""Tissot's Circles: Measuring Distortion. How to see where a map stretches, and by how much."""
CODE = 'navigation3b_tissot'
BOOK = {
    "title": "Tissot's Circles: Measuring Distortion",
    "subtitle": "How to see where a map stretches, and by how much",
    "chapters": [
        ("A way to see the stretch",
         "A map can be checked by picturing small circles on the globe and seeing what they become on the flat map. A French mathematician of the 1800s, Nicolas Auguste Tissot, showed how to do this. The marks are called Tissot's indicatrix."),
        ("Circles become ovals",
         "On a map that keeps shape, the circles stay round, though they may grow or shrink. On a map that keeps area, they keep their size but stretch into ovals. Most flat maps do some of both, so the circles become ovals of different sizes and tilts."),
        ("Two numbers at each point",
         "At each point, the stretch has two main values: the largest scale and the smallest scale. The ratio between them shows how far that point is from keeping its shape. Where the two values are equal, the circle stays round."),
        ("Reading the pattern",
         "When the ovals are drawn across a whole map, the pattern shows where it is safe to measure. Ovals that swell toward the edge warn that distances there are less reliable. Ovals that stay small and nearly round mark the good region."),
        ("Checking a map yourself",
         "A navigator can test a chart by measuring a known distance on the ground and comparing it with the map's scale bar in that area. If the two disagree, the map is stretched there. Use the scale bar drawn on the map, not one number written in a corner."),
        ("Why it costs money",
         "A survey that is out by a few percent can cost real money when it is used to price land, fencing or pipe. Checking the stretch first takes little time, and it can save a job from being quoted wrong."),
    ],
    "test": [
        ("What does Tissot's indicatrix show?",
         [("a", "The colours of a map"), ("b", "How the scale stretches at each point of a map"), ("c", "The depth of the sea"), ("d", "The age of the map")], "b"),
        ("On a map that keeps area, what happens to small circles drawn on the globe?",
         [("a", "They vanish"), ("b", "They turn into squares"), ("c", "They stay perfectly round"), ("d", "They keep their size but stretch into ovals")], "d"),
        ("What do the two main scale values at a point tell you?",
         [("a", "How far the map is from keeping its shape at that point"), ("b", "The population there"), ("c", "The height of the sea"), ("d", "The date of the survey")], "a"),
        ("Where is a map usually safest for measuring distances?",
         [("a", "Near the edges, where the ovals are largest"), ("b", "Anywhere, since the distortion is always the same"), ("c", "Only where the map is printed in colour"), ("d", "Where the ovals are small and nearly round")], "d"),
        ("What is the safest way to check a map's scale in one area?",
         [("a", "Use the scale written in the corner only"), ("b", "Trust the map and skip the check"), ("c", "Measure a known distance on the ground and compare it with the map's scale bar"), ("d", "Use a ruler held near the edge")], "c"),
    ],
}
