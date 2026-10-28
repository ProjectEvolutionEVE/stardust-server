"""Reinforcement learning: agents and rewards, Markov decision processes, Q-learning, policy gradients, exploration and reward design."""
CODE = 'computing5_reinforcement_learning'
BOOK = {
    "title": 'Reinforcement Learning',
    "subtitle": 'Learning by trial, error and reward, step by step',
    "chapters": [
        ('Agent and reward',
         'In reinforcement learning, an agent acts in an environment and receives a reward signal. It learns which actions lead to more reward over time.'),
        ('Markov decision processes',
         'The problem is often written as a Markov decision process: states, actions, the chance of each next state, and rewards. The next state depends only on the current state and the action taken.'),
        ('Q-learning',
         'Q-learning, described in 1989, keeps a value for each state and action, the expected total reward. It updates these values as the agent gains experience.'),
        ('Policy gradients',
         'Policy gradient methods learn the action choices directly, nudging up the chance of actions that led to good rewards. They suit large or continuous action spaces.'),
        ('Exploration',
         'An agent must try new actions to learn, but also use what it already knows. Methods such as epsilon-greedy sometimes pick a random action.'),
        ('Reward design',
         'An agent will find any loophole in the reward and exploit it, a problem called reward hacking. Designing a reward that truly matches the goal is one of the hardest parts.'),
    ],
    "test": [
        ('What does an agent receive from the environment?',
         [('a', 'A reward signal'), ('b', 'A new car'), ('c', 'A birthday card'), ('d', 'A password')], 'a'),
        ('What are the parts of a Markov decision process?',
         [('a', 'Colours and sounds'), ('b', 'Users and printers'), ('c', 'Pages and chapters'), ('d', 'States, actions, next-state chances and rewards')], 'd'),
        ('What does Q-learning keep for each state and action?',
         [('a', 'A photo'), ('b', 'An expected total reward'), ('c', 'A sound'), ('d', 'A password')], 'b'),
        ('What does epsilon-greedy do?',
         [('a', 'Always picks the first action'), ('b', 'Deletes the reward'), ('c', 'Sometimes picks a random action to explore'), ('d', 'Stops learning')], 'c'),
        ('What is reward hacking?',
         [('a', 'Hacking a password'), ('b', 'Painting the reward'), ('c', 'Stealing a laptop'), ('d', 'Exploiting a loophole in the reward')], 'd'),
    ],
}
