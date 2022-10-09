Merge the GraphicMods and Textures folders to your Dolphin's user folder,
"...Documents/Dolphin Emulator/Load/" if standard mode
or "<folder with dolphin.exe>/User/Load/" if in portable mode
Enable Textures under Dolphin's "Graphics/Advanced/Load Custom Textures" (Prefetch Custom Textures recommended too)
and Enable Bloom Scaling with "Graphics/Advanced/Enable Graphics Mods"

For the HD textures, you will probably need to increase the internal resolution to notice any difference.

Right click the game in the list -> Properties -> Choose the Graphics Mods tab and check the "Native Resolution Bloom" option
This will reduce Bloom offset issues, though to get perfect bloom offset you
must disable "Graphics/Hacks/Vertex Rounding" !!WHILE THE GAME IS RUNNING!! - this is due to how dolphin ini overrides work.
You will notice a 1px width bar on the edge of the screen that bleeds colors, but bloom will be properly offset (only at odd resolutions at this time, ex 3x, 5x, 7x...) 