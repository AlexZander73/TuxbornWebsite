---
edit_uri: https://github.com/Omni-guides/Tuxborn/wiki/Known-quest‐blocking-bugs-in-Tuxborn
---

This page is to cover an assortment of known issues that can block various quests in Tuxborn. Some of these will be vanilla/AE Skyrim content, and some will be related to mods. The vanilla/AE ones we can't do a whole lot about. Mod ones may be fixable, and we'll call out where we can which ones are getting active attention from our devs.

For Steam Deck players in particular, note that solutions for these issues pretty much require you to get into the console. Since we also know that the console regularly crashes if you use the on-screen keyboard, getting a Bluetooth keyboard for use with your Deck is _highly_ recommended. If nothing else so that if you run into any of these problems, you can try these solutions!

Here's the running list of issues we know about so far.

## Vanilla and AE content

### QuickLoot may interfere with certain vanilla side quests

<details>
<summary><i>QuickLoot blocking quests issue...</i></summary>
<br>

There are several side quests in the base game that require you to harvest items off of corpses. Some examples of these are:

1. Harvesting elf blood samples for Septimus during Discerning the Transmundane in the main quest
2. Harvesting a briar heart, from a Forsworn Briarheart, for Neloth during the Dragonborn DLC side quest Briarheart Necropsy
3. Taking an ash sample from an ash spawn, also for Neloth, during the Dragonborn DLC side quest Telvanni Research

In all cases, the base game behavior is that you would activate the corpse as per usual, but get an extra prompt, asking you if you want to harvest what you're looking for, or search the corpse as per usual.

QuickLoot is confirmed to interfere with this functionality in the case of the Briarheart Necropsy quest, and may also do so with the other two. The usual key or button to activate a corpse is used by QuickLoot to let you simply take items off the corpse one at a time. And this blocks you from getting the necessary prompt to continue your quest.

Fortunately, this is easily addressed. You have two options, settings within QuickLoot's MCM:

1. On the General tab, you can disable QuickLoot for corpses in particular while leaving it on for other types of containers
2. On the Controls tab, you can set the two hotkeys for toggling QuickLoot off and on again, and then use those hotkeys to temporarily disable the mod long enough for you to proceed with the quest

Also, you can hit the button that would normally let you search via QuickLoot, which should then bring up the expected prompt.

</details>

### Pillars for control cubes in Nchardak may not let you activate them

<details>
<summary><i>What to do if the control cube pillars don't work...</i></summary>
<br>

This is a known bug in vanilla Skyrim that can reproduce in Tuxborn. When you are running Nchardak on Solstheim with Neloth the wizard, you will need to activate several pillars for the control cubes you're tasked with getting in that ruin. Sometimes these pillars may not actually have an activator on them.

