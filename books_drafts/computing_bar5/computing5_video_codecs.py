"""Video Codecs in Depth: how video is squeezed by predicting motion, transforming blocks and choosing how much detail to keep."""
CODE = 'computing5_video_codecs'
BOOK = {
    "title": 'Video Codecs in Depth',
    "subtitle": 'Predicting motion, transforming blocks, and deciding what to keep',
    "chapters": [
        ('Why video needs compression',
         'Uncompressed video is far too large to stream or store easily. A codec, short for coder and decoder, reduces the data while keeping the picture pleasing. Most of the saving comes from the fact that frames are very similar to each other.'),
        ('Motion estimation',
         'The encoder looks for blocks in an earlier frame that match blocks in the current frame. It records the motion vector that links them. Only the small difference is then stored, which saves a great deal of data.'),
        ('Transform coding',
         'Blocks of pixel differences are converted into frequency components, most often with a discrete cosine transform. Most of the energy ends up in a few low-frequency values. The rest can be stored coarsely or dropped.'),
        ('Quantisation and rate control',
         'Quantisation rounds the frequency values to fewer levels, and this is where most information is lost. Rate control sets how much quantisation to use so the output fits a target bitrate. Tighter control gives steadier quality.'),
        ('Hardware decoding',
         'Dedicated decoding hardware plays video with little power and no heavy load on the main processor. Phones and TVs rely on it for long battery life. Support depends on the codec and the device.'),
        ('Choosing a codec',
         'A codec is chosen for quality per bit, device support, licensing and encoding cost. Newer codecs often compress better but need more computing to encode. Practical choices balance all of these together.'),
    ],
    "test": [
        ('What is a codec?',
         [('a', 'A type of camera battery'), ('b', 'A coder and decoder pair that reduces video data'), ('c', 'A brand of television'), ('d', 'A style of subtitle')], 'b'),
        ('What is a motion vector?',
         [('a', 'A type of car engine'), ('b', 'A bar on a graph'), ('c', 'A way to sort names'), ('d', 'A record of where a block of an earlier frame moved to')], 'd'),
        ('What does a discrete cosine transform do to a block?',
         [('a', 'It converts it into frequency components'), ('b', 'It paints it red'), ('c', 'It deletes its edges'), ('d', 'It moves it to the cloud')], 'a'),
        ('Where is most information lost in a video codec?',
         [('a', 'In the file name'), ('b', 'In the audio volume knob'), ('c', 'In quantisation, when values are rounded'), ('d', 'In the cable length')], 'c'),
        ('What is the benefit of hardware decoding?',
         [('a', 'Making the video print on paper'), ('b', 'Removing the need for a screen'), ('c', 'Turning video into text'), ('d', 'Playing video with little power and little load on the main processor')], 'd'),
    ],
}
