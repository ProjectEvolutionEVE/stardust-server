"""Route Choice Models: how travellers choose between routes, and how models of choice use travel times and costs."""
CODE = 'navigation5_route_choice'
BOOK = {
    "title": 'Route Choice Models',
    "subtitle": 'Choice sets, utility, travel times, logit models, data and uses',
    "chapters": [
        ('Choosing a way',
         'Every trip has more than one possible route. Travellers weigh time, cost, comfort and safety, often without thinking about it. Route choice models try to describe these decisions in a clear way.'),
        ('Choice sets',
         'A choice set is the list of routes a traveller is likely to consider. Models must decide which routes belong in the set, because a route nobody considers should not be counted.'),
        ('Utility',
         'Utility is a measure of how attractive a route is to a traveller. It is built from the features of the route, such as time and cost. Higher utility means a route is more likely to be chosen.'),
        ('Travel times',
         'Travel time is one of the most important features. It changes with traffic, weather and time of day. Models use measured times to estimate how choices change at busy times.'),
        ('Logit models',
         'Logit models turn utilities into probabilities. Each route gets a chance of being chosen, and the chances add up to one. This gives a simple and widely used way to predict choices.'),
        ('Data and uses',
         'Route choice data come from surveys, traffic counts and GPS traces. Models help planners decide where to build roads and how to set tolls. Their results are only as good as the data used.'),
    ],
    "test": [
        ('What is a choice set?',
         [('a', 'A set of dishes'), ('b', 'A box of tools'), ('c', 'A group of sailors'), ('d', 'The list of routes a traveller is likely to consider')], 'd'),
        ('What does utility measure in a route model?',
         [('a', 'The width of the road'), ('b', 'How attractive a route is to a traveller'), ('c', 'The number of trees beside it'), ('d', 'The colour of the signs')], 'b'),
        ('What do logit models turn utilities into?',
         [('a', 'Probabilities that add up to one'), ('b', 'Pictures of roads'), ('c', 'Songs'), ('d', 'Weights of cars')], 'a'),
        ('Why do travel times in a model change?',
         [('a', 'Because clocks are painted'), ('b', 'Because roads never change'), ('c', 'Because traffic, weather and time of day change them'), ('d', 'Because maps have colours')], 'c'),
        ('What are route choice models used for?',
         [('a', 'Helping planners decide on roads and tolls'), ('b', 'Choosing the colour of cars'), ('c', 'Writing poetry'), ('d', 'Growing crops')], 'a'),
    ],
}
