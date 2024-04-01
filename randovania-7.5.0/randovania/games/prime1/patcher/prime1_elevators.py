# These are hard-coded into the Randomprime API
# Used by the prime1 patcher
from __future__ import annotations

RANDOMPRIME_CUSTOM_NAMES = {
    ("Impact Crater", "Crater Entry Point"): "Crater Entry Point",  # 2818083
    ("Impact Crater", "Metroid Prime Lair"): "Essence Dead Cutscene",
    ("Frigate Orpheon", "Exterior Docking Hangar"): "Frigate Escape Cutscene",
    ("Phendrana Drifts", "Transport to Magmoor Caverns West"): "Phendrana Drifts North (Phendrana Shorelines)",  # 45
    ("Phendrana Drifts", "Transport to Magmoor Caverns South"): "Phendrana Drifts South (Quarantine Cave)",  # 1900634
    ("Magmoor Caverns", "Transport to Chozo Ruins North"): "Magmoor Caverns North (Lava Lake)",  # 31
    ("Magmoor Caverns", "Transport to Phendrana Drifts North"): "Magmoor Caverns West (Monitor Station)",  # 852002
    ("Magmoor Caverns", "Transport to Tallon Overworld West"): "Magmoor Caverns East (Twin Fires)",  # 1048608
    ("Magmoor Caverns", "Transport to Phazon Mines West"): "Magmoor Caverns South (Magmoor Workstation, Debris)",
    # 1703972
    (
        "Magmoor Caverns",
        "Transport to Phendrana Drifts South",
    ): "Magmoor Caverns South (Magmoor Workstation, Save Station)",  # 1769512
    ("Phazon Mines", "Transport to Tallon Overworld South"): "Phazon Mines East (Main Quarry)",  # 28
    ("Phazon Mines", "Transport to Magmoor Caverns South"): "Phazon Mines West (Phazon Processing Center)",  # 1638417
    ("Tallon Overworld", "Transport to Chozo Ruins West"): "Tallon Overworld North (Tallon Canyon)",  # 917509
    ("Tallon Overworld", "Transport to Chozo Ruins East"): "Tallon Overworld East (Frigate Crash Site)",  # 1441848
    ("Tallon Overworld", "Transport to Magmoor Caverns East"): "Tallon Overworld West (Root Cave)",  # 1507378
    ("Tallon Overworld", "Transport to Chozo Ruins South"): "Tallon Overworld South (Great Tree Hall, Upper)",
    # 2687012
    ("Tallon Overworld", "Transport to Phazon Mines East"): "Tallon Overworld South (Great Tree Hall, Lower)",
    # 2818083
    ("Tallon Overworld", "Artifact Temple"): "Artifact Temple",  # 1049306
    ("Chozo Ruins", "Transport to Tallon Overworld North"): "Chozo Ruins West (Main Plaza)",  # 125
    ("Chozo Ruins", "Transport to Magmoor Caverns North"): "Chozo Ruins North (Sun Tower)",  # 1572903
    ("Chozo Ruins", "Transport to Tallon Overworld East"): "Chozo Ruins East (Reflecting Pool, Save Station)",
    # 4063276
    ("Chozo Ruins", "Transport to Tallon Overworld South"): "Chozo Ruins South (Reflecting Pool, Far End)",  # 4128808
    ("End of Game", "Credits"): "Credits",
}

