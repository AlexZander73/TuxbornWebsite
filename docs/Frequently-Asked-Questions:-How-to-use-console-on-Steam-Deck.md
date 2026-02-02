---
edit_uri: https://github.com/Omni-guides/Tuxborn/wiki/Frequently-Asked-Questions:-How-to-use-console-on-Steam-Deck
---

Tuxborn has a known issue with the console crashing if you try to use it on Steam Deck with the on-screen keyboard.

This issue is known to happen regardless of how you interact with the console: whether by typing directly on the touchscreen, or by using your sticks and trigger button to select characters that way. Once you try to enter a console command, that's the point of failure that invokes the crash.

There are at least a couple mods out there that attempt to fix this problem, and the Tuxborn team is investigating them to see about putting such a mod in a future release. Until we settle on a solution, there are several workarounds we recommend for Tuxborn Steam Deck players to use.

## Use a physical keyboard

If you have a Bluetooth keyboard, you can pair it with your Deck and use it to access the console. There are all kinds of Bluetooth keyboards available, so if you don't have one and your budget allows for it, shop around for one that appeals to you. Some specific brands used and recommended by Tuxborn players include iClever and ProtoArc.

If your only physical keyboard is one with a USB-C connector, you should be able to make that work just by plugging it into the Deck's one USB-C port as well if your Deck is not plugged in. If your keyboard does not have a USB-C connector specifically, you can still make this work if you have an appropriate adapter (USB-A to USB-C, most likely, unless you have a very unusual keyboard).

If you have a dock for your Steam Deck, and that dock has more than one USB-C port, then that would also work. This would let you use the console via physical keyboard while the Deck stays plugged in.

## Stream your Deck to your computer

There are a couple of different ways you can connect your computer to your Deck, so that you can use the computer's own keyboard to access the game's console.

### Use the Steam Link app

The [Steam Link app](https://store.steampowered.com/remoteplay) is available for a number of platforms. So you can use that to briefly connect to a Tuxborn game in progress on your Deck, if you need to get into the console. Instructions as follows:

1. Download and install the correct version of Steam Link for your computer
2. Make sure your computer and your Steam Deck are both on the same network, and that you are logged into Steam on both
3. Close Steam, then launch Steam Link
4. Steam Link should see your Deck as a thing it can connect to
5. Initiate a pairing
6. You should be given a 4-digit code to enter on your Deck; do that

Now you should have a valid pairing to use between your computer and your Deck, and you should only need to enter a code for this once. If you run into a point in your game where you suddenly have to use the console, do this:

1. Launch Steam Link on your computer
2. Your Deck is already paired, so tell Steam Link to connect to it
3. It should take a moment or two, but then Tuxborn should show up on your computer, with your game in progress
4. You should now be able to use your computer's keyboard to open up the console and do whatever you require
5. Stop the stream to return to playing on your Deck

Note: while Steam Link will give you a full screen for the stream, the Tuxborn window will not fill your entire screen. You'll get a 1280x800 window by default, because that's the Steam Deck's own screen size. But you don't need to care about this, if all you want to do is open the console and fix something.

This procedure is confirmed to work on both PCs and Macs.

### Use Remote Play settings in Steam on your computer

The Steam Link app is a standalone thing, but very similar functionality also exists in the Remote Play settings in Steam on your computer. You may wish to try both approaches, just to see if one works better for you than the other.

If you use the Remote Play settings route, be sure to initiate the streaming on your computer, not on your Deck. Otherwise, your Deck will connect to your computer's desktop!

## If you are an iPhone user

### Use the BTKBD app

If you have an iPhone, you can install the app BTKBD. This will allow your phone to act as a pairable Bluetooth keyboard, and this should work in both Gaming mode and Desktop mode. Instructions to do this are as follows:

1. Install the BTKBD app
2. Go into your Bluetooth settings on your Steam Deck
3. Look for the toggle labeled "Show All Devices" and turn that on
4. Look for the "btkbd" item in the resulting list, and connect to it
5. You should see a Bluetooth Pairing Request pop up on your phone, asking for permission for the Steam Deck to connect
6. Tap on the Pair button to finish the pairing

You should now be able to use your phone to both launch and type into the console as necessary, while Tuxborn is running.

## If you are an Android user

The [Bluetooth Keyboard & Mouse](https://play.google.com/store/apps/details?id=io.appground.blek&hl=en-US) app for Android may be a viable solution for the problem. We need Steam Deck players with Android phones to confirm! If you are such a player, please test and check back with Annathepiper.

## Options that work only in Desktop mode

Some options available only work if you're willing to play Tuxborn in Desktop mode on your Deck. These options, at least, should work for both iPhone and Android users.

### Use the KDE plugin available via Decky

If you use Decky on your Steam Deck, there is a KDE plugin for it. We'll add instructions on how to do this once we confirm them.

### Use the KDE Connect app

Instructions to use this app would be:

1. Install the app on your phone
2. When it asks for permission to detect devices on your local network, allow it to do so
3. It should see your Steam Deck, and give you an option to send a pairing request to it
4. Send the pairing request, and on your Steam Deck, accept it
5. The app's "Remote Input" functionality should now be available to send mouse _or_ keyboard input to your Deck

When you launch Tuxborn in Desktop mode, you should then be able to use the app on your phone to send input to the console if you need to.

#### If you use this app as an iPhone user

The on-screen iPhone keyboard does not immediately show a tilde key, which _is_ necessary for accessing the Skyrim console. To get to the tilde key:

1. Tap the 123 button on the keyboard to put it into numeric mode
2. Then tap the #+= button to bring up symbols
3. You should now have the tilde available and can use it to launch the console

Then tap on the ABC button on the keyboard to return to alphabetic mode.

## Workarounds to try in-game

If the above solutions don't work for you, then as a last resort, there are also some known workarounds are described in [this YouTube video](https://www.youtube.com/watch?v=Km5ZJ2fAzC8) and on [this Reddit thread](https://www.reddit.com/r/SteamDeck/comments/18cyrzt/skyrim_console_commands_steam_deck_keyboard/).

The Reddit thread also links to [this Steam Community post](https://steamcommunity.com/app/489830/discussions/0/4034726433734168392/) that describes an enchanter table workaround. This workaround has been confirmed as working by Tuxborn players, so try that one first. Note that you will need to do this at the start of every play session, because the workaround will not persist across sessions! Or at the very least, you should do this workaround before trying to open your console.

## Credits

Many thanks to the following players on #txbn-general for info for this page:

* Danshov | Kida for the info on the BTKBD app
* SLURMP for the info on the Bluetooth Keyboard & Mouse app
* kierkegoth for confirming that streaming the Deck to computer works for PC