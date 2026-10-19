# Debris-field minerals and their starting prices

Eric 10-19: "Go." and "Set what you believe should be the right prices on the market... prices will self adjust."
Prices set by Claude on that delegation. Whole credits per **lot**; every floor is half the start (nothing trades
below it); the reference price the bank leans toward starts at the start price. The original five (iron, copper,
silver, gold, industrial diamond) are unchanged. Eric may change any number.

Source of truth: `minerals.py` (generated from it; `schema.sql` v15 loads the same rows and `test_server.py` checks
them). Densities in kg/m³ are real pure-mineral values (webmineral / mindat). Yields are each element's share by
weight from the formula (rule 27). Rarity band shares per field size are in `static/debris-flight.js` (MIX).

| Tier | Band | Code | Name | Formula | Density | Yields (smelting) | Lot | Start | Floor | Per kg |
|---|---|---|---|---|---:|---|---:|---:|---:|---:|
| 1 common | common | `basalt` | Basalt | rock: mostly plagioclase and pyroxene | 2,900 | - | 100 kg | 50 | 25 | 0.5 |
| 1 common | common | `iron-nickel` | Iron-nickel metal | Fe,Ni (taken as 90% iron, 10% nickel) | 7,900 | 90.00% iron, 10.00% nickel | 100 kg | 400 | 200 | 4 |
| 1 common | common | `water-ice` | Water ice | H₂O | 917 | - | 100 kg | 40 | 20 | 0.4 |
| 2 ore | plentiful | `iron` | Iron ore (hematite) | Fe₂O₃ | 5,300 | 69.94% iron | 100 kg | 200 | 100 | 2 |
| 2 ore | plentiful | `magnetite` | Iron ore (magnetite) | Fe₃O₄ | 5,150 | 72.36% iron | 100 kg | 220 | 110 | 2.2 |
| 2 ore | plentiful | `bauxite` | Aluminium ore (bauxite) | Al(OH)₃ | 2,400 | 34.59% aluminium | 100 kg | 300 | 150 | 3 |
| 2 ore | plentiful | `olivine` | Magnesium ore (olivine) | Mg₂SiO₄ | 3,270 | 34.55% magnesium | 100 kg | 150 | 75 | 1.5 |
| 2 ore | plentiful | `quartz` | Quartz | SiO₂ | 2,650 | 46.74% silicon | 100 kg | 100 | 50 | 1 |
| 2 ore | ore | `copper` | Copper ore (chalcopyrite) | CuFeS₂ | 4,190 | 34.63% copper, 30.43% iron | 100 kg | 600 | 300 | 6 |
| 2 ore | ore | `ilmenite` | Titanium ore (ilmenite) | FeTiO₃ | 4,720 | 31.55% titanium, 36.81% iron | 100 kg | 500 | 250 | 5 |
| 2 ore | ore | `pentlandite` | Nickel ore (pentlandite) | (Fe,Ni)₉S₈ (taken as Fe₄.₅Ni₄.₅S₈) | 4,800 | 34.22% nickel, 32.56% iron | 100 kg | 900 | 450 | 9 |
| 2 ore | ore | `sphalerite` | Zinc ore (sphalerite) | ZnS | 4,050 | 67.10% zinc | 100 kg | 400 | 200 | 4 |
| 2 ore | ore | `galena` | Lead ore (galena) | PbS | 7,600 | 86.60% lead | 100 kg | 400 | 200 | 4 |
| 2 ore | ore | `chromite` | Chromium ore (chromite) | FeCr₂O₄ | 4,790 | 46.46% chromium, 24.95% iron | 100 kg | 400 | 200 | 4 |
| 2 ore | ore | `pyrolusite` | Manganese ore (pyrolusite) | MnO₂ | 5,060 | 63.19% manganese | 100 kg | 300 | 150 | 3 |
| 2 ore | ore | `apatite` | Phosphate (apatite) | Ca₅(PO₄)₃F | 3,190 | 18.43% phosphorus | 100 kg | 300 | 150 | 3 |
| 2 ore | ore | `graphite` | Graphite | C | 2,250 | 100.00% carbon | 100 kg | 300 | 150 | 3 |
| 2 ore | ore | `sulfur` | Native sulfur | S | 2,070 | 100.00% sulfur | 100 kg | 150 | 75 | 1.5 |
| 2 ore | ore | `spodumene` | Lithium ore (spodumene) | LiAlSi₂O₆ | 3,150 | 3.73% lithium, 14.50% aluminium | 100 kg | 1,000 | 500 | 10 |
| 2 ore | scarce | `silver` | Silver ore (acanthite) | Ag₂S | 7,300 | 87.06% silver | 10 kg | 300 | 150 | 30 |
| 2 ore | scarce | `cobaltite` | Cobalt ore (cobaltite) | CoAsS | 6,300 | 35.52% cobalt | 10 kg | 200 | 100 | 20 |
| 2 ore | scarce | `cassiterite` | Tin ore (cassiterite) | SnO₂ | 6,990 | 78.77% tin | 10 kg | 160 | 80 | 16 |
| 2 ore | scarce | `wolframite` | Tungsten ore (wolframite) | (Fe,Mn)WO₄ (taken as Fe₀.₅Mn₀.₅WO₄) | 7,300 | 60.63% tungsten | 10 kg | 200 | 100 | 20 |
| 2 ore | scarce | `molybdenite` | Molybdenum ore (molybdenite) | MoS₂ | 4,730 | 59.94% molybdenum | 10 kg | 240 | 120 | 24 |
| 2 ore | scarce | `monazite` | Rare-earth ore (monazite) | (Ce,La,Nd)PO₄ (taken as Ce₀.₅La₀.₂₅Nd₀.₂₅PO₄) | 5,150 | 15.29% neodymium, 29.71% cerium, 14.73% lanthanum | 10 kg | 300 | 150 | 30 |
| 2 ore | scarce | `uraninite` | Uranium ore (uraninite) | UO₂ | 10,950 | 88.15% uranium | 10 kg | 500 | 250 | 50 |
| 2 ore | scarce | `gold` | Native gold | Au | 19,300 | 100.00% gold | 1 kg | 200 | 100 | 200 |
| 2 ore | scarce | `diamond` | Industrial diamond | C | 3,510 | 100.00% carbon | 1 kg | 100 | 50 | 100 |
| 2 ore | rare | `platinum` | Native platinum | Pt | 21,450 | 100.00% platinum | 1 kg | 300 | 150 | 300 |
| 2 ore | rare | `palladium` | Native palladium | Pd | 12,020 | 100.00% palladium | 1 kg | 300 | 150 | 300 |
| 2 ore | rare | `iridium` | Native iridium | Ir | 22,560 | 100.00% iridium | 1 kg | 400 | 200 | 400 |
| 3 shock | shock | `shocked-quartz` | Shocked quartz | SiO₂ | 2,650 | 46.74% silicon | 10 kg | 200 | 100 | 20 |
| 3 shock | shock | `impact-glass` | Impact glass | SiO₂ | 2,200 | 46.74% silicon | 10 kg | 200 | 100 | 20 |
| 3 shock | shock | `maskelynite` | Maskelynite | NaAlSi₃O₈–CaAl₂Si₂O₈ glass (taken as albite) | 2,550 | 10.29% aluminium, 32.13% silicon | 10 kg | 300 | 150 | 30 |
| 3 shock | shock | `coesite` | Coesite | SiO₂ | 2,920 | 46.74% silicon | 10 kg | 400 | 200 | 40 |
| 3 shock | shock-rare | `stishovite` | Stishovite | SiO₂ | 4,290 | 46.74% silicon | 1 kg | 100 | 50 | 100 |
| 3 shock | shock-rare | `ringwoodite` | Ringwoodite | Mg₂SiO₄ | 3,900 | 34.55% magnesium | 1 kg | 100 | 50 | 100 |
| 3 shock | lonsdaleite | `lonsdaleite` | Lonsdaleite | C | 3,520 | 100.00% carbon | 1 kg | 2,000 | 1,000 | 2000 |
| 3 shock | brownleeite | `brownleeite` | Brownleeite | MnSi | 5,820 | 66.17% manganese, 33.83% silicon | 1 kg | 20,000 | 10,000 | 20000 |

