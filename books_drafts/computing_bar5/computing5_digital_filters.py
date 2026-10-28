"""Digital Filters: how a stream of numbers is reshaped by weighted sums, and how poles and zeros show what a filter does."""
CODE = 'computing5_digital_filters'
BOOK = {
    "title": 'Digital Filters',
    "subtitle": 'Reshaping a stream of numbers, and what that costs',
    "chapters": [
        ('What a filter does',
         'A digital filter takes a stream of input numbers and produces a new stream that is changed in a chosen way. Lowpass filters keep bass and remove hiss, for example. Filters appear in audio, images, sensors and radio.'),
        ('Impulse response',
         'The impulse response is what a filter outputs when it receives a single sharp spike. Knowing this response fully describes a linear filter. It is the starting point for analysing any filter.'),
        ('FIR and IIR filters',
         'A finite impulse response filter, or FIR, uses only a fixed set of input values and is always stable. An infinite impulse response filter, or IIR, feeds its output back in. IIR filters are efficient but can become unstable if designed badly.'),
        ('Poles, zeros and frequency response',
         "Poles and zeros are points in a complex plane that describe a filter's behaviour. Poles close to the edge of the unit circle create strong peaks. The frequency response shows how much each frequency is boosted or cut."),
        ('Design tools',
         'Designers use software to place poles and zeros and to check the frequency response. Design tools also check stability and how the filter behaves with real rounding. Testing with real signals catches problems that theory can miss.'),
        ('Latency',
         'A filter takes time to respond, which is called latency. FIR filters with long responses can add noticeable delay. Real-time work, such as live audio, needs filters that balance sharpness against delay.'),
    ],
    "test": [
        ('What does a digital filter do to a stream of numbers?',
         [('a', 'It deletes every second number'), ('b', 'It turns numbers into words'), ('c', 'It reshapes the stream in a chosen way'), ('d', 'It stores the numbers on paper')], 'c'),
        ('What is an impulse response?',
         [('a', 'The output a filter gives when it receives a single sharp spike'), ('b', 'The sound of a car horn'), ('c', 'A heart rate reading'), ('d', 'The time a filter takes to install')], 'a'),
        ('Which kind of filter is always stable?',
         [('a', 'Any IIR filter with feedback'), ('b', 'A filter with no design'), ('c', 'A filter that grows over time'), ('d', 'The FIR filter')], 'd'),
        ('What do poles near the edge of the unit circle create?',
         [('a', 'Silence in every frequency'), ('b', 'Strong peaks in the frequency response'), ('c', 'A new colour for the screen'), ('d', 'A broken file name')], 'b'),
        ('What is latency in a filter?',
         [('a', 'The volume of the output'), ('b', 'The number of inputs it has'), ('c', 'The delay before the filter responds'), ('d', "The cost of the filter's box")], 'c'),
    ],
}
