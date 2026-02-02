---
edit_uri: https://github.com/Omni-guides/Tuxborn/wiki/Frequently-Asked-Questions:-Shades-of-Mortality
---

This page covers the Shades of Mortality mod in Tuxborn's load order in depth, since this one gets a lot of attention.

## "Why do I keep turning into a ghost every time something kills me?"

This is because Tuxborn includes a death mechanics mod called Shades of Mortality. Its main impact is that any time you receive a killing blow, instead of actually killing you, it will turn you ethereal for a few seconds and also drop a significant debuff on you that'll nerf your health, magicka, and stamina regeneration rates. It'll also cut down on the amount of damage you're able to do when you come back from being ethereal.

## "I really prefer the vanilla death mechanics. Can I turn this mod off?"

This mod is considered optional in the Tuxborn load order. So if you decide you don't like it, it's safe to disable it in MO2. Just make sure you don't have its effect active on you first. Doublecheck your list of active effects to be sure. If you don't see the "Death's Grip" effect, you're clear to disable the mod.

As per what is mentioned in the Readme, if you wish to disable Shades of Mortality, you actually need to disable two things:

* Shades of Mortality itself
* Resurrection API for Skyrim 1.6

If you are running Tuxborn 1.0 or 1.0.1, you will also need to turn this off:

* Resurrection API

## "How can I get rid of the Death's Grip nerf?"

The nerf from Shades of Mortality is _not_ permanent, but it won't go away on its own, you have to cure it. There are a few ways to do this offered in the keywords INI files included with the mod:

