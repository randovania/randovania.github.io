---
layout: post
title: "How to dump a decrypted copy of Metroid: Samus Returns"
tags: samus_returns
---
Using Godmode9 from your 3DS, you can dump a decrypted copy of the game. This guide will ensure you get a proper dump either as a .3ds or .cxi file.

## Game Cartridge

If you're using the NTSC version, navigate to `[C:] GAMECART` -> `00040000001BB200_v00.trim.3ds`.

If you're using the PAL version, navigate to `[C:] GAMECART` -> `00040000001BFB00_v00.trim.3ds`.

{% include blog/figure.html src="/assets/guides/godmode9/godmode9-cart-1.png" caption="Godmode9 screen for game cartridge" %}

Next, navigate to `NCSD image options...` -> `Decrypt file (0:/gm9/out)`, then press A to confirm. 

Copy the `.3ds file` from this directory on the SD Card to some place on your computer.

{% include blog/figure.html src="/assets/guides/godmode9/godmode9-cart-2.png" caption="Menu to decrypt 3DS file to output folder on SD Card" %}

## Game Installed on SD Card

If you're using the NTSC version, navigate to `[A:] SYSNAND SD` -> `title` -> `00040000` -> `001bb200` -> `content` -> `00000000.tmd`.

If you're using the PAL version, navigate to `[A:] SYSNAND SD` -> `title` -> `00040000` -> `001bfb00` -> `content` -> `00000000.tmd`.

{% include blog/figure.html src="/assets/guides/godmode9/godmode9-sd-1.png" caption="Godmode9 screen for installed game path for CXI files" %}

Next, navigate to `TMD file options...` -> `Dump CXI/NDS file`, then press A to confirm.

Copy the `.cxi file` from the `0:/gm9/out` directory on the SD Card to some place on your computer.

{% include blog/figure.html src="/assets/guides/godmode9/godmode9-sd-2.png" caption="Menu to decrypt CXI file to output folder on SD Card" %}