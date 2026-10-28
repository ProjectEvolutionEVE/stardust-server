"""Image Compression and the JPEG Pipeline: how a still picture is converted, transformed, rounded and packed into a smaller file."""
CODE = 'computing5_jpeg_pipeline'
BOOK = {
    "title": 'Image Compression and the JPEG Pipeline',
    "subtitle": 'Colour change, block transform, rounding and packing',
    "chapters": [
        ('Why images are compressed',
         'A raw photograph holds a large amount of data, and most of it is redundant. Compression removes redundancy and some detail the eye is unlikely to notice. JPEG is the most widely used format for photographs.'),
        ('Colour transforms',
         'The image is converted from red, green and blue into a brightness channel and two colour-difference channels. The eye is more sensitive to brightness than to colour detail. The colour channels can therefore be stored at a lower resolution.'),
        ('The discrete cosine transform',
         'The picture is cut into blocks of eight by eight pixels. Each block is converted with a discrete cosine transform into frequency components. Smooth areas leave most of their energy in a few values.'),
        ('Quantisation tables',
         'Each frequency value is divided by a number from a quantisation table and rounded. Higher frequencies usually get larger divisors, so fine detail is lost first. The table is the main setting that controls quality.'),
        ('Entropy coding',
         'The rounded values are packed with an entropy coder, such as Huffman coding, which gives shorter codes to common values. This step is lossless, so it does not change the picture further. It saves the final amount of space.'),
        ('Artefacts and newer formats',
         'Heavy compression causes artefacts, such as blocky patches and blurred edges around sharp lines. Newer formats use more advanced transforms and prediction to do better at the same quality. The choice depends on quality, speed and support in software.'),
    ],
    "test": [
        ('Why does JPEG change the colour channels?',
         [('a', 'Colour cannot be stored'), ('b', 'The eye is less sensitive to colour detail than to brightness'), ('c', 'Brightness is always zero'), ('d', 'Colour makes files larger only in print')], 'b'),
        ('What size are the blocks in a JPEG transform?',
         [('a', 'One by one pixel'), ('b', 'Ten by ten thousand pixels'), ('c', 'Two hundred by two hundred pixels'), ('d', 'Eight by eight pixels')], 'd'),
        ('What does a quantisation table control?',
         [('a', 'The main trade-off of quality against file size'), ('b', 'The name of the photographer'), ('c', 'The font of the caption'), ('d', 'The shape of the frame')], 'a'),
        ('Which step in JPEG is lossless?',
         [('a', 'Quantisation'), ('b', 'Colour rounding'), ('c', 'Entropy coding'), ('d', 'Cutting into blocks of pixels')], 'c'),
        ('What are blocky patches a sign of?',
         [('a', 'A very good camera'), ('b', 'A missing battery'), ('c', 'A fast internet connection'), ('d', 'Heavy compression')], 'd'),
    ],
}
