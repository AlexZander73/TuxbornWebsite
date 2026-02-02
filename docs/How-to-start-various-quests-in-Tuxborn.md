---
edit_uri: https://github.com/Omni-guides/Tuxborn/wiki/How-to-start-various-quests-in-Tuxborn
---

This page covers how to start various important quests available in the Tuxborn modpack.

Some of this information duplicates what's on the [Vanilla player homes available in Tuxborn](Vanilla-player-homes-available-in-Tuxborn/) and [Mod player homes available in Tuxborn](Mod-player-homes-available-in-Tuxborn/) pages, but since those cases are relevant here, I've called them out here as well.

For content that's part of the base game, including Anniversary Edition content, have a look at [Base game content in Tuxborn](Base-game-content-in-Tuxborn/) to get an idea of how that is impacted by our load order (including the Thieves Guild, the College of Winterhold, Goldenhills Plantation, etc.).

Several of the larger quest mods in our load order have their own overview pages, so we will not cover them there. The individual overviews can be found linked at [Quest mod overviews](Quest-mod-overviews/). Here, we'll cover shorter blurbs about smaller quest mods.

Quests covered on this page include:

* Anniversary Edition quests for armor, homes, or weapons
* Beyond Reach
* Depths of the Reach
* Fan Favorite (Dwarven Mail AE armor)
* The Gray Cowl of Nocturnal
* The Unquiet Dead (Goldenhills Plantation quest)
* Undeath

## Anniversary Edition quests for armor, homes, or weapons

Tuxborn is running Rebalancing Anniversary Edition, which bumps up the level requirements for just about all the homes and armor sets in the AE. So if you're expecting an AE quest to kick off and you haven't seen it do so yet, this is probably why (exception: the quest to get Goldenhills Plantation, see below for more on that).

Also, be aware that some of the very best AE armor sets have had their level requirements bumped up significantly. Example: you will not get the Studded Dragonscale Armor to spawn at Yorgrim Overlook until you're at least level 50. 

Check the MCM for this mod and adjust any level requirements you feel appropriate.

## Beyond Reach

Beyond Reach is one of the mods that will auto-start on you as soon as you reach level 25.

The opening encounter for this will be a priestess of Mara and her bodyguard finding you as soon as you enter any major city in Skyrim. The priestess will react very strongly to you, and will be possessed by Mara herself, who will deliver you an objective to go solve a dire problem "in the west". The priestess' bodyguard will then talk to you, and give you a bit more information, as well as the objective to go find a merchant near Markarth who can take you to the Reach.

## Depths of the Reach

This quest does not auto-start. To trigger it, you will need to visit Deep Folk Crossing. For planning purposes, you might consider running Project AHO first, _or_ the Lost to the Ages quest, since either of these will specifically give you reasons to go find Deep Folk Crossing. Note that AHO will give you an actual quest marker, which could be helpful if you don't already have it on your map. Lost to the Ages will not.

When you reach Deep Folk Crossing, you will find a couple of dead bodies, as well as green swirling smoke along the bridge there. You'll also be attacked by a wraith-like creature.

After you kill it, search the two bodies, and you should find a journal that'll kick off the quest. You may wish to take your time proceeding through this one, as its final boss encounter will be challenging for low-level characters.
 
## Fan Favorite (Dwarven Mail AE armor)

"Fan Favorite" is an Anniversary Edition quest that's supposed let you get an enchanted set of Dwarven Mail armor. However, this quest is known to be buggy, even in the vanilla AE. So you will probably also see it being buggy in Tuxborn. Further complicating the matter, this quest is impacted by On a Crimson Trail, the mod in the Tuxborn load order in charge of coordinating the various Crimson Dirks armor quests.

The way this plot is intended to work is this: just south of Ivarstead, there's a camp with a dead Wood Elf identified as "Arena Fan". He's supposed to have a note on him that will direct you to Bthalft, a bit further south. There, you'll find an Orc you need to kill, from whom you can get the armor.

Thanks to the On a Crimson Trail changes, you can basically go straight to Bthalft and kill the Orc without ever having to find the dead Arena Fan.

However, if you want to stick closer to the original intended flow of this quest and you want to look for Arena Fan's body, be aware that it has issues spawning correctly. If you get to his camp and his body is actually there, he may or may not actually have the necessary note on him. Or, the body may not spawn at all. The UESP wiki page for this quest suggests you try to re-enable the Arena Fan's body by its refID, but so far, no Tuxborn player has reported getting this to work.

Some known console solutions you can try instead are:

1. If you really want to see the Arena Fan's Note, you can use the console to spawn yourself a copy of it into your inventory. Its refID will most likely be FE02D81B. Then you can read the note and proceed to the same quest stage as in option 1. The console command would be `player.additem FE02D81B 1`.
2. If the body hasn't spawned, it's possible it's actually clipped somewhere beneath the ground. So you can try using the `tcl` command in the console to disable collision, so that you can move beneath the ground to look for him. Once you're done with that, make sure you're placed aboveground again, and then turn collision back on using the same command.

Final note: the enchanted items worn by the Orc you kill as part of this quest are _not_ displayable at the LOTD museum. So this quest is mostly useful if you're a completist, _or_ if you want the enchanted armor pieces for yourself or a light-armor-using follower. You should be able to just straight up craft Dwarven Mail armor yourself, for purposes of museum display.

## The Gray Cowl of Nocturnal

The following requirements must be met to launch The Gray Cowl of Nocturnal:

* You must complete The Way of the Voice in the main quest
* You must be at least level 10
* You must steal or pickpocket something

Once all of these requirements are met, you should get a vision of a place you need to go to.

This mod may or may not interest you depending on whether you plan to play a thief. If you _are_ planning to play a thief, then you will meet the requirements to start this mod anyway, as you need to do some preliminary theft in order to get Brynjolf to pay attention to you and launch the Thieves Guild main quest.

If you are _not_ planning on running the Thieves Guild but want to run Gray Cowl of Nocturnal anyway, you might want to put a bit of thought into appropriate circumstances under which an otherwise law-abiding Dragonborn might steal something. (My personal fave for this: stealing things as a moral imperative while running Project AHO.)

## The Unquiet Dead (Goldenhills Plantation)

See the [Goldenhills Plantation](Goldenhills-Plantation/) page for further details on this. We're running CC Farming, which heavily impacts that plot.

## Undeath

You need to fulfill these requirements to be able to launch Undeath:

* Level 30 or above
* Enchanting at 50 or above
* Conjuration at 75 or above

If you meet these requirements, then a note should spawn in the Silver-Blood Inn that you can read to kick off the Undeath questline. You'll need to look in the room immediately to the left of the inn's entrance, the one you sleep in when you rent a room for the night.

(If the note is not immediately obvious, search the room thoroughly. At least one Tuxborn player has reported the note clipping into the floor of the room, as of Tuxborn build 1.1.3.)

## Credits

Thank you to the following players on #txbn-general:

* Arlemy, for bringing to my attention that the Thieves Guild Requirements mod wants you to steal one thing worth 250 septims, not 250 things
* Kok0, for pointing out that you need to launch Way of the Voice in order to be able to run The Gray Cowl of Nocturnal
* Cal, for asking about how to start Undeath, and reporting the issue with the necessary note clipping into the floor