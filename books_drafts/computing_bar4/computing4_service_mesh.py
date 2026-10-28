"""Service Meshes and Sidecars: proxies beside each service, traffic policy, mutual identity, proxy telemetry, the cost of extra hops, and adoption choices."""
CODE = "computing4_service_mesh"
BOOK = {
    "title": "Service Meshes and Sidecars",
    "subtitle": "Proxies beside each service, and what they cost",
    "chapters": [
        ("Proxies beside each service",
         "A service mesh places a small proxy beside each service. This proxy is called a sidecar. Traffic to and from the service passes through it, so the application code need not handle every network detail itself."),
        ("Traffic policy",
         "The mesh can set rules for retries, timeouts, and which version of a service receives traffic. Teams can change these rules in one place, without redeploying every service."),
        ("Mutual identity",
         "Proxies can prove each service's identity with certificates, and they can encrypt traffic between services. Each side checks who it is talking to before it trusts the other."),
        ("Telemetry from proxies",
         "Because all traffic passes through the proxies, they can report request counts, errors and delays for every call. This gives consistent measurements without changing the application code."),
        ("Cost and latency of extra hops",
         "Each call now passes through two proxies. This adds a little delay, and each service instance needs extra processor time and memory for its sidecar. Across many services, these costs add up."),
        ("Adoption choices",
         "A mesh adds real complexity. Teams should start with a clear need, such as mutual encryption or consistent measurements, and adopt the mesh gradually. They also need the skills to run it well."),
    ],
    "test": [
        ("What is a sidecar?",
         [("a", "A proxy placed beside each service"), ("b", "A type of hard drive"), ("c", "A car part"), ("d", "A user interface panel")], "a"),
        ("What can a mesh change through traffic policy?",
         [("a", "Print invoices"), ("b", "Rename files"), ("c", "Set retries and timeouts without redeploying each service"), ("d", "Change player names")], "c"),
        ("What does mutual identity mean?",
         [("a", "Two people share a password"), ("b", "All services share one account"), ("c", "Each service proves its identity to the other"), ("d", "Users vote on identity")], "c"),
        ("Why does a mesh add cost?",
         [("a", "It removes all servers"), ("b", "It stops encryption"), ("c", "It deletes logs"), ("d", "Each call passes through extra proxies, adding delay and resource use")], "d"),
        ("How should a team adopt a mesh?",
         [("a", "Start with a clear need and adopt gradually"), ("b", "All at once, without planning"), ("c", "Never adopt it"), ("d", "Only on phones")], "a"),
    ],
}
