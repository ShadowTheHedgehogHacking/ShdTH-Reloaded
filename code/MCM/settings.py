#!/usr/bin/python
# This Python file uses the following encoding: utf-8

# Written in Python v2.7.12 by DRGN of SmashBoards (Daniel R. Cappel).
version = 4.4
# Modified for Shadow The Hedgehog USA Memory Regions (Set Game version 1.06 when picking Shadow ISO) by dreamsyntax
# 4.4.1 last tested version - dreamsyntax

# Find the official thread here for usage and other documentation: 
# http://smashboards.com/threads/melee-code-manager-easily-add-codes-to-your-game.416437/
from collections import OrderedDict


# The value below affects the Code Offset Converter in the Tools tab. If set to False, the search will be much slower, but 
# will also have a little better chance of finding a match.
quickSearch = True

# globalFontSize can set the default size of the program's font, even apart from your system's (OS dependant) settings.
# Negative values indicate pixel size, while positive values are standard font points.
globalFontSize = -12

# So far, the value below is only used for determining a default revision when adding new code changes for a mod in the Mod Construction tab.
# You should also have a DOL by this revision in the Original DOLs folder to add such code changes to a mod.
defaultRevision = 'NTSC 1.06' # Should follow the revision string convention of "[region] [version]"

# The following will ensure that the mod "Enable OSReport Print on Crash" is always installed in your game, as
# long as it's also found in your Mods Library. Change this to False if you don't want this behavior.
alwaysEnableCrashReports = False

