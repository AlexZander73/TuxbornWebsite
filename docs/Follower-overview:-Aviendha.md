---
edit_uri: https://github.com/Omni-guides/Tuxborn/wiki/Follower-overview:-Aviendha
---

This is the follower added to Skyrim by the [Wheel of Time mod](https://www.nexusmods.com/skyrimspecialedition/mods/55404?tab=description), which does what you'd probably expect from that name: it sets up crossover content between Skyrim and the world of the Wheel of Time books by Robert Jordan. Aviendha appears as a character in those books, and how well this version of her adheres to her portrayal in the series is outside the scope of this wiki page. Players who've read the books will need to judge for themselves how accurate the mod's portrayal of her is.

## Where and when to recruit her

Aviendha would normally spawn by coming through a portal from her world, on the Riverwood bridge. In our load order, we are running a patch that moves her portal spawn a bit off to the west of the bridge, on the north bank of the river. This allows for players not having to spawn her if they don't wish to do so.

Finding Aviendha will also trigger the Wheel of Time mod's overall plot.

## How to summon her

Aviendha has no known means to summon her. So if you get separated from her and need to move her back to you, the best course of action to follow is to use the console to move her back to you. In order for this to work, you'll need her refID.

Investigation into what her refID actually _is_ showed that this may be variable depending on playthroughs, or depending upon what stage of the Wheel of Time questline is active.

So the safest way to determine Aviendha's refID is as follows:

1. Load up a prior save where she is easily accessible, preferably actively following you
2. Open your console and click on her to make her the active refID
3. You should be able to grab her refID from console output, make a screenshot or otherwise make a note of that information
4. Then return to your current save
5. Use the refID noted in step 3 for this command: `prid refID` (replace refID here with the actual refID)
6. Then use this command to move Aviendha to you: `moveto player`

We will update this page if we confirm a known constant refID for her.

### Using Aviendha with UMF

The Wheel of Time mod page says the following re: managing Aviendha with follower frameworks:

> Don't manage Aviendha with follower frameworks such as AFT and NFF, as it may cause issues with her functionality. 
If you insist on using another framework anyway, wait until after the quest Darkfriends, as it will most likely fail otherwise.

Because of this, we recommend _against_ trying to manage her with UMF, even though UMF is a lightweight follower framework mod. If you want to try it anyway, we therefore recommend _only_ using UMF as a possible means to summon her back to you if you get separated, by using UMF's Check command. (We will update this page if we can confirm if that safely works. Until we do, attempt this only with the greatest caution, and make sure to make a viable save file first so that you can return to that save if trying this does not work for you.)

## Best follower use

She's a decent early game follower, with a focus on archery and the use of her spear. So if you want to muster a squad very quickly to help you fight Mirmulnir at the watchtower, she's an option to consider.

However, since she's not trainable, you may find her usefulness limited once you're past the early stretches of your playthrough.

## Level of commentary to you

Aviendha does not have a wide variety of commentary in general; she's not nearly as talkative as a lot of other followers in our load order. If you prefer less talkative followers, you might consider Aviendha on those grounds.

She is known to have some commentary on your house, and will chat with your spouse and/or children.

<details>
<summary><i>Small spoiler on a topic Aviendha may throw at you...</i></summary>
<br>

*** 

Aviendha may advocate to you that you take Ysolda as a romantic interest, and she is _very_ insistent about this. She'll also have some harsh commentary if you shoot down the idea. YMMV on how annoying this may be, but we do recommend watching out for this if you choose to run her.

***

</details>

## Level of commentary about main quest, side quests, factions, and mods

Aviendha out of the gate is set up to respond very positively to Whiterun, and to make friends with Ysolda and Adrianne there. She has a small number of conversations you may hear her have with those two NPCs in particular.

Aviendha is also set up to have commentary on major main quest events, as well as the weather and major Skyrim locations. But her range of comments on those topics isn't large, and if you're running her in conjunction with other, more talkative followers, her remarks may be easily overlooked.

## Some important notes

Once you're past a certain point of the Wheel of Time mod, Aviendha is not hugely critical. There's an early plot point in the mod's quest line involving her, but a big stretch of the middle of it does not require her to be present.

However, according to the Wheel of Time mod page, the final quest stage of the mod involves unlocking the ability to romance her. So if that's of interest to you, you should probably keep her available to play up to that part. And if you're a WoT fan in particular, you may just want her around for RP and ambiance reasons.

If you choose to dismiss her from her service, she will return to the Bannered Mare in Whiterun. She has no known means of asking her to live at any specific player home, so if you do dismiss her but decide to recruit her again later, look for her there.