<div align="center"><h1>Shadow The Hedgehog: Reloaded</h1>
<img src="https://raw.githubusercontent.com/ShadowTheHedgehogHacking/ShdTH-Reloaded/master/workspace/res/title_screen.png" align="center" />
</div>

## About
Shadow the Hedgehog: Reloaded is a quality of life and enhancement mod for the original Shadow the Hedgehog.

Release video:
https://youtu.be/1yM2kJjyhZQ

Reloaded is for the USA GameCube version, playable via Dolphin emulator (recommended), Nintendont for Wii / Wii U, and Swiss for GameCube.

The main features are below, with a more complete changelist being included in the download.

## Less Tedious Gameplay
The primary goal is to make the game less tedious and annoying, both on a short and long term scale. This is mainly accomplished by:
- Lowering lengthy mission objective numbers
- Increasing the available objects for missions
- Lowering the number of endings needed to unlock Last Story
- Changing the Expert Mode unlock requirement to unlock after beating Last Story
- Making slow elevators / platforms / doors and such much faster
- Cutscenes are always skippable

## More Genuine Challenge
The secondary goal is to make the game more fun by increasing its challenge and replayability, where appropriate. While the game's artificial difficulty (padded story requirements and inflated mission objectives) is minimized, authentic difficulty is enhanced.
- All stage rankings are much harder
- The Secret Door system was reworked into simply being additional pathways instead of one-time useless bonuses
- Secret Keys were changed to Red Rings and have been shuffled around here and there

## Misc. Quality of Life Changes
Many other miscellaneous annoyances are also addressed.
- Checkpoint collision no longer slows down Shadow
- Shadow’s Homing Attack homes in much faster and more precise tracking
- Shadow can now use the Slide move for as long as the melee (B) or (X) button is held down
- Shadow can be told to JumpDash rather than HomingAttack by holding the (L) button before performing a HomingAttack/JumpDash
- Shadow can control his DigitalSpline speeds on Digital Circuit and Mad Matrix by holding (A) to speed up or (B) to slow down
- The player can press Z at any time to change between Reloaded melee-weapon style and the Original game. Shadow will retain this choice until the next time the game is launched.
- Shadow can now activate melee collision by holding (B) which creates trails. While holding (B), Shadow can also hold (L) to rapidly swing the weapon based on the speed he is moving.
- If Shadow is holding a melee weapon, he can now slide out of a SpinDash, HomingAttack, or JumpDash with (B). He can still AirAttack with melee weapons but he must double press (B), holding the last (B) to compensate for the attack collision change
- Shadow can pick a Mission character at any time with Dpad. This will prevent activating other partners. You can restore activating partners you run into by pressing Dpad UP at any time.
- Shadow no longer has the Skid/Brake state
- Shadow no longer has the Triangle Jump Exit state
- Shadow can LightDash additionally from a SkyDive, JumpDash, Homing Attack where before he could only do it while Falling, Jumping, or on Ground
- The jumping GUN mech has an improved hover ability and more responsive rotation
- CarType Vehicles can be dismounted mid-air (Brake button is moved to Y button) and are much faster if tapping (A). Holding (A) retains original speed
- AirSaucer is revamped to be much more responsive. It also no longer has a double jump and instead has a downward spike

## Fixed Oversights
There's also some pure bug fixes.
- GEO | Remove double collisions in Death Ruins
- GEO | Remove extra/unused geo across multiple stages
- ENEMY | Artifical Chaos's glowing eyes are 90 degrees off; appearing to the side of the eye sockets
- ENEMY | BigFoot TypeB has a strange issue where the Glass Shine would float relative to Shadow's camera
- EVENT | Shadow's expert level complete animation has unlit rings (US version PS2/GC issue)
- EVENT | The first cutscene with Commander has him with broken hand/finger rig (corrected files taken from PS2 version)
- EVENT | Circus Park/Prison Island normal missions have a textureless white chaos emerald
- LAYOUT | The Doom has a GUN Robot that falls through the ground, making it easy to miss this enemy
- LAYOUT | Port JPN ver layout bugfixes, if they made sense
- LAYOUT | Remove duplicate gravity switches in Space Gadget, making LOUD noises when passed
- AUDIO | Lower the volume of Super Shadow's Chaos Spear charge sound effect, which largely overpowers everything else
- AUDIO | Iron Jungle EggBreaker 0511 restored Omega's missing intro line audio
- AUDIO | Eggman missing radio filter for some lines where he is represented by EggMonitor
- AUDIO | Large delay for Black Doom's line "Those are our Black Arms soldiers..."
- AUDIO/FNT | Subtitle timings have been modified to match with the English audio recordings for the EN subtitles
- AUDIO | GUN Soldiers no longer incorrectly mention Black Arms in The Doom / Lost Impact

## Restored Content
As a bonus, some unused content has been integrated into the game.
- Unused Music
  - “E.G.G.M.A.N. (Doc Robeatnix Mix)” was added to the Lava Shelter version of the Egg Dealer boss. The Egg Dealer theme still plays in the other Egg Dealer fights
  - “What I Am” by Magna-Fi replaces “Almost Dead” by Powerman 5000 for the GUN Fortress endings
  - “Broken” by Sins of a Divine Mother is added as a unique ending theme to the Black Comet endings, instead of reusing the GUN Fortress ending theme
