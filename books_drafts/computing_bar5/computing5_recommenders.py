"""Recommender systems: collaborative filtering, matrix factorisation, content features, cold start, evaluation and feedback loops."""
CODE = 'computing5_recommenders'
BOOK = {
    "title": 'Recommender Systems',
    "subtitle": 'How services guess what you might like next',
    "chapters": [
        ('Liking patterns',
         'Collaborative filtering recommends items that people with similar tastes enjoyed. It uses patterns in who liked what, not the content of the items.'),
        ('Matrix factorisation',
         'Matrix factorisation breaks a big table of users and items into smaller sets of hidden factors. It was widely studied during the Netflix Prize contest of 2006 to 2009.'),
        ('Content features',
         'Content-based recommenders use the features of each item, such as genre or ingredients. They work for new items, where patterns of use are not yet known.'),
        ('The cold-start problem',
         'A new user or new item has little history, so the system knows little about it. Teams use questions, popular items or content features to start.'),
        ('Evaluation',
         'Recommenders are tested offline on held-out data and then online with controlled experiments. Live tests show whether people actually engage more.'),
        ('Feedback loops',
         'A system that recommends only what is already popular can narrow choices and reinforce itself. Good designs add variety and let users steer.'),
    ],
    "test": [
        ('What does collaborative filtering use?',
         [('a', 'Patterns in who liked what'), ('b', 'The weather in the city'), ('c', "The user's shoe size"), ('d', 'The price of paper')], 'a'),
        ('What did the Netflix Prize contest concern?',
         [('a', 'Designing cinemas'), ('b', 'Improving a recommendation system'), ('c', 'Printing posters'), ('d', 'Selling popcorn')], 'b'),
        ('What does content-based recommending use?',
         [('a', 'Features of each item, such as genre'), ('b', "Only the user's name"), ('c', 'Only the time of day'), ('d', 'Only the printer')], 'a'),
        ('What is the cold-start problem?',
         [('a', 'Servers that are too cold'), ('b', 'A frozen screen'), ('c', 'Winter sales'), ('d', 'Little history for a new user or item')], 'd'),
        ('What is a feedback loop risk?',
         [('a', 'Making the screen brighter'), ('b', 'Turning off the network'), ('c', 'Narrowing choices by recommending only what is already popular'), ('d', 'Adding more colours')], 'c'),
    ],
}
