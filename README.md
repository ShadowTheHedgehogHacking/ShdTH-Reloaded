<div align="center"><h1>Shadow The Hedgehog: Reloaded</h1>  
<img src="https://raw.githubusercontent.com/ShadowTheHedgehogHacking/ShdTH-Reloaded/master/workspace/res/title_screen.png" align="center" />
</div>


Shadow the Hedgehog: Reloaded is an improvement mod of Shadow the Hedgehog designed to make the game less tedious, increase challenge, fix bugs and oversights, restore some unused content, and generally remix levels.

Reloaded is for the GameCube version, and is playable on Dolphin Emulator (recommended), Nintendont for Wii and Wii U, and Swiss for GameCube.

Reloaded v1.2 is the final revision, released on 2024-07-01.

Release video: https://youtu.be/1yM2kJjyhZQ

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
- In-game timing can be used for speedruns, as we apply the timing mechanisms from [ShadowSX](https://www.shadowspeedrun.com/ShadowSX/)

Player Actions
- Shadow is generally faster and more responsive.
- Hold L to always perform a Jump Dash instead of a Homing Attack. This is useful if you don't want to target enemies while platforming.
- You can toggle between Original and Reloaded melee weapon styles with the Z button. In Reloaded style, hold B to activate the weapon's hitbox, and hold B+L to perform rapid swings while running. You can also lock-in the weapon's hitbox by sliding while holding B.
- Go faster or slow down while riding the cyberspace circuits by pressing the A and B buttons.
- Shadow can now slide out of a spindash, homing attack, and jump dash.
- Sliding duration is player controlled. Hold X to slide as long as you want.
- Air Saucers are much more mobile. Pressing A twice results in a downward spike instead of a double jump.
- You can tap A to make cars and motorcycles accelerate much faster and maintain a higher top speed. You can dismount at any time. Press Y to brake.

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

### ROM Validation
Please verify the ROM you are attempting to patch is a 1:1 ShadowTheHedgehog GameCube ISO.

GCZ/WIA/RVZ or any other format than ISO is not supported. Please convert to ISO, then compare your game to the table below.

You can get your hashes of your ISO by right clicking your game in Dolphin's game list -> `Properties` -> `Verify` tab.

| ROM    | CRC32 Hash    | SHA-1 Hash                               |
| ------ | ------------- | ---------------------------------------- |
| NTSC-U | f582cf1e      | 5dc81ad9c97549394e30bedc252bfa37d4db1de0 |
| PAL    | db7d8cd9      | 05b34c82c0fe8aa504539e4dfbba89957c7fc788 |
| NTSC-J | 529baa3a      | 1d4d1a069d87bdcc6985ffd16d1d19328bb3ae69 |



A How-To-Setup video is available. Check the releases page.

### Nintendont Users: Custom Build Required
At time of release of v1.2 (2024/07/01) Nintendont does not officially support oversized ISOs.

You will need to use [this build of Nintendont instead](https://github.com/nfsman34/Nintendont-SonicRiders/releases) until [this PR is merged](https://github.com/FIX94/Nintendont/pull/1213). When the PR is merged, you can update your official Nintendont and switch to it.
If playing with Nintendont, enable Unlocked Read Speed before launching the game.


### Computer
1. Download [the latest release from here](https://github.com/ShadowTheHedgehogHacking/ShdTH-Reloaded/releases) - choosing either the original aspect ratio version or the widescreen version. Patchers exist for NTSC-U, NTSC-J, and PAL.
2. Extract your chosen version release zip.
3. Get the latest release or dev Dolphin - [dolphin-5.0-21460 or newer recommended](https://dolphin-emu.org/download/)
4. Visit https://shadowthehedgehoghacking.github.io/xdelta-wasm/ or any other xdelta3 patcher of your choice.
5. Specify your original ISO as the `Source file`.
6. Specify the `reloaded-[region]-[aspect].xdelta` file you extracted as the `Patch file`.
7. Click `Apply Patch`: It will then 'download' the patched file as `ISO NAME-patched.iso` (nothing is actually uploaded/downloaded, it is all done on-device).
8. If you run into errors, likely the ISO is wrong hash for the xdelta you downloaded. Double check your original game in `Dolphin Verify` tab.
9. It is recommended to also download the `Dolphin Addons` and `Optional Cheats and Preferences` to get the best experience, performance, and further customize Reloaded to your liking.
10. From `Optional Cheats and Preferences`, place the `GUPR8P.ini` file in `\GameSettings` of your `Dolphin User Folder`. You can find your `Dolphin User Folder` by launching Dolphin and clicking `File` on the menu bar, then `Open User Folder`.
11. Enable Cheats in `Dolphin -> Config`. Right click the game the list and choose `Properties` to pick what cheats you want.
12. Under `Dolphin -> Config -> Advanced` enable `CPU Clock Override` and try various values (CPU dependent). I highly recommend at least `150%` if your CPU can handle it. Otherwise a suggested maximum value of `200%` should run the game at full 60fps at all times.
13. From Dolphin Addons, follow the instructions included with the file to install them and enable the custom textures / graphic mod if you desire.
14. If playing on Nintendont or Swiss, I recommend using [CodeManager2](https://github.com/CLF78/CodeManager2) to build GCT files in order to use cheats on hardware. Select the `GUPR8P.ini` file using CodeManager2.

### Android
1. Download [the latest release from here](https://github.com/ShadowTheHedgehogHacking/ShdTH-Reloaded/releases) - choosing either the original aspect ratio version or the widescreen version. Patchers exist for NTSC-U, NTSC-J, and PAL.
2. Download and install the [ROM Patcher](https://github.com/btimofeev/UniPatcher/releases/latest)
3. Place your original ShadowTheHedgehog ROM in ISO format into an accessible folder
4. Extract the Reloaded release zip you downloaded, and place the `reloaded-[region]-[aspect].xdelta` somewhere UniPatcher will be able to access it.
5. Specify the output file & click the pink floating action button.
6. `ISO NAME [PATCHED].iso` should be created successfully. If you run into errors, likely the ISO is wrong hash, double check your original game.
7. Turn off "Emulate Disc Speed" in your game configuration, or Dolphin configuration.

### Validate Patched ISO
You can get your hashes of your ISO by right clicking your game in Dolphin's game list -> `Properties` -> `Verify` tab.

Below are the expected results after patching your ISO with Reloaded v1.2.

| ROM                          | CRC32 Hash    | SHA-1 Hash                               |
| ---------------------------- | ------------- | ---------------------------------------- |
| RELOADED                     | e159740e      | 7496bb93064e75b6346b4d4219e89fddaf35c1be |
| RELOADED WIDESCREEN          | 608b69c4      | 246329735cd79fd0fe187c61b94487e75c42f1b7 |

### Changelog
[A human changelog history can be found here.](https://github.com/ShadowTheHedgehogHacking/ShdTH-Reloaded/blob/master/workspace/changelog.pdf)

# Credits

### Direct Contributions

- LimblessVector
: Project Lead, Designer, Programmer/Developer, Art Direction/Implementation

- dreamsyntax
: Programmer/Developer, Widescreen, work on Heroes Power Plant, other misc tools

- TheHatedGravity
: Model, Movie, Widescreen, Font (Universal MET)

- BlazinZzetti
: Code Contributor, Developer of Shadow SX

### Thanks

- SEGA and Sonic Team
: for the original Shadow the Hedgehog

- igorsabra4
: for Heroes Power Plant and other file reversing assistance

- Sewer56
: for HeroesONE Reloaded and other file reversing assistance

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

- Sanglish, Jesus_PK, TheFetiʂhMachiոe, dreamsyntax's mom
: Custom Hint Translation assistance

- aldelaro5 and DME contributors
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

[Click here to learn how to build from source (not recommended for most users)](https://github.com/ShadowTheHedgehogHacking/ShdTH-Reloaded/blob/master/workspace)