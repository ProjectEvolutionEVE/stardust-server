"""Load Balancers: how incoming work is shared fairly across several servers."""
CODE = "computing3c_load_balancers"
BOOK = {
    "title": "Load Balancers",
    "subtitle": "How incoming work is shared fairly across several servers",
    "chapters": [
        ("One door, many servers",
         "When several servers run the same program, something must decide which one takes each request. A load balancer stands at the front and makes that choice. Users see one address, and the work is shared out behind it."),
        ("Ways to share the work",
         "A simple method is round robin, which sends each new request to the next server in turn. Another is to send new work to the server with the fewest active requests. Each method suits a different kind of work."),
        ("Checking health",
         "A load balancer checks that each server is still answering. A server that fails the check is taken out of rotation until it recovers. This keeps users away from a broken machine."),
        ("Sessions and memory",
         "If a server remembers something about a user, the next request must reach that same server, or the memory must be shared. Keeping that memory somewhere every server can reach is often simpler and safer."),
        ("The balancer can fail too",
         "A single load balancer is a single point of failure, because if it stops, everything behind it is cut off. Real setups run two or more, with a switch-over if one stops. That adds cost, so it is a choice to weigh."),
        ("A money view",
         "Several smaller servers behind a balancer can cost less than one huge machine, and they can be added one at a time. The balancer itself has a price too. Compare the two before you buy."),
    ],
    "test": [
        ("What is a load balancer's job?",
         [("a", "Painting the servers"), ("b", "Storing all the money"), ("c", "Sharing incoming work across several servers"), ("d", "Playing sound")], "c"),
        ("What is round robin?",
         [("a", "Sending each new request to the next server in turn"), ("b", "A kind of ring"), ("c", "Turning off all the servers"), ("d", "Sending every request to one server only")], "a"),
        ("What does a health check do?",
         [("a", "Charges the users"), ("b", "Checks that each server still answers, and removes one that fails"), ("c", "Deletes the logs"), ("d", "Checks the weather")], "b"),
        ("Why can remembered user state cause trouble behind a balancer?",
         [("a", "Because servers cannot count to ten"), ("b", "Because memory is free"), ("c", "Because users never come back"), ("d", "Because a later request may reach a different server that does not have it")], "d"),
        ("Why is a single load balancer a risk?",
         [("a", "It is a single point of failure: if it stops, the system stops"), ("b", "It makes every server faster"), ("c", "It has no cost at all"), ("d", "It replaces the users")], "a"),
    ],
}
