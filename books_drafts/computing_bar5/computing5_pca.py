"""Principal component analysis: directions of variance, eigenvectors, dimension reduction, reconstruction error and limits."""
CODE = 'computing5_pca'
BOOK = {
    "title": 'Principal Component Analysis',
    "subtitle": 'Finding the main directions of spread in data, and keeping only the important ones',
    "chapters": [
        ('Too many columns',
         'Real data often has many measurements per item. Principal component analysis, or PCA, finds a smaller set of directions that capture most of the spread.'),
        ('Directions of variance',
         'The first principal component points where the data varies most. The next one points in the direction of most remaining variation, at a right angle to the first.'),
        ('Eigenvectors',
         "The principal components are eigenvectors of the data's covariance matrix. Their eigenvalues show how much variance each one captures."),
        ('Reducing dimensions',
         'Projecting the data onto the top few components gives a compact version. Keeping only the most important directions often loses little information.'),
        ('Reconstruction error',
         'The difference between the original data and its rebuilt version from a few components is the reconstruction error. It shows what was lost.'),
        ('Limits',
         'PCA finds straight directions only, so curved structure can be missed. Scaling the features first matters, and kernel PCA or autoencoders can help with curves.'),
    ],
    "test": [
        ('What does PCA aim to do?',
         [('a', 'Find fewer directions that capture most of the spread'), ('b', 'Paint the data'), ('c', 'Delete all rows'), ('d', 'Count visitors')], 'a'),
        ('What does the first principal component point to?',
         [('a', 'The direction of least variation'), ('b', 'The top of the screen'), ('c', 'A random direction'), ('d', 'The direction of most variation')], 'd'),
        ('What are principal components mathematically?',
         [('a', 'Pictures of data'), ('b', 'Eigenvectors of the covariance matrix'), ('c', 'Passwords'), ('d', 'Printer settings')], 'b'),
        ('What is reconstruction error?',
         [('a', 'A spelling mistake'), ('b', 'A server crash'), ('c', 'What is lost when the data is rebuilt from few components'), ('d', 'A missing chart')], 'c'),
        ('What is a limit of PCA?',
         [('a', 'It works only on paper'), ('b', 'It needs no numbers'), ('c', 'It makes data bigger'), ('d', 'It finds straight directions and can miss curved structure')], 'd'),
    ],
}
