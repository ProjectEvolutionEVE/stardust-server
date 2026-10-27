"""The Fast Fourier Transform: frequency views of signals, the divide-and-conquer FFT, convolution and polynomial multiplication."""
CODE = 'computing5_fft'
BOOK = {'title': 'The Fast Fourier Transform',
 'subtitle': 'Seeing a signal by its frequencies, quickly',
 'chapters': [('Frequency views of signals',
               'A signal can be described by how it changes over time, or by which frequencies it contains. The Fourier transform converts between these two views. Music, radio '
               'and images all use frequency descriptions.'),
              ('The discrete Fourier transform',
               'The discrete Fourier transform takes n samples and returns n frequency values. Computed directly, it needs about n squared operations. This cost limited its use '
               'on large data for a long time.'),
              ('The divide-and-conquer FFT',
               'The fast Fourier transform splits the samples into even and odd parts, transforms each half, and combines the results. This brings the work down to about n log n '
               'operations. Cooley and Tukey published the widely used form in 1965.'),
              ('Convolution',
               'Convolution combines two signals, for example to apply a filter to audio. Through the Fourier transform, a convolution becomes a simple multiplication of '
               'frequency values. This is why the FFT is central to filtering.'),
              ('Polynomial multiplication',
               'Multiplying two polynomials is the same as convolving their coefficient lists. Using the FFT, the product can be computed in about n log n time. This makes large '
               'multiplications practical in computer algebra and cryptography.'),
              ('Audio and other uses',
               'Audio tools use the FFT to analyse pitch, remove noise and compress sound. Image processing and radar use it in similar ways. The FFT is one of the most widely '
               'used algorithms in engineering.')],
 'test': [('What does the Fourier transform change a signal into?',
           [('a', 'A map of a city'), ('b', 'A list of names'), ('c', 'A paragraph of text'), ('d', 'A description by frequencies')],
           'd'),
          ('About how many operations does the direct discrete Fourier transform need for n samples?',
           [('a', 'Exactly one'), ('b', 'About n squared'), ('c', 'About the square root of n'), ('d', 'Zero')],
           'b'),
          ('What does the fast Fourier transform bring the work down to?',
           [('a', 'About n log n operations'), ('b', 'About n cubed operations'), ('c', 'A fixed amount no matter the size'), ('d', 'Exactly twice n')],
           'a'),
          ('What does convolution become after the Fourier transform?',
           [('a', 'A deletion of samples'), ('b', 'A random shuffle'), ('c', 'A simple multiplication of frequency values'), ('d', 'A printed image')],
           'c'),
          ('Which of these uses the FFT?',
           [('a', 'Only writing letters by hand'), ('b', 'Audio analysis and noise removal'), ('c', 'Only sorting names'), ('d', 'Only printing receipts')],
           'b')]}
