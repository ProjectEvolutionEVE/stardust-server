"""Feature Stores: shared, reusable inputs for machine learning, kept consistent between training and live use."""
CODE = 'computing5_feature_stores'
BOOK = {
    "title": 'Feature Stores',
    "subtitle": 'Shared model inputs, kept the same for training and live use',
    "chapters": [
        ('What a feature is',
         'A feature is a measured input to a model, such as the number of purchases in the last week. Many teams compute the same features again and again for different models. A feature store is a shared place to define, store and serve them.'),
        ('Offline and online copies',
         'Training uses an offline store of past feature values, often large and kept in batches. Live predictions use an online store that answers quickly for one customer or item at a time. Both copies must come from the same definition.'),
        ('Point-in-time correctness',
         'When building training data, each feature must hold the value that was known at the time of each example. Using a later value leaks the future into the model. Point-in-time joins are the standard way to avoid this mistake.'),
        ('Feature reuse',
         'Once a feature is defined well, other teams can use it without rebuilding it. This saves effort and keeps the meaning of a feature consistent across projects. Naming, ownership and documentation make reuse practical.'),
        ('Freshness',
         'Some features must be updated within seconds, while others can be a day old. Freshness is a trade-off between cost, complexity and how quickly the world changes. Each feature should state how fresh it promises to be.'),
        ('Costs',
         'Storing and serving features costs money, especially for online lookups at high volume. Teams remove features that no model uses and monitor their computing bills. A smaller, well-kept set of features is often better than a large, neglected one.'),
    ],
    "test": [
        ('What is a feature in a machine learning system?',
         [('a', 'A type of computer screen'), ('b', 'A measured input to a model'), ('c', "A user's favourite colour"), ('d', 'A way to pay for servers')], 'b'),
        ('What is the online store used for?',
         [('a', 'Printing training reports'), ('b', 'Storing old emails'), ('c', 'Recording the weather'), ('d', 'Quick lookups for live predictions')], 'd'),
        ('What does point-in-time correctness prevent?',
         [('a', 'Leaking future values into training examples'), ('b', 'Slow screens'), ('c', 'Broken keyboards'), ('d', 'Duplicate passwords')], 'a'),
        ('What is one benefit of feature reuse?',
         [('a', 'Features never need documentation'), ('b', 'Models stop needing any data'), ('c', 'Teams avoid rebuilding the same feature and keep its meaning consistent'), ('d', 'Every feature becomes the same')], 'c'),
        ('Why does a feature need a stated freshness?',
         [('a', 'Freshness changes the font of the report'), ('b', 'Old features are always illegal'), ('c', 'Freshness sets the number of users'), ('d', 'Freshness is a trade-off between cost and how fast the world changes')], 'd'),
    ],
}
