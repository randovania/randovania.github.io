---
game-id: prime1
short-name: Prime
long-name: Metroid Prime
randomize:
- All items including Artifacts
- Elevator destinations
- Starting locations
- Door locks
need-to-play:
- An ISO of any GameCube release of the game
- A modded Wii, or Dolphin Emulator
multiworld: true
development-state: stable
faq:
- question: An item collection message sometimes shows up when collecting items,
    even when disabled. Why?
  answer: In a multiworld, you must not collect items for other players too 
    quickly. To avoid issues, the message box is forced in situations a problem 
    could happen. For more details on the problem, check *Randovania Help -> 
    Multiworld*.
- question: What is a Shiny Missile Expansion?
  answer: "Missile Expansions have a 1 in 1024 of being Pok\xE9mon-style shiny: they
    look different but behave entirely the same as normal.\n\nIn a multiworld game,
    only your own Missile Expansions can be shiny."
- question: What versions of the game are supported?
  answer: All Gamecube versions are supported. If it plays with tank controls, 
    it can be randomized. Wii/Trilogy version is not supported at this time.
- question: Won't seeds requiring glitches be incompletable on PAL, JP, and 
    Player's Choice due to the version differences from NTSC 0-00?
  answer: When the output ISO is generated, the input version is automatically 
    detected, and any bug or sequence break fixes present on that version are 
    undone. This reverts the game to be functionally equivalent to NTSC 0-00, 
    meaning that all versions of Prime are guaranteed to be logically 
    completable when randomized.
- question: Why do I not take heat damage in some rooms in Magmoor, despite not 
    having Varia Suit?
  answer: "Some rooms in Magmoor are not coded to be superheated. These include:\n\
    - All Elevator Rooms\n- Burning Trail\n- Storage Cavern\n- Every room after Twin
    Fires Tunnel\n"
---
