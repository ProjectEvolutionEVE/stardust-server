"""Required Time of Arrival: Arriving at the right moment, not just the right place."""
CODE = 'navigation5_rta'
BOOK = {
    'title': 'Required Time of Arrival',
    'subtitle': 'Arriving at the right moment, not just the right place',
    'chapters': [
        ('Arriving on time', 'Required Time of Arrival gives an aircraft a time to pass a set point. The aircraft then adjusts its speed to meet that time within a small margin.'),
        ('Speed control', 'Within a tight range, the flight system changes speed. Flying a little slower or faster is often cheaper than holding or making a late, sharp change.'),
        ('Metering', 'Air traffic can be spaced out by arrival times at a point. This is called metering, and it keeps a busy airport flowing smoothly.'),
        ('Fuel and cost', 'Flying slower can save fuel, while flying faster costs more. Timed arrivals help balance these trade-offs for each flight.'),
        ('Schedules', 'Airlines and airports use the planned times to keep schedules steady. Predictable arrivals reduce waiting and queues.'),
        ('The benefits', 'When many aircraft meet their times, airports use their runways better and passengers wait less. The system works best when everyone agrees on the timing.'),
    ],
    'test': [
        ('What does RTA give an aircraft?', [('a', 'A new paint scheme'), ('b', 'A new pilot'), ('c', 'A time to pass a set point'), ('d', 'A sea route')], 'c'),
        ('What is metering?', [('a', 'Measuring rainfall'), ('b', 'Counting seats'), ('c', 'Painting runways'), ('d', 'Spacing aircraft out by arrival times at a point')], 'd'),
        ('Flying a little slower often:', [('a', 'Saves fuel'), ('b', 'Costs more fuel'), ('c', 'Causes the ground to move'), ('d', 'Stops the engine')], 'a'),
        ('Why do timed arrivals help airports?', [('a', 'Predictable arrivals reduce waiting and queues'), ('b', 'They remove runways'), ('c', 'They stop flights'), ('d', 'They change the weather')], 'a'),
        ('When does the system work best?', [('a', 'When no one follows the plan'), ('b', 'When everyone agrees on the timing'), ('c', 'When it is night only'), ('d', 'When aircraft are not counted')], 'b'),
    ],
}
