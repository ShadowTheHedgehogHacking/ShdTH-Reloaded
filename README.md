<div align="center"><h1>Shadow The Hedgehog: Reloaded</h1>  
<img src="https://raw.githubusercontent.com/ShadowTheHedgehogHacking/ShdTH-Reloaded/master/workspace/res/title_screen.png" align="center" />
</div>

Shadow the Hedgehog: Reloaded is an improvement mod of Shadow the Hedgehog designed to make the game less tedious, increase challenge, fix bugs and oversights, restore some unused content, and generally remix levels.

Reloaded is for the USA GameCube version, and is playable on Dolphin emulator (recommended), Nintendont for Wii and Wii U, and Swiss for GameCube.

Reloaded v1.2 is the final revision.

1.0 Release video:
https://youtu.be/1yM2kJjyhZQ


## Main Changes

Unlocks and Story Pacing
- Cutscenes are always skippable.
- Last Story now unlocks after 3 Story endings, instead of all 10.
- Expert Mode unlocks after beating Last Story, instead of requiring all A Ranks. Expert Mode now has a unique ending animation. You can also practice Expert levels in Select Mode by locking in a stage with the X button.

Missions
- Many missions are more forgiving, allowing you to miss a few enemies or objects instead of needing to find ALL of them.
- Partner characters won't stop you with their "camera zoom" introductions when you first meet them.
- Partner characters won't automatically swap your active mission if you manually "lock in" your desired mission, either via D-Pad or by the Pause Menu. D-Pad Up will reset back to automatic swapping.

Levels
- S Rank has been added to the Rank system. Good luck!
- The Secret Door system was reworked into additional pathways instead of one-time bonuses. You can now find extra routes and secrets, even on your first playthrough.
- The Secret Keys have been replaced with Red Rings, and have been shuffled around for many levels.
- Many "forced waiting" sections, such as elevators, are faster than before, or are skippable if you're skilled enough.

Player Actions
- Shadow is generally faster and more responsive.
- Hold L to always perform a Jump Dash instead of a Homing Attack. This is useful if you don't want to target enemies while platforming.
- You can toggle between Original and Reloaded melee weapon styles with the Z button. In Reloaded style, hold B to activate the weapon's hitbox, and hold B+L to perform rapid swings while running. You can also lock-in the weapon's hitbox by sliding while holding B.
- Go faster or slow down while riding the cyberspace circuits by pressing the A and B buttons.
- Shadow can now slide out of a spindash, homing attack, and jump dash.
- Sliding duration is player controlled. Hold X to slide as long as you want.
- You can tap A to make cars and motorcycles accelerate much faster and maintain a higher top speed.

Unused Content
- An inaccessible area in Lost Impact is now reachable.
- Some unused dialogue was restored/added where appropriate.
- “E.G.G.M.A.N. (Doc Robeatnix Mix)” was added to Lava Shelter's Egg Dealer fight. This was normally only played briefly during a cutscene.
- "Who I Am", a planned track, was added to GUN Fortress Hero and Final Haunt Dark endings.
- "Broken", a planned track, was added to Black Comet's endings. (Black Comet normally reused a GUN Fortress ending track.)

Visuals
- Widescreen and 4:3 ratio options.
- The bloom effect was reduced.
- The palette of some similar-looking stages were changed to differentiate them.
- Maria's eyes were adjusted.
- Stray HP Bar pixel was removed.
- Wrong Artificial Chaos eye glow rotation was fixed.
- Unrigged GUN Bigfoot Type B cockpit glare was fixed.
- All unlit ring inhibitors in cutscenes featuring Shadow were fixed.
- The PS2 exclusive hand rig/animations for the Commander were fixed.
- Chaos Emeralds have a darkened texture in all cutscenes.

## How to play / Setup
Please verify you are using a 1:1 ShadowTheHedgehog GameCube ISO:

TODO: Make a table

USA: <hash> || CRC32 `f582cf1e` || SHA-1 `5dc81ad9c97549394e30bedc252bfa37d4db1de0`
JPN: <hash>
PAL: <hash>

---

A How-To-Setup video is available here, and though it says v1.0, the setup is the same for v1.2:
https://youtu.be/uv9gpqEbXU4

TODO: Update below using xdelta wasm

To play this mod, you must:
1. Download the latest Release (v1.2) - picking if you want 4:3 or 16:9 version
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

### TODO: Move this to its own page, with a link here instead.

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
: Reloaded Co-Developer, work on Heroes Power Plant, other misc tools

- TheHatedGravity
: Model, Movie, and Font Help

- BlazinZzetti
: Code Contributor, Developer of Shadow SX, and Help

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

- The Spectral Star, Jesus_PK, $$$Link, Angry Waiter, and many more! 
: Testing, Feedback

- Sanglish, Jesus_PK, dreamsyntax's mom, 
: Custom Hint Translation assistance

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
