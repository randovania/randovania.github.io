---
game-id: samus_returns
short-name: MSR
long-name: 'Metroid: Samus Returns'
randomize: []
need-to-play: []
multiworld: false
development-state: experimental
faq:
- question: What are the icons on the bottom of the HUD?
  answer: 'These elements are present in the vanilla game, but they have been slightly
    revamped. From left to right, the HUD shows the amount of DNA you currently have,
    the amount of DNA collected per area out of how many in that area, and the amount
    of Metroids that are still alive. '
- question: Do I still need to beat Metroids and collect DNA to progress areas?
  answer: No you do not. All the hazardous liquid has already been drained. Metroids
    can now drop any item in the game as well as DNA.
- question: Do I have to beat the Queen Metroid to beat the game?
  answer: In order to beat the game, you must collect the required Metroid DNA, find
    the Baby, and defeat Proteus Ridley.
- question: How much Metroid DNA is required to beat the game?
  answer: The amount of required DNA is configurable from 0 to 39 DNA. The HUD shows
    how much DNA is located in each area, just like in the vanilla game.
- question: How do I access Proteus Ridley?
  answer: In the vanilla game, the Surface area where Proteus Ridley resides is a
    separate map from the starting Surface. These are normally not connected. This
    has been changed to warp the player to the other Surface map by passing the Baby
    blocks in the Landing Site. Once enough DNA is collected to access Ridley, you
    can no longer warp from Surface West to Surface East.
- question: Are there any hints?
  answer: "All Chozo Seals have been repurposed to provide a hint to an item somewhere
    in the world. The region the item is located will be specified.\n\nNew seals have
    been added in all areas except Surface which hint at the location of DNA. See
    the `Hints` tab for more information."
- question: Why is this pickup not animating?
  answer: While progressive pickups update to have the correct model, due to limitations
    these models are not animated.
- question: I collected Beam Burst, but I cannot use it.
  answer: Beam Burst requires at least the Wave Beam to function.
- question: What are Reserve Tanks?
  answer: "Reserve Tanks are items that restore a certain ammo type when depleted.
    In vanilla, these tanks can be unlocked by using certain amiibo, but in the randomizer,
    this has been changed to make them be actual pickups.\n\nBy default, the Energy
    Reserve Tank restores 299 Energy, the Aeion Reserve Tank restores 500 Aeion, and
    the Missile Reserve Tank restores 30 Missiles or 10 Super Missiles. Note that
    when the Missile Reserve Tank is depeleted, it only restores whatever ammo was
    last used, and not both."
- question: I collected the Missile Reserve Tank, but I cannot see nor use it.
  answer: Due to limitations, the Missile Reserve Tank will remain deactivated until
    the Missile Launcher is in your inventory. This prevents a bug where the reserve
    will activate even if you have no usable Missiles.
---
