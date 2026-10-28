"""Colour Science and Colour Spaces: how eyes see colour, how colour is described with numbers, and why displays need calibration."""
CODE = 'computing5_colour_science'
BOOK = {
    "title": 'Colour Science and Colour Spaces',
    "subtitle": 'How we see colour, how it is measured, and why screens differ',
    "chapters": [
        ('How human eyes see colour',
         "The eye has three kinds of cone cells, each most sensitive to a different range of wavelengths. Colour is the brain's reading of their combined responses. Many different light mixtures can look exactly the same."),
        ('CIE colour spaces',
         'The CIE created standard colour spaces in 1931, based on measurements of human observers. They describe colour with numbers that are independent of any particular device. Other spaces are defined relative to these standards.'),
        ('Gamma',
         "Screens and cameras encode brightness non-linearly, which is called gamma. This matches the eye's sensitivity and makes better use of the available values. Mixing or blurring colour values without accounting for gamma gives wrong results."),
        ('Wide gamut',
         'A colour gamut is the range of colours a device can show. Wide-gamut displays can show more intense greens and reds than older screens. Content must be mapped carefully between gamuts to avoid harsh clipping.'),
        ('Colour management',
         "Colour management tags images with their colour space and converts them to the display's space. Without it, the same file can look different on different screens. Consistent workflows keep colours predictable from camera to print."),
        ('Display calibration',
         'Calibration measures a display and adjusts its settings so it matches a target. A calibrated screen shows colour more accurately over time. Ambient light and ageing panels can shift results, so calibration is repeated.'),
    ],
    "test": [
        ('How many kinds of cone cells does the human eye have?',
         [('a', 'Three'), ('b', 'One'), ('c', 'Seven'), ('d', 'Twelve')], 'a'),
        ('What did the CIE create in 1931?',
         [('a', 'The first colour television'), ('b', 'A printing press'), ('c', 'Standard colour spaces based on human observers'), ('d', 'A paint brand')], 'c'),
        ('What is gamma in this context?',
         [('a', 'A kind of screen cable'), ('b', 'The non-linear way brightness is encoded'), ('c', 'The colour of the sky'), ('d', 'A type of microphone')], 'b'),
        ('What is a colour gamut?',
         [('a', 'The weight of a printer'), ('b', 'The number of pixels in a photo'), ('c', 'The name of a camera'), ('d', 'The range of colours a device can show')], 'd'),
        ('What does colour management do?',
         [('a', "It converts images to the display's colour space using their tags"), ('b', 'It deletes all colour from an image'), ('c', 'It changes the time of day'), ('d', 'It sends colour by post')], 'a'),
    ],
}