# Below are hex ranges that indicate safe areas (free space) for custom code. Between each set of parenthesis, you have the start of a region, followed 
# by the end of that region. You may add new regions, as long as you follow the same formatting that you see here.
#
# (I recommend making a copy of this file or the line(s) you modify, in case you make a mistake or
# would like to undo it later. Then, you can just comment out the back-up line(s) by preceding it with a '#'.)
#
# Remember that each entry needs to be followed by a comma, except for the last one.
# If you'd like to remove all of these regions, you still need to preserve the variable here;
# just make it equal to an empty pair of brackets, i.e. "commonCodeRegions = {}"
#
# You may also add regions. Just be sure that you know what you're doing and have tested the region, and that no regions overlap with one another!
customCodeRegions = OrderedDict([
    ( 'NTSC 1.06|Gen Regions', [ ( 0x4AC, 0x23E0 ) ] ), # Total space: 0x1F34 - This is what we use in Shadow the Hedgehog modding
	# The regions in this first list are the same between all game revisions, hence "ALL" specified for the code region.
	( 'ALL|Common Code Regions', [ ( 0x2C8, 0x398 ), ( 0x39C, 0x498 ), ( 0x4E4, 0x598 ), ( 0x5CC, 0x698 ),			# 0xD0,  0xFC,  0xB4, 0xCC 	= 0x34C
								 ( 0x6CC, 0x798 ), ( 0x8CC, 0x998 ), ( 0x99C, 0xA98 ), ( 0xACC, 0xB98 ),			# 0xCC,  0xCC,  0xFC, 0xCC 	= 0x360
								 ( 0xBCC, 0xE98 ), ( 0xECC, 0xF98 ), ( 0xFCC, 0x1098 ), (0x10CC, 0x1198 ),			# 0x2CC, 0xCC,  0xCC, 0xCC 	= 0x530
								 ( 0x1220, 0x1298 ), ( 0x1308, 0x1398 ), ( 0x1408, 0x1498 ), ( 0x1508, 0x1598 ),	# 0x78,  0x90,  0x90, 0x90 	= 0x228
								 ( 0x15F0, 0x1698 ), ( 0x16CC, 0x1898 ), ( 0x18CC, 0x1998 ), ( 0x19CC, 0x1E98 ),	# 0xA8,  0x1CC, 0xCC, 0x4CC = 0x80C
								 ( 0x1ECC, 0x1F98 ), ( 0x1FCC, 0x2098 ), ( 0x20CC, 0x2198 ) ] ),					# 0xCC,  0xCC,  0xCC 		= 0x264
																														# Total space of above:  0x1874 Bytes

	( 'NTSC 1.02|20XXHP 4.07 Regions', [ ( 0x18DCC0, 0x197B30 ), 		# Tournament Mode Region 	(0x9E70)
									#	 ( 0x32B96C, 0x32C208 ),		# Area 4 of USB/MCC 		(0x89C)		< Can be included if you remove the PAL FSM List
										 ( 0x32C998, 0x332834 ), 		# Extra USB/MCC Region 		(0x5E9C)
										 ( 0x39063C, 0x3907F4 ),		# Area 5 of USB/MCC 		(0x1B8)
										 ( 0x407540, 0x408F00 ), ] ),	# Aux Code Regions 			(0x19C0)
																				# Total space = 0x11884 Bytes (Or 0x12120 if you add Area 4 of MCC)

																								#______________
	( 'NTSC 1.02|20XXHP 5.0 Regions', [ ( 0x39C, 0x498 ), ( 0x8CC, 0x998 ), ( 0x9CC, 0xA98 ),		#          \
										( 0xECC, 0xF98 ), ( 0xFCC, 0x1098 ), ( 0x1308, 0x1398 ),	  #         \_____ Subset of Common Code Regions (0x87C bytes)
										( 0x1508, 0x1598 ), ( 0x15CC, 0x1698 ), ( 0x18CC, 0x1998 ),	    #       |
										( 0x1ECC, 0x1F98 ), ( 0x20CC, 0x2198 ),					#______________|
										( 0x18DCC0, 0x197B30 ), 				# Tournament Mode Region 	(0x9E70)
										( 0x32BA70, 0x32C208 ),					# Most of Area 4 of USB/MCC (0x798)
	 									( 0x32C998, 0x332834 ), 				# Extra USB/MCC Region 		(0x5E9C)
										#( 0x39063C, 0x3907F4 ), ] ),			# Area 5 of USB/MCC 		(0x1B8)
										( 0x39063C, 0x39078C ), ] ), 			# Area 5 of USB/MCC 		(0x150) # Ended early for space for codes with static location
																						# Total space = 0x10E70 Bytes

	# The following regions are used for the multiplayer tournament mode (which of course will no longer be functional if you use this space). 
	# If you use this space, you may want to add a code that prevents people from accessing this mode so that the game doesn't crash when someone tries to use it.
	( 'NTSC 1.02|Tournament Mode Region, P1', [ ( 0x18DCC0, 0x18E8C0 ) ] ), 	# Total space: 0xC00
	( 'NTSC 1.01|Tournament Mode Region, P1', [ ( 0x18D674, 0x18E274 ) ] ), 	# Total space: 0xC00
	( 'NTSC 1.00|Tournament Mode Region, P1', [ ( 0x18CDC0, 0x18D9C0 ) ] ), 	# Total space: 0xC00
	( 'PAL 1.00|Tournament Mode Region, P1', [ ( 0x18E804, 0x18F404 ) ] ), 		# Total space: 0xC00
	# These regions are part of one contiguous space, and are separated here so that the 
	# Aux Code Regions can remain vanilla, allowing use of the "Enable OSReport Print on Crash" code.
	( 'NTSC 1.02|Tournament Mode Region, P2', [ ( 0x18E8C0, 0x197B30 ) ] ), 	# Total space: 0x9270
	( 'NTSC 1.01|Tournament Mode Region, P2', [ ( 0x18E274, 0x1974E4 ) ] ), 	# Total space: 0x9270
	( 'NTSC 1.00|Tournament Mode Region, P2', [ ( 0x18D9C0, 0x196DE4 ) ] ), 	# Total space: 0x9424
	( 'PAL 1.00|Tournament Mode Region, P2', [ ( 0x18F404, 0x1986A0 ) ] ), 		# Total space: 0x929C
	# The tournament mode regions for versions other than 1.02 have not yet been tested. Please let me know the results if you test them.

	# The regions below are for the unused 'USB Screenshot' feature, described here:
	# http://smashboards.com/threads/the-dol-mod-topic.326347/page-11#post-19130116
	# More accurately known as parts of the "MCC Regions" (Dolphin OS Multi-Channel Communication API)
	
	# If these are used for custom code, then the following changes also need to be made: 
	# 0x1a1b64 --> 60000000, 0x1a1c50 --> 60000000 (nops branch links to these regions; these are DOL addresses for v1.02)
	# MCM will handle the nops above for you if these regions are used, so these notes are just mentioned here in case you want to do something manually.
	( 'NTSC 1.02|Screenshot Regions', [ ( 0x22545c, 0x225644 ), ( 0x329428, 0x329640 ), ( 0x32a890, 0x32a9a0 ), ( 0x32b96c, 0x32c208 ), ( 0x39063c, 0x3907f4 ) ] ),
	( 'NTSC 1.01|Screenshot Regions', [ ( 0x224cd4, 0x224ebc ), ( 0x328750, 0x328968 ), ( 0x329bb8, 0x329cc8 ), ( 0x32ac94, 0x32B530 ), ( 0x38f95c, 0x38fb14 ) ] ),
	( 'NTSC 1.00|Screenshot Regions', [ ( 0x22414c, 0x224334 ), ( 0x327b00, 0x327d18 ), ( 0x328f68, 0x329078 ), ( 0x32a044, 0x32A8E0 ), ( 0x38e778, 0x38e930 ) ] ),
	( 'PAL 1.00|Screenshot Regions', [ ( 0x2272cc, 0x2274b4 ), ( 0x329704, 0x32991c ), ( 0x32AB6C, 0x32AC7C ), ( 0x32BC48, 0x32C4E4 ), ( 0x390564, 0x39071c ) ] ),
								# Space:		0x1e8 					0x218 					0x110 					0x89c 					0x1b8 				= 0xF64 Bytes Total

	# The following is commented out because it seems to cause crashing. Perhaps another nop is needed. More testing required.
	# The code here relates to playing MTH files, so if you don't need those, this may work for you.
	# ( 'NTSC 1.02|Screenshot Regions', [ ( 0x32C998, 0x332834 ) ] ), # Total space: 0x5E9C Bytes
	# ( 'NTSC 1.01|Screenshot Regions', [ ( 0x32BCB8, 0x331B54 ) ] ),
	# ( 'NTSC 1.00|Screenshot Regions', [ ( 0x32B068, 0x330F04 ) ] ),
	# ( 'PAL 1.00|Screenshot Regions', [ ( 0x32CC78, 0x332B14 ) ] ),

	# The regions below are used for the game's vanilla Debug Menu, which of course will no longer be functional if you use this space.
	# The Debug Mode itself (DbLevel) may still work to some extent, but you would at least need a new method to enter it.
	( 'NTSC 1.02|Debug Mode Region', [ ( 0x3f7124, 0x3fac20 ) ] ), # Total space: 0x3AFC (same for all game versions)
	( 'NTSC 1.01|Debug Mode Region', [ ( 0x3f6444, 0x3f9f40 ) ] ),
	( 'NTSC 1.00|Debug Mode Region', [ ( 0x3f5294, 0x3f8d90 ) ] ),
	( 'PAL 1.00|Debug Mode Region', [ ( 0x3f7ecc, 0x3fbae8 ) ] ),

	# These are unused areas containing text used for debugging the game, and have been tested to be safe for overwriting.
	# However, they will disable the use of OS Report features, such as in the useful "Enable OSReport Print on Crash" code.
	# CrazyHand places the FSM Engine and FSM Entries directly after this region.
    ( 'NTSC 1.06|Aux Code Regions', [ ( 0x407540, 0x4088B0 ) ] ),
	( 'NTSC 1.02|Aux Code Regions', [ ( 0x407540, 0x4088B0 ) ] ), # Total space: 0x1370
	( 'NTSC 1.01|Aux Code Regions', [ ( 0x406860, 0x407BD0 ) ] ),
	( 'NTSC 1.00|Aux Code Regions', [ ( 0x405580, 0x4068F0 ) ] ),
	( 'PAL 1.00|Aux Code Regions', [ ( 0x408400, 0x409770 ) ] ),

	# The following regions are only for use with extended NTSC 1.02 SSBM DOLs
	# Part 1 of Data Section 8
	( 'NTSC 1.02|Gecko Code Handler Storage', [ ( 0x4385E0, 0x4395E0 ) ] ), # 0x1000
	# Part 2 of Data Section 8
	( 'NTSC 1.02|Gecko Code List Storage', [ ( 0x4395E0, 0x446EE0 ) ] ), # 0xD900

])


