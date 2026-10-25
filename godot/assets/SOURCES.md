# Where the art comes from

Every file here is NASA imagery, downloaded 2026-10-24 (Eric approved NASA's free textures, 10-24). NASA media
guidelines: https://www.nasa.gov/nasa-brand-center/images-and-media/ . NASA imagery is generally free to use, including
commercially, but: no NASA logo or insignia anywhere in the game, and nothing that implies NASA endorses the game.
Credit each source as listed below (in the game's credits).

## planets/

| File | Source | Credit |
|---|---|---|
| `jupiter.jpg` (720×360) | https://assets.science.nasa.gov/content/dam/science/cds/3d/resources/image/jupiter/Jupiter.jpg (page: https://science.nasa.gov/3d-resources/jupiter) | JPL & Caltech (from Voyager images) |
| `saturn.jpg` (720×360) | https://assets.science.nasa.gov/content/dam/science/cds/3d/resources/image/saturn/Saturn.jpg (page: https://science.nasa.gov/3d-resources/saturn) | JPL & Caltech. NASA labels this map "Fictional" (an artist's map, not a photograph) |
| `sun_sdo_hmi.jpg` (resized 2048 → 1024) | https://sdo.gsfc.nasa.gov/assets/img/latest/latest_2048_HMIIC.jpg (the HMI colourised intensitygram of 2026-10-24 07:15 UTC; policy: https://sdo.gsfc.nasa.gov/gallery/copyright/) | Courtesy of NASA/SDO and the AIA, EVE, and HMI science teams |

NASA's 3D Resources has no Sun texture; the SDO photograph of the Sun's disc is used instead (the game draws the Sun
as a disc facing the camera, and cuts away the photo's caption and black sky).

## asteroids/

Collected for the debris fields (not used in the game yet). The `*_diff.png` and `*_n.png` files are the models' own
textures, extracted by Godot's importer.

| File | Source | Credit |
|---|---|---|
| `bennu.glb` (565 m across) | https://assets.science.nasa.gov/content/dam/science/psd/solar/2023/09/b/Bennu_1_1.glb (page: https://science.nasa.gov/resource/bennu-3d-model) | NASA Visualization Technology Applications and Development (VTAD) |
| `vesta.glb` | https://assets.science.nasa.gov/content/dam/science/psd/solar/2023/09/v/Vesta_1_100.glb (page: https://science.nasa.gov/resource/vesta-3d-model) | NASA Visualization Technology Applications and Development (VTAD) |

## Looked at, not used

- The wormhole: Les Bossinas' 1998 painting for NASA Glenn's Breakthrough Propulsion Physics project
  (https://www.nasa.gov/centers/glenn/images/content/101681main_CD1998_76634_1200x900.jpg). A spaceship sits across
  the front of the wormhole, so it can't be cut out as a texture. The wormhole stays as the browser game draws it.
