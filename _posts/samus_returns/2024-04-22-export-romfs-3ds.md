---
layout: post
title: "How to extract your Metroid: Samus Returns RomFS"
tags: samus_returns
---
You can either extract your RomFS using Godmode9 from your 3DS, or using Citra from an installation file (.3ds or .cia). We'll show you how to do it using both methods.

## Godmode9

### Game Installed on SD Card

If you're using the NTSC version, navigate to **[A:] SYSNAND SD -> title -> 00040000 -> 001bb200 -> content -> 00000000.tmd**.

If you're using the PAL version, navigate to **[A:] SYSNAND SD -> title -> 00040000 -> 001bfb00 -> content -> 00000000.tmd**.

{% include blog/figure.html src="/assets/guides/godmode9/godmode9-1.png" caption="Godmode9 screen for installed game path" %}

Next, navigate to **TMD file options... -> Mount CXI/NDA to drive**, then press A to confirm.

Highlight the **romfs** directory, and press A while holding R to open another menu. From here, select **Copy to 0:/gm9/out**. Copy the extracted RomFS folder from this directory on the SD Card to some place on your computer.

{% include blog/figure.html src="/assets/guides/godmode9/godmode9-2.png" caption="Menu to extract RomFS to output folder on SD Card" %}

### Game Cartridge

If you're using the NTSC version, navigate to **[C:] GAMECART -> 00040000001BB200_v00.trim.3ds**.

If you're using the PAL version, navigate to **[C:] GAMECART -> 00040000001BFB00_v00.trim.3ds**.

{% include blog/figure.html src="/assets/guides/godmode9/godmode9-3.png" caption="Godmode9 screen for game cartridge" %}

Next, navigate to **NCSD image options... -> Mount image to drive**, then press A to confirm.

Press A to enter the **content0.game** directory. Highlight the **romfs** directory, and press A while holding R to open another menu. From here, select **Copy to 0:/gm9/out**. Copy the extracted RomFS folder from this directory on the SD Card to some place on your computer.

{% include blog/figure.html src="/assets/guides/godmode9/godmode9-4.png" caption="Menu to extract RomFS to output folder on SD Card" %}

## Citra

First, download and setup Citra. Once you've set it up, navigate to **File -> Install CIA...** to add the directory with your game image or simply double click on **Add New Game Directory** in the main window. Your game should be shown in Citra now.

{% include blog/figure.html src="/assets/guides/romfs_msr/citra1.png" caption="The Citra game window" %}

Finally, right click on the game and select **Dump RomFS**.

{% include blog/figure.html src="/assets/guides/romfs_msr/citra2.png" caption="Menu showing how to dump the RomFS" %}