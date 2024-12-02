---
layout: post
title: "Input Validation"
tags: prime1 prime2
---
When an error happens when exporting the game, it's important to make sure the game files you are using are the originals with no modifications. Randovania only supports unmodified game files.

# Verifying your game files

## Metroid Prime and Metroid Prime 2: Echoes

Both games only support the GameCube versions of the game, with uncompressed files in the ISO format.

In order to verify the if your ISO is identical, we recommend using [Dolphin Emulator](https://dolphin-emu.org/).

{% include blog/figure.html src="/assets/guides/input_validation/dolphin-game-list.png" caption="Dolphin Game List" %}

Make sure the ISO you want to verify is in Dolphin's Game Folders, then right click → Properties.

{% include blog/figure.html src="/assets/guides/input_validation/verify-result.png" caption="Game verified, with good dump" %}

In the new window, select the tab Verify and then press **Verify Integrity**. You should see `Good dump` in `Redump.org Status`.