* Anything that triggers the "Cure Disease" magic effect should work, including:
    * Asking a Vigilant of Stendarr to cure you
    * Cure Disease potions, whether they are ones you buy, or ones you craft
    * The Cure Disease spells you can acquire if you run either Project AHO or Wyrmstooth
    * The [Dwemer Automated Apothecary](https://legacy-of-the-dragonborn.fandom.com/wiki/Dwemer_Automated_Apothecary), craftable as part of running Legacy of the Dragonborn
* All potions of "Well-Being" provided in the game via Dragonborn
* The three highest-tier healing potions available via vanilla content:
    * Potion of Vigorous Healing
    * Potion of Extreme Healing
    * Potion of Ultimate Healing
* The Grand Healing Restoration spell

The following vanilla means of curing diseases will _not_ work to cure Death's Grip, because other mods in our load order turn off their ability to do so:

* Praying at shrines or altars
* Eating Garlic Bread

If you want to use this mod in your load order, it is highly recommended to stock up on means to cure the debuff as soon as you can, and start with whatever items are easiest for you to get first. This will probably be Cure Disease potions.

Additionally, you can cure this debuff by sleeping it off. By default, sleeping in a safe location such as an inn or one of your houses, for eight or more hours, will cure the debuff for you.

## "I like the mod's idea, but I don't like some of what it does. Can I customize it?"

Yes. There is no MCM, but the mod has an INI file that lives at this path in the Tuxborn file structure:

`/mods/Shades of Mortality - Death Alternative SKSE (Disable Together - remove all effects before hand on a running save)/SKSE/Plugins/shades-of-mortality.ini`

You can open this up from a command line or file explorer on your device, or edit it directly in MO2, whichever works better for you.

Look at the comments on the various options in the file, which explain what they all do. Or look at the [Shades of Mortality page on Nexus](https://www.nexusmods.com/skyrimspecialedition/mods/136825) for additional details on its various options.

## "Why does Shades of Mortality take my gold when I die?"

By default, the mod has an option bRemoveGold which is set to true in its INI file. If you don't like this feature, you should set it to false.

## "I like the mod's idea, but I don't think it quite goes far enough in penalizing me for a death. How can I customize this?"

We suggest a couple of options.

### Make the Death's Grip nerf more severe

You can increase the percentages on the hit to health, magicka, and stamina regen. By default these are set to 40 percent. You can raise that percentage if you want. The relevant values to change in the INI file are fInjuryHealthDecreaseModifier, fInjuryStaminaDecreaseModifier, and fInjuryMagickaDecreaseModifier.

### Activate the Blade and Blunt injury system

If you're playing on a non-BFCO profile, then consider turning on the injury mechanics in Blade and Blunt! By default in our load order, this mechanic is active only if you're playing Survival Mode. So you could either activate Survival Mode, _or_, if you just want the injury mechanic without turning on Survival Mode, you can get into Blade and Blunt's INI file.

In our load order, you'll want the copy of Blade and Blunt's INI file in Tuxborn - Settings. This is the path if you're editing the file outside of MO2:

`/mods/Tuxborn - Settings/SKSE/Plugins/BladeAndBlunt.ini`

Inside that file, you will see the following on the first two lines:

`bEnableInjuries = false`  
`bEnableInjuriesOnlyWithSM = true`

Toggle each of these lines if you'd like to turn on the injury mechanic at all times. So you would change line 1 to true, and line 2 to false.

Blade and Blunt's injury system is very compatible with how Shades of Mortality works, in terms of the RP perspective. Both mods expect you to rest to cure injuries. Shades of Mortality is actually a little more forgiving in that it lets you use a Cure Disease potion immediately to cure its nerf, and it doesn't make the nerf more severe over time--whereas Blade and Blunt will penalize you with an infection if you _don't_ cure your injury, and that infection _will_ get worse! So that can add an extra layer of risk if you neglect to take care of your Dragonborn.

## "The mod page on Nexus talks about adding a CureInjury keyword to other things to allow them to cure the Death's Grip nerf. How do I do that?"

There is a secondary INI file provided with the mod that handles this. Here's the path to that file:

`/mods/Shades of Mortality - Death Alternative SKSE (Disable Together - remove all effects before hand on a running save)/shade-of-mortality_KID.ini`

Inside that file is a single line that looks like this:

`keyword = CureInjury|Potion|0xae723|100`

This follows the syntax of Keyword Item Distributor. Basically this is saying to apply the CureInjury keyword to the item with the ID of 0xae723 in the game, and do it a hundred percent of the time. That ID represents bought/found Cure Disease potions, hence the "Potion" type specified.

If you want to add additional lines to this file, you can do so, but you need to follow the same syntax.

Look at the [Keyword Item Distributor page on Nexus](https://www.nexusmods.com/skyrimspecialedition/mods/55728) for more information about how that syntax works.

We recommend making changes to this file if and _only_ if you are comfortable with looking up the relevant IDs for the items you want to add. For items in the vanilla game, UESP is a reliable source for that.

You can also add items from mods, but getting the relevant IDs for that may take a bit more detective work. Again, look at the Keyword Item Distributor page for more information on how the mod supports this. 

_Do not_ touch this file if the necessary syntax doesn't make sense to you!

### "I'm still playing 1.0 of Tuxborn, can I get the additional cures for Death's Grip?"

Yes, but you will need to manually include them. This is a specific example of how to edit the keyword file without having to worry about looking up specific cure IDs, and to retroactively apply the 1.1 cures to 1.0 playthroughs. Use these instructions if you'd like to do that.

Shades of Mortality in Tuxborn 1.1 includes an extra file with cures, and the contents of that file are as follows:

<pre>keyword = CureInjury|Magic Effect|AlchCureDisease|100
keyword = CureInjury|Potion|DLC2RestoreAll01|100
keyword = CureInjury|Potion|DLC2RestoreAll02|100
keyword = CureInjury|Potion|DLC2RestoreAll03|100
keyword = CureInjury|Potion|DLC2RestoreAll04|100
keyword = CureInjury|Potion|DLC2RestoreAll05|100
keyword = CureInjury|Potion|DLC2RestoreAll06|100
keyword = CureInjury|Potion|RestoreHealth04|100
keyword = CureInjury|Potion|RestoreHealth05|100
keyword = CureInjury|Potion|RestoreHealth06|100
keyword = CureInjury|Magic Effect|RestoreHealthFFSelfArea|100</pre>

Do the following to add these cures to your 1.0 or 1.0.1 Tuxborn run:

1. Make sure Tuxborn isn't running.
2. Find the keyword file described immediately above, shade-of-mortality_KID.ini.
3. Open that file and add all of the above quoted keyword lines to it.
4. Save the file.
5. Relaunch Tuxborn. The additional cures should now be available to you for the next time you need to get rid of the Death's Grip debuff.