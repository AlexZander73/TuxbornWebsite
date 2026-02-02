---
edit_uri: https://github.com/Omni-guides/Tuxborn/wiki/Tuxborn-in-ultra‐wide
---

For the benefit of our PC players, please note that Tuxborn does not officially support play with ultra-wide monitors. The reason for this is, neither Ouroboros nor Omni has such a monitor, and so they can't confirm appropriate configurations to get Tuxborn to work with them. 

This page is to document reports from players who have succeeded in getting this to work. Be advised that this does count as Rule 11 territory. So please be mindful of that if you try any of these configurations!

These reports are provided as-is, and the Tuxborn team cannot guarantee they work, because see previous commentary re: we don't have monitors to test these ourselves. Please direct questions about the configs to the players that reported them.

We will, however, be happy to document confirmations from other players on what configs work for them. If you'd like to report such a confirmation, or would like to report a working ultra-wide config of your own, talk to Annathepiper to submit your info for this page.

## Configuration from Capstone

Capstone attempted to validate the config provided by An0n (see following), and found that the UI described there appeared to be out of date. If An0n's config does not work, please try setting options in Complete Widescreen Fix as per these provided screenshots from Capstone:

<details>
<summary><i>First options screen...</i></summary>
<br>

[[https://github.com/Omni-guides/Tuxborn/blob/main/images/Tux%20Wiki%20Complete%20Widescreen%20Fix%20Options%201.png]]
</details>

<details>
<summary><i>Second options screen...</i></summary>
<br>

[[https://github.com/Omni-guides/Tuxborn/blob/main/images/Tux%20Wiki%20Complete%20Widescreen%20Fix%20Options%202.png]]
</details>

## Configuration from @An0n

User @An0n on #txbn-general installed the mod [Complete Widescreen Fix](https://www.nexusmods.com/skyrimspecialedition/mods/1778), and reported the following specifics:

1. Placed after SkyHUD in the Tuxborn 1.1.3 load order
2. While running the installer for the mod, selected SkyUI and RaceMenu options, as both of those exist in our load order
3. On the final install screen for Complete Widescreen Fix, selected the following options:
    * (Option unknown? label not visible in screenshot), but includes NO, YES, and YES - Without Tween Menu options: NO
    * Survival Mode Improved - SKSE: YES
    * Constructable Object Custom Keyword System: YES
    * Playstation 4 Button Icons for SkyUI: NO
    * Remove QuickSave Button From SkyUI System Menu: NO
    * SkyUI - Survival Mode Integration: NO
    * SunHelm Survival and Needs: NO
    * Forget Spell: NO
    * Pastel Markers - Vanilla - SkyUI - Anniversary Edition: NO
    * Body Slots - SkyUI: NO
    * Quest Journal Fix for SkyUI: YES (Recommended)
    * Better Dialogue Control - Widescreen Fix: YES (Recommended)
    * Better MessageBox Control - Widescreen Fix: YES (Recommended)
    * Campfire 1.12.1 and Frostfall 3.4.1SE - Widescreen: NO
    * SkyUI Weapons Pack SE - Widescreen Fix: NO
    * Wider MCM Menu for SkyUI: NO
    * SkyHUD: YES
    * Less Intrusive HUD II SE - AE: NO
    * Dragonborn Voice Over: NO
    * Elder Scrolls Levelling and Attributes: NO

## Problems you may run into

While the Tuxborn team cannot provide official support, we will document known problems and their solutions here.

### MCM may be thrown over to the right side of the screen

Known solution for this is to make sure that [Wider MCM Menu for SkyUI](https://www.nexusmods.com/skyrimspecialedition/mods/22825) (which is included in Tuxborn) is _after_ Complete Widescreen Fix in the load order.

## Credits

Thanks to the following players on #txbn-general for info submitted for this page:

* An0n for the Complete Widescreen Fix configuration
* Capstone for providing screenshots for Complete Widescreen Fix options
* oxelder (and also An0n and Capstone) for identifying the solution to the problem of the MCM appearing too far right on the screen