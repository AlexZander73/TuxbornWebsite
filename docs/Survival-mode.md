---
edit_uri: https://github.com/Omni-guides/Tuxborn/wiki/Survival-mode
---

‼️ **All players please be advised that this information applies only to Tuxborn build 1.1.3 and earlier. It will not apply to Tuxborn 1.2 once that build is released, as we will be dropping official support for Survival Mode in that build.** ‼️

## How to launch Survival Mode

Our load order does not prompt you at the beginning of your game about whether you want to turn on Survival Mode, but that doesn't mean it's not available! The option to turn it on is still available in the main game settings, the same as in the vanilla Anniversary Edition.

If you forget to turn on Survival Mode immediately as soon as you launch your playthrough, it should be safe for you to do so at any time. Take note, depending on what Alternate Start option you choose in chargen, it might be specifically wise to not turn on Survival Mode immediately! See the [Shipwrecked Off the Coast](Creating-your-character/#shipwrecked-off-the-coast) section of the [Creating your character](Creating-your-character/) page for details.

## What mods we use that impact Survival Mode

The following mods are the ones of most interest in our load order for a Survival Mode run:

* [Starfrost](https://www.nexusmods.com/skyrimspecialedition/mods/97536)
* [Survival Mode Improved](https://www.nexusmods.com/skyrimspecialedition/mods/78244), which Starfrost is based off of
* [Gourmet](https://www.nexusmods.com/skyrimspecialedition/mods/96876), the cooking overhaul, since food is of much greater importance in Survival Mode
* [Blade and Blunt](https://www.nexusmods.com/skyrimspecialedition/mods/34549), because if you're running Survival Mode, Blade and Blunt's injury system will turn on

Read up on these if you want some information in advance to plan your Survival Mode run.

## ‼️ IMPORTANT WARNING ABOUT FAST TRAVEL ‼️

Fast travel is not turned off by default in Survival Mode in our load order. It _is_ possible to turn it off, in the appropriate INI file.

However, we very strongly recommend you do _not_ turn off fast travel. If you do, it will break the Dev Aveza in Legacy of the Dragonborn, which relies on fast travel being active in order to work. This is not an issue Tuxborn can fix, since it's a conflict of functionality between how LOTD handles the airship, and how Survival Mode Improved handles turning off fast travel.

If and *only if* you don't actually care about running LOTD in general or getting the Dev Aveza in particular, and you _do_ care about having fast travel explicitly disabled, then the INI file you want is SurvivalModeImproved.ini under "Tuxborn - Settings". You can edit it in MO2 directly, or, edit it from your command line or file explorer at the following path:

`/mods/Tuxborn - Settings/SKSE/Plugins/SurvivalModeImproved.ini`

Inside that file, the very first option is the one that toggles fast travel:

`bDisableFastTravel=0`

But again: **DO NOT TOUCH THIS SETTING IF YOU WANT THE DEV AVEZA TO WORK.**

## How to handle your travel without disabling fast travel

Not disabling fast travel does present a problem for any players who might really want to run a no-fast-travel playthrough, we know! First and foremost, it does mean you'll need to simply develop the habit of not launching fast travel on your own.

But fortunately, our load order does include some additional options to travel around the map, and to make doing so in Survival Mode less onerous. These options include:

* Carriage drivers available in the smaller holds as well as the larger cities
* Ferryboat operators on the largest bodies of water (Lake Honrich, Lake Ilinalta, Sea of Ghosts, etc.)
* Gjalund Salt-Sage's ship the Northern Maiden is still available to take you to Solstheim
* The Dev Aveza and the AHO, both of which not only serve as in-character means of transport, but also as mobile player homes, which could be hugely beneficial in a Survival Mode run
* Major DLC-sized mods that take you out of the main Skyrim worldspace generally will have in-character means to reach them:
    * Ships at the Solitude Docks (Wyrmstooth, Midwood Isle)
    * Wagons you can take to get to your target location (Moonpath to Elsweyr, Beyond Reach)
    * Portal (such as with Gray Cowl of Nocturnal)
* There are a number of [Means of teleportation in Tuxborn](Means-of-teleportation-in-Tuxborn/), including devices and spells, several of which are tied to various player homes, such as Clockwork Castle

## Camping in Survival Mode

Tuxborn does not include a standalone camping mod, but we do have a few options to consider if you want to plan to camp in Survival Mode, especially if you're doing a no-fast-travel run and you haven't acquired either the airship or the AHO yet.

### AE Camping

The Camping content of the Anniversary Edition is still available. This lets you create a set of Camping Supplies at any forge, with a piece of leather and three pieces of firewood. Using any set of Camping Supplies will create a small campsite for you, including a campfire, a crate to sit on, and a lean-to with a bedroll to sleep in.

However, there are three things to be aware of when making Camping Supplies. 

1. Each set of Camping Supplies is good for only one use. You will have to keep making new ones to create different places to camp.
2. A camp made with Camping Supplies will persist until you either explicitly break camp, _or_ use a different set of Camping Supplies to camp someplace else, in which case your previous camp will despawn.
3. Camping Supplies are _heavy_. Be mindful of this in Survival Mode since your carry weight will be nerfed.

### Rains' Shelter

Rains' Shelter is the superior choice for camping, with or without Survival Mode active. This is an item available via Legacy of the Dragonborn, and you don't even have to launch LOTD beforehand if you know where to look. 

See [this section](Frequently-Asked-Questions:-Legacy-of-the-Dragonborn/#rains-shelter) of the [Frequently Asked Questions: Legacy of the Dragonborn](Frequently-Asked-Questions:-Legacy-of-the-Dragonborn/) page for details.

### Gore

Gore has custom camping functionality. So if you pick him up as an early follower, you can take advantage of this. See [his mod page on Nexus](https://www.nexusmods.com/skyrimspecialedition/mods/85298) for more details on how this would work.

## Food and hunger in Survival Mode

Players familiar with vanilla Survival Mode will know that it has a Hunger mechanic, and that you need to eat food on a regular basis lest you get hit with an increasingly worse Stamina debuff.

In our load order, this behavior has been altered by the combo of Starfrost and Gourmet. (See provided links to those mods' pages on Nexus, above.) Gourmet makes a lot of changes to food recipes, and brings in a greater variety of them, with a variety of useful buffs. Starfrost interacts with this, lessening the duration of the buffs provided by Gourmet foods. If you go without eating long enough, you will receive debuffs that will have scaled impacts on how fast your Health, Stamina, and Magicka regenerate, getting worse at each stage. So it does remain in your best interests to eat something on a regular basis. The debuffs are the main difference between how vanilla Survival Mode handles Hunger, and how Starfrost does.

Note also that Starfrost lowers your base Health regeneration by 100%. So stocking up on food that boosts your Health regen back up is a very good idea.

If you want to take advantage of the Gourmet functionality, try to collect as many recipes as you can. Various merchants will sell them. And once you read them, you can make any of those items at a cooking fire or oven, as appropriate. Read up on the mod to get a sense of what buffs the various recipes can provide.

If you don't want to bother to cook your own food but still want to take advantage of food buffs, some recommended other options for this include:

* Get a Homecooked Meal. In Gourmet, this item will give you a different buff than it will in vanilla: it increases your Health, Magicka, and Stamina Regeneration by 50%. But as per vanilla, you can still only get one of these once per day. Options to get one are:
    * Your spouse if you have one
    * Millie in the LOTD museum will make you one on request as well
* If you have [Xelzaz](https://www.nexusmods.com/skyrimspecialedition/mods/62893) as a follower, he can cook for you twice per day
* As part of his camping functionality (see above), Gore can also cook for you
* Katana and her crew (Megara and Shale) can cook for you as well
* If you acquire the AHO via the Project AHO mod, it has a machine on board that can make juices out of raw foods, and these will give you significant buffs when consumed

## Cold in Survival Mode

Starfrost's page on Nexus goes into detail on how it handles cold. It's less punishing on the player than vanilla Skyrim's Survival Mode, but you will still be vulnerable to the weather and should plan accordingly.

See above recommendations re: camping, since you'll need to do that a lot when traversing cold areas. Also see recommendations re: food, and in particular, sources of hot food.

Think very carefully about your armor choices, as you will get better warmth protection off of Heavy Armor than you will Light Armor. You may wish to plan your build around Heavy Armor, accordingly. If you tend to prefer Light Armor, you might also consider a Heavy Armor build specifically for cold parts of the map, and a Light Armor build for the less cold parts.

Keep yourself as healthy as possible, as Starfrost gives you Warmth bonuses for that.

And keep a stock of torches handy, as those can also help. Just be mindful that torches have weight, and since your carry weight will be nerfed, you don't want to carry a crazy amount of torches with you.

## Access to supplies in Survival Mode, and player homes

Put some thought into how to set up your access to supplies in a Survival Mode run. Under normal circumstances in Tuxborn, our having LOTD in our load order pretty much makes all other player homes far less necessary. In Survival Mode, however, those player homes can serve as places you can stop to rest up, _warm up_, and get additional supplies if you need them.

So put careful thought into what player homes you want. A strategically located player home could be truly helpful, especially if it comes well-stocked with necessary crafting stations and is well-supplied!

Also, remember that LOTD does provide access to the Stash Supplies spell on its MCM. Depending on how hardcore you want to be in your RP, you may or may not wish to take advantage of this in Survival Mode. We will however note that while not all things stashed via that spell can be retrieved without returning to the Safehouse, the spell _will_ let you get at Miscellaneous items. And torches and AE Camping Supplies get filed under Miscellaneous.

Likewise, either of the mobile player homes available in Tuxborn could be much more important in Survival Mode, the Dev Aveza in particular. If you get the airship, having it will bypass just about all overland travel you'd otherwise need to do through cold areas. You _will_ still need to travel to various places overland to discover them so that the Dev Aveza can reach them afterwards, so you aren't completely off the hook for traveling in the cold--but you will only have to go to those places overland _once_.

And if you want to deliberately restrict the use of the airship for RP purposes, keep in mind as well that it can also serve as a place to keep heavy supplies, like torches and camping supplies.

## Best followers to consider for Survival Mode

As noted above in previous sections, both Gore and Xelzaz would be strong followers to consider for a Survival Mode run.

Katana and her crew may also be good to consider, as they can all cook for you as noted above, and Megara can heal you and cure diseases.