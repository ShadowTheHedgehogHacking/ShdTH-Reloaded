<div align="center"><h1>Shadow The Hedgehog: Reloaded</h1>
<img src="https://raw.githubusercontent.com/ShadowTheHedgehogHacking/ShdTH-Reloaded/master/workspace/res/title_screen.png" align="center" />
</div>

## About
Shadow the Hedgehog: Reloaded is a quality of life and enhancement mod for the original Shadow the Hedgehog.

Reloaded is for the USA GameCube version, playable via Dolphin emulator (recommended), Nintendont for Wii / Wii U, and Swiss for GameCube (untested).

Reloaded is still in-progress. The project goals are listed below, and are at varying levels of completeness. A more verbose and detailed changelist will be made once the first release is finalized.

## Less Tedious Gameplay
The primary goal is to make the game less tedious and annoying, both on a short and long term scale. This is mainly accomplished by:
- Lowering lengthy mission objective numbers
- Increasing the available objects for missions
- Lowering the number of endings needed to unlock Last Story
- Changing the Expert Mode unlock requirement to unlock after beating Last Story
- Making slow elevators / platforms / doors and such much faster
- Cutscenes are always skippable
- And countless adjustments to stage object layouts, for less haphazard placement

## More Genuine Challenge
The secondary goal is to make the game more fun by increasing its challenge and replayability, where appropriate. While the game's artificial difficulty (padded story requirements and inflated mission objectives) is minimized, authentic difficulty is enhanced.
- All stage rankings are much harder
- Expert mode is much harder and more unique
- The Secret Door system was reworked into simply being additional pathways instead of one-time useless bonuses
- Secret Keys were changed to Red Rings and have been shuffled around here and there
- And many changes to stage object layouts, for more challenge in some areas

## Misc. Quality of Life Changes
Many other miscellaneous annoyances are also addressed
- Checkpoint collision no longer slows down Shadow
- Shadow’s Homing Attack homes in much faster and has perfect tracking; no more orbiting around your target
- Shadow can now use the Slide move for as long as the melee (B) button is held down
- Shadow can be told to JumpDash rather than HomingAttack by holding the (L) button before performing a HomingAttack/JumpDash
- Shadow can cancel LightDash by pressing the (L) button
- Shadow can control his DigitalSpline speeds on Digital Circuit and Mad Matrix by holding (A) to speed up or (B) to slow down
- Shadow no longer has the Skid/Brake state
- Shadow no longer has the Triangle Jump Exit state 
- Shadow can LightDash additionally from a SkyDive, JumpDash, Homing Attack where before he could only do it while Falling, Jumping, or on Ground
- The jumping GUN mech has an improved hover ability and more responsive rotation
- CarType Vehicles can be dismounted mid-air (Brake button is moved to Y button) and are much faster if tapping (A). Holding (A) retains original speed
- AirSaucer is revamped to be much more responsive. It also no longer has a double jump and instead has a downward spike
- And many more small changes

## Fixed Oversights
- ENEMY | Artifical Chaos's glowing eyes are 90 degrees off; appearing to the side of the eye sockets
- ENEMY | BigFoot TypeB has a strange issue where the Glass Shine would float relative to Shadow's camera
- EVENT | Shadow's expert level complete animation has unlit rings (US version PS2/GC issue)
- EVENT | The first cutscene with Commander has him with broken hand/finger rig (corrected files taken from PS2 version)
- EVENT | Circus Park/Prison Island normal missions have a textureless white chaos emerald
- LAYOUT | The Doom has a GUN Robot that falls through the ground, making it easy to miss this enemy 

## Refreshed Art
And finally, some artistic changes were made to improve the game’s art style and presentation.
- The menus were updated in a new style
- The palette of some stages were redone so they would be more vibrant and less dull
- An optional texture pack of enhanced (not upscaled!) textures was compiled for Dolphin. This pack uses:
  - Uncompressed textures from the Xbox version,
  - The highest resolution available for each texture (some stages used low res versions of many textures),
  - Some imported textures from Sonic Adventure, Sonic Adventure 2, and Sonic Heroes,
  - And a few custom textures for the remaining edge cases
- An additional optional texture pack of upscaled textures was made using the above as the basis
- Some music tracks that went unused in-game are added
  - “E.G.G.M.A.N. (Doc Robeatnix Mix)” was added to the Lava Shelter version of the Egg Dealer boss. The Egg Dealer theme still plays in the other Egg Dealer fights
  - “What I Am” by Magna-Fi replaces “Almost Dead” by Powerman 5000 for the GUN Fortress endings
  - “Broken” by Sins of a Divine Mother is added as a unique ending theme to the Black Comet endings, instead of reusing the GUN Fortress ending theme
  - Expert Mode’s ending has a unique theme and credits animation. ;)

## How to play / Setup
Please verify you are using a 1:1 ShadowTheHedgehog USA ISO: md5: `fc936c9b0144c925b45b805fd39da2ac`

To play this mod, you must:
1. Build a custom ISO overwriting any files from the `files` folder
2. Enable Cheats and use provided game config .ini from the `code` folder

### Extraction of Game / FST Format

1. Get the latest beta or dev Dolphin - [dolphin-5.0-16648 or newer recommended](https://dolphin-emu.org/download/)
2. Before launching dolphin, create an empty file
   `portable.txt` in the same folder as Dolphin.exe
3. Open Dolphin
4. Right-click Shadow The Hedgehog in the game list
5. Select Properties
6. Select FileSystem Tab
7. Right-click "Disc"
8. Select Extract Entire Disc...
9. Select a new folder where you will store the game content and modify its files

### Replacement of Files & Converting FST to ISO
1. Open the newly extracted folder and merge/overwrite the `files` folder files
2. Open Dolphin
3. Open Config (next to Graphics and Controllers)
4. Select Paths Tab
5. Select "Add" for Game Folders
6. Navigate to the folder where you extracted the game
7. Open the `sys` folder, and select "Select Folder"
8. Close the confirmation pane, your games list should populate a new 0 filesize game of Shadow The Hedgehog. The 0 filesize entry is the FST format game
9. Right click the FST format game and pick `Convert File...`
10. The Convert window will appear, click "Convert..." and name it `game.iso` for Nintendont, or `ShdTH-Reloaded.iso` for Dolphin
11. Move/Save the ISO to the Path Dolphin detects your games. A new ShadowTH-Reloaded entry should appear in your Dolphins game list with greater than 0 filesize. Use this when playing the game
12. Click View -> Purge Game List Cache if the Reloaded Icon is not appearing on the new entry. If it still does not appear, the files were not properly replaced