The issue is described on [the UESP page for Nchardak](https://en.uesp.net/wiki/Skyrim:Nchardak), down in the Bugs section. We can confirm that the proposed solution there, leaving the cell and then coming back in, does appear to fix the problem in our load order. So if you see this happen, try that solution. Nchardak has multiple zones, so you should be able to move between cells fairly quickly.

If that does _not_ work for you, additional solutions are available on the UESP page for the associated quest, [The Path of Knowledge](https://en.uesp.net/wiki/Skyrim:The_Path_of_Knowledge#Bugs).
</details>

### Boss doesn't spawn and Word Wall doesn't work in final room when running Bleak Falls Barrow

<details>
<summary><i>Bleak Falls Barrow issues...</i></summary>
<br>

We have had player reports of an issue with Bleak Falls Barrow, when you reach the last room, and two problems happen:

1. The Word Wall for the first word of Unrelenting Force doesn't work
2. The boss doesn't come out of his sarcophagus

If this happens to you, this workaround should work:

1. Exit the dungeon, using the usual exit you'd do if you'd finished it normally
2. Then go back inside the same way
3. To get back up onto the ledge you jumped off of to leave, there should be a prompt to let you climb back up (E if you are playing on PC with keyboard, A button if you're playing on a handheld or with a controller)
4. Return to the Word Wall, which should now be active
5. Boss should now exit his sarcophagus as per normal
</details>

### Can't talk to Clavicus Vile's statue in Haemar's Shame

<details>
<summary><i>Haemar's Shame has, shall we say, some issues...</i></summary>
<br>

Clavicus Vile's statue in Haemar's Shame is vanilla content, but in Tuxborn, we've got a known issue with the statue being impacted by the There Is No Umbra mod. The issue occurs when the player is not able to initiate conversation with Clavicus Vile, just pray at the shrine. And this can block two different quests: A Daedra's Best Friend (vanilla), and There Is No Umbra.

Root cause is that There Is No Umbra is adding an invisible NPC into the space that the original statue occupies. Umbra adds additional lines for Vile, and the mod needed to add in the invisible NPC to implement that. Unfortunately, the original statue and the invisible NPC have overlapping hitboxes, and differently named activators:

* Original statue: Shrine of Clavicus Vile. You need this activator if you're running A Daedra's Best Friend.
* Invisible NPC added by Umbra mod: Shrine to Clavicus Vile. You need this activator if you're running There is No Umbra.

If you're having trouble hitting the right activator, you have a few options to try for fixing this:

1. If looking directly at the statue is not getting you the correct activator, try looking to the statue's left (player's right). There is a separate activator area that runs roughly from Vile's lifted left hand down to his feet.
2. You can also try looking at the statue's feet. This particular option may work better for Steam Deck players.
3. If neither option 1 nor option 2 works for you, try this:

    a. Open your console and use the `tcl` command to turn off collision

    b. Carefully move yourself forward to clip into the statue until you see the activator change to the one you need

    c. Use the activator and proceed with the conversation as your quest requires

    d. Move yourself back out and use the `tcl` console command again to turn collision back on

4. Worst case scenario, try these:

    a. Quest stages for A Daedra's Best Friend can be found on [that quest page](https://en.uesp.net/wiki/Skyrim:A_Daedra%27s_Best_Friend) on the UESP. Use those quest stages in the `setstage` console command to advance the quest as required.

    b. There is No Umbra has a [Walkthrough and Troubleshooting article](https://www.nexusmods.com/skyrimspecialedition/articles/5204) with suggestions on what to do when talking to Vile as part of that quest.

We are investigating a potential patch to address this problem, but any such patch would be applied in Tuxborn's next release. So for the time being, please try these workarounds and use whichever one works for you.
</details>

### Bjormund Wind-Strider's body doesn't spawn at the top of the tower at Arcwind Point

<details>
<summary><i>This is a vanilla/AE bug, but it can also repro in Tuxborn 1.1.3...</i></summary>
<br>

The bug is what it says in the header: when you try to finish off Bones for a Crow and you get to the top of the tower at Arcwind Point, you may find that Bjormund Wind-Strider's body isn't actually there.

While this is a general Skyrim/AE bug, there is at least one Tuxborn-specific aspect to this. The Rebalancing Anniversary Edition mod sets a level requirement on Bones for a Crow. You can't launch at _at all_ unless you're level 50 or above. So assuming that you meet that level requirement, that is the only change RAE makes to this quest.

UESP does note the absence of Bjormund's body as a known issue, and offers this console command as a solution:

`player.placeatme FE02681C`

This works in Tuxborn, and will move Bjormund to you. But you may find him to be _alive_, in which case you'll have to fight him. If he spawns alive, he will attack you on sight.

Once you kill him, you'll be able to loot his body for the Dragonbone Mail and the Dragonplate Insulated Helmet, Dragonplate Insulated Boots, and Dragonplate Insulated Gauntlets. This should allow you to resolve the quest.

‼️ **IMPORTANT NOTE: This bug will only reproduce on Tuxborn 1.1.3 or earlier, since we are disabling all of the quests for Alternative Armors in the AE as of 1.2, and that includes the Bones for a Crow quest. So you should not see this occur at all in 1.2.** ‼️
</details>

### Target leader doesn't spawn for radiant Companions quests

<details>
<summary><i>This is also a vanilla bug, but it can reproduce in Tuxborn...</i></summary>
<br>

There are two different radiant quests for the Companions that have known issues with a target you have to kill not actually spawning. These quests are:

* "Trouble in Skyrim", where you're asked to go kill the boss in a variety of locations, such as bandit camps, draugr tombs, etc.
* "Striking the Heart", where you have to go kill a leader of the Silver Hand

In either case, the bug would be when you show up at the location assigned, and there is no actual leader present for you to kill. The UESP and Elder Scrolls wikis both reference this as a potential risk for these quests, and provide some console solutions to try.

If you are running "Trouble in Skyrim", then a potential console command for you to try would be:

`setstage cr05 20`

If you are running "Striking the Heart", try this one:

`setstage cr09 20`

If these solutions don't work for you, here are reference links with additional potential solutions:

* [Trouble in Skyrim on UESP](https://en.uesp.net/wiki/Skyrim:Trouble_in_Skyrim)
* [Striking the Heart on UESP](https://en.uesp.net/wiki/Skyrim:Striking_the_Heart)
* [Trouble in Skyrim on Elder Scrolls Wiki](https://elderscrolls.fandom.com/wiki/Trouble_in_Skyrim)
* [Striking the Heart on Elder Scrolls Wiki](https://elderscrolls.fandom.com/wiki/Striking_the_Heart)
</details>

### Arena Fan's body doesn't spawn if you're trying to find the Dwarven Mail

<details>
<summary><i>Another bug from Alternative Armors quests which can reproduce in Tuxborn 1.1.3...</i></summary>
<br>

This is for the AE quest that lets you get the Dwarven Mail, and this is another one that's known to happen in vanilla AE, not just in Tuxborn. The issue is that if you want to get the Dwarven Mail as part of the AE content, the body of the NPC you're supposed to find often just does not spawn.

In our particular load order, you don't actually _have_ to find the Arena Fan's body, you can go straight to Bthalft and kill the Orc there instead if you want to get this armor.

See the [How to start various quests in Tuxborn](How-to-start-various-quests-in-Tuxborn/) page for a bit more detail on this.

‼️ **IMPORTANT NOTE: This issue will reproduce only in Tuxborn 1.1.3 or earlier. Since we are removing the quests for all Alternative Armor Creations in the AE in Tuxborn 1.2, this problem should no longer occur as of that build.** ‼️
</details>

### Dead guard's body doesn't spawn outside Dragon Bridge

<details>
<summary><i>Yet another Alternative Armors quest that's buggy in Tuxborn 1.1.3...</i></summary>
<br>

If you're trying to run the AE quest Over the Edge to get the enchanted set of Steel Soldier Armor, our load order may have an issue with the body of the dead guard you have to find not spawning by the river. If you can't find that dead guard's body, this will block you from continuing the quest.

If this issue triggers for you, you should be able to get past it with this console command:

`setstage ccBGSSSE058_MiscQuest 40`

‼️ **IMPORTANT NOTE: This issue will reproduce only in Tuxborn 1.1.3 or earlier. Since we are removing the quests for all Alternative Armor Creations in the AE in Tuxborn 1.2, this problem should no longer occur as of that build.** ‼️
</details>

### Kragrash's Letter does not spawn at Ironback Hideout for the Night Hunter quest

<details>
<summary><i>NOT an Alternative Armors quest being buggy, but an AE bug nonetheless...</i></summary>
<br>

The Elite Crossbows Creation has a quest called Night Hunter, which lets you find a cache of fancy crossbows and crossbow bolts at Ironback Hideout. In our load order, the mod called Thwack hooks the Night Hunter quest in with Sorine Jurard's side quests in Dawnguard, making it so that her last quest in her chain sends you to the hideout. And by extension, making it so that the cache of crossbows becomes your final reward for getting schematics for her.

However, you may run into an issue with Kragrash's Letter not spawning correctly at Ironback Hideout. If this happens, use the following console command to unblock the quest and proceed to the point of being able to find Kragrash's body:

`setstage ccBGSSSE043_VampireHunterQuest 20`

So far this is confirmed to reproduce only in 0.5.2, so this is not a high priority issue. But if any player confirms a repro of this in Tuxborn 1.1.3 or in the 1.2 beta, please report it and we'll update this wiki entry appropriately.
</details>

### Gunmar's radiant quest for killing a master vampire breaks if it sends you to Movarth's Lair

<details>
<summary><i>Vanilla bug, but it can reproduce in Tuxborn...</i></summary>
<br>

If you get Gunmar's radiant quest [Cleansing Light](https://en.uesp.net/wiki/Skyrim:Cleansing_Light) for killing a master vampire in Dawnguard, and it sends you to Movarth's Lair, there is a known bug as per the UESP with the quest being blocked from finishing. Movarth's Lair does not have a proper boss set, so it's impossible to clear it. The USSEP tried to fix it, but the attempted fix didn't work and was reverted, as per the UESP [Movarth's Lair](https://en.uesp.net/wiki/Skyrim:Movarth%27s_Lair) page.

So if you get this quest, best recommendation is to try to run Laid to Rest, the Morthal quest to clear that lair, to have in-character grounds to have cleared the place. Killing Movarth will _not_ count for Gunmar's quest because Movarth isn't tagged as a boss, but RP-wise, that'll do.

You can then get the objective to return to Gunmar by entering the following in your console:

`setstage DLC1RH02 100`
</details>

### Target animal doesn't spawn for Companions Animal Extermination quest

<details>
<summary><i>Another vanilla bug with Companions radiant quests that can repro in Tuxborn...</i></summary>
<br>

Adding to the set of Companions radiant quests known to be potentially janky, the ["B" variant of the quest Animal Extermination](https://en.uesp.net/wiki/Skyrim:Animal_Extermination_(B)) can sometimes fail if the location you're sent to is one you've already cleared. In that scenario, the animal you're supposed to kill doesn't re-spawn, so you have nothing there to kill, and therefore you're blocked from finishing the quest.

In Tuxborn's load order, this quest can also potentially ask you to clear out a den of werewolves. If the location you're sent to normally has some other kind of animal (such as [Clearspring Cave](https://en.uesp.net/wiki/Skyrim:Clearspring_Cave), which by default is supposed to have a troll), then a similar problem could occur.

If you see either scenario occur for this quest, try the UESP's recommended console fix:

`setstage cr02 20`

This should mark the location as cleared for you, and let you return to Jorrvaskr to turn in the quest.
</details>

## Known issues with mods

### Cannot talk to the Khajiit in Falkreath to launch Moonpath to Elsweyr

<details>
<summary><i>If you see that the Khajiit by Falkreath won't talk to you...</i></summary>
<br>

We've had a couple of players report an issue with not being able to launch Moonpath to Elsweyr, even if they meet the known requirements for doing so (at least level 18, The Way of the Voice completed, 70+ displays). They were blocked by not being able to talk to either Verina or Ku'rana, by their wagon in Falkreath.

If this happens to you, then try these steps to resolve:

1. Wait for 24 hours in-game
2. Save your game
3. Relaunch

This should hopefully make you able to talk to the Khajiit and successfully launch Moonpath.
</details>

### Killing Sybille Stentor prior to running Unfaltered Virtue breaks Unfaltered Virtue

See [Mod overview: Unfaltered Virtue](Mod-overview:-Unfaltered-Virtue/) for details on this.

### Daedric pillar blocks access to a lever to open a gate in Jaws of Oblivion quest in Warden of the Coast

We have a known issue with a Daedric pillar blocking access to a locked gate while running this quest. More details, and steps for a fix, on the [Mod overview: Warden of the Coast](Mod-overview:-Warden-of-the-Coast/) page.

### The opening quest for The Tools of Kagrenac may not launch even if you've met the requirements

<details>
<summary><i>Tools of Kagrenac is known to be janky about starting up...</i></summary>
<br>

As per the info given by the Nexus page for the Tools of Kagrenac mod, you need to complete the side quest Arniel's Endeavor at the College of Winterhold. (And by extension, this means you also need to play the entire College of Winterhold plotline, because you can't finish Arniel's Endeavor until you do.)

Once that quest concludes and you acquire Keening, what's supposed to happen with Tools of Kagrenac is that a few in-game days later, a courier should arrive with a letter for you. However, we've had multiple players see issues with the quest launching properly in our load order, so you may need to take additional steps to fix this problem.

You may need to do one or more of the following:

1. Drop Keening in any location and pick it up. In theory, this is supposed to turn Keening into a quest item, which is the sign that the quest has properly launched. If nothing obvious happens, try the additional steps of waiting for at least 12 hours, then changing cells a time or two, preferably with the result of putting yourself into a location where a courier can find you, such as coming out of a shop.
2. If this does not work for you, there is a toggle in the Tools of Kagrenac MCM which allows you to enable an alternate means of launching the quest. If you turn this on, then the launch mechanism should be to pick up _any_ item. You may need to change cells the same way as in option 1, however, to get the courier to spawn and be able to find you.
3. Last but not least, if neither of the previous options work for you, you may need to use the console to port yourself to the courier, who could have gotten stuck somewhere. Use this console command to move yourself directly to the courier: `player.moveto 00039FB7`
</details>

### Forgotten Knowledge quest in Midwood Isle breaks if you're playing in third person

<details>
<summary><i>Take a little care when drinking on Midwood...</i></summary>
<br>

While running the [Forgotten Knowledge](https://tes-mods.fandom.com/wiki/Forgotten_Knowledge) quest in Midwood Isle, there is a scene where you go drinking a lot with Tyrek, your temporary follower. You're scripted to drink until you pass out.

If you are playing in third person, however, this can create a situation where you partially clip into the floor and cannot move.

A known workaround for this is to temporarily shift to first person instead. Player Danshov on the #txbn-general channel reported being able to get past this point by going into first person, sitting on a nearby chair, and sitting up again. That unblocked the quest and allowed it to proceed.
</details>

### Questing Culture quest may not launch at level 36 for Bretons

The expected behavior here is that Breton characters should be able to find three powerful artifacts in the world that will give you extra abilities. If you haven't found them by level 36, you're supposed to have a dream that will kick off the quest for you and give you quest markers and objectives to locate the items.

However, the launch of this quest appears to be erratic. If you pass level 36 and still haven't had the dream and gotten the quest, try launching it with this console command: `setstage MANNAZ_Breton_QuestingCulture_Quest 10`

Info directly from Enai, creator of Mannaz, notes two points of interest here:

1. The quest launches if you've gone a long time without finding the relics.
2. Similarly to how LOTD will often send you out of the main Skyrim worldspace to find random relics for Auryen or for research projects, the Breton artifacts can likewise spawn in mod worldspaces. So you won't get a quest marker to find those relics until you're in the correct worldspace. Since one of them is known to spawn on Solstheim in particular, be on the lookout for that.
</details>

## OLD FIXES, issues resolved in current build or in a upcoming update

<details>
<summary><i>Archive of older fixes...</i></summary>
<br>

### Bards College Burning of King Olaf Festival doesn't stop

This is a known issue on PC builds of Skyrim, as documented on the UESP. What happens with this is that when you run the Bards College, and successfully help Viarmo present King Olaf's Verse to Elisif, you can then proceed to the Burning of King Olaf's Festival, where you are officially proclaimed a bard. The bug kicks in with how this festival never actually stops, and NPCs will stand around in festival mode.

This includes NPCs you have to talk to in order to pick up the quests for fetching instruments, which you need to do if you want to get the three Bards College teachers to bump your skills for you.

The known workaround for this problem is to open up the console and enter the following command:

`setstage MS05KingOlafsFestival 200`

### **Battle of the Champions quest doesn't start even if you meet our load order's requirements**

Since we are running Rebalancing Anniversary Edition in our load order, this means that if you want to run the Civil War Champions content, you need to meet the following requirements:

* You need to be at least level 20
* You have to have joined a side in the Skyrim civil war, you cannot be neutral

However, even if you meet these requirements, you may see that the Battle of the Champions quest doesn't start for you, and you may not even see the expected notice on the counter of the Drunken Huntsman. If this happens, the following console command should let you proceed to launch the quest:

`setstage FE01B927 20`

This command should also work:

`setstage ccFFBSSE001_Quest 20`

We recommend stage 20 specifically as that's most relevant to the requirements specified above.

Once you use this command to kickstart the quest, it should proceed normally.

### **There Is No Umbra**

We have a known issue with the There Is No Umbra quest, where you must merge the sword with a dagger, in the box at the Atronach Forge, and then pulling the lever. The lever is not actually visibly present, which blocks you being able to do this.

There are two possible workarounds for this problem until we deploy a real fix in a future Tuxborn update:

1. Use the `tcl` command in the console to temporarily turn off collision, so that you can sink a bit into the box and get to that lever so you can use it. The lever is currently located _inside_ the box. Then move back out and use the same command to turn collision back on again.
2. Or, use the console command `setstage 0_FloatingSwordQuest03 30` to progress past that part of the quest.

This issue does appear to be specific to running the Daumbra mod. Regular vanilla functionality of the Atronach Forge is not impacted.

### Blocked while running Fixing the Transmuter quest in The Midden - Expanded

This is _not_ a guaranteed repro, since this reproed in 0.5.2 and so far has _not_ reproed in 1.1.1 in our testing. But noting it in here in case any player sees it. If anyone does repro this in Tuxborn's current build, please report it to #txbn-support.

Once you acquire the Arcane Grotto in the mod The Midden - Expanded, there's a side quest you can run involving fixing a transmuter machine located in one of that home's rooms. It will expect you to find the door into the basement of the Winterhold Astronomy Tower, a door which you can locate just to the west of the bridge that leads up to the college.

However, partway through, this possible bug may come into play. If it does, what will happen is that the trail goes cold. Casting the Clairvoyance spell will lead you into a chamber with a couple of upright draugr sarcophagi set into the icy wall, to the left of a low shelf. The spell's path will point straight at the sarcophagus to the immediate left of the shelf, but there will be no way to activate this sarcophagus.

[This YouTube video](https://www.youtube.com/watch?v=_mEfZaL0Y3U) shows, at about seven minutes in, what's _supposed_ to happen: the sarcophagus should fall open on its own, and the draugr it contains should try to attack you.

If the bug occurs, and the sarcophagus doesn't open, then you'll be blocked from proceeding since you _do_ have to go through that sarcophagus to get to the next area for the quest. This workaround should unblock you:

1. Stand in front of the sarcophagus and open up the console
2. Click on the center of the sarcophagus lid to make sure it's the active object for console commands
3. Type `disable`

This should remove the lid so that you can proceed on through. You may also see the inert draugr that was supposed to attack you. If you do, go ahead and attack it. Once you take out the draugr, you should be clear to proceed with the quest.
</details>

## Credits
Thanks to the following players on #txbn-general:

* TSP for reporting the issue with the lever on the Atronach Forge during the Daumbra mod, and the workaround for the issue in Bleak Falls Barrow
* locoron for additional detective work on the Daumbra mod problem
* Kyaralys for reporting the issue with the Companions quests
* Vengerq for reporting the issue with the Battle of the Champions quest
* Millie for the tip about the workaround to unblock talking to the Khajiit for Moonpath to Elsweyr
* Mr. Beifersbééfh for reporting the issue with the side quest for Auryen's Notes: The Tools of Kagrenac
* Feenie for confirming the search button as a means of bringing up the prompt that QuickLoot interferes with on some vanilla quests
* david aka claudekennilol, for providing the console command to launch the Questing Culture quest for Bretons