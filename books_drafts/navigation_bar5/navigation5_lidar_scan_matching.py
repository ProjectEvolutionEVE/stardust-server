"""LiDAR Scan Matching: lining up laser scans taken at different places so they form one map."""
CODE = 'navigation5_lidar_scan_matching'
BOOK = {
    "title": 'LiDAR Scan Matching',
    "subtitle": 'Point clouds, iterative closest point, registration, drift, maps and speed',
    "chapters": [
        ('Point clouds',
         'A laser scanner measures many distances in every direction. Together these form a point cloud, a set of 3D points that outline the surroundings. Each new scan gives another cloud.'),
        ('Iterative closest point',
         'Iterative closest point pairs each point in one scan with the nearest point in another. It then moves one scan to reduce the gaps, and repeats the steps. The process stops when the scans fit well.'),
        ('Registration',
         'Registration is the job of lining up two scans so that they match. Once they are registered, the vehicle\'s motion between them is known. Registration is the core of scan matching.'),
        ('Drift',
         'Each match has a small error. When many scans are chained together, these errors build up. The path and the map gradually drift from the truth.'),
        ('Maps',
         'Registered scans are combined into a map of the surroundings. The map can be used to find the vehicle later. Loop closure can correct the map when the vehicle returns to a known place.'),
        ('Speed',
         'The matching must run fast enough to keep up with the scanner. Subsampling the points and starting from a good guess both help. Speed is a key limit in real vehicles.'),
    ],
    "test": [
        ('What is a point cloud?',
         [('a', 'A cloud of steam'), ('b', 'A weather map'), ('c', 'A set of 3D points measured by a laser scanner'), ('d', 'A shop display')], 'c'),
        ('What is iterative closest point?',
         [('a', 'A race'), ('b', 'A closing time'), ('c', 'A shop rule'), ('d', 'A method that repeatedly pairs points and moves one scan to fit the other')], 'd'),
        ('What is registration?',
         [('a', 'Lining up two scans so they match'), ('b', 'Signing a form'), ('c', 'Counting cars'), ('d', 'Painting a map')], 'a'),
        ('Why does drift happen?',
         [('a', 'It never happens'), ('b', 'Small errors build up as scans are chained together'), ('c', 'Lasers get hotter'), ('d', 'Maps shrink')], 'b'),
        ('Why does speed matter in scan matching?',
         [('a', 'To make scans blurry'), ('b', 'To change colour'), ('c', 'A vehicle needs answers quickly as it moves'), ('d', 'To play music')], 'c'),
    ],
}
