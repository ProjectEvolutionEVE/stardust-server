"""Logistics & Hauling (10-20): space, weight and getting goods home. Built on rules 10, 13, 22 and store.py."""
CODE = "logistics"
BOOK = {
    "title": "Logistics & Hauling",
    "subtitle": "Space, weight, and getting your goods home",
    "chapters": [
        ("What logistics means",
         "Logistics is getting the right goods to the right place, with room to keep them. Haulers on Earth always asked "
         "two questions: will it fit, and how heavy is it? Aboard the Starship you ask the same two."),
        ("Nothing is unlimited",
         "Every place that holds goods has a size. Your ship's hold has a size, and so does your own fixed space in the "
         "Starship's cargo hold. Your hangar has a set number of ship slots. Plan your loads around them."),
        ("Size and weight",
         "Every piece has a real size and a real weight. Weight is size times density, so two pieces the same size can "
         "weigh very different amounts. A piece only goes into your hold if its shape fits and there's room left."),
        ("Unloading",
         "When you unload at the Starship, each piece in your ship's hold goes into your space in the cargo hold, until "
         "that space is full. Whatever doesn't fit stays aboard your ship. Every unload gives you a receipt."),
        ("Where things are kept",
         "Raw materials go to your space in the cargo hold. Blueprints go in your filing cabinet. Valuables go in the "
         "lockbox inside it. Library books you check out sit on your bookshelf. You can see it all at your Desk under "
         "My items, a folder for each place."),
        ("Making room",
         "When your cargo space is full, you make room by selling. The Starship bank keeps a standing bid on every item, "
         "so you can always sell a full lot. Before you buy, check you have room: the market only lets you buy what fits."),
    ],
    "test": [
        ("Is your space in the Starship's cargo hold unlimited?",
         [("a", "Yes"), ("b", "No, it has a fixed size"), ("c", "Only for gold"), ("d", "Only at night")], "b"),
        ("What decides a piece's weight?",
         [("a", "Its colour"), ("b", "Its size times its density"), ("c", "The market price"), ("d", "Its name")], "b"),
        ("What happens to pieces that don't fit when you unload?",
         [("a", "They are lost"), ("b", "They stay aboard your ship"), ("c", "The bank buys them"), ("d", "They go to your bed")], "b"),
        ("Where are your blueprints kept?",
         [("a", "In the cargo hold"), ("b", "On the bookshelf"), ("c", "In the filing cabinet"), ("d", "In the closet")], "c"),
        ("Your cargo space is full. What is a quick way to make room?",
         [("a", "Sell a lot to the bank's standing bid"), ("b", "Ask another player"), ("c", "Wait for it to grow"), ("d", "Go to sleep")], "a"),
    ],
}
