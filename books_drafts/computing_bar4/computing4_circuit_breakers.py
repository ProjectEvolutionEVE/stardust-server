"""Circuit Breakers and Bulkheads: stopping calls to failing services, the three states, isolating pools, fallbacks, tuning and testing."""
CODE = "computing4_circuit_breakers"
BOOK = {
    "title": "Circuit Breakers and Bulkheads",
    "subtitle": "Stopping calls to a failing service, and keeping one failure from spreading",
    "chapters": [
        ("Stopping calls to a failing service",
         "When a service keeps failing, every call to it wastes time and holds threads and connections. The failure can then spread to the callers. A circuit breaker watches the calls, and stops sending them when failures pile up."),
        ("Three states",
         "A closed breaker lets calls flow normally. An open breaker fails calls at once, without sending them. A half-open breaker lets a few trial calls through, to see whether the service has recovered. If the trials succeed, the breaker closes again."),
        ("Isolating pools",
         "A bulkhead gives each dependency its own pool of threads or connections, much like the watertight compartments of a ship. A slow service then cannot use up the resources needed for all the others."),
        ("Fallback responses",
         "When a breaker is open, the caller can return a fallback. This might be a cached value, a sensible default, or a message asking the user to try again later. A good fallback keeps the page useful without the failing part."),
        ("Tuning thresholds",
         "A breaker needs a rule for tripping, such as a failure rate over a short window. It also needs a wait before the half-open trial and a number of trial calls. Settings that are too sensitive trip on ordinary blips. Settings that are too loose react too late."),
        ("Testing the breaker",
         "Test that the breaker opens under failure, stays open for its wait time, and closes again after the trial calls succeed. Injecting faults in a test environment shows whether the fallbacks really work when they are needed."),
    ],
    "test": [
        ("What does a circuit breaker do when it is open?",
         [("a", "Sends every call twice"), ("b", "Logs the user out"), ("c", "Opens the hold"), ("d", "Fails calls at once without sending them")], "d"),
        ("What is the half-open state for?",
         [("a", "Permanent shutdown"), ("b", "Doubling the traffic"), ("c", "Storing backups"), ("d", "Trying a few calls to see if the service has recovered")], "d"),
        ("What is a bulkhead?",
         [("a", "A separate pool of resources for each dependency"), ("b", "A kind of firewall rule"), ("c", "A type of database"), ("d", "A user login screen")], "a"),
        ("Why is a fallback useful?",
         [("a", "It hides all errors forever"), ("b", "It makes calls slower"), ("c", "It deletes the cache"), ("d", "It keeps the page useful without the failing part")], "d"),
        ("What happens if the thresholds are too sensitive?",
         [("a", "It never trips"), ("b", "It makes the service faster"), ("c", "It trips on ordinary blips"), ("d", "It removes the fallbacks")], "c"),
    ],
}
