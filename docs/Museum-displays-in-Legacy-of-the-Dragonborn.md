---
edit_uri: https://github.com/Omni-guides/Tuxborn/wiki/Museum-displays-in-Legacy-of-the-Dragonborn
---

This page covers questions on the topic of how to display items in the Dragonborn Gallery, in Legacy of the Dragonborn. See the main [Frequently Asked Questions: Legacy of the Dragonborn](Frequently-Asked-Questions:-Legacy-of-the-Dragonborn/) page for other topics pertinent to LOTD.

## "How do I display an item in the museum?"

There are a few different ways to do this:

1. Use the Display Prep Station in the Hall of Heroes office
2. Use the Display Drop-off chest immediately to the left of the Prep Station
3. Give displayable items to Auryen
4. Place items manually yourself

Using the Prep Station is usually the least complicated way to display items, as it will take everything in your inventory that's displayable. However, this can sometimes backfire on you, as it will _not_ care if the displayable item is a quest item! It will also not care if it's a thing you might actually want to use. The best known way to prevent this from happening is to mark a quest item or useful item as a Favorite, because the station _will_ check for that.

If you want a bit more direct control over what things get displayed, consider using the chest, or give things to Auryen. That way you'll know for sure that a thing to be displayed is a thing you specifically _intend_ to be displayed.

Last but not least, you can also take items to their display locations yourself, if you know where they belong in the museum. In most cases, all you'll need to do is simply place the item on the intended display. Some known exceptions to this are:

1. The Armory, where you'll need to place items in the storage cabinet to the left of the stairs when you come in
2. The gems display in the Gallery of Natural Science
3. The cabinet for the Jewelry display on the second floor of the Hall of Heroes

If you don't know where to put a particular item, you can almost always find out where it belongs by looking it up on [the LOTD wiki](https://legacy-of-the-dragonborn.fandom.com/wiki/Legacy_of_the_Dragonborn_Wiki).

## "How can I tell if an item is displayable in the museum?"

<p>Our load order handles this by three symbols, provided via these mods working together:</p>

