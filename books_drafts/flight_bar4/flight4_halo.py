"""Halo and Lissajous Orbits: looping paths around the balance points where two bodies' pulls cancel out."""
CODE = "flight4_halo"
BOOK = {
    "title": "Halo and Lissajous Orbits",
    "subtitle": "Looping paths around the balance points in space",
    "chapters": [
        ("Balance points", "Between two large bodies, such as the Sun and the Earth, there are five special spots called Lagrange points. At these spots the pulls of the two bodies and the spin of the system balance, so a craft can stay in a steady pattern near them."),
        ("What a halo orbit is", "A halo orbit is a loop around one of these points. Seen from the side, it looks like a ring hanging over the point. Seen from above, it looks like a loop that circles the point."),
        ("Unstable motion", "A craft near a Lagrange point is not sitting still in a stable valley. A small push can grow over time, so the craft drifts away unless it is corrected. The motion is stable enough to plan with, but it always needs care."),
        ("Station-keeping there", "To stay on a halo orbit, a craft makes small burns from time to time. These burns are called station-keeping. Engineers plan them ahead, so each one is small and well timed."),
        ("Missions that used these orbits", "SOHO, the Sun-watching observatory, sits near the Sun-Earth point L1. James Webb, the space telescope, orbits the Sun-Earth point L2 on a large looping path called a Lissajous orbit. Other missions have used halo orbits too."),
        ("Transfer paths", "Getting to a halo orbit can take many months. Planners use the shape of the paths near these points to reach them with little fuel. The route in is often as important as the orbit itself."),
    ],
    "test": [
        ("What are Lagrange points?", [("a", "Colours on a map"), ("b", "Types of rocket"), ("c", "Places on the Moon's surface"), ("d", "Special spots where the pulls of two bodies balance")], "d"),
        ("What does a craft need to do to stay near a halo orbit?", [("a", "Sit still forever"), ("b", "Make small burns called station-keeping"), ("c", "Turn off all power"), ("d", "Move to the Moon")], "b"),
        ("Why is motion near these points unstable?", [("a", "The craft is too heavy"), ("b", "There is too much air"), ("c", "A small push can grow, so the craft drifts unless corrected"), ("d", "The points are made of ice")], "c"),
        ("Which observatory sits near the Sun-Earth point L1?", [("a", "SOHO"), ("b", "A bicycle"), ("c", "A lighthouse"), ("d", "A weather balloon")], "a"),
        ("What is the James Webb telescope's path called?", [("a", "A straight line"), ("b", "A square spiral"), ("c", "A low ring over the Moon"), ("d", "A Lissajous orbit")], "d"),
    ],
}
