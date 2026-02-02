---
edit_uri: https://github.com/Omni-guides/Tuxborn/wiki/Support-settings-changes
---

To make the boundaries clear of where Rule 11 starts and stops within this document we will make a list of setting changes we support. Things we tell you to do will also be supported, unless we say so.

## Setting resolution and framerate

For both of these you need to edit the SSEDisplayTweaks.ini that can be found in two places; Lower Render Resolution and Tuxborn - Settings. For most people this can best be done with Tuxborn - Settings, unless you want to have two options for resolution. Then it’s better to use Lower Render Resolution, but you will also want to change the render scale in there in the same place as your resolution.

## FOV 

FOV is handled by the MCM from Improved Alternate Conversation Camera, this can be found with the in game settings menu. To take effect you need to talk to somebody and then exit the conversation.

## Sneak stamina cost

This is part of Blade and Blunt. You can disable this feature by adding the following line to the Bladeandblunt.ini file contained within the Tuxborn - Settings mod entry under the "Patcher Output" section in MO2: `bEnableSneakStaminaCost = false`.

## Difficulty

If you find yourself wanting more or less of a challenge then include options give you there is the Custom Difficulty UI mcm, this can be found with the in game settings menu. Here you can both increase and decrease the settings to fit your taste. 

## Compass

If you miss the old compass icon, you can change that within the CompassNavigationOverhaul.ini that can be found Tuxborn - Settings. Set `UndiscoveredMeansUnknownMarkers` from =1 to =0. 

If you wish to adjust the positioning of the quest list widget provided by the same mod, you can do so with the first two settings in the `[QuestList]` section of the file. Look for the `fPositionX` and `fPositionY` values. Use the first one if you simply want to move the widget from the left to the right side of your screen. If you also want to change vertical placement, use the second value. What specific values you should set will depend upon your screen resolution, so experiment _carefully_ until you find values that look appropriate.

If you don't actually like the quest list widget and would like to turn it off without impacting the changes to the compass, then set both `bShowInExteriors` and `bShowInInteriors` to 0.

## Configuring Steam shortcut to launch Tuxborn directly

If you want to bypass having to click on the Run button in MO2 to load Tuxborn, and instead just load Tuxborn directly as soon as you click Play from your Steam, then you need to add the following string to your Tuxborn Steam shortcut's launch arguments:

`moshortcut://Tuxborn`

Place this at the end of the launch arguments string, after whatever else you have in that field.