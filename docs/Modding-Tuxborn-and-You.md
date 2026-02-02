---
edit_uri: https://github.com/Omni-guides/Tuxborn/wiki/Modding-Tuxborn-and-You
---

Modding in any way shape or form will break rule 11 with Tuxborn, anything you break is on you and if you need help stick to #modlist-modifications channel, and not the support channels of Tuxborn. The same is true if you want to know how to remove something. If you are new to modding or new to MO2, look at the guides at the end of the readme. What you find on the page is some info and tips on how Tuxborn is put together and how that is related to Rule 11.

## Just watch this

Yes, really, watch this: https://www.youtube.com/watch?v=izGoHgO4izc 

## MO2 Profiles

Profiles are one of the unsung heroes of using MO2, make good use of them. Never edit one of the base profiles, instead make a copy and start going hog wild in there. If you plan on changing a lot of stuff make a back-up copy of your rule 11 profile whenever you hit a milestone. 

## World map 

We use Flat World Map Framework to replace the map Skyrim uses, this mod doesn’t like to be overwritten by anything. So make sure anything you added is above it on the left and right side of mo2.

## Where should I place stuff within the load order

At first at the bottom, that will make it easier to check for any conflict with xedit. After you checked and fixed those, you should place them in the same place as similar mods. 

## Turning kill moves back on

Remove the no kill move esp from blade and blunt + hide the auto run file you can find in Tuxborn settings.

## MCO based animation with BFCO

Yes you can do this, but you will need to patch them to work. A quick google should point you the correct way.

## When should you rerun the Grass cache

When you have made major changes to a worldspace or added a new one, if you want to. Another easier option is disabling grass caching if you PC can handle it, only way to know is to try and see (see: https://www.nexusmods.com/skyrimspecialedition/mods/42161).

## INI settings keep reseting

Yes that is normal, a DLL is changing the settings to hit an FPS target. Disable FPS Stabilizer to 'fix' this.

## Changing Inputs on BFCO

For keyboard: BFCO MCM does powerattack, TK Dodge MCM does dodge, Dual Wield Parrying SKSE and Valhalla handle the extra block key. With a controller this is also true, but you will need to make or find a controlmap.txt. This is a pain and needs you to edit all the input codes by hand, if you make error with your game will CTD.