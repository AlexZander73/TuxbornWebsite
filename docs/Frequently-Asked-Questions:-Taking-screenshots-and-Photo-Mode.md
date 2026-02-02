---
edit_uri: https://github.com/Omni-guides/Tuxborn/wiki/Frequently-Asked-Questions:-Taking-screenshots-and-Photo-Mode
---

‼️ **FYI for all players: references on this page to Photo Mode will no longer be relevant for the 1.2 beta, as Photo Mode has been removed from the load order for that build. We're keeping info about it on this page for now, since Photo Mode does still exist in 1.1.3, and players are still running playthroughs in that build. But expect this page to be updated to adjust info about Photo Mode in forthcoming edits.** ‼️

## "How can I take screenshots in Tuxborn?"

This question doesn't actually have a single answer. We include the mod [Photo Mode](https://www.nexusmods.com/skyrimspecialedition/mods/91701) in our load order, which adds in a lot of extra functionality to let you take the best possible screenshots for your playthrough. But it's not the _only_ way to take screenshots.

Standard means of taking screenshots still apply, including but not limited to:

* If you're playing on a PC:
    * F12 should still work as the standard Steam screenshot key
    * Print Screen should still work as the standard in-game screenshot key
* If you're playing on a Steam Deck:
    * Steam button + R1 button (right bumper) is the standard Steam Deck shortcut for screenshots
    * You can also map the system function of taking a screenshot to a back button or radial menu, if you are so inclined
* If you're playing on a ROG Ally:
    * M1 or M2 (buttons on back of device) + A button
    * On a ROG Ally X, you can also assign one of the back buttons to take a screenshot
        * Uses the XBOX game bar to do the capture
        * Resulting screenshot is placed in the path `users/<your account name>/videos/captures`

## "Where is Skyrim's default screenshot location?"

In a vanilla Skyrim install, the Print Screen key will take a screenshot and save it into your main Skyrim folder. This same functionality still works in Tuxborn. The resulting screenshot should be dropped as a loose PNG file into the "Game Root" directory of your Tuxborn install. If you take more than one screenshot with this method, they will be sequentially numbered.

Given that we have several other means of taking screenshots available, this one is arguably the least useful. But we're documenting it here anyway, for the sake of being thorough. And it can always be used as a fallback option, in case the other screenshot approaches don't work for some reason!

## "Where is Steam's default screenshot location on Windows?"

If you play Skyrim in Windows (whether on a PC or on a handheld), your default screenshot location will be here for screenshots taken when you hit F12:

`C:\Program Files (x86)\Steam\userdata\<userid>\760\remote\489830\screenshots`

The &lt;userid&gt; part of this path will change depending on your system, so we're not specifying a number in this example. Your path should otherwise match this example.

## "Where is Steam's default screenshot location on Linux?"

