---
edit_uri: https://github.com/Omni-guides/Tuxborn/wiki/Tuxborn-1.2-beta-information
---

This page is a roundup of information on what's in the 1.2 beta release of Tuxborn.

## ‼️ Important disclaimers ‼️

1. All content here will be subject to change without warning as testing on the beta build proceeds! So please keep checking back for any new updates.
2. All content here is pertinent ONLY to the beta build, and should not be considered canon for the current official build, 1.1.3, or any build earlier than that.
3. Content here should not be considered final. It is subject to change based on results of the beta, and how soon we will be able to proceed to making it a full release. So while a bunch of what we cover here is _probably_ going to be in the final official build, this is _not_ guaranteed.
4. Content here should not be considered full and complete. It's based entirely upon Anna's direct playtesting experience with 1.2 test builds, as well as conversations with Ouroboros. Anna will keep adding to this page as she continues to playtest the beta and get more familiar with what's in it.
5. Content here is not in its final form either. Once we're closer to releasing 1.2 officially, it will be better integrated into the rest of the wiki at large. For now, it will stay on this page as a quick reference for everything known about the beta.

## How to get the beta

The beta build is only available as an optional file on the [Files tab](https://www.nexusmods.com/skyrimspecialedition/mods/114206?tab=files) of Tuxborn's page on Nexus. You can download it from there. Procedure to install would be more or less the same as installing the official build using either Wabbajack or Jackify. You'd just need to install from disk using that specific Wabbajack file.

1.2 is _not_ save safe with 1.1.3, so if you have a 1.1.3 install right now with a playthrough you care about keeping, DO NOT INSTALL THE BETA ON TOP OF IT. You will lose your playthrough. So if you want to install the beta _and_ keep your 1.1.3 playthrough running, you will need enough additional storage space on your computer or device to allow for this.

## How to report bugs if you see them

You can use the #txbn-support channel for this. Putting something in the subject line to make it clear that it's for the beta build specifically is encouraged. "Beta" or "1.2 beta" or "[1.2 beta]", whatever works for you.

If you want to be thorough, please also search the support channel to see if anyone else has already seen your issue. Keep an eye as well on the Known issues section of this page. Anna will keep that list up to date for any issues that come to her directly.

Things to include in a bug:

1. Any crash logs. You can find locations of crash logs on your platform on the pinned "Important Information and FAQs" post in the support channel.
2. Any relevant screenshots and/or video. If you need any help on how to take screenshots in Tuxborn, have a look at [Frequently Asked Questions: Taking screenshots and Photo Mode](Frequently-Asked-Questions:-Taking-screenshots-and-Photo-Mode/). The parts of that page about Photo Mode are NOT relevant to the beta, but everything else on that page is.
3. Your platform and profile.

You may ask Anna to doublecheck any issue you come across if you wish, to see if she can reproduce the problem.

## Areas that need extra eyes for testing

Anna plays on Steam Deck so has that aspect covered, at least for non-MCO profiles.

Players who've enjoyed the BFCO profiles, additional eyes on the MCO profiles is good for all platforms, including Steam Deck. Make sure the MCO animations aren't doing anything funky.

TSP has been testing on PC, but additional PC testers certainly wouldn't hurt.

And any players testing on non-Deck handhelds (ROG Ally, Legion Go, etc.) would be definitely welcome.

Read down the rest of this page for specifics on various areas where testing would be good.

## Changes in profiles in MO2

All BFCO profiles now replaced by MCO equivalents, so all animations related to BFCO should now have MCO equivalents.

The controls configuration used in the BFCO profiles should still be the same though. So if you were previously playing on one of the BFCO profiles, you can choose the MCO equivalent of it, and your control configuration should be the same. If it's not, please report it as an issue on #txbn-support.

## Base game content changes

See [Anniversary Edition content in Tuxborn 1.2 beta](Anniversary-Edition-content-in-Tuxborn-1.2-beta/) for an overview of changes made to Anniversary Edition content.

## Updates for existing mods from previous builds

Where relevant, everything we’ve kept should be updated to latest versions (and yes this includes Community Shaders, we should now be running a current version of that).

### Static Skill Leveling

Static Skill Leveling is no longer in Optionals, as Ouroboros considers it a core part of his vision for the list. 

If you choose to deactivate it, this will count as a Rule 11 moving forward. Previous advice re: not deactivating it on a save in progress still applies. If you turn it off, you _must_ start a new save.

### Shades of Mortality

<details>
<summary><i>Full info on changes with Shades of Mortality...</i></summary>
<br>

Shades of Mortality is also no longer in Optionals, and configuration file has changed from an INI to a TOML file.

The TOML file will contain the same various options previously contained in the INI file, and you can still change it to customize whatever aspects of Shades may not appeal to you. You will just need to look in a different file to do so. The path to the new file is:

`/mods/Shades of Mortality - Death Alternative SKSE/SKSE/Plugins/shades.toml`

The information provided on [Frequently Asked Questions: Shades of Mortality](Frequently-Asked-Questions:-Shades-of-Mortality/) regarding how to change certain behaviors, such as making it not eat your gold when you die, is still accurate aside from what file you have to change. Use that other link for reference.

There will be new behavior with this mod, in that you will see the Death’s Grip nerf up to THREE TIMES now in your effects list, not just once. The reason for this is because the mod has been rewritten from the ground up, and now there is an individual nerf for each attribute. It is possible to therefore see one, two, or three instances of the nerf.

However, you can still cure all occurrences of the nerf by a single cure. All cures described on the FAQ for Shades still apply.

Since Shades is no longer optional in the load order, turning it off will _also_ count as a Rule 11 moving forward. However, the potential still exists for it to interfere with certain parts of Wheels of Lull and Tools of Kagrenac. See [Mod overview: Wheels of Lull](Mod-overview:-Wheels-of-Lull/) and [Mod overview: Tools of Kagrenac](Mod-overview:-Tools-of-Kagrenac/) for further details. So you may find that you'll still need to temporarily turn off the mod to make it through the problem spots in those two mods. Just be sure to turn it back on again to return from the Rule 11 state, unless you plan to keep Shades off permanently!

Two important notes for Shades in the 1.2 beta, though:

1. The Death's Grip nerf is currently deactivated for all character types. Ouroboros is experimenting with settings and may be refining them further in the next beta update. All players on the current beta build, you'll still see the ghost effect kick in if you take a killing blow, but you won't see the Death's Grip nerf activate. Expect further information on this when we do a new build.
2. Bringing Wintersun back in means that it is now once more possible to cure diseases by praying at altars and shrines. This has, however, caused an issue with Shades. Styxx, author of the mod, says that the intent is that praying at altars or shrines _should_ cure the Death's Grip nerf. It currently does _not_. We're investigating this and it may be fixed in a later Tuxborn release. For now, please assume that while praying at altars and shrines will cure diseases again, it will _not_ cure Death's Grip.
</details>

### Apocalypse

<details>
<summary><i>Apocalypse has been updated, and fans of Ocato's Recital should take note...</i></summary>
<br>

We've updated Apocalypse to the latest version available. If you're a fan of that particular pack of spells, _especially_ if you're a fan of Ocato's Recital, be advised that Apocalypse has rejiggered that spell, to smooth out its being rather OP.

Ocato's still exists, but now it only lets you store _one_ spell rather than three, as is the case in 1.1.3. Now, there will be two additional spells that you can use alongside Ocato's as you level Alteration.

The new spells are:

- Medora's Memory, Adept level spell, fires off at combat the same as Ocato's, but at 2x the normal spell duration
- Silmane's Spell Sentinel, Expert level spell, fires off _every 30 seconds_ in combat

So these changes are critical to know if you've been relying on Ocato's for your build. _Especially_ if you're specializing in magic.

Other changes to Apocalypse spells may now also be in play, so if you see an Apocalypse spell behaving differently than what you're used to, the update to the mod will probably be why.
</details>

### Now using full version of JaySerpa's Destroy the Dark Brotherhood mod

We are removing Unfaltered Virtue, the mod we were previously using to overhaul the plotline destroying the Dark Brotherhood. We'll be swapping that out in favor of the full version of JaySerpa's Destroy the Dark Brotherhood - Quest Expansion mod. Previously, we'd just been using the version of JaySerpa's mod that impacted your being kidnapped by Astrid.

### Fix for guard armors not being displayable in Legacy of the Dragonborn's museum

<details>
<summary><i>Can you finally display all the guard armors in the LOTD museum now? Yes! Yes you can!</i></summary>
<br>

Tuxborn has been using Sons of Skyrim, a mod that overhauls the appearances of the armor worn by the guards in every Skyrim hold. Up to build 1.1.3, we had an issue with the guard armors for Solitude and Whiterun being the only ones known to be displayable in the Dragonborn Gallery.

We had been trying to run the appropriate patch to make the armors displayable with LOTD. However, Sons of Skyrim 2.0 adds its versions of the armors as brand new pieces, whereas Sons of Skyrim 1.5 does the armor changes via replacers. Ouroboros determirned that 1.5 works better in conjunction with LOTD, so we have rolled Sons of Skyrim back to that version.

So now all hold guard armors should be properly displayable. This impacts helmets, shields, and the armor piece. Boots and gloves are _not_ displayable. LOTD's guard armor displays don't expect the boots and gloves, so Sons of Skyrim's LOTD patch is behaving in accordance with that.

Some of the holds have variants of armor that will not be displayable, such as the Markarth Light Guard armor. But in each hold, you should find at least one example of a displayable helmet, armor, and shield.

Expected behavior with this patch is that you should in theory be able to buy guard pieces from blacksmiths in the various holds. Failing that, especially in the smaller holds, guards are frequently casualties of dragon attacks. So you might want to scan the immediate area after killing any dragons, just to see if there are any dead guards whose gear you need to appropriate. Some holds have guards stationed outside their capital cities (Solitude, Whiterun, the Rift), but this is not universal. See the table under the prompt below for more details.

<details>
<summary><i>Some suggestions on where to look for armor as follows...</i></summary>
<br>

| Hold | Blacksmiths | Notes
| --- | --- | --- |
| Eastmarch | Oengul | No Eastmarch guards are known to patrol anywhere outside of Windhelm, so Windhelm's blacksmith is likely to be your best bet here unless you manage to trigger a dragon attack in Windhelm. (TBD: whether you can get this armor off of any dead Stormcloaks.) |
| Falkreath | Lod | | 
| Haafingar | Beirand | Haafingar guards are known to patrol around Dragon Bridge, in addition to the guards on duty in Solitude. |
| Hjaalmarch | Al'Hassan | Al'Hassan is a Redguard merchant added in Morthal by Interesting NPCs. He runs a forge, so he _might_ have the Morthal guard armor for sale. |
| The Pale | Rustleif, Seren | One Pale guard is also known to patrol that road that leads past Loreius Farm, if you're heading along that road from Whiterun. |
| The Reach | Ghorza, Moth | Running the Forsworn Conspiracy and letting the Forsworn rampage their way out of the city is a guaranteed way to kill a whole bunch of Markarth guards at once. So if you haven't already bought the pieces off any relevant Markarth merchant, you can always try that. |
| The Rift | Balimund | Riften gets frequent dragon attacks, which can kill the guards at the gate _or_ any of the guards at nearby farms. Failing that, there are known Rift guards in Ivarstead and at Sarethi Farm, and there are also always dead ones at Shor's Watchtower. |
| Whiterun | Warmaiden's, Eorlund Gray-Mane | Depending on how badly your battle with Mirmulnir at the watchtower goes, you may have one or more Whiterun guard casualties there. The dragon is also known to drop vanilla-style Whiterun guard armor as loot, which also is still displayble. But if you want Sons of Skyrim style pieces, check the dead guards during that battle. If you get through the battle without any guard casualties, check the vendors in Whiterun to see who's selling the pieces. A few other places where Whiterun guards may be found on duty: Riverwood (after the part of the main quest where Balgruuf orders a detachment sent there), Whitewatch Tower, and the road that runs right by Honningbrew Meadery, which is good for at least two or three guards. |
| Winterhold | N/A | Since Winterhold doesn't have its own blacksmith, Winterhold guards will be your best bet for this. Failing that, be on the lookout for any guards that might die during the part of the College plotline where you have to kill the magic anomalies in the town. Or, look for the one Winterhold guard that patrols near Whistling Mine. |
</details>
</details>

## Brand new mods added

### Subclasses of Skyrim 2

We're adding a mod called [Subclasses of Skyrim 2](https://www.nexusmods.com/skyrimspecialedition/mods/98784), which allows further refinement of your character and their skills. This adds a new "Destiny" custom skills menu, for which you'll periodically get perks through the normal course of your play, for a total of 7 perks and 35 possible paths. See the mod link for additional details.

### New spell packs

We have some more new spells available!

* [Immersive Illusion Spells](https://www.nexusmods.com/skyrimspecialedition/mods/142357): What it says on the tin. 15 additional spells for the Illusion school of magic
* [Lost Grimoire SSE](https://www.nexusmods.com/skyrimspecialedition/mods/4455): Adds 115 additional spells to our load order, that do a wide variety of things. Notable new spells so far include:
    - Bound Chest
    - Bound Pickaxe
    - Bound Woodcutter's Axe

### New monsters

We're expanding the set of creature mods from modder Mihail, so be on the lookout for new monsters to fight in the wild.

In particular, be on the lookout for [Elemental Golems](https://www.nexusmods.com/skyrimspecialedition/mods/106477). They _will_ be a serious problem for lower level characters, and the frost golem is known to spawn just north of Meridia's shrine near Solitude. Be very, _very_ cautious heading that way. Gear up _very_ well, or bring a squad of followers.

Also, we have [female giants](https://www.nexusmods.com/skyrimspecialedition/mods/44490) now!

### New followers

Here are the two new followers officially added to the beta:

* [Follower overview: Sa'chil](Follower-overview:-Sa'chil/)
* [Follower overview: Varinia](Follower-overview:-Varinia/)

There is a third follower who's a surprise mystery follower, who we will _not_ be discussing on this page, because we want it to be a surprise. ;)

### New craftable armor and outfits

We are adding a _lot_ of new craftable armor and clothing items to the list, too many to list here, so we will not for the sake of brevity. Suffice to say you have a bunch more craftable armor options now.

And craftable clothing items as well, if you want to play a mage build! There are even now outfit options for alchemists and bards. These will be a way to use all those linen wraps you can find in draugr tombs, if you're so inclined.

### Overhauled NPC appearances

A lot of the NPCs will look different now, as we're using a collection of NPC overhauls by the modder SassiestAssassin, the same creator responsible for the wonderful Project ja-Kha'jay, also in our load order!

Look for [Children of the Hist](https://www.nexusmods.com/skyrimspecialedition/mods/98103), [Children of the Ash](https://www.nexusmods.com/skyrimspecialedition/mods/122165), [Children of the Green](https://www.nexusmods.com/skyrimspecialedition/mods/122164), [Children of the Pariah](https://www.nexusmods.com/skyrimspecialedition/mods/97981), and [Children of the First](https://www.nexusmods.com/skyrimspecialedition/mods/122167) on Nexus for some examples.

Note also that the replacer we're using for Lydia has also updated, so she'll look different than she did in the 1.1.3 build. More info on this at [Lydia of Whiterun - SerketHetyt's Housecarls](https://www.nexusmods.com/skyrimspecialedition/mods/127167).

### Fix for Steam Deck console and RaceMenu issues

This is a big important thing in the beta for all Steam Deck players! We're trying out [RaceMenu OverlayFix and Various Mod Fixes](https://www.nexusmods.com/skyrimspecialedition/mods/138586), which has shown in preliminary testing to be a very promising fix for prior issues with the console crashing on Steam Deck. We think it may also fix issues in RaceMenu as well.

So Steam Deck players, do please test this and let us know your results! If you run into issues, please report them to #txbn-support.

### New quest and dungeon mods

We are adding some new quest and dungeon mods!

For the Vicn fans, [DAc0da](https://www.nexusmods.com/skyrimspecialedition/mods/134405) is now available in Tuxborn as of the beta. Note that DAc0da has _not_ been voiced in English yet, so what voicing you'll hear for that mod is AI-generated via ElevenLabs.

Some other known quest and dungeon mods we're adding include:

* [Behind and Beyond](https://www.nexusmods.com/skyrimspecialedition/mods/137361)
* [Elden Root - A Tale of Valenwood](https://www.nexusmods.com/skyrimspecialedition/mods/76341)
* [Hammet's Dungeon Pack 1](https://www.nexusmods.com/skyrimspecialedition/mods/12186)
* [Hammet Dungeon Pack 2](https://www.nexusmods.com/skyrimspecialedition/mods/95339)
* [Miasma](https://www.nexusmods.com/skyrimspecialedition/mods/167571)
* [Once We Were Here](https://www.nexusmods.com/skyrimspecialedition/mods/149820)
* [Redeeming Fultheim - A Blades Quest Addon](https://www.nexusmods.com/skyrimspecialedition/mods/136788)

Side note about Hammet's Dungeon Pack 1: this mod's description on Nexus says it adds five additional followers to the game. In our load order, we are _not_ including those followers, as we already have a bunch of followers available.

### Handheld Lanterns

<details>
<summary><i>New lantern type! Highly recommended for those who find Tuxborn's light levels a problem in the early game...</i></summary>
<br>

We still have the previous craftable lanterns we were using, but now we also have versions of them that you can hold like a torch. They also have physics enabled! Check 'em out at [Handheld Lanterns](https://www.nexusmods.com/skyrimspecialedition/mods/135973).

A notable thing about these new lanterns is, they're easier to make than the other ones, all you need is any junk lantern you might happen to find in dungeons or ruins. You will be able to make any of the handheld lantern types at a forge with any junk lantern. They will basically look a lot like the wearable lanterns and will cast the same kind of light, but they'll be handheld rather than wearable. So you may be able to make these faster than the wearable types, to get a confirmed useful light source.

Also, pro tip: a junk lantern is one of the things that can possibly spawn in the Museum Spoils chest in the Hall of Heroes office in LOTD's museum. So if you take the Relic Hunter start, or otherwise get started early on LOTD, be sure and check there to see if a lantern is in the spawned loot. If one is, you can have a guaranteed handheld lantern as soon as you take that to a forge.

See below in the Known issues section for an issue Anna reported with these lanterns.
</details>

### SearchUI

This is a tool Ouroboros is adding to make finding things you'd normally try to do during the console easier. It works by giving you a search prompt, where you enter a text string describing the thing you want. It will then open up a temporary chest that contains things that match your search string, and you can pull what you want out of that.

For purposes of the beta, this can be used as a tool to make testing certain things faster.

Once we go live with this build, recommended use of this tool would be for situations where you are _supposed_ to get a quest reward, but for some reason, it doesn't spawn. An example of this would be Tuxborn's known periodic issue where, if you're playing the vanilla version of the quest to get the Ebony Mail, Boethiah's champion isn't actually carrying it. Doing it this way would be easier and safer for players who aren't comfortable with working with the console.

### Main Menu Video

[Animations](https://www.nexusmods.com/skyrimspecialedition/mods/160238) on the main menu screen!

## Mods returning from previous builds

### Wintersun

We're bringing Wintersun back! This was made possible by TSP identifying a fix for an issue with Wintersun that could KILL YOU in previous Tuxborn builds. So now we get to have Wintersun back. All hail TSP for making this possible. ❤️

This now means that your choice of deity _will_ be relevant to your character build again. Choose wisely!

### Nether's Follower Framework

<details>
<summary><i>What to know about the impact of bringing NFF back to Tuxborn...</i></summary>
<br>

The return of NFF re-opens the possibility of using it to allow a subset of available followers to live with you at the Safehouse! This will apply only to followers you can control with NFF, but that's a fairly large set of followers, as follows:

* All base game followers, including Rulnik Wind-Strider, added by the AE quest A Dying Wish
* Lydia, who even though she's modded is still running vanilla-compatible code
* All followers from Interesting NPCs
* Ralya and Runs-With-Sticks from our mod that expands Cidhna Mine
* Any Warden of the Coast followers that survive the plot, once you finish that mod; Warden followers revert to running vanilla code when the questline is complete

For standalone custom followers: unless their pages on Nexus explicitly say that it's safe for you to do so, don't try to add them to NFF, you will likely break them. So whether or not you can have any given custom follower live with you at the Safehouse is still going to depend upon what options that follower has available in their code. Several of our custom followers do have options to let you pick a home for them, but not all of them.

Known custom followers who can be invited to live at the Safehouse or any other player home: Katana, Megara, Shale, Xelzaz, Remiel.

Unknown yet whether the two new followers we're bringing in (Varinia and Sa'chil) have "live at this specific house" options, everybody be on the lookout for those.

Lucien can't be invited to live at a specific player home, but he will sandbox indefinitely in any place you tell him to wait, so this is almost as good. Jesper, who is known to be running the same core code Lucien is, will also likely have this behavior if you choose to run him.
</details>

### Obsidian Weathers and Seasons

We're returning to using Obsidian Weathers and Seasons in the beta, which is why the overall look and feel of light and color is going to be different from 1.1.3. Please note a known issue pertaining to this, down in the Known issues section.

## Mods removed for the beta

### Photo Mode

<details>
<summary><i>No more Photo Mode, moving forward...</i></summary>
<br>

Photo Mode has been removed from Tuxborn in the beta. The reason for this is, for many builds now, Photo Mode has had a known issue with breaking your ability to move around if you try to use it in a BFCO profile.

All other methods of taking screenshots in Tuxborn described in [Frequently Asked Questions: Taking screenshots and Photo Mode](Frequently-Asked-Questions:-Taking-screenshots-and-Photo-Mode/) still apply.

The main things this will cost us are:

1. No longer having the fancy effects Photo Mode allowed you to put into screenshots
2. The ability to turn off the UI for screenshot purposes

If you want to put Photo Mode back, or if you want something else that will let you turn off the UI for screenshots without having to resort to the console, you'll need to Rule 11.

If you don't want to Rule 11, for now you will need to activate the console and use the `tm` command to turn off the UI before you take a screenshot. Use the same command to turn it back on again.
</details>

### Other removed mods

<details>
<summary><i>Details on more things that have been removed, and why...</i></summary>
<br>

The following mods are known to have been removed in the beta:

* Rebalancing Anniversary Edition
* On a Crimson Trail
* Starfrost and Survival Mode Improved
* Undeath
* Quest Journal Overhaul
* Underwhelming Multiple Followers
* Pilgrim and related patches
* Azurite Weathers and Seasons, and Azurite III - HDR
* QuickLoot
* Trade and Barter
* Photo Mode (as described above)
* Knight of the North
* Unfaltered Virtue

Rebalancing Anniversary Edition was a big source of questions we kept getting along the lines of "I'm supposed to be able to do X in Anniversary Edition content but can't, what's wrong?" The removal of RAE means that in most cases, requirements for starting AE quests will now match vanilla. However, some parts of the AE are still impacted by other things in our load order, such as LOTD. See [Anniversary Edition content in Tuxborn 1.2 beta](Anniversary-Edition-content-in-Tuxborn-1.2-beta/) for further information.

On a Crimson Trail has been removed because it was known to be buggy in its attempt to provide a framework quests for the various Alternative Armors quests. And since we're removing the Alternative Armors quests, which are themselves _also_ known to be buggy, On a Crimson Trail is no longer relevant. So it's out.

Undeath was removed for reasons of it being repeatedly buggy, especially if you tried to play a vampire/vampire lord while also being a lich at the same time.

Quest Journal Overhaul was removed due to it having some recurring ongoing issues with marking stuff as New that wasn't _actually new_ in your journal. It also mangled the journal display on PCs if you play with controller but happened to hit the J key on your keyboard.

QuickLoot was removed due to bugginess in certain mod areas (such as Carved Brink) that caused crashes if you tried to unlock and open certain chests. It also had issues with interfering with base game functionality, such as feeding on sleeping NPCs as a vampire, gathering blood samples for Septimus, or harvesting a briar heart for Neloth during Tel Mithryn side quests.

Knight of the North was removed because it was basically overhauling the quest for acquiring the items in the Divine Crusader Creation in the AE. But the problem with this was that LOTD was _also_ overhauling that quest, and the two versions of the quest were not playing nicely with one another. So KotN has been removed to resolve this conflict.

Unfaltered Virtue is known to have a breaking bug if Sybille Stentor dies before you launch it. Our load order also includes Unmasking Sybille, and killing her _is_ a possible outcome of that mod! (TBD: Confirm with Ouro that this is the reason for removing this mod.)
</details>

## Miscellaneous other changes

We have removed the ability to smelt down junk items at a smelter. The reason for this is, adding all those smelting recipes _is_ a performance hit to the game. So in the beta, we recommend you sell junk items to vendors instead and use the gold to buy crafting mats, or other supplies you might need. This _will_ impact your available inventory, of course. So you may need to make more use of the Stash Supplies spell, or any other methods of improving your carry weight as detailed at [Carry Weight in Tuxborn](Carry-Weight-in-Tuxborn/).

## Known issues

<details>
<summary><i>Running list of Known Issues, as observed by or reported to Anna...</i></summary>
<br>

1. Obsidian’s power for configuring color profiles has been removed, it was causing issues with Community Shaders, with everything rendering black if you chose the “Bleak” profile while outside. We are already seeing reports that Obsidian may be causing additional issues. So all players testing the beta, please keep a sharp eye on the overall color levels for your install, and see if anything looks like a texture hasn't been properly loaded.
2. In prior playtesting, Anna saw some issues with invisible opponents while playing Carved Brink. This, too, is a possible issue with that mod not playing nicely with Community Shaders.
3. Under certain conditions, you may see prominent flickering if you're standing near a fire in an otherwise dark room, such as the common room at the Bannered Mare. This is a Community Shaders thing as well, and not a thing Ouro can actually fix at this time.
4. Alert players may notice Val Serano is present in the downloads directory once you finish installing, but he is NOT present in MO2. We _were_ going to try including Val as a follower, but we discovered issues with him in pre-beta playtesting, and for now Ouro has therefore yanked him from being installed. He just hasn't been cleaned up out of the list of things downloaded for the build yet. So please disregard. (Apologies in advance for anyone who's a Val Serano fan from other Skyrim playthroughs!)
5. There is a major clipping issue reported in Haemar's Shame, of two different versions of the statue of Clavicus Vile overlapping badly! (There _are_ actually supposed to be two versions, a different version is put in by There is No Umbra, but they are NOT supposed to overlap that badly.) Ouro has already fixed this for the next update.
6. There is a weird flickering texture problem at Half-Moon Mill, reported on the support channel already, and Ouro has fixed this for the next update.
7. One particular type of tree has been rendering _very_ dark in the beta build, specifically the type that has the ID of TreePineForest03. It's practically black, with occasional hints of dark green. Thanks to excellent detective work by player Harrald Hairy-Breeks (thanks Harrald! 🎉), we know the root cause of this, the Lightwood Trees mod we are trying out in the beta. Ouro will be taking appropriate action to correct this in the next update.
8. You may see the AE quest A Dying Wish launch for no apparent reason, even if you haven't done the preliminary things necessary to launch it (read the relevant note in Dead Man's Drink, and visited Roadside Ruins). We are not currently aware of the root cause of this, and we're investigating.
9. There is a major clipping issue going on with the heavy Imperial Armor cuirass, originally reported by samman1v and reproduced by Anna, where a female character's bosom will clip right through that cuirass. And unlike when a female character isn't wearing any clothes, said bosom won't be covered by underwear, either. This has been confirmed so far to reproduce on Legate Rikke as well as the player, if you happen to be wearing this cuirass!
10. If you play in first person and you're using one of the new handheld lanterns, the positioning on the lantern seems to have issues. You may see the lantern swing completely out of your view, although it _will_ continue to work. Anna has reported this and it is under investigation. This appears to only impact first person; third person shows the lantern hanging in your hand as expected.
11. Players have reported a couple incidents of the player character outright vanishing. This does not appear to be beta-specific, it has also reproed in 1.1.3. But if anyone sees this happen in the beta, do please report in on the support channel. We're investigating and could use more information. At this time signs are suggesting that this might be specific to playing on the PC, as Anna has never reproduced this on the Deck.
12. The new Royal Elven armor set, which you'll most likely see worn by members of Thalmor patrols, seems to have a texture problem when worn by female characters. This has so far been confirmed to repro on one of Anna's test characters (a female Altmer), and on Jenassa the mercenary. Also confirmed to repro on the Tuxborn - Deck profile as well as Tuxborn - Desktop, but does _not_ repro on Tuxborn MCO - Desktop. This will require additional checking.
</details>