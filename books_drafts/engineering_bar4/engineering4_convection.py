"""Convection Correlations: Nusselt and Reynolds, and how engineers read a heat transfer table."""
CODE = "engineering4_convection"
BOOK = {
    "title": "Convection Correlations: Nusselt and Reynolds",
    "subtitle": "Dimensionless numbers, correlations and their range of use",
    "chapters": [
        ("Heat carried by moving fluid",
         "Convection moves heat when a fluid flows past a surface. Forced convection uses a fan or a pump. Natural convection needs no pump: warm fluid is lighter, so it rises, and cooler fluid sinks to take its place."),
        ("Dimensionless numbers",
         "Engineers group measurements into numbers that have no units. The Reynolds number compares inertia with viscous forces, and it tells whether a flow is smooth or turbulent. The Nusselt number compares convective heat transfer with conduction through the fluid."),
        ("Correlations",
         "A correlation is a formula fitted to test data. It links the Nusselt number to the Reynolds and Prandtl numbers. A good correlation saves building a new test for every design."),
        ("Range of use",
         "Each correlation holds only over a stated range of Reynolds numbers, fluids and shapes. Used outside that range, it can give a neat answer that is wrong."),
        ("Laminar and turbulent flow",
         "Smooth laminar flow carries heat less well near a wall than turbulent flow does. Turbulence mixes the fluid and thins the layer that resists heat flow. Flow in a pipe usually turns turbulent above a Reynolds number of about 2300."),
        ("Reading a heat transfer table",
         "A table lists values for common shapes and flows. Check the units and the conditions in the heading before you use a value. Interpolate between rows only where the table allows it."),
    ],
    "test": [
        ("What does the Reynolds number compare?",
         [("a", "Heat and mass"), ("b", "Inertial forces and viscous forces"), ("c", "Pressure and temperature"), ("d", "Length and width")], "b"),
        ("What drives natural convection?",
         [("a", "A pump"), ("b", "A fan"), ("c", "Density differences caused by warming"), ("d", "Radiation")], "c"),
        ("What does a correlation give you?",
         [("a", "An exact answer for every shape"), ("b", "A formula fitted to tests and valid over a stated range"), ("c", "The colour of the heat"), ("d", "A cost estimate")], "b"),
        ("Flow in a pipe usually turns turbulent at a Reynolds number of about what?",
         [("a", "20"), ("b", "2300"), ("c", "2 million"), ("d", "0.2")], "b"),
        ("Why must you check a table's units and conditions before using a value?",
         [("a", "Tables never change"), ("b", "Units are optional"), ("c", "Tables are estimates from the weather"), ("d", "The values hold only for the stated conditions")], "d"),
    ],
}