If you play Skyrim in Linux (whether on a PC with a Linux install, a Steam Deck, or any other handheld that's Linux-compatible), then your default screenshot location will be here:

`.local/share/Steam/userdata/<userid>/760/remote/<id of your Tuxborn install>`

As with the Windows example, the &lt;userid&gt; portion of this path is going to vary for every user.

The &lt;id of your Tuxborn install&gt; portion of the path will also vary for every user. If you don't already know the ID number of your Tuxborn install, you can find it by entering the command `protontricks -l` in a terminal window.

The path given here should be assumed to start from your home directory. If you are on a Steam Deck, this means you should be in the `/home/deck` directory. Any other Linux install, you'd be in the appropriate directory for whatever user you've set up to use.

## "I like to use Steam's setting for saving non-compressed versions of my screenshots, for best quality. Where do _those_ screenshots go?"

In this specific scenario, the screenshots go literally wherever you want them to. If you activate this setting in Steam, it will ask you tp specify a directory to save to. So you can set it to be whatever directory you want.

Turning this setting on is entirely optional. But some situations where you might consider saving the uncompressed screenshots are:

1. You might want to pick and choose good ones for use as desktop backgrounds
2. Sharing the highest quality ones with friends or on social media
3. You want to have a known custom location for all your screenshots

To turn this setting on, do the following:

1. In your Steam, go to Preferences
2. Select In-Game settings
3. Scroll down to the Screenshots section of the settings
4. Turn on the toggle for "Save an external copy of my screenshots"
5. Specify the folder you want to use in the setting for "External screenshots folder"

If you're playing on a Steam Deck, you can activate this setting in Steam in Desktop mode. Once you activate it from Desktop mode, it will apply to Gaming mode as well, but you have to turn it on in Desktop first.

## "How can I activate Photo Mode to use it to take screenshots?"

There are a few different ways to do this:

1. Photo Mode is included as an option on the in-game system menu, and you can launch it from there.
2. The Photo Mode MCM includes options to set a hotkey to activate, both for keyboard and for gamepad/controller, so you can use whichever setting is appropriate for you.
3. If you're playing on a handheld device and you have the ability to set up a radial or other kind of menu, the Photo Mode hotkey you set in the MCM would be a good candidate for an item on that menu.

## "What will Photo Mode get me that standard screenshots won't?"

Photo Mode adds a _lot_ of extra features to taking screenshots. Some immediately useful ones to consider are:

1. It includes the ability to turn off the UI, so that you won't have that cluttering your screenshot when you take it
2. You can adjust camera position to get the ideal angle for the shot
3. You can add a wide variety of filters and effects
4. Any screenshot you take with Photo Mode can optionally be turned into a loading screen you'll see periodically during your playthrough

So it's definitely worth exploring, to see which features of it appeal to you most. At the very least, the ability to turn off the UI is super helpful to improve screenshot quality.

Interested players should read over the [Photo Mode](https://www.nexusmods.com/skyrimspecialedition/mods/91701) page on Nexus to learn more about its features.

## "Where does Photo Mode store its screenshots?"

Look in your Tuxborn install, in the following path:

`/overwrite/textures/photomode`

You may wish to periodically check this folder and clean out any screenshots you don't want to keep, especially if you're using the Photo Mode option that lets you use your Photo Mode pics as loading screens. Nobody wants a bad screenshot for a loading screen, after all!

## "Are there any reasons to use standard functionality for screenshots instead of Photo Mode?"

There are a few reasons why players may wish to use standard screenshot functionality rather than Photo Mode, including:

* Anyone in the habit of sending their screenshots up to the Steam cloud for sharing
* If you want the highest quality uncompressed screenshots, and you find that Steam's ability to save uncompressed copies gives you better quality shots than Photo Mode does
* If you save all your screenshots to a single standard location, for whatever reason, such as:
    * You don't want to hunt through multiple locations for screenshots
    * You're saving screenshots out to a location on an external drive, a network drive on your house network, or to a cloud account
* You have a third-party tool you like for screenshots, and you want to use its location for screenshot storage

If any of these reasons apply to you, you may wish to stick to standard Steam-based or Skyrim-based screenshot taking, or to whatever chosen custom tool you might be using.

However, do note that you can mix and match! You can use Photo Mode's features to get the shot looking the way you want with any desired angles or effects, but then just use your preferred screenshot functionality to take the shot. If you want Photo Mode's abilities to set angles and effects, but don't care necessarily about your screenshots showing up as loading screens, a mixed approach might work for you.

## "How can I turn off the UI so I can take a screenshot?"

If you are running 1.1.3 or any build earlier than that, Photo Mode's UI includes an option to do this. So launch Photo Mode, and look for that option.

If you're running the 1.2 beta, you have one of two options:

1. Open the console and use the `tm` command
2. If you're willing to Rule 11 your install, there are mods that will allow you to do this without the console, such as No Compass in Dialogue or iHUD. Find one that suits you

## "Why is Photo Mode being removed for the 1.2 beta?"

As is described on our main Readme, it's had some ongoing issues with the BFCO profiles on Steam Deck:

> ⚠️ ❗ Photo Mode: We've included [PhotoMode](https://www.nexusmods.com/skyrimspecialedition/mods/91701), but unfortunately the button mapping for controlling it is very troublesome on gamepad/deck on the BFCO profiles - you can end up with the camera a bit stuck. To get out of this stuck camera, you need to run "tfc" twice in the in-game console. Unfortunately, this does not work on Steam Deck. Thanks to d for that one. ⚠️ ❗

So since this has been problematic for several Tuxborn versions now, we recommend that players who want to run the BFCO profiles in 1.1.3 or earlier _avoid_ using Photo Mode.

## Credits

Many thanks to the following players on #txbn-general for contributing to this page:

* Seriouszombie, for confirming behavior of default Skyrim screenshot functionality still working in Tuxborn, as well as the default Steam screenshot location in Windows
* Syotic, for the information about how to assign a back button on the ROG Ally to take screenshots, and where the resulting screenshots are placed