## Rarity bands: share of pieces by field size

| Band | Large | Medium | Small | Tiny |
|---|---:|---:|---:|---:|
| common | 55.15% | 48.15% | 40.2% | 36.24% |
| plentiful | 25% | 24% | 22% | 22% |
| ore | 14% | 18% | 22% | 22% |
| scarce | 3% | 6% | 11% | 14% |
| rare | 0.2% | 0.5% | 1% | 1.6% |
| shock | 2% | 2.5% | 2.8% | 3% |
| shock-rare | 0.6% | 0.8% | 0.9% | 1% |
| lonsdaleite | 0.05% | 0.05% | 0.1% | 0.15% |
| brownleeite | 0 | 0 | 0 | 0.01% |

Within a band every mineral is equally likely. The same shares apply in all four rings.

## Notes and open points

- Mixed formulas are simplified: pentlandite as Fe4.5Ni4.5S8, wolframite as Fe0.5Mn0.5WO4, monazite as
  Ce0.5La0.25Nd0.25PO4, iron-nickel as 90% Fe / 10% Ni by weight, maskelynite as albite glass.
- Native platinum, palladium and iridium are taken as the pure metal (real native grains are alloys and lighter).
- Uraninite uses the pure UO2 density (10,950); natural pieces are often lighter.
- Not yet mineable from the catalogue: dysprosium (would need xenotime or similar), thorium and boron (non-metals
  and energy items beyond the metal list). Monazite yields neodymium, cerium and lanthanum.
- Shock-mineral text states only what each mineral is and that on Earth it forms under extreme pressures or
  temperatures. No cause is given anywhere (canon).
