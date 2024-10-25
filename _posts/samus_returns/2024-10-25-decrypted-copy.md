---
layout: post
title: "How to dump a decrypted copy of Metroid: Samus Returns"
tags: samus_returns
---
Using Godmode9 from your 3DS, you can dump a decrypted copy of the game. The end result will provide you with one of the following files: .3ds, .cia, .app, or .cxi.

## Game Cartridge

If you're using the NTSC version, navigate to **[C:] GAMECART -> 00040000001BB200_v00.trim.3ds**.

If you're using the PAL version, navigate to **[C:] GAMECART -> 00040000001BFB00_v00.trim.3ds**.

{% include blog/figure.html src="/assets/guides/godmode9/godmode9-cart-1.png" caption="Godmode9 screen for game cartridge" %}

### 3DS File (Recommended)

Navigate to **NCSD image options... -> Decrypt file (0:/gm9/out)**, then press A to confirm. 

Copy the .3ds file from this directory on the SD Card to some place on your computer.

{% include blog/figure.html src="/assets/guides/godmode9/godmode9-cart-2.png" caption="Menu to decrypt 3DS file to output folder on SD Card" %}

### CIA File

Navigate to **NCSD image options... -> Build CIA from file**, then press A to confirm. 

Copy the .cia file from the **0:/gm9/out** directory on the SD Card to some place on your computer.

{% include blog/figure.html src="/assets/guides/godmode9/godmode9-cart-3.png" caption="Menu to decrypt CIA file to output folder on SD Card" %}

## Game Installed on SD Card

If you're using the NTSC version, navigate to **[A:] SYSNAND SD -> title -> 00040000 -> 001bb200 -> content**.

If you're using the PAL version, navigate to **[A:] SYSNAND SD -> title -> 00040000 -> 001bfb00 -> content**.

{% include blog/figure.html src="/assets/guides/godmode9/godmode9-sd-1.png" caption="Godmode9 screen for installed game path for CIA/CXI files" %}

### CIA File (Recommended)

Navigate to **00000000.tmd -> TMD file options... -> Build CIA (standard)**, then press A to confirm.

Copy the .cia file from the **0:/gm9/out** directory on the SD Card to some place on your computer.

{% include blog/figure.html src="/assets/guides/godmode9/godmode9-sd-2.png" caption="Menu to decrypt CIA file to output folder on SD Card" %}

### CXI File

Navigate to **00000000.tmd -> TMD file options... -> Dump CXI/NDS file**, then press A to confirm.

Copy the .cxi file from the **0:/gm9/out** directory on the SD Card to some place on your computer.

{% include blog/figure.html src="/assets/guides/godmode9/godmode9-sd-3.png" caption="Menu to decrypt CXI file to output folder on SD Card" %}

### APP File

Navigate to **00000001.app -> NCCH image options... -> Decrypt file (0:/gm9/out)**, then press A to confirm.

{% include blog/figure.html src="/assets/guides/godmode9/godmode9-sd-4.png" caption="Godmode9 screen for installed game path for APP file" %}

Copy the .app file from this directory on the SD Card to some place on your computer.

{% include blog/figure.html src="/assets/guides/godmode9/godmode9-sd-5.png" caption="Menu to decrypt APP file to output folder on SD Card" %}