# The Gecko hook (set below) intercepts the game's normal execution to point to the Gecko Codehandler with a standard branch.
# Warning: do not change the hook offsets unless you've first fully uninstalled all Gecko codes from your game.
# Otherwise, the old hook will still remain in your game, and your game will not run unless you manually remove it.
#
# If the regions used for the codelist or codehandler are changed, the next time you open the program and game/DOL,
# any previously installed Gecko codes will not be detected (because the program will be looking in the new region for 
# them), however their code will still be present in the same place as they were before. So you will need to reselect
# and save the mods that you'd like to be installed. And if you want the code in the old regions to be retuned the game's
# original/vanilla hex, use the "Restore" buttons found in the Code-Space Options window (located in the Mods Library tab).
# 
# Note that if Gecko codes are used, the codelist/codehandler will be placed at the start of their respective region,
# defined below. As you can see in the customCodeRegions definitions above, a single region may be one contiguous area, 
# or a collection of several areas. However, any region set for the Gecko codelist or codehandler will only use the first 
# area if there are multiple. The extra space left over in that region may still be used for standard injection mod code 
# and/or standalone functions.
geckoConfiguration = {
	'hookOffsets': { 'NTSC 1.06': 0x177B78, 'NTSC 1.02': 0x3738E0, 'NTSC 1.01': 0x372c00, 'NTSC 1.00': 0x371a2c, 'PAL 1.00': 0x3737e4 },
	'codehandlerRegion': 'Gen Regions', # If Gecko codes are used, the codehandler will be placed at the start of this region (must exist in customCodeRegions)
	'codelistRegion': 'Gen Regions' # If Gecko codes are used, the codelist will be placed at the start of this region (must exist in customCodeRegions)
}
# Recommended defaults:
#	Tournament Mode Region, P2 for the codelist, because it is the largest contiguous area
#	Tournament Mode Region, P1 for the codehandler (Aux Code Regions is a good alternative, but you will lose use of the "Enable OSReport Print on Crash" code)

