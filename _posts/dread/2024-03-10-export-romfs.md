---
layout: post
title: "How to extract your Metroid Dread RomFS"
tags: dread
---
You can either extract your RomFS using nxdumptool from your Switch, or using Ryujinx from an image (.nsp or .xci). We'll show you how to do it using Ryujinx.

First, download and setup Ryujinx. Make sure you follow their start-up guide after installation. You can download Ryujinx here: <https://ryujinx.org/download>

Once you've set it up, navigate to **Options -> Settings** to add the directory with your game image. Your game should be shown in Ryujinx now.

{% include blog/figure.html src="/assets/guides/romfs/ryujinx1.png" caption="Ryujinx main screen" %}

If you wish to use version 2.1.0, right click on the game in Ryujinx and select Manage Title Updates. Then apply the update .nsp.

Finally, right click on the game and select **Extract Data -> RomFS**.

{% include blog/figure.html src="/assets/guides/romfs/ryujinx2.png" caption="Ryujinx main screen, showing the right-click context menus to extract the RomFS" %}

Be sure to use the same version of RomFS as you intend to play the game with! If your RomFS dump does not match your game, it can cause problems with the randomizer.

We currently support **1.0.0** and **2.1.0**.