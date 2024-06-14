---
layout: post
title: "Connecting Randovania to a Real Wii or Wii U with Nintendont Multiworld"
tags: multiworld prime1 prime2
---
# Connecting Randovania to a Real Wii or Wii U with Nintendont Multiworld #  
While playing Metroid Prime or Metroid Prime 2: Echoes Multiworld Randomizer on Dolphin Emulator is the most popular method, you can also play it on a real Wii or Wii U (Wii Mode) with a [custom fork of Nintendont](https://github.com/randovania/Nintendont/) with support for networked multiworld and automatic item tracking.  
Using a real Wii and Wii U console may be favorable if your computer does not run emulated GameCube games well.  
  
## Requirements ##  
  
* **A Computer with an SD Card Reader**  
  This guide assumes using Windows, but this should be similar for other operating systems.  
* **All the prerequisites to use and generate a game with [Randovania](https://randovania.org/)**  
* **An SD Card**  
  Recommended format: FAT32 with 32 KB clusters  
  * **⚠️ WARNING** Formatting will erase all the data on that card. Backup/copy your card's files to a different location before formatting.  
  * exFAT can work, but can cause issues with other homebrew apps. NTFS will not work.  
  * USB Storage may also work, but it's difficult to tell which models are reliable with the Wii and Wii U.  
* A **Wii** or **Wii U (Wii Mode)** console with:  
  * **The Homebrew Channel**  
    * [Installation Guide](https://wii.hacks.guide/get-started)  
      (Patched/cIOSes are not needed.)  
  * **Connection to the Network**  
    * **ℹ️ NOTE** It is strongly recommended to use a wired Ethernet connection for the console instead of the console's built-in Wi-Fi if possible. The console's Wi-Fi is *slow*.  
      * Third-party adapters Ethernet using the ASIX AX88772 or AX88772A chipsets can work too, such as [this one](https://www.amazon.com/gp/product/B00MYT47EA/).  
  * **A Supported Controller**  
    * For consoles with built-in GC controller ports (most Wiis: RVL-001):  
      using those ports with a GameCube controller is recommended.  
    * For consoles without built-in GC controller ports (all Wii Us, some Wiis: RVL-101, RVL-201):  
      using a GameCube Controller Adapter with a GameCube controller is recommended:  
      Both the [official Nintendo adapter](https://smashbros.nintendo.com/buy/accessories/) and the [Mayflash adapter (in Wii U/Switch mode)](https://www.amazon.com/Mayflash-GameCube-Controller-Adapter-Switch/dp/B00RSXRLUE/) will work.  
    * Otherwise, see the [list of Nintendont-supported controllers](https://gbatemp.net/threads/nintendont.349258/#Controllers)  
  
## Steps ##  
  
 * Insert the SD Card into your computer.  
 * Generate and export the game ISO.  
 * Copy the game ISO to the `games` folder of the root of your SD Card.  
   * If the `games` folder is not present, create it.  
     For example, on Windows: *`S:\games\Prime Randomizer - MyMultiworldSession  - Nystrata.iso`*  
 * Insert the SD Card into the console.  
 * Start the Homebrew Channel  
 * Press HOME or START/PAUSE to open the Hombrew Channel Menu.  
   Take note of the IP Address in the top-left corner.  
   * If it doesn't appear, make sure your console's Internet settings are configured correctly.  
 * Open the Games Connections menu:  
   * If in the main Randovania window:  
     * *Open* -> *Automatic Item Tracker* -> *Connections*  
   * If in the Multiworld Session window:  
     * *Session and Connectivity* tab -> *Edit Game Connections*  
 * Click *Add new connection* and select *Nintendont*  
 * Enter the IP address noted from the console earlier.  
 * Find the newly created Nintendont entry, then click the ***`...`*** button next to it to reveal a menu.  
 * Click *Upload to Nintentdont to Homebrew Channel*  
   This will upload the app the Homebrew Channel and launch it automatically.  
 * With Nintendont, when asked to select a storage device, select SD  
 * <ins>**If you have a real GameCube Memory Card that you'd like to use:**</ins>  
    * Skip over the next step and select your game.  
 * <ins>**If you do not want/cannot use a GameCube Memory Card:**</ins>  
    * While in the game selection screen, press **B** to enter Nintendont settings.  
    * Set *Memcard Emulation* to `ON`.  
    * Then press **B** again to return to the game list.  
 * Then select your game.  
   The game will start when a connection is made to Randovania.  
   * If the screen remains black after a long moment, it may be that it's failing to connect to Randovania:  
     Check your connection settings and IP address and try again.  
 * Afer the game is booted, Randovania's Connections menu should say "Connected".  
   You may now play your game!  
   * If you're playing a multiworld, it is prudent to regularly check the Randovania window to ensure that it's connected.  
  
## Permanently Installing Nintendont Multiworld ##  
  
This adds a permanent Nintendont Multiworld entry to the Homebrew Channel without needing to upload it each time to play.  
* Insert the SD Card into your computer  
* Download and extract **Nintendont-v5-multiworld.zip** from [Releases · randovania/Nintendont](https://github.com/randovania/Nintendont/releases)  
* Copy the extracted Nintendont-v5-multiworld to your SD Card's `apps` folder  
    For example, on Windows: `S:\apps\Nintendont-v5-multiworld`  
* Insert the SD Card into your console, launch the Homebrew Channel, and start *Nintendont (Multiworld)*