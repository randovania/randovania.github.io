---
layout: post
title: "How to extract your Metroid: Samus Returns ExHeader"
tags: samus_returns
---
You can either extract your ExHeader using Godmode9 from your 3DS, or using Citra from an installation file (.3ds or .cia) and then using [ctrtool](https://github.com/3DSGuy/Project_CTR/releases/tag/ctrtool-v1.2.0) or [pyctr](https://github.com/ihaveamac/pyctr). We'll show you how to do it using Godmode9.

## Game Installed on SD Card

If you're using the NTSC version, navigate to **[A:] SYSNAND SD -> title -> 00040000 -> 001bb200 -> content -> 00000000.tmd**.

If you're using the PAL version, navigate to **[A:] SYSNAND SD -> title -> 00040000 -> 001bfb00 -> content -> 00000000.tmd**.

{% include blog/figure.html src="/assets/guides/godmode9/godmode9-1.png" caption="Godmode9 screen for installed game path" %}

Next, navigate to **TMD file options... -> Mount CXI/NDA to drive**, then press A to confirm.

Highlight the **extheader.bin** file, and press A while holding R to open another menu. From here, select **Copy to 0:/gm9/out**. Copy the extracted extheader.bin file from this directory on the SD Card to some place on your computer.

{% include blog/figure.html src="/assets/guides/godmode9/godmode9-exheader-sd.png" caption="Menu to extract ExHeader to output folder on SD Card" %}

### Game Cartridge

If you're using the NTSC version, navigate to **[C:] GAMECART -> 00040000001BB200_v00.trim.3ds**.

If you're using the PAL version, navigate to **[C:] GAMECART -> 00040000001BFB00_v00.trim.3ds**.

{% include blog/figure.html src="/assets/guides/godmode9/godmode9-3.png" caption="Godmode9 screen for game cartridge" %}

Next, navigate to **NCSD image options... -> Mount image to drive**, then press A to confirm.

Press A to enter the **content0.game** directory. Highlight the **extheader.bin** file, and press A while holding R to open another menu. From here, select **Copy to 0:/gm9/out**. Copy the extracted extheader.bin file from this directory on the SD Card to some place on your computer.

{% include blog/figure.html src="/assets/guides/godmode9/godmode9-exheader-cart.png" caption="Menu to extract ExHeader to output folder on SD Card" %}