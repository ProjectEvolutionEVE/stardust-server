"""Hydrogeology of Mine Sites: how groundwater moves through aquifers into pits and tunnels, and how pumping tests and monitoring keep it under control."""
CODE = "mining5_hydrogeol"
BOOK = {
    "title": "Hydrogeology of Mine Sites",
    "subtitle": "Aquifers, inflows, pumping tests, recharge and dewatering",
    "chapters": [
        ("Water under the ground",
         "Groundwater fills the spaces in rock and soil. An aquifer is a layer that holds and carries enough water to be used. Mines cut through aquifers and must manage the water they meet."),
        ("Aquifers and inflows",
         "Water flows into a pit or tunnel from the aquifers around it. The inflow rate depends on how permeable the rock is and how deep the excavation goes. Estimating inflows early helps with pump and drainage design."),
        ("Pumping tests",
         "A pumping test pumps water from a well and measures how the water level falls in nearby wells. The fall tells engineers how easily water moves through the aquifer. These tests give the key numbers for models."),
        ("Recharge",
         "Recharge is water that soaks down from rain and rivers into the aquifer. The amount of recharge controls how much water a mine must remove over time. Seasonal changes in recharge matter for planning."),
        ("Dewatering wells",
         "Dewatering wells are drilled around a pit to lower the water table. Lower water makes the pit walls safer and the mining easier. The wells are run to a plan, and their pumping rates are recorded."),
        ("Monitoring",
         "Monitoring wells measure water levels and quality over time. They show whether the dewatering is working and whether nearby water is being affected. Regular records give early warning of change."),
    ],
    "test": [
        ("What is an aquifer?",
         [("a", "A layer that holds and carries enough water to be used"), ("b", "A type of air vent"), ("c", "A kind of drill bit"), ("d", "A road sign")], "a"),
        ("What controls how fast water flows into a pit?",
         [("a", "How permeable the rock is and how deep the excavation goes"), ("b", "The colour of the pit wall"), ("c", "The time of the lunch break"), ("d", "The name of the mine")], "a"),
        ("What does a pumping test measure?",
         [("a", "The loudness of the pump"), ("b", "The weight of the drill crew"), ("c", "How the water level falls in nearby wells"), ("d", "The colour of the sky")], "c"),
        ("What is recharge?",
         [("a", "Charging a battery in a truck"), ("b", "Refilling a coffee cup"), ("c", "Adding sand to a pit"), ("d", "Water that soaks down from rain and rivers into the aquifer")], "d"),
        ("Why are monitoring wells used?",
         [("a", "To store the ore"), ("b", "To track water levels and quality over time"), ("c", "To cool the office"), ("d", "To hold the trucks")], "b"),
    ],
}