# The following codehandler is a modified version of the one posted and discussed here: http://smashboards.com/threads/ssbm-dol-that-accepts-gecko-codes.403755/
# This is a fallback, and will only be added to the DOL if Gecko Codes are used and codehandler.bin is not found in the root directory.
geckoCodehandler = ('9421FF58900100087C0802A6900100AC7C0000269001000C7C0902A6900100107C0102A690010014BC6100187F2000A6633A2000735AF9FF7F400124D8410098' # 1 line = 64 bytes
					'D86100A03FE080003E80CC00A3944010639500FFB2B440107FA802A63DE0445261EF474E63E718083CC080007CD03378390000003C6000D06063C0DE808F0000'
					'7C03200040820018808F00047C0320004082000C39EF00084800004C7FA803A6B3944010C8410098C86100A07F2000A6800100AC7C0803A68001000C7C0FF120'
					'800100107C0903A6800100147C0103A6B861001880010008382100A84C00012C4E800020806F0000808F000439EF0008710900012F89000039200000546A1F7E'
					'54653F7E746B1000546301FE4082000C54CC000C480000087E0C83782E0500002C0A000141A0002C41A200E42C0A000341A001AC418202502C0A0005418002D4'
					'41A204E02C0A000741A0050C480005F07D8C1A142C050003418200484181006040BEFF842E0500014191002C548A843E419200107C8961AE392900014800000C'
					'7C89632E39290002354AFFFF40A0FFE44BFFFF54558C003A908C00004BFFFF487C892378409E04C83529FFFF418004C07CA978AE7CA961AE4BFFFFF039EF0008'
					'40BEFF2480AFFFF8816FFFFC54B1043E54AA853E54A5273E2E8500014196001041B500147C8961AE480000107C89632E480000087C89612E7C845A147D298A14'
					'354AFFFF4080FFD44BFFFEDC546907FF418200105508F87E710900012F8900002E8500042D8A00055108083C409E0078418D04B87D8C1A14418C000C41940030'
					'4800001C40940010558C003A816C00004800001C558C003CA16C00007C8920F85529843E7D6B48385484043E7F0B204070A90003418200182C09000241820018'
					'4181001C409A002048000018419A00184800001041990010480000084198000861080001408EFE404194FE3C816FFFF8409E0020706C00084182000C710C0001'
					'41820010398B0010518B033648000008556B0716916FFFF84BFFFE0C40BEFE08546916BA546E87FE2D8E00002E05000470AE00032E8E00024194001441960050'
					'7C6407347C847A14480000685465A7FF4182000C7D27482E7C844A14418E00087C8C22142E8E00014196000880840000546367FF4182003C4090000C7C843214'
					'480000307C848214480000285465A7FF4182000C7D27482E7C844A144090000C7CCC212E4BFFFD807E0C212E4BFFFD784090000C7C8623784BFFFD6C7C902378'
					'4BFFFD6454891E78392900402C05000241800048546B500341820014418100084800001041BEFD404800000840BEFD382C0500034181001041A200107DE7482E'
					'4BFFFD247DE7492E7C64073454841A787DEF22144BFFFD1040BEFD0C7CA74A14409200145464043E91E50000908500044BFFFCF4812500042C09000041A2FCE8'
					'3929FFFF9125000481E500004BFFFCD840BEFCD4546B16BA7F475A14813A0000546E67BE419200842E050005409001742E050003409000902E050001546587FF'
					'418200087C8C22142F0E00014092002441B90018419A000C88840000480000F8A0840000480000F080840000480000E85473E53E41B90020419A001099240000'
					'3884000148000018B1240000388400024800000C91240000388400043673FFFF4080FFD44BFFFC40546587FF418200087C84621471C500014182009C7C844A14'
					'48000094546A87BE548E16BA7E677214409200083A6FFFFC809A000081330000714B0001418200087C9A2378714B0002418200107D334B7840B200087E6C9A14'
					'5465673F2C05000940800054480000797C892214480000407C8921D6480000387D242378480000307D242038480000287D242278480000207D24203048000018' 
					'7D242430480000105D24203E480000087D242630909A00004BFFFB8C2C05000A4181FB84C05A0000C07300004182000CEC43102A48000008EC4300B2D05A0000'
					'4BFFFB647D4802A654A51E787D4A2A14809A0000813300007D4803A64E80002040BEFB445469C03E7D8E6378480000354192000C7E312214480000087D292214'
					'5464C43F38A000004182FB1C7D4588AE7D4549AE38A500017C0520004BFFFFEC2E8A0004553136BA2C11003C7E27882E408200087DD1737841960008A2310000'
					'552956BA2C09003C7D27482E408200087DC9737841960008A12900004E8000202C050004408000287C8923787DC3621455CE003C4BFFFFAD7C8420F85484043E'
					'7D2B20387E2420384BFFFBC4546BE43E4BFFFBBC7C9A23785484183840920020409E000C7DE803A64E8000217DE47A1460000000600000004BFFFA6C2E050003'
					'4191005C3CA048007D836214558C003A4092002040BEFA505744003A7C8C2050508501BA506507FE90AC00004BFFFA3840BEFFBC7D2C7850512501BA90AC0000'
					'398C00047D6F2214396BFFFC7D2B6050512501BA90AB00004BFFFF942E050006419200284BFFFB28558C843E5744843E575A043E7C0C20004180FBA87C0CD000'
					'4080FBA04BFFF9E05745FFFE68A50001710300017C0518004182001C511A0FBC6B5A00025745FFFF418200086B5A0001934FFFFC534807FE4BFFF9AC2C0B0000'
					'418201382C050001418200182C050002418200142C050003418200704BFFF94054CC000C5497463E5498C43E5484063E409E00FC56F906317D9A63787F43D214'
					'575A003A418200187EF707747EF700D01F3700023B3900047F59D0502C1700004182001C3B2000007EE903A6A37A00047F79CA783B5A00024200FFF47C18C800'
					'408200AC4BFFFE905108083C409E009C5477B003418100884180008C547E063E1FDE00025497001E6EF880002C1800004082000862F730005498801E1F3E0004'
					'7F19C0503B2000001F5900047F6FD02E7F57D02E3B3900017C17C040418100347C19F000418100147C1AD8004182FFDC3AF700044BFFFFD0806FFFF860630300'
					'906FFFF892EFFFFC7EF0BB784800001C806FFFF860630100906FFFF861080001480000087C9023785464063E1C8400087DE47A144BFFF8704092000C39000000'
					'48000014546906FF546567FE7D084C305517FFFF408200087D082A785485001F418200087CA62B785485801F418200087CB02B784BFFF8300000000000DEADBEEF000000') 
					# Total size: 0x8C4 bytes (4488 characters). The length of this must be aligned to the nearest 4 bytes.


