"""Supply Elasticity and Price Response: why mines take years to respond to changes in price."""
CODE = 'mining5_elasticity'
BOOK = {
    "title": 'Supply Elasticity and Price Response',
    "subtitle": 'Why mines take years to respond to price changes',
    "chapters": [
        ('Time lags', 'A new mine can take many years from discovery to first production. Permits, financing and building all take time. Supply therefore reacts to a price rise slowly.'),
        ('Capex cycles', 'Mining spending rises and falls in cycles, often in step with prices. When prices are high, companies build more, and later the new output arrives all at once. This pattern can push prices back down.'),
        ('Inventory buffers', 'Stocks held by producers, traders and consumers can absorb short-term gaps between supply and demand. A large buffer dampens price moves, and a small one lets prices swing. Inventory data is a key input.'),
        ('Demand response', 'Buyers also respond to price, for example by using less metal or switching to a substitute. Demand response is often slower than supply response in the short run. Both sides shape the final price.'),
        ('Models', 'Economists model supply and demand with elasticities, which measure how much quantity changes when price changes. A model must fit the data and the time horizon in question. A simple model is a starting point, not a final answer.'),
        ('Forecast checks', 'Forecasts should be tested against what actually happened in past cycles. Checking the model against history shows how well it works. Forecasts are always uncertain, so ranges are better than single numbers.'),
    ],
    "test": [
        ('Why does supply react slowly to higher prices?', [('a', 'Mines cannot dig at all'), ('b', 'Prices are never higher than costs'), ('c', 'Supply always moves at once'), ('d', 'New mines take many years to find, permit and build')], 'd'),
        ('What is a capex cycle?', [('a', 'A bicycle race'), ('b', 'Mining spending that rises and falls, often with prices'), ('c', 'A type of ore'), ('d', 'A monthly rent')], 'b'),
        ('What do inventory buffers do?', [('a', 'Make the ore heavier'), ('b', 'Stop all trade'), ('c', 'Absorb short gaps between supply and demand'), ('d', 'Turn metal into wood')], 'c'),
        ('What does an elasticity measure?', [('a', 'How much quantity changes when price changes'), ('b', 'How loud a machine is'), ('c', 'How tall a mine shaft is'), ('d', 'How bright a colour is')], 'a'),
        ('Why are forecasts better as ranges than single numbers?', [('a', 'Because ranges are cheaper to print'), ('b', 'Because forecasts are always uncertain'), ('c', 'Because single numbers are illegal'), ('d', 'Because ranges never change')], 'b'),
    ],
}
