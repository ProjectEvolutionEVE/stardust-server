"""Service Credits and SLA Penalties: how service-level promises are measured, credited and disputed, and what they cost the provider."""
CODE = "computing5_sla_credits"
BOOK = {
    "title": "Service Credits and SLA Penalties",
    "subtitle": "How service promises are measured, credited and disputed",
    "chapters": [
        ("Credit schedules",
         "A credit schedule sets how much a customer is credited for each level of missed service. The bigger the miss, the bigger the credit. The schedule should be simple enough to check."),
        ("Measuring uptime",
         "Uptime is the share of time a service is available. It is measured over a stated period, with clear rules for what counts as down. Define the measurement method in the contract."),
        ("Disputes",
         "Customers and providers may disagree about whether an outage counts. Clear measurement data and a defined process for disputes settle most cases. Keep logs of every incident."),
        ("Contractual exposure",
         "Each promise is a potential cost. Credits and penalties add up when many customers are affected at once. Count the total exposure, not just one customer's credit."),
        ("Pricing risk",
         "Strict promises raise the price of the service because the provider must hold spare capacity and staff. Set promises the business can really keep. Price the risk of breaking them."),
        ("Reporting",
         "Report uptime and credits openly to customers, with the method stated. Regular reports build trust and show where improvements are needed."),
    ],
    "test": [
        ("What does a credit schedule set?",
         [("a", "The office opening hours"), ("b", "How much a customer is credited for each level of missed service"), ("c", "The price of paper"), ("d", "The staff holiday rota")], "b"),
        ("What is uptime?",
         [("a", "The time a server is turned off"), ("b", "The length of a lunch break"), ("c", "The number of users in a room"), ("d", "The share of time a service is available")], "d"),
        ("What helps settle disputes about outages?",
         [("a", "Clear measurement data and a defined process"), ("b", "Guessing"), ("c", "Ignoring the customer"), ("d", "Deleting the logs")], "a"),
        ("Why does total exposure matter?",
         [("a", "Exposure is only a weather term"), ("b", "Exposure never costs money"), ("c", "Credits add up when many customers are affected at once"), ("d", "Exposure only matters to lawyers' dogs")], "c"),
        ("Why can strict service promises raise prices?",
         [("a", "Strict promises are free to keep"), ("b", "The provider must hold spare capacity and staff to keep them"), ("c", "Prices never depend on promises"), ("d", "Strict promises remove all costs")], "b"),
    ],
}