# Names for use when "elevator" isn't implied
UI_CUSTOM_NAMES = {
    # Ruins
    ("Chozo Ruins", "Transport to Tallon Overworld North"): "Main Plaza Elevator",
    ("Chozo Ruins", "Transport to Magmoor Caverns North"): "Sun Tower Elevator",
    ("Chozo Ruins", "Transport to Tallon Overworld East"): "Reflecting Pool West Elevator (Save)",
    ("Chozo Ruins", "Transport to Tallon Overworld South"): "Reflecting Pool South Elevator (Far)",
    # Magmoor
    ("Magmoor Caverns", "Transport to Chozo Ruins North"): "Lava Lake Elevator",
    ("Magmoor Caverns", "Transport to Phendrana Drifts North"): "Monitor Station Elevator",
    ("Magmoor Caverns", "Transport to Tallon Overworld West"): "Twin Fires Elevator",
    ("Magmoor Caverns", "Transport to Phazon Mines West"): "Magmoor Workstation West Elevator (Debris)",
    ("Magmoor Caverns", "Transport to Phendrana Drifts South"): "Magmoor Workstation South Elevator (Save)",
    # Mines
    ("Phazon Mines", "Transport to Tallon Overworld South"): "Main Quarry Elevator",
    ("Phazon Mines", "Transport to Magmoor Caverns South"): "Phazon Processing Elevator",
    # Phendrana
    ("Phendrana Drifts", "Transport to Magmoor Caverns West"): "Phendrana Shoreline Elevator",
    ("Phendrana Drifts", "Transport to Magmoor Caverns South"): "Quarantine Cave Elevator",
    # Tallon
    ("Tallon Overworld", "Transport to Chozo Ruins West"): "Tallon Canyon Elevator",
    ("Tallon Overworld", "Transport to Chozo Ruins East"): "Frigate Crash Site Elevator",
    ("Tallon Overworld", "Transport to Magmoor Caverns East"): "Root Cave Elevator",
    ("Tallon Overworld", "Transport to Chozo Ruins South"): "Upper/South Great Tree Elevator",
    ("Tallon Overworld", "Transport to Phazon Mines East"): "Lower/North Great Tree Elevator",
    # Frigate
    ("Frigate Orpheon", "Exterior Docking Hangar"): "Exterior Docking Hangar",
    # Impact Crater
    ("Impact Crater", "Crater Entry Point"): "Crater Entry Point",
    ("Impact Crater", "Metroid Prime Lair"): "Essence Dead Cutscene",
}

# Names for use when "elevator" is implied
SHORT_UI_CUSTOM_NAMES = {
    # Ruins
    ("Chozo Ruins", "Transport to Tallon Overworld North"): "Main Plaza",
    ("Chozo Ruins", "Transport to Magmoor Caverns North"): "Sun Tower",
    ("Chozo Ruins", "Transport to Tallon Overworld East"): "Reflecting Pool West (Save)",
    ("Chozo Ruins", "Transport to Tallon Overworld South"): "Reflecting Pool South (Far)",
    # Magmoor
    ("Magmoor Caverns", "Transport to Chozo Ruins North"): "Lava Lake",
    ("Magmoor Caverns", "Transport to Phendrana Drifts North"): "Monitor Station",
    ("Magmoor Caverns", "Transport to Tallon Overworld West"): "Twin Fires",
    ("Magmoor Caverns", "Transport to Phazon Mines West"): "Workstation West (Debris)",
    ("Magmoor Caverns", "Transport to Phendrana Drifts South"): "Workstation South (Save)",
    # Mines
    ("Phazon Mines", "Transport to Tallon Overworld South"): "Main Quarry",
    ("Phazon Mines", "Transport to Magmoor Caverns South"): "Phazon Processing",
    # Phendrana
    ("Phendrana Drifts", "Transport to Magmoor Caverns West"): "Phendrana Shoreline",
    ("Phendrana Drifts", "Transport to Magmoor Caverns South"): "Quarantine Cave",
    # Tallon
    ("Tallon Overworld", "Transport to Chozo Ruins West"): "Tallon Canyon",
    ("Tallon Overworld", "Transport to Chozo Ruins East"): "Frigate Crash Site",
    ("Tallon Overworld", "Transport to Magmoor Caverns East"): "Root Cave",
    ("Tallon Overworld", "Transport to Chozo Ruins South"): "Upper/South Great Tree",
    ("Tallon Overworld", "Transport to Phazon Mines East"): "Lower/North Great Tree",
    # Frigate
    ("Frigate Orpheon", "Exterior Docking Hangar"): "Frigate Destroyed",
    # Impact Crater
    ("Impact Crater", "Crater Entry Point"): "Crater Entry Point",
    ("Impact Crater", "Metroid Prime Lair"): "Essence Dead",
}
