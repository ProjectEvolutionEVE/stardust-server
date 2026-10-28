"""Basis Risk and Physical Premiums: the gap between a benchmark price and the price of real material."""
CODE = 'mining5_basis'
BOOK = {
    "title": 'Basis Risk and Physical Premiums',
    "subtitle": 'The gap between a benchmark price and the real material',
    "chapters": [
        ('Spot premiums', 'A benchmark price is a quoted price for a standard metal. Real material often sells above or below that benchmark, and the difference is a premium or discount. Premiums change with local supply and demand.'),
        ('Freight and location', 'Transport costs and distance affect what a buyer will pay in each place. A metal near a port may sell for more than the same metal inland. Freight is one reason the local price differs from the benchmark.'),
        ('Quality differences', 'Ore and metal vary in purity, size and impurities, and each grade can carry its own price. A buyer will pay more for a cleaner product. Quality rules are written into the contract.'),
        ('Hedge mismatch', 'A hedge is a futures position that tracks the benchmark. If the physical premium moves differently from the benchmark, the hedge does not fully protect the seller. This gap is the basis risk.'),
        ('Market data', 'Basis levels are reported by price services and brokers, often for each region and grade. Good data helps sellers see when a premium is unusually high or low. Old or thin data can mislead.'),
        ('Managing basis', 'Managing basis risk means choosing hedges that match the real material, setting contract terms that share the risk, and watching the premiums closely. Some sellers accept a small basis risk to keep the hedge simple. The choice should be deliberate.'),
    ],
    "test": [
        ('What is a benchmark price?', [('a', 'The price of a used bicycle'), ('b', 'The cost of a lunch'), ('c', 'A quoted price for a standard metal'), ('d', 'A fixed tax rate')], 'c'),
        ('What is a physical premium?', [('a', 'The amount real material sells above or below the benchmark'), ('b', 'A bonus for a healthy worker'), ('c', 'A reward for a sports team'), ('d', 'A free gift with a purchase')], 'a'),
        ('Why can a metal near a port sell for more than the same metal inland?', [('a', 'Ports make metal heavier'), ('b', 'Transport costs and distance change what buyers will pay'), ('c', 'Inland metal is always fake'), ('d', 'Ports paint the metal gold')], 'b'),
        ('What is basis risk?', [('a', 'The risk of a broken chair'), ('b', 'The risk of rain on a holiday'), ('c', 'The risk of a spelling error'), ('d', 'The risk that the hedge moves differently from the real material price')], 'd'),
        ('Why does quality matter in pricing?', [('a', 'Cleaner material usually earns a higher price'), ('b', 'Quality is never checked'), ('c', 'Dirtier material always sells for more'), ('d', 'Quality changes the weather')], 'a'),
    ],
}
