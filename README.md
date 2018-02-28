# MC_Utils
Various tools I use to help with Minecraft server administration. Pull requests with additional tools or optimizations (I don't know the first thing about Python, this is my first real go at it) are absolutely welome. Let's make a solid toolkit for server admins everywhere!

## Requirements:
Python 3.x

By using NEI to dump csv files and then copying those files to the same directory as the python scripts, you can easily search for a mod by name to get a list of every biome, block, enchantment, item and potion effect that comes from that mod printed out for you. I use this to gather information about how much impact removing a mod from a server could have. I can't always think of every block, item, etc that a mod might add, so this allows me to easily find out if I can remove a mod with minimal impact on inventories of players, blocks in the world, etc.

```
python csvProcessor.py <MODNAME TO SEARCH>
```

### Example usage:
```python csvProcessor.py enviromine```
will output
```
Caves:enviromine.world.biomes.BiomeGenCaves
enviromine:gas:enviromine.blocks.BlockGas
enviromine:firegas:enviromine.blocks.BlockGas
enviromine:elevator:enviromine.blocks.BlockElevator
enviromine:davy_lamp:enviromine.blocks.BlockDavyLamp
enviromine:firetorch:enviromine.blocks.BlockFireTorch
enviromine:offtorch:enviromine.blocks.BlockFireTorch
enviromine:burningcoal:enviromine.blocks.BlockBurningCoal
enviromine:flammablecoal:enviromine.blocks.BlockFlammableCoal
enviromine:esky:enviromine.blocks.BlockEsky
enviromine:freezer:enviromine.blocks.BlockFreezer
enviromine:no_phys_block:enviromine.blocks.BlockNoPhysics
enviromine:elevator:enviromine.items.ItemElevator
enviromine:davy_lamp:enviromine.items.ItemDavyLamp
enviromine:badWaterBottle:enviromine.items.EnviroItemBadWaterBottle
enviromine:saltWaterBottle:enviromine.items.EnviroItemSaltWaterBottle
enviromine:coldWaterBottle:enviromine.items.EnviroItemColdWaterBottle
enviromine:rottenFood:enviromine.items.RottenFood
enviromine:spoiledMilk:enviromine.items.ItemSpoiledMilk
enviromine:camelPack:enviromine.items.EnviroArmor
enviromine:gasMask:enviromine.items.EnviroArmor
enviromine:hardHat:enviromine.items.EnviroArmor
potion.enviromine.heatstroke:enviromine.EnviroPotion
potion.enviromine.frostbite:enviromine.EnviroPotion
potion.enviromine.dehydration:enviromine.EnviroPotion
potion.enviromine.insanity:enviromine.EnviroPotion
```
