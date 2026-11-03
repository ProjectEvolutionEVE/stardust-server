# Refined materials: colour groups and starting prices

Eric 11-03: "a table or color code ... almost like a hazmat chart" so blueprint designers can see what a design needs, and
refined goods "bought and sold once they are refined and processed". Source of truth: `materials_refining.py`
(GROUPS, COMPONENTS, prices); `ensure_market()` lists each item once at server start, then the market moves its price.

Prices set by Claude on Eric's standing word for the market (10-19: "prices will self adjust"); every floor is half the
start. A smelted material starts at **2x** its cheapest ore's price per kg of the element it yields; a native material
(already the element) at **1.25x**; the rest at the set prices below. Lots by value: under 5 a kg trades in 100 kg lots,
under 50 a kg in 10 kg lots, otherwise 1 kg. Eric may change any number.

Water ice, basalt, native iron-nickel and industrial diamond are not listed twice: they trade as their debris-field item.

## Colour chart

| Colour | Kind | For |
|---|---|---|
| blue `#4a90d9` | Structural & Frames | hulls, frames, beams, panels, pressure vessels |
| yellow `#f5c518` | Electrical & Electronics | wiring, circuits, contacts, chips, solar cells |
| orange `#f07f1a` | Power & Fuel | batteries, fuel, reactors, engines |
| purple `#9b59d0` | Magnets & Motors | magnets, motors, generators |
| red `#d9443a` | Heat & Radiation Shielding | heat shields, radiation shielding, parts that survive extreme heat |
| green `#3fae5a` | Life Support & Growing | air, water, the greenhouse, fertilizer |
| white `#e6e6e6` | Chemicals & Catalysts | acids, catalysts, refining and smelting supplies |
| brown `#a8743d` | Building & Ceramics | bricks, glass, cement, furnaces, timber work |
| cyan `#2ec4c9` | Cutting & Wear | cutting, drilling and grinding tools, hard-wearing parts |

## Prices

| Material | Kinds (first = its colour) | Per kg | Lot | Start | Floor |
|---|---|---:|---:|---:|---:|
| Iron | Structural & Frames, Magnets & Motors | 5.72 | 10 kg | 57 | 28 |
| Nickel | Structural & Frames, Magnets & Motors, Power & Fuel | 52.60 | 1 kg | 53 | 26 |
| Cobalt | Power & Fuel, Magnets & Motors | 112.61 | 1 kg | 110 | 55 |
| Copper | Electrical & Electronics | 34.65 | 10 kg | 350 | 175 |
| Aluminium | Structural & Frames, Electrical & Electronics | 17.35 | 10 kg | 170 | 85 |
| Titanium | Structural & Frames | 31.70 | 10 kg | 320 | 160 |
| Magnesium | Structural & Frames, Chemicals & Catalysts | 8.68 | 10 kg | 87 | 43 |
| Zinc | Structural & Frames, Power & Fuel | 11.92 | 10 kg | 120 | 60 |
| Tin | Electrical & Electronics | 40.62 | 10 kg | 410 | 205 |
| Lead | Heat & Radiation Shielding, Power & Fuel | 9.24 | 10 kg | 92 | 46 |
| Chromium | Structural & Frames | 17.22 | 10 kg | 170 | 85 |
| Manganese | Structural & Frames, Power & Fuel | 9.50 | 10 kg | 95 | 47 |
| Tungsten | Heat & Radiation Shielding, Cutting & Wear | 65.97 | 1 kg | 66 | 33 |
| Molybdenum | Structural & Frames | 80.08 | 1 kg | 80 | 40 |
| Lithium | Power & Fuel | 536.19 | 1 kg | 540 | 270 |
| Silver | Electrical & Electronics | 68.92 | 1 kg | 69 | 34 |
| Gold | Electrical & Electronics, Heat & Radiation Shielding | 250.00 | 1 kg | 250 | 125 |
| Platinum | Chemicals & Catalysts, Electrical & Electronics | 375.00 | 1 kg | 380 | 190 |
| Palladium | Chemicals & Catalysts, Electrical & Electronics | 375.00 | 1 kg | 380 | 190 |
| Iridium | Heat & Radiation Shielding | 500.00 | 1 kg | 500 | 250 |
| Silicon | Electrical & Electronics, Power & Fuel, Building & Ceramics | 4.28 | 100 kg | 430 | 215 |
| Carbon (graphite) | Chemicals & Catalysts, Heat & Radiation Shielding, Power & Fuel | 3.75 | 100 kg | 380 | 190 |
| Boron | Heat & Radiation Shielding, Cutting & Wear | 50.00 | 1 kg | 50 | 25 |
| Sulfur | Chemicals & Catalysts | 1.88 | 100 kg | 190 | 95 |
| Phosphorus | Life Support & Growing, Chemicals & Catalysts | 32.56 | 10 kg | 330 | 165 |
| Neodymium (rare earth) | Magnets & Motors | 392.41 | 1 kg | 390 | 195 |
| Dysprosium (rare earth) | Magnets & Motors | 600.00 | 1 kg | 600 | 300 |
| Hydrogen | Power & Fuel, Chemicals & Catalysts | 7.00 | 10 kg | 70 | 35 |
| Oxygen | Life Support & Growing, Power & Fuel | 0.90 | 100 kg | 90 | 45 |
| Nitrogen | Life Support & Growing | 2.00 | 100 kg | 200 | 100 |
| Methane | Power & Fuel, Chemicals & Catalysts | 3.00 | 100 kg | 300 | 150 |
| Ammonia | Life Support & Growing, Chemicals & Catalysts | 3.00 | 100 kg | 300 | 150 |
| Carbon dioxide | Life Support & Growing | 1.00 | 100 kg | 100 | 50 |
| Helium-3 | Power & Fuel | 5,000.00 | 1 kg | 5,000 | 2,500 |
| Sand (silica sand, bulk) | Building & Ceramics | 0.30 | 100 kg | 30 | 15 |
| Clay | Building & Ceramics | 0.30 | 100 kg | 30 | 15 |
| Limestone | Building & Ceramics, Chemicals & Catalysts | 0.40 | 100 kg | 40 | 20 |
| Soil (bulk) | Life Support & Growing | 0.50 | 100 kg | 50 | 25 |
| Timber - softwood (Douglas-fir) | Building & Ceramics | 2.00 | 100 kg | 200 | 100 |
| Timber - hardwood (white oak) | Building & Ceramics | 4.00 | 100 kg | 400 | 200 |
| Uranium | Power & Fuel, Heat & Radiation Shielding | 113.44 | 1 kg | 110 | 55 |
| Thorium | Power & Fuel | 100.00 | 1 kg | 100 | 50 |