# For the Menu Text Converter:
menuTextDictionary = {

	# Single-Byte Characters
	'1a' : ' ',  '03' : '\n', # Space, and newLine (line break)

	# English numbers & alphabet			Found in Start.dol
	'2000': '0', '2001': '1', '2002': '2', '2003': '3', '2004': '4', '2005': '5', '2006': '6', '2007': '7', '2008': '8', '2009': '9',
	'200a': 'A', '200b': 'B', '200c': 'C', '200d': 'D', '200e': 'E', '200f': 'F', '2010': 'G', '2011': 'H', '2012': 'I', '2013': 'J',
	'2014': 'K', '2015': 'L', '2016': 'M', '2017': 'N', '2018': 'O', '2019': 'P', '201a': 'Q', '201b': 'R', '201c': 'S', '201d': 'T',
	'201e': 'U', '201f': 'V', '2020': 'W', '2021': 'X', '2022': 'Y', '2023': 'Z',
	'2024': 'a', '2025': 'b', '2026': 'c', '2027': 'd', '2028': 'e', '2029': 'f', '202a': 'g', '202b': 'h', '202c': 'i', '202d': 'j',
	'202e': 'k', '202f': 'l', '2030': 'm', '2031': 'n', '2032': 'o', '2033': 'p', '2034': 'q', '2035': 'r', '2036': 's', '2037': 't',
	'2038': 'u', '2039': 'v', '203a': 'w', '203b': 'x', '203c': 'y', '203d': 'z',

	# Japanese Hiragana						Found in Start.dol
	'203e': 'ぁ', '203f': 'あ', '2040': 'ぃ', '2041': 'い', '2042': 'ぅ', '2043': 'う', '2044': 'ぇ', '2045': 'え', '2046': 'ぉ', '2047': 'お', 
	'2048': 'か', '2049': 'が', '204a': 'き', '204b': 'ぎ', '204c': 'く', '204d': 'ぐ', '204e': 'け', '204f': 'げ', '2050': 'こ', '2051': 'ご', 
	'2052': 'さ', '2053': 'ざ', '2054': 'し', '2055': 'じ', '2056': 'す', '2057': 'ず', '2058': 'せ', '2059': 'ぜ', '205a': 'そ', '205b': 'ぞ', 
	'205c': 'た', '205d': 'だ', '205e': 'ち', '205f': 'ぢ', '2060': 'っ', '2061': 'つ', '2062': 'づ', '2063': 'て', '2064': 'で', '2065': 'と', 
	'2066': 'ど', '2067': 'な', '2068': 'に', '2069': 'ぬ', '206a': 'ね', '206b': 'の', '206c': 'は', '206d': 'ば', '206e': 'ぱ', '206f': 'ひ', 
	'2070': 'び', '2071': 'ぴ', '2072': 'ふ', '2073': 'ぶ', '2074': 'ぷ', '2075': 'へ', '2076': 'べ', '2077': 'ぺ', '2078': 'ほ', '2079': 'ぼ', 
	'207a': 'ぽ', '207b': 'ま', '207c': 'み', '207d': 'む', '207e': 'め', '207f': 'も', '2080': 'ゃ', '2081': 'や', '2082': 'ゅ', '2083': 'ゆ', 
	'2084': 'ょ', '2085': 'よ', '2086': 'ら', '2087': 'り', '2088': 'る', '2089': 'れ', '208a': 'ろ', '208b': 'ゎ', '208c': 'わ', '208d': 'を', 
	'208e': 'ん',

	# Japanese Katakana						Found in Start.dol
	'208f': 'ァ', '2090': 'ア', '2091': 'ィ', '2092': 'イ', '2093': 'ゥ', '2094': 'ウ', '2095': 'ェ', '2096': 'エ', '2097': 'ォ', '2098': 'オ', 
	'2099': 'カ', '209a': 'ガ', '209b': 'キ', '209c': 'ギ', '209d': 'ク', '209e': 'グ', '209f': 'ケ', '20a0': 'ゲ', '20a1': 'コ', '20a2': 'ゴ', 
	'20a3': 'サ', '20a4': 'ザ', '20a5': 'シ', '20a6': 'ジ', '20a7': 'ス', '20a8': 'ズ', '20a9': 'セ', '20aa': 'ゼ', '20ab': 'ソ', '20ac': 'ゾ', 
	'20ad': 'タ', '20ae': 'ダ', '20af': 'チ', '20b0': 'ヂ', '20b1': 'ッ', '20b2': 'ツ', '20b3': 'ヅ', '20b4': 'テ', '20b5': 'デ', '20b6': 'ト', 
	'20b7': 'ド', '20b8': 'ナ', '20b9': 'ニ', '20ba': 'ヌ', '20bb': 'ネ', '20bc': 'ノ', '20bd': 'ハ', '20be': 'バ', '20bf': 'パ', '20c0': 'ヒ', 
	'20c1': 'ビ', '20c2': 'ピ', '20c3': 'フ', '20c4': 'ブ', '20c5': 'プ', '20c6': 'ヘ', '20c7': 'ベ', '20c8': 'ペ', '20c9': 'ホ', '20ca': 'ボ', 
	'20cb': 'ポ', '20cc': 'マ', '20cd': 'ミ', '20ce': 'ム', '20cf': 'メ', '20d0': 'モ', '20d1': 'ャ', '20d2': 'ヤ', '20d3': 'ュ', '20d4': 'ユ', 
	'20d5': 'ョ', '20d6': 'ヨ', '20d7': 'ラ', '20d8': 'リ', '20d9': 'ル', '20da': 'レ', '20db': 'ロ', '20dc': 'ヮ', '20dd': 'ワ', '20de': 'ヲ', 
	'20df': 'ン', '20e0': 'ヴ', '20e1': 'ヵ', '20e2': 'ヶ',

	# Punctuation							Found in Start.dol
	'20e3': '　', '20e4': '、', '20e5': '。', # These are the "ideographic"/Japanese space, comma, and period (the space here is not the same space character found under '1a')
	'20e6': ',', '20e7': '.', '20e8': '•', '20e9': ':', '20ea': ';', '20eb': '?', '20ec': '!', '20ed': '^', '20ee': '_', '20ef': '—', # '20ef' is an "em dash" (U+2014)
	'20f0': '/', '20f1': '~', '20f2': '|', '20f3': "'", '20f4': '"', '20f5': '(', '20f6': ')', '20f7': '[', '20f8': ']', '20f9': '{', 
	'20fa': '}', '20fb': '+', '20fc': '-', '20fd': '×', '20fe': '=', '20ff': '<', '2100': '>', '2101': '¥', '2102': '$', '2103': '%', # '20fd' is not simply another x, but a multiplication sign (U+00D7)
	'2104': '#', '2105': '&', '2106': '*', '2107': '@',

	# Japanese Kanji						Group 1, Found in Start.dol
	'2108': '扱', '2109': '押', '210a': '軍', '210b': '源', '210c': '個', '210d': '込', '210e': '指', '210f': '示', '2110': '取', '2111': '書',
	'2112': '詳', '2113': '人', '2114': '生', '2115': '説', '2116': '体', '2117': '団', '2118': '電', '2119': '読', '211a': '発', '211b': '抜',
	'211c': '閑', '211d': '本', '211e': '明',

	# Misc Items, Set 1						Found in SdMenu.usd				(Only accessible if the game is set to English)
	#'4000': 'é', '4001': '〇', '4002': 'Ⅱ', '4003': '王', '4004': '国', '4005': '山', '4006': '頂', 	# 4002 seems to be a Roman numeral 2

	# Misc Items, Set 2						Found in SdMenu.dat				(Only accessible if the game is set to Japanese)
	'4000': '々', '4001': '「', '4002': '」', '4003': '『', '4004': '』', '4005': '♂', '4006': '♀', '4007': '〇', '4008': '→', '4009': 'Ⅱ', # The corner brackets are quotation marks in East Asian languages

	# Japanese Kanji						Group 2, Found in SdMenu.dat 	(Only accessible if the game is set to Japanese)
	'400a': '亜', '400b': '暗', '400c': '以', '400d': '位', '400e': '意', '400f': '医', '4010': 'ー', '4011': '員', '4012': '隠', '4013': '右', # 4010 may instead be 一
	'4014': '宇', '4015': '影', '4016': '映', '4017': '液', '4018': '越', '4019': '円', '401a': '援', '401b': '演', '401c': '炎', '401d': '遠',
	'401e': '奥', '401f': '応', '4020': '横', '4021': '王', '4022': '屋', '4023': '俺', '4024': '音', '4025': '下', '4026': '化', '4027': '仮',

	'4028': '何', '4029': '価', '402a': '加', '402b': '可', '402c': '果', '402d': '歌', '402e': '花', '402f': '課', '4030': '過', '4031': '牙',
	'4032': '画', '4033': '介', '4034': '会', '4035': '解', '4036': '回', '4037': '壊', '4038': '怪', '4039': '悔', '403a': '懐', '403b': '界',
	'403c': '開', '403d': '外', '403e': '崖', '403f': '鎧', '4040': '格', '4041': '獲', '4042': '学', '4043': '楽', '4044': '割', '4045': '活',

	'4046': '巻', '4047': '看', '4048': '管', '4049': '観', '404a': '間', '404b': '含', '404c': '器', '404d': '基', '404e': '期', '404f': '棄',
	'4050': '帰', '4051': '気', '4052': '記', '4053': '貴', '4054': '起', '4055': '技', '4056': '橘', '4057': '客', '4058': '逆', '4059': '久',
	'405a': '仇', '405b': '休', '405c': '宮', '405d': '急', '405e': '球', '405f': '旧', '4060': '牛', '4061': '去', '4062': '巨', '4063': '距',

	'4064': '競', '4065': '共', '4066': '協', '4067': '強', '4068': '恐', '4069': '況', '406a': '狂', '406b': '狭', '406c': '驚', '406d': '玉',
	'406e': '均', '406f': '禁', '4070': '近', '4071': '金', '4072': '銀', '4073': '具', '4074': '空', '4075': '遇', '4076': '群', '4077': '兄',
	'4078': '型', '4079': '形', '407a': '憩', '407b': '系', '407c': '経', '407d': '計', '407e': '軽', '407f': '撃', '4080': '激', '4081': '決',
	
	'4082': '結', '4083': '月', '4084': '剣', '4085': '見', '4086': '険', '4087': '減', '4088': '現', '4089': '限', '408a': '己', '408b': '五',
	'408c': '後', '408d': '語', '408e': '護', '408f': '公', '4090': '功', '4091': '効', '4092': '向', '4093': '好', '4094': '工', '4095': '抗',
	'4096': '攻', '4097': '行', '4098': '鋼', '4099': '降', '409a': '高', '409b': '号', '409c': '合', '409d': '国', '409e': '酷', '409f': '黒',
	
	'40a0': '今', '40a1': '左', '40a2': '差', '40a3': '再', '40a4': '最', '40a5': '歳', '40a6': '祭', '40a7': '細', '40a8': '菜', '40a9': '在',
	'40aa': '坂', '40ab': '咲', '40ac': '作', '40ad': '削', '40ae': '撮', '40af': '殺', '40b0': '参', '40b1': '山', '40b2': '算', '40b3': '残',
	'40b4': '使', '40b5': '刺', '40b6': '四', '40b7': '士', '40b8': '始', '40b9': '姿', '40ba': '子', '40bb': '止', '40bc': '鰤', '40bd': '試',

	'40be': '事', '40bf': '字', '40c0': '持', '40c1': '時', '40c2': '自', '40c3': '失', '40c4': '質', '40c5': '実', '40c6': '写', '40c7': '射',
	'40c8': '捨', '40c9': '者', '40ca': '邪', '40cb': '若', '40cc': '弱', '40cd': '主', '40ce': '守', '40cf': '手', '40d0': '殊', '40d1': '種',
	'40d2': '首', '40d3': '受', '40d4': '収', '40d5': '拾', '40d6': '終', '40d7': '習', '40d8': '襲', '40d9': '集', '40da': '住', '40db': '十',
	
	'40dc': '獣', '40dd': '重', '40de': '出', '40df': '術', '40e0': '瞬', '40e1': '順', '40e2': '初', '40e3': '所', '40e4': '女', '40e5': '除',
	'40e6': '傷', '40e7': '勝', '40e8': '商', '40e9': '小', '40ea': '少', '40eb': '床', '40ec': '晶', '40ed': '消', '40ee': '章', '40ef': '賞',
	'40f0': '上', '40f1': '乗', '40f2': '城', '40f3': '場', '40f4': '常', '40f5': '情', '40f6': '状', '40f7': '心', '40f8': '振', '40f9': '新',
	
	'40fa': '深', '40fb': '真', '40fc': '神', '40fd': '身', '40fe': '辛', '40ff': '進', '4100': '陣', '4101': '水', '4102': '数', '4103': '寸',
	'4104': '世', '4105': '制', '4106': '性', '4107': '成', '4108': '整', '4109': '星', '410a': '声', '410b': '青', '410c': '積', '410d': '切',
	'410e': '接', '410f': '設', '4110': '絶', '4111': '先', '4112': '専', '4113': '戦', '4114': '泉', '4115': '選', '4116': '前', '4117': '然',
	
	'4118': '全', '4119': '狙', '411a': '素', '411b': '組', '411c': '阻', '411d': '壮', '411e': '掃', '411f': '操', '4120': '早', '4121': '祖',
	'4122': '総', '4123': '走', '4124': '送', '4125': '遭', '4126': '像', '4127': '増', '4128': '足', '4129': '速', '412a': '賊', '412b': '族',
	'412c': '続', '412d': '存', '412e': '損', '412f': '他', '4130': '多', '4131': '太', '4132': '打', '4133': '対', '4134': '耐', '4135': '待',
	
	'4136': '態', '4137': '替', '4138': '隊', '4139': '代', '413a': '台', '413b': '大', '413c': '題', '413d': '択', '413e': '脱', '413f': '誰',
	'4140': '短', '4141': '壇', '4142': '弾', '4143': '断', '4144': '段', '4145': '値', '4146': '知', '4147': '地', '4148': '遅', '4149': '蓄',
	'414a': '着', '414b': '中', '414c': '宙', '414d': '丁', '414e': '挑', '414f': '町', '4150': '調', '4151': '跳', '4152': '長', '4153': '頂',
	
	'4154': '鳥', '4155': '直', '4156': '墜', '4157': '追', '4158': '通', '4159': '定', '415a': '底', '415b': '弟', '415c': '抵', '415d': '程',
	'415e': '敵', '415f': '的', '4160': '適', '4161': '鉄', '4162': '天', '4163': '店', '4164': '転', '4165': '点', '4166': '伝', '4167': '殿',
	'4168': '登', '4169': '途', '416a': '度', '416b': '土', '416c': '倒', '416d': '島', '416e': '投', '416f': '盗', '4170': '当', '4171': '討',
	
	'4172': '逃', '4173': '透', '4174': '頭', '4175': '闘', '4176': '動', '4177': '同', '4178': '道', '4179': '得', '417a': '特', '417b': '毒',
	'417c': '内', '417d': '謎', '417e': '二', '417f': '肉', '4180': '日', '4181': '乳', '4182': '入', '4183': '年', '4184': '能', '4185': '破',
	'4186': '敗', '4187': '背', '4188': '輩', '4189': '配', '418a': '倍', '418b': '売', '418c': '博', '418d': '爆', '418e': '箱', '418f': '半',
	
	'4190': '反', '4191': '番', '4192': '彼', '4193': '飛', '4194': '匹', '4195': '必', '4196': '百', '4197': '氷', '4198': '表', '4199': '評',
	'419a': '秒', '419b': '不', '419c': '付', '419d': '婦', '419e': '富', '419f': '負', '41a0': '部', '41a1': '風', '41a2': '復', '41a3': '物',
	'41a4': '分', '41a5': '文', '41a6': '聞', '41a7': '兵', '41a8': '平', '41a9': '並', '41aa': '別', '41ab': '変', '41ac': '編', '41ad': '返',
	
	'41ae': '保', '41af': '歩', '41b0': '報', '41b1': '抱', '41b2': '放', '41b3': '方', '41b4': '法', '41b5': '砲', '41b6': '訪', '41b7': '豊',
	'41b8': '暴', '41b9': '冒', '41ba': '摩', '41bb': '魔', '41bc': '枚', '41bd': '毎', '41be': '満', '41bf': '味', '41c0': '未', '41c1': '密',
	'41c2': '夢', '41c3': '無', '41c4': '名', '41c5': '命', '41c6': '迷', '41c7': '滅', '41c8': '面', '41c9': '猛', '41ca': '木', '41cb': '目',
	
	'41cc': '問', '41cd': '紋', '41ce': '野', '41cf': '役', '41d0': '優', '41d1': '有', '41d2': '由', '41d3': '裕', '41d4': '遊', '41d5': '余',
	'41d6': '与', '41d7': '容', '41d8': '用', '41d9': '要', '41da': '来', '41db': '頼', '41dc': '落', '41dd': '乱', '41de': '利', '41df': '裏',
	'41e0': '離', '41e1': '率', '41e2': '立', '41e3': '竜', '41e4': '了', '41e5': '涼', '41e6': '量', '41e7': '力', '41e8': '緑', '41e9': '類',
	
	'41ea': '冷', '41eb': '烈', '41ec': '裂', '41ed': '恋', '41ee': '練', '41ef': '連', '41f0': '路', '41f1': '楼', '41f2': '録', '41f3': '惑',
	'41f4': '慄'

	} 
	# Info on editing the images used to display these characters in-game can be found here: https://smashboards.com/threads/changing-menu-text.368452/page-2#post-21591476