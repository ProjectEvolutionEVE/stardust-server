"""Price Forecasting Models: how analysts estimate future metal prices, and why every forecast can be wrong."""
CODE = "mining5_price_forecast"
BOOK = {'title': 'Price Forecasting Models',
 'subtitle': 'Estimating where metal prices may go, and how far to trust the estimate',
 'chapters': [('Time series',
               'A time-series model looks at past prices and their patterns, such as trends and seasonal '
               'swings. It assumes the past says something about the future. It works best when conditions '
               'change slowly.'),
              ('Fundamentals',
               'Fundamental models look at supply, demand, stocks held and costs of production. If supply '
               'grows faster than demand, prices tend to pressure downward. Analysts combine this with the '
               'time series.'),
              ('Futures curves',
               'Futures prices show what buyers and sellers agree to pay for metal on future dates. The '
               'shape of this curve gives a market view of expected prices, though it is not a promise.'),
              ('Forecast error',
               'Every forecast has an error. Good analysts measure how far past forecasts missed, and use '
               'that to set a range rather than a single number.'),
              ('Scenarios',
               'Instead of one forecast, analysts build a few scenarios, such as a strong economy, a slow '
               'one and a shock. Each scenario gives a different price path and a different plan.'),
              ('Limits',
               'Prices can jump on news that no model predicted. A forecast is a guide for planning, not a '
               'certain answer. Plans should still hold up if the forecast is wrong.')],
 'test': [('What does a time-series model use?',
           [('a', 'The colour of the ore'),
            ('b', 'The number of trucks'),
            ('c', 'Past prices and their patterns'),
            ('d', 'Staff birthdays')],
           'c'),
          ('What does a futures curve show?',
           [('a', 'What buyers and sellers agree to pay for metal on future dates'),
            ('b', 'The depth of the mine'),
            ('c', 'The weight of a truck'),
            ('d', 'The price of a meal')],
           'a'),
          ('Why do analysts measure forecast error?',
           [('a', 'To make the forecast longer'),
            ('b', 'To avoid all planning'),
            ('c', 'To remove the market'),
            ('d', 'To set a range instead of trusting one number')],
           'd'),
          ('What is the point of building scenarios?',
           [('a', 'To pick one forecast and ignore the rest'),
            ('b', 'To test different price paths and plans'),
            ('c', 'To stop metal being sold'),
            ('d', 'To change the law')],
           'b'),
          ('Why can prices move in ways no model predicted?',
           [('a', 'Metal has no value'),
            ('b', 'Models are always exact'),
            ('c', 'News and shocks can arrive suddenly'),
            ('d', 'Prices only change on Sundays')],
           'c')]}