* [The Curator's Companion](https://www.nexusmods.com/skyrimspecialedition/mods/38529)
* [moreHUD](https://www.nexusmods.com/skyrimspecialedition/mods/12688)
* [moreHUD Inventory Edition](https://www.nexusmods.com/skyrimspecialedition/mods/18619)

These three mods should make the symbols visible in these scenarios:

* The item is in your inventory
* You're viewing items in a chest, a dead body you're looting, or any other type of container
* You're viewing the inventory of a shopkeeper or any other type of merchant, such as a Khajiit trader
* The item is in the area around you, and you look at it without picking it up

As described on the Curator's Companion page linked here, there are three main types of symbols to look for. Click over to the mod page to see what the symbols look like. All of them have a dragon head symbol that represents the museum, and the variants of the symbol are:

* Blue plus sign: this means the item is new to you and you have not displayed it yet (if it's a unique item), or any other items of that type (if it's not a unique item)
* Yellow dot: this means the item is one you've seen before, but is still not displayed yet
* Green checkmark: this means the item is displayed in the museum, or an item of the same type already is

One caveat for this is that the Curator's Companion mod is known to be a little flaky when tracking items that have known variants, such as the backpacks from the Anniversary Edition. See below for more info on this.

## "I want to make a replica of something, but the replica recipe doesn't show up at the station!"

The replica stations have some fairly strict rules about when you can make a replica of a displayable item. Two big things to check first are, making sure you don't have it favorited, and also that it's not equipped, tempered, or enchanted. If you want to use the original item, make a replica _first_, and then improve the original in whatever way you see fit.

Also, if the item is a quest item you'll turn in at the end of the quest, you probably won't see a replica option for it at the station until after you've turned in the item.

Last but not least, some items just will flat out not have replica recipes. Not all displayable items do.

See the LOTD wiki page for [Replica Stations](https://legacy-of-the-dragonborn.fandom.com/wiki/Replica_Station) for more info.

If you are not sure whether the item you want to make a replica of has a recipe to do so, look that item up on [the LOTD wiki](https://legacy-of-the-dragonborn.fandom.com/wiki/Legacy_of_the_Dragonborn_Wiki). LOTD's official wiki is generally good about stating whether or not you can make a replica of something at all. So if the wiki doesn't say you can, assume this is intended behavior on LOTD's part.

If you have your heart set on both using and displaying an item that doesn't have a replica recipe you can use at the station, your only real solution for this will be to get into the console and spawn an extra copy. Best practice for that would be to, again, doublecheck the item on LOTD's wiki. They will most likely have the relevant item ID included under Technical Info for the item, in a sidebar.

## "How can I get displayable versions of all the guard armor sets for the Armory?"

We are using Sons of Skyrim in our load order, which changes up all the various hold guard armors. Gear you might get off a dead guard is _not_ going to be displayable by default, usually. So here are the known methods you can use to get displayable versions of those armor pieces for your museum:

* For Whiterun, Mirmulnir will drop the vanilla-style Whiterun pieces as loot when you take him out at the watchtower.
* For Solitude, Beirand the blacksmith sells displayable versions of the Solitude armor pieces. There are also loose Solitude armor pieces lying around his forge as well as around the corner in Castle Dour, but those _are_ marked "Steal". So if you want to nab them, take appropriate precautions before you try to pick them up.

Other possible things to check:

* Armor pieces may show up as loot in chests
* Visit blacksmiths _or_ general vendors in all of the rest of the holds to see whether or not they include displayable armor pieces in their inventories

Worst case scenario, you may need to spawn copies of the missing armors in your console. We'll add more info on how to do that as we confirm it.

## "I already displayed an item, but another item of that same type tells me it's still displayable, is this a bug?"

LOTD is known to be a little flaky when trying to process items for display where there are known possible variations of the item. This most commonly happens with items added to Skyrim by the Anniversary Edition, but is _not_ limited to those.

Example AE items where this is known to reproduce include but are not limited to:

* [Backpacks](https://en.uesp.net/wiki/Skyrim:Adventurer%27s_Backpack)
* [Necromancer robes](https://en.uesp.net/wiki/Skyrim:Necromantic_Grimoire)
* All five versions of the [dual-school mage robes](https://en.uesp.net/wiki/Skyrim:Arcane_Accessories)
* [Brawler gauntlets](https://en.uesp.net/wiki/Skyrim:Fearsome_Fists) (museum display can take both enchanted and unenchanted versions of these, so that counts as multiple versions)

Tuxborn has no way to fix this, since it's a LOTD-side issue. Suggested way to handle this is to limit your display of such items to a known specific type of that item. For example, display only the AE backpacks that have no bedrolls. Or, limit the dual-school mage robes to only one skill level, such as Novice.

Refer to the given links for the specific AE Creations for which this is known to be a problem. A full list of [all AE Creations](https://en.uesp.net/wiki/Skyrim:Creation_Club) is available on the UESP, and you can use that for reference, in case you run into any AE items not mentioned specifically here.

Base game items where this is known to also be a problem include:

* Mythic Dawn Robes (there are two versions, with and without a hood)

Please report to Annathepiper any other items that show this behavior, whether or not they are part of the wiki, and she'll update this page to add them.

## "Are Fate Cards useful for something? They aren't displayable?"

Individual Fate Cards aren't useful for anything, but full decks of them _are_. Each full deck of Fate Cards gives a buff to the player, as documented [on the LOTD wiki](https://legacy-of-the-dragonborn.fandom.com/wiki/Fate_Cards). Players who like to do crafting may want the Deck of Builders in particular, as this is one of the few ways in Tuxborn's load order to buff your Smithing, Alchemy, and Enchanting. Thieves may well want the Deck of Shadows. And loot goblins, the Deck of Travelers.

The various decks of Fate Cards are also all displayable. So even if you don't care about the buff available off any given deck, you can still display it in your museum.

Individual cards drop all over the game as loot. There are also some loose ones lying around in the Safehouse.

And if you are missing any specific cards, you can go visit [Varicio the Collector](https://legacy-of-the-dragonborn.fandom.com/wiki/Varicio_the_Collector), who hangs out in the New Gnisis Cornerclub in Windhelm. He'll trade cards with you. So you can use him as a means to try to get any specific cards you want.

## "How can I get the Imperial Dragon and Storm-Bear armor sets for display without running Battle of the Champions?"

Our load order blocks players from running Battle of the Champions without committing to a side in the civil war. However, if you don't _want_ to run the civil war, the armor pieces in question have also been distributed out to officers on both sides, both named and generic. So it should still be possible for you to acquire the pieces.

Captain Aldis in Castle Dour wears the Imperial Dragon armor, and he is _not_ set Essential. Since dragons are very likely to strafe Solitude during an LOTD run, any dragon that attacks within range of Castle Dour should cause Aldis and other Imperials to join the fight. And a suitably high-level dragon may in fact kill Aldis. Aldis is therefore your likely best bet as a source for the Imperial pieces.

One other likely bet is to run the plot When The Cat's Away, in the AE content. This is the plot to get the Silver Armor at Lund's Hut, and it will end by you being attacked by an Imperial captain and two East Empire Company guards as soon as you come out of the hut. The captain will probably have Imperial Dragon armor on, although he may not have all of the required pieces.

Sulla, who you will have to fight just before entering Blackreach in Alftand, should be wearing the Imperial Dragon pieces.

The Stormcloak pieces would take a bit more luck and work. You may find officers spawning, alive or dead, as part of the following world encounters:

* Imperials vs. Stormcloaks
* Imperial patrol (with or without prisoner)
* Stormcloak patrol
* Thalmor vs. Stormcloaks
* Scavenger looting dead Imperial and Stormcloak soldiers
* Bandits wearing stolen Imperial armor who hit you up for gold, and then attack you

It's also possible that Valmir may spawn with one set or the other of the pieces, if you run Forelhost in the Rift.

Once you start running LOTD's Shattered Legacy quest, its early stages should take you to the fort at Pale Pass, where there is active combat going on between the Imperials and the Stormcloaks. Officers from both sides may spawn there, so keep an eye on any combat you see happening near you when you're running that part of the plot. You may be able to acquire the necessary pieces this way.

Last but not least, players inclined to thievery may be able to outright steal the pieces from named officers, with Security maxed out to 100 and the Perfect Touch perk unlocked. There should be at least one named officer in all cities in Skyrim, as well as the various military camps. With the exception of Aldis, almost all of these officers will be set Essential. So you won't be able to get their armor unless you steal it off of them.

## "Is there a list of craftable items that are displayable?"

Not really, because a full list would be too large to compile properly. But here are some guidelines:

* Any vanilla armor and weapons that you can make at a forge should be displayable in the Armory, which has displays arranged by gear type, such as Steel, Glass, Ebony, etc.
* Armor sets available via the Alternative Armors Creations in the Anniversary Edition should be craftable to get non-enchanted versions, and in several cases, crafting them will be the only way you can get displayable versions since a bunch of the quests for those armors will give you enchanted versions and you can't display those (example: Spell Knight Armor)

A fast way to figure out what craftable gear is displayable is to scroll through the menu at a forge. Check all the categories you're able to make things in, and you should see which items are displayable via the symbols provided by the LOTD Curator's Companion mod. (See above for further details on that.)

## "Is there an easy way I can get a large amount of crafting materials for making museum display items?"

If you want to try crafting a bunch of armor and/or weapons to quickly fill out your displays in the Armory portion of the museum, you may be stymied by lack of materials. Here are a few tips on how to quickly build up your stash of ore, ingots, and leather strips.

In the first several dungeons and/or mod areas you visit, grab _everything_ that drops from slain enemies, or which you find lying around or in containers as loot. A lot of it can be quickly melted down at smelters, especially the one right in the Safehouse. Some of these items may themselves be displayable, which lets you off the hook for crafting those items yourself. Leather items can likewise be broken down into leather strips at a tanning rack.

If you'd rather sell acquired items instead, you can do that, and build up a stock of gold you can then use to purchase mats you need from merchants.

Some notes on good dungeons for this:

* Helgen Keep: in Tuxborn you won't have the original Skyrim start for Helgen, but you _will_ need to visit the place regardless. If you take the Relic Hunter start in LOTD, one of your objectives will bring you to Helgen as well. It is worth your while to consider venturing partway into Helgen Keep, _even though your objective won't require it_. You won't be able to get all the way through, but you'll find a lot of dead Imperials and Stormcloaks that fought with each other. You can nab all of their gear.
* Bleak Falls Barrow: Grab everything dropped by every draugr you kill.
* Silent Moons Camp: Both versions of the initial LOTD museum fetch quests will send you here. Gear looted from slain bandits is a source of materials as well, not only iron, but maybe also leather.
* Carved Brink: If you run Carved Brink early-ish in your game, once you get to Faceted Stones, you'll see Corrupted Shades dropping various types of corrupted weapons. These aren't useful for anything, but they _can_ be smelted down into moonstone. One of the side quests in Carved Brink will also send you to a mine that contains both ebony and gold ore veins, so you can start building up a stock of those there, too.
* Any Dwemer dungeon will serve as an excellent source of dwarven metal. In general, you'll want to nab each and every scrap metal item you find in Dwemer dungeons, not only for purposes of making displayable armor and weapons, but _also_ because you'll want those items later when you build the Dwemer planetarium inside your museum. So no matter what Dwemer dungeon you enter, _grab everything_. You'll need it.

For best results, turn on the Stash Supplies spell to aid you, because you will of course get overloaded very quickly following this approach.

## "Can I place stolen items on display in the museum?"

You can, but you should exercise caution when doing so, especially if the items are placed inside a container when displayed, such as the jewelry items in the Hall of Heroes. If the item is suitably high value, and you need to take it back off display for some reason, you may risk pissing off Auryen or museum guards if they witness you taking the item.

We therefore recommend that you clear the Stolen flag off of an item by selling it to a fence and buying it back, if at all possible, before you place it on display.

If you just want to store stolen items somewhere in the museum vs. displaying them, your best option will be the storage chests inside the Safehouse, the ones in the same room with the Sell Cart. The only people who'll witness you taking anything out of that storage are any followers you may have active.

Even better, consider stashing items in the smuggler's hold on board the Dev Aveza! More info about that on the [Player homes in Legacy of the Dragonborn](Player-homes-in-Legacy-of-the-Dragonborn/) page.

## "Speaking of stolen items, why is Auryen's Finder's Keepers quest sending me to find a thing I can only get by stealing?"

The Finder's Keepers quest does not actually track whether the item it wants you to find is a thing you can only get by stealing; it just cares about whether you can, in theory, get the item. Player's choice on how to interpret this from an RP perspective, and whether Auryen himself actually knows the item is not acquirable through legitimate means!

If the quest _does_ ask you to fetch a item you could only get by stealing, and you don't actually want to steal the item, then your best course of action will be to tell Auryen you're having trouble finding the artifact. Then he should randomly choose a different one for you to pursue.