- Unused Dialogue
  - Some dialogue triggers were restored just by fixing them. Shadow's new opening comment in GUN Fortress was originally positioned too high to trigger, and Doom's comment about Gerald after the first shield generator in Space Gadget had its render distance set too low.
  - Some stages had unused voice lines for approaching the Goal Ring while the Dark or Hero missions were active, like in Glyphic Canyon and Sky Troops.
  - Since Shadow is able to switch missions at any time, some new dialogue can now be heard before you would normally get the appropriate mission character, such as Doom's comments on the first Chaos Emerald in Westopolis.

## Refreshed Art
And finally, some artistic changes were made to improve the game’s art style and presentation.
- The menus were updated in a new style
- The palette of some similar looking stages were changed to differentiate them
- Devil Doom boss fight music will no longer be interrupted by Shadow getting Dark/Hero Shadow (filling up the meters)
- Expert Mode’s ending has a unique theme and credits animation. ;)


## How to play / Setup
Please verify you are using a 1:1 ShadowTheHedgehog USA ISO:


CRC32: `f582cf1e`


or


SHA-1: `5dc81ad9c97549394e30bedc252bfa37d4db1de0`


A How-To-Setup video is available here, and though it says v1.0, the setup is the same for v1.1:
https://youtu.be/uv9gpqEbXU4

To play this mod, you must:
1. Download the latest Release (v1.1) - picking if you want 4:3 or 16:9 version
### Computer
2. Place your original ShadowTheHedgehog USA in ISO format in the Patcher folder
3. Rename your ISO to `GUPE8P.iso` if its not already named this.
4. Run `Apply Patch-Windows.bat` if on Windows, `Apply Patch-Mac.command` if on Mac, `Apply Patch-Linux.sh` if on Linux 
5. ShdTH-Reloaded.iso should be created successfully. If you run into errors, likely the ISO is wrong hash, double check your original game.
6. It is recommended to also download the `Dolphin Addons` and `Optional Cheats and Preferences` to further customize Reloaded to your liking
7. From Optional Cheats and Preferences, place the `GUPE8P.ini` file in `Dolphin\User\GameSettings` (or `Documents\Dolphin Emulator\GameSettings` if not in portable mode)
8. Enable Cheats in Dolphin -> Config. Right click the game the list and choose `Properties` to pick what cheats you want
9. If playing on original hardware use [CodeManager2](https://github.com/CLF78/CodeManager2) to build GCT files in order to use cheats on hardware. Select the `GUPE8P.ini` file using CodeManager2.
10. From Dolphin Addons, follow the instructions included with the file to install them and enable the custom textures / graphic mod as you desire
### Android
2. Download and install the [ROM Patcher](https://github.com/btimofeev/UniPatcher/releases/latest)
3. Place your original ShadowTheHedgehog USA in ISO format into a folder
4. Place the `GUPE8P.iso.vcdiff` from vcdiff folder into a folder
5. Specify the output file & click the pink floating icon.
6. `ISO NAME [PATCHED].iso` should be created successfully. If you run into errors, likely the ISO is wrong hash, double check your original game.
7. It is recommended to also download the `Dolphin Addons` and `Optional Cheats and Preferences` to further customize Reloaded to your liking.

## How to Build Reloaded Yourself
IT IS RECOMMENDED TO USE THE "RELEASES" TAB RATHER THAN DOING THE BELOW. The below does not account for Nintendont compatibility by file deletion/downsampling/AFS replacements.
1. Build a custom ISO overwriting any files from the `ISO EDITS` folder (below is steps how to do this)
2. Enable Cheats and use provided game config .ini from the `code` folder - placing the `GUPE8P.ini` file in `Dolphin\User\GameSettings`

### Extraction of Original Game / FST Format
1. Get the latest beta or dev Dolphin - [dolphin-5.0-20347 or newer recommended](https://dolphin-emu.org/download/)
2. (Optional: only do this step if you want to keep config separate) Before launching dolphin, create an empty file
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

# Credits
### Direct Contributions

- LimblessVector
: Project Lead

- dreamsyntax
: Reloaded Co-Hacker, Major Help and Feedback

- TheHatedGravity
: Model, Movie, and Font Help

- BlazinZzetti
: Code Contributor and Help

### Thanks

- SEGA and Sonic Team
: for the original Shadow the Hedgehog

- igorsabra4
: for Heroes Power Plant and other file reversing help

- Sewer56	
: for HeroesONE Reloaded and other file reversing help

- MainMemory
: for HeroesONE

- DonutStopGaming
: for symbol map and struct research

- metaconstruct, UnclePunch, psiLupan, and DRGN (Melee modding community)
: for Melee Code Manager and assistance with DOL modification

- Shadowth117
: Model Help

- SonikkuA
: Model Help

- aldelaro5
: for Dolphin Memory Engine

- InternetExplorer
: for "Intro to Wii Game Modding" guide

- Jos / Josjuice
: for help with some tricky hardware only exceptions and all the awesome Dolphin work they do

- kiwi515
: for help fixing weird hardware-only exceptions

- Every Dolphin Contributor
: for Dolphin and its debug features

- Link Master, gamemasterplc, CosmoCortney, and TeconMoon
: for various RAM reference codes and discoveries

And the Heroes & Shadow Hacking Central Discord community for their input, motivation, miscellaneous help, and friendship. We could never have gotten this far without all of you. <3
