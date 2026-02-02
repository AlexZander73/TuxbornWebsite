---
edit_uri: https://github.com/Omni-guides/Tuxborn/wiki/Replacing-CS-with-ENB
---

Be aware that this breaks Rule 11, no ifs, ands, or buts about it.

First, let's start with removing CS. Go to the Shaders header in MO2 and disable everything in there. Those were the main components of CS, but there are still some things to do.

Next, go into Late Loaders and disable Light Placer, Placed Light, and CS Lights.

You might also want to remove the weather mod for the one your ENB uses. If so, you need to disable Azurite Weathers and Seasons, and Azurite III - HDR.

Finally, you now need to add your ENB to Tuxborn. Don’t place the files in the Game Root folder. Instead, make a new empty mod within MO2, by making a folder called Root in there, and placing the ENB files in that folder.

Now make sure to follow all the instructions on the page of the ENB you want, and in particular, look for any dependencies your ENB has that aren't already included in Tuxborn's load order. This will likely include some type of lighting overhaul, so be aware you will need to either find or create appropriate patches for external lighting overhauls to work in Tuxborn's load order.