---
game-id: dread
short-name: Dread
long-name: Metroid Dread
randomize:
- All items
- Elevator and shuttle destinations
- Starting locations
- Door locks
- A new goal has been added (DNA Hunt)
need-to-play:
- A modded Switch with Atmosphere and SimpleModManager; or Ryujinx
- A dumped RomFS of your original game. Either version 1.0.0 or 2.1.0
multiworld: true
development-state: stable
faq:
- question: What Switch Emulators does Randovania support?
  answer: Randovania only officially supports Ryujinx as an emulator, with no plans
    to support additional emulators.
- question: Why does this missile door not open after I shoot a missile at it?
  answer: Shoot another missile at the door. In the process of making certain missile
    doors possible to open from both sides, this issue shows up.
- question: Using an Energy Recharge Station heals me to 299, but my energy maximum
    is 249. Which one is correct?
  answer: The 299 is a display error. You can always see the correct value in the
    inventory screen.
- question: Why is this pickup not animating, or displaying visual effects?
  answer: While progressive pickups update to have the correct model, due to limitations
    these models are not animated or have any additional effects.
- question: Can I use other mods?
  answer: "Depending on which files the other mods change, it can go from simple to
    impossible.\n\n* If a Lua file is modified, very likely it's not compatible.\n
    * If a PKG file is modified, it'll have to be combined with the one from Randovania.\n
    * Other mods likely work fine.\n\nWhen reporting issues, your first step is always
    to reproduce the issue without mods, **no matter how simple** the mod is."
- question: I picked up the Speed Booster / Phantom Cloak / Storm Missile but can't
    use them!
  answer: "Press ZL + ZR + D-Pad Up to fix the issue. Check the entry 'Crashing after
    suit upgrade' in 'Known Crashes' tab for important rules of when to use this button
    combination.\n\nYou can also save and reload your game."
- question: I entered the arena for Golzuna/Experiment Z-57 but it isn't there!
  answer: "Golzuna and Experiment Z-57 will not appear unless the X have been released
    from Elun.\n\nTo activate the fight against Experiment Z-57, you must use the
    Morph Ball Launcher to enter the arena."
- question: I opened the Wide Beam door in Dairon's Teleport to Cataris, but it won't
    let me through!
  answer: "Unlocking this door before turning on the power will render it unopenable.\n
    \nTo fix this, simply save and reload the game."
- question: I received a Beam/Missile upgrade from an E.M.M.I., and now my arm cannon
    doesn't work!
  answer: Reload from checkpoint immediately to fix the issue. Your checkpoint was
    saved after killing the E.M.M.I., so you will not lose progress.
- question: Why are items, hints, and the seed hash not displaying properly in my
    game?
  answer: "Currently, English is the only officially supported language.\n\nYou must
    set your language to English to see all the text the randomizer changes."
---
