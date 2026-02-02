---
edit_uri: https://github.com/Omni-guides/Tuxborn/wiki/Creating-your-character
---

This page covers several recommendations for creating your character in Tuxborn.

## RaceMenu suggestions

### Loading provided presets

<details>
<summary><i>Instructions on how to load provided presets in RaceMenu...</i></summary>
<br>

Tuxborn's load order includes three different sets of pre-made presets. You should be able to get at these by using RaceMenu's UI to get to the Presets tab.

If you are a Steam Deck (or Ally or other handheld) player, or playing with a controller on PC, you should then be able to use your left stick to load the dialogue for finding the provided presets.

PC keyboard players, you should use your F5 key.

By default, the UI should take you to the correct directory immediately. You should see subdirectories that contain all three of the sets of provided presets, from Foamimi, Lamenthia, and Zooey. There are a large number of presets in each directory, so feel free to browse all of them and see if any of them are to your liking.
</details>

### Loading your own presets

<details>
<summary><i>How to load your own presets in RaceMenu in Tuxborn...</i></summary>
<br>

If you have your own previously made preset files you'd like to use, _or_ presets acquired from other creators, this is also an option. As long as the preset file is in .jslot format, you should be able to include it in your Tuxborn files.

You will need to manually place any such files you want to use in the following path in the Tuxborn install, once it's completed:

`/mods/[NoDelete] Custom Presets Go in Here/SKSE/Plugins/CharGen/Presets`

You should place such files _before_ starting the game, so that RaceMenu will actually see them.

See the [Additional player resources](Additional-player-resources/) page for some suggestions on presets on Nexus known to work acceptably well with Tuxborn.
</details>

### Saving a new preset

<details>
<summary><i>How to save your character settings as a preset to use again later...</i></summary>
<br>

Once you get your character design the way you want it, if you want to do so, you can save out a new preset with that design for later use.

Deck/Handheld/Controller players, you can do that on the RaceMenu Presets tab with your right stick.

Keyboard players should use F9 to save a new preset.

Look in this location for your newly saved preset file:

`/overwrite/SKSE/Plugins/CharGen/Presets`

It is recommended that you move or at least copy the file out of that location, to whatever other directory you like, so that you have a backup copy if you need one.
</details>

### Using Presets in RaceMenu if you want to run a BFCO profile on Deck, other handheld, or playing with controller

Players have reported issues to the Tuxborn team with the BFCO profiles behaving oddly if you want to load or save a character preset. We do not have a real fix at this time, but we _do_ have a workaround. If you're playing on a Steam Deck, try the following steps:

1. Follow the same instructions given to keyboard players in the official Readme about turning on Combat Keyboard Keys, and turning off Tuxborn Combat Controller, in the Optionals section of MO2
2. Launch the BFCO profile you want
3. Once you're in RaceMenu, you should see the same input options available to non-BFCO players for dealing with Presets, specifically:
    1. Left Stick click to load a preset
    2. Right Stick click to save a preset
4. Make whatever changes you want to your character, then proceed out of RaceMenu to the starting cell
5. As per standard instructions, wait for museum list building to complete
6. At this point, make a new save and exit the game
7. Reverse what you did in step 1, turn Combat Keyboard Keys back off, and turn Tuxborn Combat Controller back on
8. Load up your new save, and now you should be clear to enter the world

Note: at this time, to the best of our knowledge, this issue seems to be specific to the Steam Deck. PC players using keyboard or controller do not appear to be impacted. If you _are_ a PC player though and can see this issue, let us know and we'll update this info accordingly. Also let us know if you're reproing this issue, and you're on a non-Deck device such as the ROG Ally.

### Finishing and naming your character

Our main install guide already warns you about additional steps you should take to make RaceMenu work correctly if you're going to run a BFCO profile. Be sure to follow the guide's recommendations on that.

But if you're specifically playing on a Deck or other handheld, or playing with a controller on PC, please see previous section for a workaround you may need to follow to make it through RaceMenu correctly.

#### How to avoid issue with getting stuck in RaceMenu after naming your character

We've had semi-regular issues with players trying to name their characters and not actually exiting RaceMenu as expected.

At least on Deck, a way to avoid this problem is as follows:

1. When you get the input box to enter your name, you should also see the Deck's on-screen keyboard load
2. Enter your desired character name
3. Do _not_ dismiss the on-screen keyboard
4. Instead. either click on the Submit button on the on-screen keyboard, _or_ hit your right trigger button, either of these should count to submit your character name properly
5. You should then proceed out of RaceMenu and see the Pronouns dialog appear.

While you should in theory be able to dismiss the on-screen keyboard and then click on the Submit button on the dialog where you enter your character name, in actual practice, this seems to be the cause of Deck players getting stuck.

We will update this section of the page if we confirm this workaround applies on other devices, as well.

## Suggestions for character race selection

In-depth advice on what race you should play is outside the scope of this doc, but I _will_ note that the Tuxborn load order includes mods which influence racial buffs, so this may play into your build choices. Players may wish to do a little preliminary research on the following mods, to see what these buffs are:

* [Freyr - Integrated Standing Stones of Skyrim](https://www.nexusmods.com/skyrimspecialedition/mods/88043)
* [Mannaz - Integrated Races of Skyrim](https://www.nexusmods.com/skyrimspecialedition/mods/87219)

## Which combat system to use

Please see [Frequently Asked Questions: Which profile to use](Frequently-Asked-Questions:-Which-profile-to-use/) for further info on this.

## Beginning Alternate Start

See the [Alternate Start in Tuxborn](Alternate-Start-in-Tuxborn/) page for some tips and suggestions on which start option you should take.

## How long you should wait in the starting cell

We mention this on the main starting guide, but I'm going to call it out again here because it's important.

Initial startup of the game needs to take several extra minutes to generate a bunch of lists used by Legacy of the Dragonborn. We strongly recommend that you hang out in the starting cell until you receive the alert that the list generation is complete. The alert you're looking for will read:

`Museum list building complete.`

And you actually do need to dismiss this alert, so you can't miss it. So hang out in the starting cell until you can see and dismiss this alert. Then you should be able to use the bed in the cell to proceed with your chosen start option, or, lockpick your way out of the cell if you want to go that route.

## Credits

Thanks to the following players on #txbn-general:

* TSP, for commentary on BFCO
* LilBeee, for corrections on how the Shipwrecked Off the Coast Alternate Start works
* HardenedSteel, for recommending the Duneborne preset pack
* F0R35TS, for confirming functionality of the Duncan De la Fonte preset