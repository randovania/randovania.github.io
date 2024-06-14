---
layout: post
title: "Connecting Randovania to a Real Wii or Wii U"
tags: multiworld prime1 prime2
---
# Connecting Randovania to a Real Wii or Wii U  

While playing Metroid Prime or Metroid Prime 2: Echoes Multiworld Randomizer on Dolphin Emulator is the most popular method, you can also play it on a real Wii or Wii U Wii Mode ("vWii") with a [custom fork of Nintendont](https://github.com/randovania/Nintendont/) with support for networked multiworld and automatic item tracking.  
Using a real Wii and Wii U console may be favorable if your computer does not run emulated GameCube games well.  
  
## Requirements  

* **A USB Storage Device or SD Card**  
  * **Recommended device**: From most to least preferred: USB Hard Drive, SD card, USB flash drive  
  * **Recommended format**: FAT32 with 32 KB clusters  
    **⚠️ WARNING** Formatting will erase all the data on that storage device. Backup/copy your storage device's files to a different location before formatting.  
    * NTFS will not work. exFAT can work, but may cause issues with other homebrew apps.   
* **A Wii or Wii U vWii** with:  
  * **The Homebrew Channel**  
    * [Installation Guide](https://wii.hacks.guide/get-started)  
      (Patched/cIOSes are not needed.)  
  * **A Network Connection**  
    * **ℹ️ NOTE** It is strongly recommended to use a wired Ethernet connection for the console instead of the console's built-in Wi-Fi if possible. Using Wi-Fi may be more unstable.  
      * Third-party adapters Ethernet using the ASIX AX88772 or AX88772A chipsets can work too, such as [this one](https://www.amazon.com/gp/product/B00MYT47EA/).  
  * **A Supported Controller**  
    * For consoles with built-in GC controller ports (most Wiis: RVL-001):  
      using those ports with a GameCube controller is recommended.  
    * For consoles without built-in GC controller ports (all Wii Us, some Wiis: RVL-101, RVL-201):  
      using a GameCube Controller Adapter with a GameCube controller is recommended:  
      Both the [official Nintendo adapter](https://smashbros.nintendo.com/buy/accessories/) and the [Mayflash adapter (in Wii U/Switch mode)](https://www.amazon.com/Mayflash-GameCube-Controller-Adapter-Switch/dp/B00RSXRLUE/) will work.  
    * Otherwise, see the [list of Nintendont-supported controllers](https://gbatemp.net/threads/nintendont.349258/#Controllers)  
  
## Steps  
  
 * Insert the storage device into your computer.  
 * Generate and export the game ISO.  
 * Copy the game ISO to the `games` folder of the root of your storage device.  
   * If the `games` folder is not present, create it.  
     For example, on Windows: `S:\games\Prime Randomizer - MyMultiworldSession  - Player.iso`  
 * Insert the storage device into the console.  
 * Start the Homebrew Channel  
 * Press the **HOME** or **START/PAUSE** button to open the Menu in the Homebrew Channel.  
   Take note of the IP Address in the top-left corner.  
   * If it doesn't appear, make sure your console's Internet settings are configured correctly.  
 * Open the Games Connections menu in Randovania:  
   * If in the main Randovania window:  
     * `Open` -> `Automatic Item Tracker` -> `Connections`  
   * If in the Multiworld Session window:  
     * `Session and Connectivity` tab -> `Edit Game Connections`  
 * Click `Add new connection` and select `Nintendont`  
 * Enter the IP address noted from the console earlier.  
 * Find the newly created Nintendont entry, then click the `⋯` button next to it to reveal a menu.  
 * Click `Upload to Nintentdont to Homebrew Channel`  
   This will upload the app the Homebrew Channel and launch it automatically.  
 * In Nintendont, when prompted, choose the storage device that you are using.  
 * **If you do not want/cannot use a real GameCube Memory Card:**  
    * While in the game selection screen, press **B** to enter Nintendont settings.  
    * Set `Memcard Emulation` to `ON`.  
    * Then press **B** again to return to the game list. 
 * **If you have a real GameCube Memory Card that you'd like to use:**  
    * Go to the next step.   
 * Then select your game.  
   The game will start when a connection is made to Randovania.  
 * Afer the game is booted, Randovania's Connections menu should say "Connected".  
   You may now play your game!  
   * If you're playing a multiworld, it is prudent to regularly check the Randovania window to ensure that it's connected.  
  
## Permanently Installing Nintendont Multiworld  
  
These are **optional** steps that add a permanent Nintendont Multiworld entry to the Homebrew Channel without needing to upload it each time to play.  
* Insert the SD Card/USB Storage device into your computer  
* Download and extract **Nintendont-v5-multiworld.zip** from [Releases · randovania/Nintendont](https://github.com/randovania/Nintendont/releases)  
* Copy the extracted Nintendont-v5-multiworld to your storage device's `apps` folder  
    For example, on Windows: `S:\apps\Nintendont-v5-multiworld`  
* Insert the storage into your console, launch the Homebrew Channel, and start *Nintendont (Multiworld)*
  * In the Homebrew Channel, you can switch between apps on your USB device and SD card by pressing **1** or **X**.

## Troubleshooting  
  
* **After selecting the game in Nintendont Multiworld, the screen remains black and the game does not start.**  
  * This may indicate that Randovania is failing to connnect to Nintendont Multiworld.  
  * Try repeating the steps until it works and checking your console's Internet settings.  
  * If you are using Wi-Fi, try switching to a wired Ethernet connection.  
* **I've started Nintendont Multiworld but Randovania stills says "Disconnected".**  
  * The connection doesn't begin until the game itself is started. Randovania should display "Connected" after the game has been started.  
* **I'm already in the playable game, but but Randovania stills says "Disconnected".**  
  * Try repeating the steps until it works and checking your console's Internet settings.
  * If you are using Wi-Fi, try switching to a wired Ethernet connection.  
