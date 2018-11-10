from header_factions import *

####################################################################################################################
#  Each faction record contains the following fields:
#  1) Faction id: used for referencing factions in other files.
#     The prefix fac_ is automatically added before each faction id.
#  2) Faction name.
#  3) Faction flags. See header_factions.py for a list of available flags
#  4) Faction coherence. Relation between members of this faction.
#  5) Relations. This is a list of relation records.
#     Each relation record is a tuple that contains the following fields:
#    5.1) Faction. Which other faction this relation is referring to
#    5.2) Value: Relation value between the two factions.
#         Values range between -1 and 1.
#  6) Ranks
#  7) Faction color (default is gray)
####################################################################################################################

## CC
default_kingdom_relations = [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02)]
## CC

factions = [
  ("no_faction","No Faction",0, 0.9, [], []),
  ("commoners","Commoners",0, 0.1,[("player_faction",0.1)], []),
  ("outlaws","Outlaws", max_player_rating(-30), 0.5,[("commoners",-0.6),("player_faction",-0.15)], [], 0x999999), ## CC
# Factions before this point are hardwired into the game end their order should not be changed.

  ("neutral","Neutral",0, 0.1,[("player_faction",0.0)], [],0xFFFFFF),
  ("innocents","Innocents", ff_always_hide_label, 0.5,[("outlaws",-0.05)], []),
  ("merchants","Merchants", ff_always_hide_label, 0.5,[("outlaws",-0.5),], []),

## CC
  ("dark_knights","{!}Dark Knights", 0, 0.5,[("outlaws", 0.1)], [], 0x800000),
  ("black_khergits","{!}Black Khergits", 0, 0.5,[("outlaws", 0.1)], [], 0x800000),
## CC

  ("culture_1",  "{!}culture_1", 0, 0.9, [], []),
  ("culture_2",  "{!}culture_2", 0, 0.9, [], []),
  ("culture_3",  "{!}culture_3", 0, 0.9, [], []),
  ("culture_4",  "{!}culture_4", 0, 0.9, [], []),
  ("culture_5",  "{!}culture_5", 0, 0.9, [], []),
  ("culture_6",  "{!}culture_6", 0, 0.9, [], []),

#  ("swadian_caravans","Swadian Caravans", 0, 0.5,[("outlaws",-0.8), ("dark_knights",-0.2)], []),
#  ("vaegir_caravans","Vaegir Caravans", 0, 0.5,[("outlaws",-0.8), ("dark_knights",-0.2)], []),

  ("player_faction","Player Faction",0, 0.9, [], []),
## CC
  #changed name so that can tell difference if shows up on map
  ("player_supporters_faction","Player's Supporters",0, 0.9, [("player_faction",1.00),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02)], [], 0xFF4433),
  
  ("kingdom_1_noble_rebels",  "Swadian Rebels",   0, 0.9, default_kingdom_relations, [], 0x996633),
  ("kingdom_2_noble_rebels",  "Vaegir Rebels",    0, 0.9, default_kingdom_relations, [], 0x6666CC),
  ("kingdom_3_noble_rebels",  "Khergit Rebels",   0, 0.9, default_kingdom_relations, [], 0x8866CC),
  ("kingdom_4_noble_rebels",  "Nord Rebels",      0, 0.9, default_kingdom_relations, [], 0x339999),
  ("kingdom_5_noble_rebels",  "Rhodok Rebels",    0, 0.9, default_kingdom_relations, [], 0x339933),
  ("kingdom_6_noble_rebels",  "Sarranid Rebels",  0, 0.9, default_kingdom_relations, [], 0x999933),
  
  ("kingdom_1",  "Kingdom of Swadia",   0, 0.9, default_kingdom_relations, [], 0xEE7744),
  ("kingdom_2",  "Kingdom of Vaegirs",  0, 0.9, default_kingdom_relations, [], 0x9696FF),
  ("kingdom_3",  "Khergit Khanate",     0, 0.9, default_kingdom_relations, [], 0xCC99FF),
  ("kingdom_4",  "Kingdom of Nords",    0, 0.9, default_kingdom_relations, [], 0x33DDDD),
  ("kingdom_5",  "Kingdom of Rhodoks",  0, 0.9, default_kingdom_relations, [], 0x33DD33),
  ("kingdom_6",  "Sarranid Sultanate",  0, 0.9, default_kingdom_relations, [], 0xDDDD33),
## CC

##  ("kingdom_1_rebels",  "Swadian rebels", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_2_rebels",  "Vaegir rebels",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_3_rebels",  "Khergit rebels", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_4_rebels",  "Nord rebels",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_5_rebels",  "Rhodok rebels",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),

  ("kingdoms_end","{!}kingdoms_end", 0, 0,[], []),
  ("robber_knights",  "{!}robber_knights", 0, 0.1, [], []),
  ("khergits","{!}Khergits", 0, 0.5,[("player_faction",0.0)], []),
##  ("rebel_peasants","Rebel Peasants", 0, 0.5,[("vaegirs",-0.5),("player_faction",0.0)], []),

  ("manhunters","Manhunters", 0, 0.5,[("outlaws",-0.6),("player_faction",0.1)], [], 0x80ff80), ## CC
  ("deserters","Deserters", 0, 0.5,[("manhunters",-0.6),("merchants",-0.5),("player_faction",-0.1)], [], 0xff8080), ## CC
  #("mountain_bandits","Mountain Bandits", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0x888888),
  #("forest_bandits","Forest Bandits", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0x888888),

  ("undeads","{!}Undeads", max_player_rating(-30), 0.5,[("commoners",-0.7),("player_faction",-0.5)], []),
  ("slavers","{!}Slavers", 0, 0.1, [], []),
  ("peasant_rebels","{!}Peasant Rebels", 0, 1.0,[("noble_refugees",-1.0),("player_faction",-0.4)], []),
  ("noble_refugees","{!}Noble Refugees", 0, 0.5,[], []),
]
