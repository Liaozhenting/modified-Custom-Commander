import random

from header_common import *
from header_items import *
from header_troops import *
from header_skills import *
from ID_factions import *
from ID_items import *
from ID_scenes import *

####################################################################################################################
#  Each troop contains the following fields:
#  1) Troop id (string): used for referencing troops in other files. The prefix trp_ is automatically added before each troop-id .
#  2) Toop name (string).
#  3) Plural troop name (string).
#  4) Troop flags (int). See header_troops.py for a list of available flags
#  5) Scene (int) (only applicable to heroes) For example: scn_reyvadin_castle|entry(1) puts troop in reyvadin castle's first entry point
#  6) Reserved (int). Put constant "reserved" or 0.
#  7) Faction (int)
#  8) Inventory (list): Must be a list of items
#  9) Attributes (int): Example usage:
#           str_6|agi_6|int_4|cha_5|level(5)
# 10) Weapon proficiencies (int): Example usage:
#           wp_one_handed(55)|wp_two_handed(90)|wp_polearm(36)|wp_archery(80)|wp_crossbow(24)|wp_throwing(45)
#     The function wp(x) will create random weapon proficiencies close to value x.
#     To make an expert archer with other weapon proficiencies close to 60 you can use something like:
#           wp_archery(160) | wp(60)
# 11) Skills (int): See header_skills.py to see a list of skills. Example:
#           knows_ironflesh_3|knows_power_strike_2|knows_ironflesh_2|knows_athletics_2|knows_riding_2
# 12) Face code (int): You can obtain the face code by pressing ctrl+E in face generator screen
# 13) Face code (int)(2) (only applicable to regular troops, can be omitted for heroes):
#     The game will create random faces between Face code 1 and face code 2 for generated troops
# 14) Troop image (string): If this variable is set, the troop will use an image rather than its 3D visual during the conversations
#  town_1   Sargoth
#  town_2   Tihr
#  town_3   Veluca
#  town_4   Suno
#  town_5   Jelkala
#  town_6   Praven
#  town_7   Uxkhal
#  town_8   Reyvadin
#  town_9   Khudan
#  town_10  Tulga
#  town_11  Curaw
#  town_12  Wercheg
#  town_13  Rivacheg
#  town_14  Halmar
####################################################################################################################

# Some constant and function declarations to be used below...
# wp_one_handed () | wp_two_handed () | wp_polearm () | wp_archery () | wp_crossbow () | wp_throwing ()
def wp(x):
  n = 0
  r = 10 + int(x / 10)
#  n |= wp_one_handed(x + random.randrange(r))
#  n |= wp_two_handed(x + random.randrange(r))
#  n |= wp_polearm(x + random.randrange(r))
#  n |= wp_archery(x + random.randrange(r))
#  n |= wp_crossbow(x + random.randrange(r))
#  n |= wp_throwing(x + random.randrange(r))
  n |= wp_one_handed(x)
  n |= wp_two_handed(x)
  n |= wp_polearm(x)
  n |= wp_archery(x)
  n |= wp_crossbow(x)
  n |= wp_throwing(x)
  return n

def wpe(m,a,c,t):
   n = 0
   n |= wp_one_handed(m)
   n |= wp_two_handed(m)
   n |= wp_polearm(m)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n

def wpex(o,w,p,a,c,t):
   n = 0
   n |= wp_one_handed(o)
   n |= wp_two_handed(w)
   n |= wp_polearm(p)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n
   
def wp_melee(x):
  n = 0
  r = 10 + int(x / 10)
#  n |= wp_one_handed(x + random.randrange(r))
#  n |= wp_two_handed(x + random.randrange(r))
#  n |= wp_polearm(x + random.randrange(r))
  n |= wp_one_handed(x + 20)
  n |= wp_two_handed(x)
  n |= wp_polearm(x + 10)
  return n

## skill overhaul
# def knows_one_handed(x):
  # return x << (skl_power_one_handed << 2)

# def knows_two_handed(x):
  # return x << (skl_power_two_handed << 2)
  
# def knows_polearm(x):
  # return x << (skl_power_polearm << 2)
  
# def knows_melee(o,w,p):
  # n = 0
  # n |= knows_one_handed(o)
  # n |= knows_two_handed(w)
  # n |= knows_polearm(p)
  # return n
  
def_attrib = attr(7,5,4,4)
## skill overhaul
  
  
#Skills
knows_common = knows_riding_1|knows_speechcraft_2|knows_inventory_management_2|knows_looting_2|knows_leadership_1 ## skill overhaul 
knows_common_multiplayer = knows_speechcraft_10|knows_inventory_management_10|knows_looting_10|knows_leadership_10|knows_spotting_10|knows_pathfinding_10|knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10 ## CC


def_attrib_multiplayer = int_30|cha_30

def_int_cha = int_4|cha_4 ## CC

knows_warrior_npc = knows_weapon_master_2|knows_shield_2|knows_ironflesh_1|knows_athletics_1|knows_power_strike_2|knows_riding_2|knows_inventory_management_2|knows_looting_2
knows_merchant_npc = knows_riding_2|knows_speechcraft_3|knows_inventory_management_3|knows_looting_3 #knows persuasion
knows_tracker_npc = knows_weapon_master_1|knows_shield_1|knows_ironflesh_2|knows_athletics_2|knows_spotting_2|knows_pathfinding_2|knows_tracking_2|knows_inventory_management_2|knows_looting_2

## CC
lord_attrib = str_20|agi_19|int_18|cha_21|level(38)
knows_lord_1 = knows_riding_3|knows_speechcraft_2|knows_inventory_management_2|knows_looting_2|knows_leadership_7

knight_attrib_1 = str_17|agi_16|int_13|cha_16|level(22)
knight_attrib_2 = str_18|agi_17|int_14|cha_17|level(26)
knight_attrib_3 = str_19|agi_18|int_15|cha_18|level(30)
knight_attrib_4 = str_20|agi_19|int_16|cha_20|level(35)
knight_attrib_5 = str_21|agi_20|int_17|cha_23|level(41)
knight_skills_1 = knows_riding_3|knows_power_strike_3|knows_shield_2|knows_weapon_master_2|knows_ironflesh_2|knows_athletics_1|knows_tactics_2|knows_leadership_4
knight_skills_2 = knows_riding_4|knows_power_strike_4|knows_shield_3|knows_weapon_master_3|knows_ironflesh_3|knows_athletics_2|knows_tactics_3|knows_leadership_5
knight_skills_3 = knows_riding_5|knows_power_strike_5|knows_shield_4|knows_weapon_master_4|knows_ironflesh_4|knows_athletics_3|knows_tactics_4|knows_leadership_6
knight_skills_4 = knows_riding_6|knows_power_strike_6|knows_shield_5|knows_weapon_master_5|knows_ironflesh_5|knows_athletics_4|knows_tactics_5|knows_leadership_7
knight_skills_5 = knows_riding_7|knows_power_strike_7|knows_shield_6|knows_weapon_master_6|knows_ironflesh_6|knows_athletics_5|knows_tactics_6|knows_leadership_8
## CC

#These face codes are generated by the in-game face generator.
#Enable edit mode and press ctrl+E in face generator screen to obtain face codes.


reserved = 0

no_scene = 0

swadian_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
swadian_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
swadian_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
swadian_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
swadian_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

swadian_face_younger_2 = 0x00000000000062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_young_2   = 0x00000003c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_middle_2  = 0x00000007c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_old_2     = 0x0000000bc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_older_2   = 0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000

vaegir_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
vaegir_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
vaegir_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
vaegir_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
vaegir_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

vaegir_face_younger_2 = 0x000000003f00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_young_2   = 0x00000003bf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_middle_2  = 0x00000007bf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_old_2     = 0x0000000cbf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_older_2   = 0x0000000ff100230c4deeffffffffffff00000000001efff90000000000000000

khergit_face_younger_1 = 0x0000000009003109207000000000000000000000001c80470000000000000000
khergit_face_young_1   = 0x00000003c9003109207000000000000000000000001c80470000000000000000
khergit_face_middle_1  = 0x00000007c9003109207000000000000000000000001c80470000000000000000
khergit_face_old_1     = 0x0000000b89003109207000000000000000000000001c80470000000000000000
khergit_face_older_1   = 0x0000000fc9003109207000000000000000000000001c80470000000000000000

khergit_face_younger_2 = 0x000000003f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_young_2   = 0x00000003bf0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_middle_2  = 0x000000077f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_old_2     = 0x0000000b3f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_older_2   = 0x0000000fff0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000

nord_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
nord_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
nord_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
nord_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
nord_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

nord_face_younger_2 = 0x00000000310023084deeffffffffffff00000000001efff90000000000000000
nord_face_young_2   = 0x00000003b10023084deeffffffffffff00000000001efff90000000000000000
nord_face_middle_2  = 0x00000008310023084deeffffffffffff00000000001efff90000000000000000
nord_face_old_2     = 0x0000000c710023084deeffffffffffff00000000001efff90000000000000000
nord_face_older_2   = 0x0000000ff10023084deeffffffffffff00000000001efff90000000000000000

rhodok_face_younger_1 = 0x0000000009002003140000000000000000000000001c80400000000000000000
rhodok_face_young_1   = 0x0000000449002003140000000000000000000000001c80400000000000000000
rhodok_face_middle_1  = 0x0000000849002003140000000000000000000000001c80400000000000000000
rhodok_face_old_1     = 0x0000000cc9002003140000000000000000000000001c80400000000000000000
rhodok_face_older_1   = 0x0000000fc9002003140000000000000000000000001c80400000000000000000

rhodok_face_younger_2 = 0x00000000000062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_young_2   = 0x00000003c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_middle_2  = 0x00000007c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_old_2     = 0x0000000bc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_older_2   = 0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000

man_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
man_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
man_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
man_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
man_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

man_face_younger_2 = 0x000000003f0052064deeffffffffffff00000000001efff90000000000000000
man_face_young_2   = 0x00000003bf0052064deeffffffffffff00000000001efff90000000000000000
man_face_middle_2  = 0x00000007bf0052064deeffffffffffff00000000001efff90000000000000000
man_face_old_2     = 0x0000000bff0052064deeffffffffffff00000000001efff90000000000000000
man_face_older_2   = 0x0000000fff0052064deeffffffffffff00000000001efff90000000000000000

merchant_face_1    = man_face_young_1
merchant_face_2    = man_face_older_2

woman_face_1    = 0x0000000000000001000000000000000000000000001c00000000000000000000
woman_face_2    = 0x00000003bf0030067ff7fbffefff6dff00000000001f6dbf0000000000000000

swadian_woman_face_1 = 0x0000000180102006124925124928924900000000001c92890000000000000000
swadian_woman_face_2 = 0x00000001bf1000061db6d75db6b6dbad00000000001c92890000000000000000

khergit_woman_face_1 = 0x0000000180103006124925124928924900000000001c92890000000000000000
khergit_woman_face_2 = 0x00000001af1030025b6eb6dd6db6dd6d00000000001eedae0000000000000000

refugee_face1 = woman_face_1
refugee_face2 = woman_face_2
girl_face1    = woman_face_1
girl_face2    = woman_face_2

mercenary_face_1 = 0x0000000000000000000000000000000000000000001c00000000000000000000
mercenary_face_2 = 0x0000000cff00730b6db6db6db7fbffff00000000001efffe0000000000000000

vaegir_face1  = vaegir_face_young_1
vaegir_face2  = vaegir_face_older_2

bandit_face1  = man_face_young_1
bandit_face2  = man_face_older_2

undead_face1  = 0x00000000002000000000000000000000
undead_face2  = 0x000000000020010000001fffffffffff

#NAMES:
#

## CC
tf_guarantee_all_armors = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet
tf_guarantee_all_armors_and_shield = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield
## CC

tf_guarantee_all = tf_guarantee_all_armors_and_shield|tf_guarantee_horse|tf_guarantee_ranged
tf_guarantee_all_wo_ranged = tf_guarantee_all_armors_and_shield|tf_guarantee_horse

troops = [
  ["player","Player","Player",tf_hero|tf_unmoveable_in_party_window,no_scene,reserved,fac_player_faction,
   [],
   str_4|agi_4|int_4|cha_4,wp(15),0,0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["multiplayer_profile_troop_male","multiplayer_profile_troop_male","multiplayer_profile_troop_male", tf_hero|tf_guarantee_all, 0, 0,fac_commoners,
   [itm_leather_jerkin, itm_leather_boots],
   0, 0, 0, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["multiplayer_profile_troop_female","multiplayer_profile_troop_female","multiplayer_profile_troop_female", tf_hero|tf_female|tf_guarantee_all, 0, 0,fac_commoners,
   [itm_tribal_warrior_outfit, itm_leather_boots],
   0, 0, 0, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["temp_troop","Temp Troop","Temp Troop",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10|knows_looting_10,0],
##  ["game","Game","Game",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
##  ["unarmed_troop","Unarmed Troop","Unarmed Troops",tf_hero,no_scene,reserved,fac_commoners,[itm_arrows,itm_short_bow],def_attrib|str_14,0,knows_common|knows_power_draw_2,0],

####################################################################################################################
# Troops before this point are hardwired into the game and their order should not be changed!
####################################################################################################################
  ["find_item_cheat","find_item_cheat","find_item_cheat",tf_hero|tf_is_merchant,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10|knows_looting_10,0],
  ["random_town_sequence","Random Town Sequence","Random Town Sequence",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10|knows_looting_10,0],
  ["tournament_participants","Tournament Participants","Tournament Participants",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10|knows_looting_10,0],
  ["tutorial_maceman","Maceman","Maceman",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_tutorial_club,itm_leather_jerkin,itm_hide_boots],
   def_attrib|level(1),wp(50),knows_common,mercenary_face_1,mercenary_face_2],
  ["tutorial_archer","Archer","Archer",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [itm_tutorial_short_bow,itm_tutorial_arrows,itm_linen_tunic,itm_hide_boots],
   attr(8,7,5,5)|level(5),wp(100),knows_common|knows_power_draw_4,mercenary_face_1,mercenary_face_2],
  ["tutorial_swordsman","Swordsman","Swordsman",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_tutorial_sword,itm_leather_vest,itm_hide_boots],
   attr(8,7,5,5)|level(5),wp(80),knows_common,mercenary_face_1,mercenary_face_2],

  ["novice_fighter","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   attr(8,7,5,5)|level(5),wp(60),knows_common,mercenary_face_1, mercenary_face_2],
  ["regular_fighter","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   attr(11,10,5,5)|level(11),wp(90),knows_power_strike_1|knows_ironflesh_1|knows_athletics_1|knows_riding_1|knows_shield_2|knows_weapon_master_2,mercenary_face_1, mercenary_face_2],
  ["veteran_fighter","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,0,fac_commoners,
   [itm_hide_boots],
   attr(13,12,6,6)|level(17),wp(110),knows_power_strike_2|knows_ironflesh_3|knows_athletics_2|knows_riding_2|knows_shield_3|knows_weapon_master_3,mercenary_face_1, mercenary_face_2],
  ["champion_fighter","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   attr(15,15,6,6)|level(22),wp(140),knows_power_strike_3|knows_ironflesh_4|knows_athletics_3|knows_riding_3|knows_shield_4|knows_weapon_master_4,mercenary_face_1, mercenary_face_2],

  ["arena_training_fighter_1","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   attr(8,7,5,5)|level(5),wp(60),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_2","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   attr(9,8,5,5)|level(7),wp(70),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_3","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   attr(10,9,5,5)|level(9),wp(80),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_4","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   attr(11,10,5,5)|level(11),wp(90),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_5","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   attr(12,11,5,5)|level(13),wp(100),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_6","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   attr(13,12,5,5)|level(15),wp(110),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_7","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   attr(13,12,6,6)|level(17),wp(120),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_8","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   attr(14,13,6,6)|level(19),wp(130),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_9","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   attr(15,14,6,6)|level(21),wp(140),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_10","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   attr(16,15,6,6)|level(23),wp(150),knows_common,mercenary_face_1, mercenary_face_2],

  ["cattle","Cattle","Cattle",0,no_scene,reserved,fac_neutral, [], def_attrib|level(1),wp(60),0,mercenary_face_1, mercenary_face_2],


#soldiers:
#This troop is the troop marked as soldiers_begin
  ["farmer","Farmer","Farmers",tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_linen_tunic,itm_coarse_tunic,itm_nomad_boots,itm_wrapping_boots],
   attr(8,6,5,5)|level(4),wp(75),knows_common,man_face_middle_1, man_face_old_2],
  ["townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_cleaver,itm_knife,itm_club,itm_quarter_staff,itm_dagger,itm_stones,itm_leather_cap,itm_linen_tunic,itm_coarse_tunic,itm_leather_apron,itm_nomad_boots,itm_wrapping_boots],
   attr(8,6,5,5)|level(4),wp(75),knows_common,mercenary_face_1, mercenary_face_2],
  ["watchman","Watchman","Watchmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_arrows,itm_hunting_bow,itm_bolts_2,itm_light_crossbow,itm_spiked_club,itm_fighting_pick,itm_sword_medieval_a,itm_tab_shield_round_a,itm_tab_shield_round_b,itm_padded_cloth,itm_leather_jerkin,itm_leather_cap,itm_padded_coif,itm_footman_helmet,itm_nomad_boots,itm_wrapping_boots],
   attr(10,9,5,5)|level(9),wp(106),knows_common|knows_shield_1|knows_weapon_master_1|knows_ironflesh_1|knows_athletics_1,mercenary_face_1, mercenary_face_2],
  ["mercenary_crossbowman","Mercenary Crossbowman","Mercenary Crossbowman",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [itm_heavy_bolts,itm_crossbow,itm_tab_shield_pavise_a,itm_tab_shield_round_b,itm_spiked_club,itm_fighting_pick,itm_sword_medieval_a,itm_padded_leather,itm_padded_leather,itm_leather_cap,itm_padded_coif,itm_footman_helmet,itm_nomad_boots,itm_wrapping_boots],
   attr(12,12,6,6)|level(16),wp_one_handed (138) | wp_two_handed (138) | wp_polearm (138) | wp_archery (138) | wp_crossbow (170) | wp_throwing (138),knows_ironflesh_2|knows_athletics_3|knows_power_strike_1,mercenary_face_1, mercenary_face_2],   
  ["mercenary_sharpshooter","Mercenary Sharpshooter","Mercenary Sharpshooter",tf_mounted|tf_guarantee_ranged|tf_guarantee_all_armors,no_scene,reserved,fac_commoners,
   [itm_heavy_bolts,itm_heavy_crossbow,itm_tab_shield_pavise_b,itm_tab_shield_round_c,itm_spiked_club,itm_fighting_pick,itm_sword_medieval_b,itm_mail_shirt,itm_mail_shirt,itm_skullcap,itm_mail_coif,itm_footman_helmet,itm_leather_boots,itm_nomad_boots],
   attr(15,13,7,7)|level(22),wp_one_handed (175) | wp_two_handed (175) | wp_polearm (175) | wp_archery (175) | wp_crossbow (200) | wp_throwing (175),knows_ironflesh_3|knows_athletics_5|knows_power_strike_2|knows_riding_2,mercenary_face_1, mercenary_face_2],
  ["caravan_guard","Caravan Guard","Caravan Guards",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm,no_scene,0,fac_commoners,
   [itm_light_lance,itm_fighting_pick,itm_sword_medieval_a,itm_voulge,itm_tab_shield_round_b,itm_tab_shield_round_c,itm_leather_jerkin,itm_leather_vest,itm_hide_boots,itm_padded_coif,itm_nasal_helmet,itm_footman_helmet,itm_courser], ## CC
   attr(12,12,5,5)|level(14),wp(138),knows_ironflesh_3|knows_athletics_3|knows_riding_3|knows_shield_3|knows_weapon_master_3|knows_power_strike_2,mercenary_face_1, mercenary_face_2],
  ["mercenary_swordsman","Mercenary Swordsman","Mercenary Swordsmen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_bastard_sword_a,itm_sword_medieval_b,itm_sword_medieval_c,itm_tab_shield_heater_c,itm_throwing_swords,
   itm_mail_hauberk,itm_haubergeon,itm_leather_boots,itm_mail_chausses,itm_kettle_hat,itm_mail_coif,itm_flat_topped_helmet, itm_helmet_with_neckguard],
   attr(15,13,6,6)|level(20),wp(175),knows_riding_3|knows_ironflesh_5|knows_athletics_5|knows_shield_4|knows_weapon_master_4|knows_power_strike_4|knows_power_throw_3,mercenary_face_1, mercenary_face_2],
  ["hired_blade","Hired Blade","Hired Blades",tf_mounted|tf_guarantee_all_armors_and_shield,no_scene,reserved,fac_commoners,
   [itm_bastard_sword_b,(itm_sword_of_war,imod_tempered),itm_sword_medieval_d_long,itm_tab_shield_heater_cav_a,itm_throwing_swords,
   itm_haubergeon,itm_mail_chausses,itm_iron_greaves,itm_plate_boots,itm_guard_helmet,itm_great_helmet,itm_bascinet, itm_leather_gloves],
   attr(17,14,7,7)|level(25),wp(225),knows_riding_3|knows_ironflesh_7|knows_athletics_7|knows_shield_5|knows_weapon_master_5|knows_power_strike_5|knows_power_throw_4,mercenary_face_1, mercenary_face_2],
  ["mercenary_horseman","Mercenary Horseman","Mercenary Horsemen",tf_mounted|tf_guarantee_horse|tf_guarantee_all_armors_and_shield|tf_guarantee_polearm,no_scene,reserved,fac_commoners,
   [itm_lance,itm_bastard_sword_a,itm_sword_medieval_b,itm_tab_shield_heater_c,itm_mail_shirt,itm_haubergeon,itm_leather_boots,itm_norman_helmet,itm_mail_coif,itm_helmet_with_neckguard,itm_hunter,itm_courser],
   attr(13,15,6,6)|level(20),wp(175),knows_ironflesh_4|knows_athletics_2|knows_riding_4|knows_shield_3|knows_weapon_master_3|knows_power_strike_3,mercenary_face_1, mercenary_face_2],
  ["mercenary_cavalry","Mercenary Cavalry","Mercenary Cavalry",tf_mounted|tf_guarantee_horse|tf_guarantee_all_armors_and_shield|tf_guarantee_polearm,no_scene,reserved,fac_commoners,
   [(itm_heavy_lance,imod_balanced),itm_bastard_sword_a,itm_great_sword,itm_sword_medieval_d_long,itm_tab_shield_heater_c,itm_cuir_bouilli,itm_banded_armor,itm_mail_chausses,itm_kettle_hat,itm_mail_coif,itm_flat_topped_helmet,itm_helmet_with_neckguard,itm_heavy_warhorse,itm_heavy_warhorse],
   attr(15,16,7,7)|level(25),wp(225),knows_ironflesh_6|knows_athletics_3|knows_riding_6|knows_shield_4|knows_weapon_master_4|knows_power_strike_4,mercenary_face_1, mercenary_face_2],
  ["mercenaries_end","{!}mercenaries_end","{!}mercenaries_end",0,no_scene,reserved,fac_commoners,
   [],
   def_attrib|level(4),wp(75),knows_common,mercenary_face_1, mercenary_face_2],

## CC
  ["refugee","Refugee","Refugees",tf_female|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_commoners,
   [itm_knife,itm_pitch_fork,itm_sickle,itm_hatchet,itm_club,itm_dress,itm_robe,itm_woolen_dress, itm_headcloth, itm_woolen_hood, itm_wrapping_boots],
   def_attrib|level(1),wp(56),knows_common,refugee_face1,refugee_face2],
  ["peasant_woman","Peasant Woman","Peasant Women",tf_female|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_commoners,
   [itm_knife,itm_pitch_fork,itm_sickle,itm_hatchet,itm_club,itm_dress,itm_woolen_dress, itm_headcloth, itm_woolen_hood, itm_wrapping_boots],
   def_attrib|level(1),wp(56),knows_common,refugee_face1,refugee_face2],
  ["follower_woman","Camp Follower","Camp Follower",tf_female|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_commoners,
   [itm_bolts,itm_light_crossbow,itm_nordic_shield,itm_hide_covered_round_shield,itm_hatchet,itm_hand_axe,itm_voulge,itm_fighting_pick,itm_club,itm_dress,itm_woolen_dress, itm_skullcap, itm_wrapping_boots],
   attr(8,7,5,5)|level(5),wp(88),knows_common,refugee_face1,refugee_face2],
  ["hunter_woman","Huntress","Huntresses",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   [itm_bolts,itm_crossbow,itm_nordic_shield,itm_hide_covered_round_shield,itm_hatchet,itm_hand_axe,itm_voulge,itm_fighting_pick,itm_club,
   itm_dress,itm_leather_jerkin, itm_skullcap, itm_wrapping_boots],
   attr(9,11,5,5)|level(10),wp(106),knows_riding_1|knows_power_strike_1|knows_ironflesh_1|knows_athletics_1,refugee_face1,refugee_face2],
  # rider
  ["hunter_woman_rider","Mounted Huntress","Mounted Huntresses",tf_female|tf_mounted|tf_guarantee_horse|tf_guarantee_armor|tf_guarantee_polearm,0,0,fac_commoners,
   [itm_light_lance,itm_nordic_shield,itm_hide_covered_round_shield,itm_hatchet,itm_hand_axe,itm_voulge,itm_fighting_pick,itm_club,
   itm_dress,itm_leather_jerkin, itm_skullcap, itm_wrapping_boots,itm_saddle_horse],
   attr(9,11,5,5)|level(10),wp(106),knows_riding_1|knows_power_strike_1|knows_ironflesh_1|knows_athletics_1,refugee_face1,refugee_face2],
  ["fighter_woman_rider","Mounted Camp Defender","Mounted Camp Defenders",tf_female|tf_mounted|tf_guarantee_horse|tf_guarantee_all_armors_and_shield|tf_guarantee_polearm,0,0,fac_commoners,
   [itm_lance,itm_fur_covered_shield,itm_hide_covered_round_shield,itm_hatchet,itm_voulge,itm_mail_shirt,itm_byrnie, itm_skullcap, itm_wrapping_boots,itm_courser,itm_hunter],
   attr(12,14,5,5)|level(16),wp(125),knows_riding_2|knows_power_strike_2|knows_ironflesh_2|knows_athletics_2,refugee_face1,refugee_face2],
  ["sword_sister_rider","Mounted Sword Sister","Mounted Sword Sisters",tf_female|tf_mounted|tf_guarantee_horse|tf_guarantee_all_armors_and_shield|tf_guarantee_polearm,0,0,fac_commoners,
   [itm_heavy_lance,itm_sword_medieval_b,itm_sword_khergit_3,itm_plate_covered_round_shield,itm_tab_shield_small_round_c,itm_heavy_warhorse,itm_charger_black,
   itm_coat_of_plates,itm_coat_of_plates,itm_plate_boots,itm_guard_helmet,itm_helmet_with_neckguard,itm_leather_gloves],
   attr(14,16,6,6)|level(22),wp(175),knows_riding_3|knows_power_strike_3|knows_ironflesh_3|knows_athletics_3|knows_shield_2|knows_weapon_master_2,refugee_face1,refugee_face2],
   
  ["fighter_woman","Camp Defender","Camp Defenders",tf_female|tf_guarantee_all_armors_and_shield,0,0,fac_commoners,
   [itm_steel_bolts,itm_crossbow,itm_heavy_crossbow,itm_fur_covered_shield,itm_hide_covered_round_shield,itm_hatchet,itm_voulge,itm_mail_shirt,itm_byrnie, itm_skullcap, itm_wrapping_boots],
   attr(12,14,5,5)|level(16),wp(125),knows_riding_2|knows_power_strike_2|knows_ironflesh_2|knows_athletics_2,refugee_face1,refugee_face2],
  ["sword_sister","Sword Sister","Sword Sisters",tf_female|tf_guarantee_all_armors_and_shield,0,0,fac_commoners,
   [itm_heavy_bolts,itm_sniper_crossbow,itm_sword_medieval_b,itm_sword_khergit_3,itm_plate_covered_round_shield,itm_tab_shield_small_round_c,
   itm_coat_of_plates,itm_coat_of_plates,itm_plate_boots,itm_guard_helmet,itm_helmet_with_neckguard,itm_leather_gloves],
   attr(14,16,6,6)|level(22),wp(175),knows_riding_3|knows_power_strike_3|knows_ironflesh_3|knows_athletics_3|knows_shield_2|knows_weapon_master_2,refugee_face1,refugee_face2],

   ["manhunter","Manhunter","Manhunters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_manhunters,
   [itm_mace_3,itm_winged_mace,itm_nasal_helmet,itm_padded_cloth,itm_aketon_green,itm_aketon_green,itm_wooden_shield,itm_nomad_boots,itm_wrapping_boots,itm_sumpter_horse],
   attr(11,9,5,5)|level(10),wp(62),knows_common|knows_ironflesh_1|knows_athletics_1,bandit_face1, bandit_face2],
  ["slave_driver","Slave Driver","Slave Drivers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse ,0,0,fac_manhunters,
   [itm_club_with_spike_head,itm_segmented_helmet,itm_tribal_warrior_outfit,itm_nordic_shield,itm_leather_boots,itm_leather_gloves,itm_khergit_leather_boots,itm_steppe_horse],
   attr(13,11,5,5)|level(14),wp(100),knows_ironflesh_1|knows_athletics_1|knows_power_strike_1|knows_riding_2,bandit_face1, bandit_face2],
  ["slave_hunter","Slave Hunter","Slave Hunters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield ,0,0,fac_manhunters,
   [itm_winged_mace,itm_maul,itm_kettle_hat,itm_mail_shirt,itm_tab_shield_round_c,itm_leather_boots,itm_leather_gloves,itm_courser],
   attr(15,13,5,5)|level(18),wp(112),knows_ironflesh_2|knows_athletics_2|knows_riding_3|knows_power_strike_2,bandit_face1, bandit_face2],
  ["slave_crusher","Slave Crusher","Slave Crushers",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_manhunters,
   [itm_sledgehammer,itm_spiked_mace,itm_mail_hauberk,itm_bascinet_2,itm_bascinet_3,itm_mail_mittens,itm_tab_shield_round_d,itm_mail_chausses,itm_splinted_leather_greaves,itm_hunter],
   attr(16,14,6,6)|level(22),wp(138),knows_ironflesh_2|knows_athletics_2|knows_riding_4|knows_power_strike_3,bandit_face1, bandit_face2],
  ["slaver_chief","Slaver Chief","Slaver Chiefs",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_manhunters,
   [itm_military_hammer,itm_warhammer,itm_brigandine_red,itm_plate_covered_round_shield,itm_scale_gauntlets,itm_mail_mittens,itm_guard_helmet,itm_plate_boots,itm_mail_boots,itm_warhorse_brigandine,itm_warhorse_brigandine],
   attr(17,15,7,7)|level(26),wp(163),knows_ironflesh_4|knows_athletics_3|knows_riding_5|knows_power_strike_4,bandit_face1, bandit_face2], ## CC itm_plate_covered_round_shield
## CC
   
#peasant - retainer - footman - man-at-arms -  knight
  ["swadian_recruit","Swadian Recruit","Swadian Recruits",tf_guarantee_armor,0,0,fac_kingdom_1,
   [itm_scythe,itm_hatchet,itm_pickaxe,itm_club,itm_stones,itm_tab_shield_heater_a,itm_leather_cap,itm_felt_hat,itm_felt_hat,
    itm_shirt,itm_coarse_tunic,itm_leather_apron,itm_nomad_boots,itm_wrapping_boots],
   attr(8,6,5,5)|level(4),wp(75),knows_common,swadian_face_younger_1, swadian_face_middle_2],
  ["swadian_militia","Swadian Militia","Swadian Militia",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_1,
   [itm_bolts_2,itm_spiked_club,itm_fighting_pick,itm_boar_spear,itm_hunting_crossbow,itm_tab_shield_heater_a,
    itm_padded_cloth,itm_red_gambeson,itm_arming_cap,itm_arming_cap,itm_ankle_boots,itm_wrapping_boots],
   attr(11,8,5,5)|level(9),wp(94),knows_common,swadian_face_young_1, swadian_face_old_2],
  ["swadian_footman","Swadian Footman","Swadian Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_kingdom_1,
   [itm_spear,itm_fighting_pick,itm_sword_medieval_b_small,itm_sword_medieval_a,itm_tab_shield_heater_b,
    itm_mail_with_tunic_red,itm_ankle_boots,itm_mail_coif,itm_norman_helmet],
   attr(13,11,5,5)|level(14),wp_melee(106)|wp_throwing(115),knows_common|knows_shield_2|knows_weapon_master_2|knows_ironflesh_2|knows_athletics_2|knows_power_strike_2|knows_power_throw_1,swadian_face_young_1, swadian_face_old_2],
## CC
  ["swadian_footman_rider","Swadian Mounted Footman","Swadian Mounted Footmen",tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_kingdom_1,
   [itm_light_lance,itm_fighting_pick,itm_sword_medieval_b_small,itm_sword_medieval_a,itm_tab_shield_heater_b,
    itm_mail_with_tunic_red,itm_ankle_boots,itm_mail_coif,itm_norman_helmet,itm_saddle_horse],
   attr(13,11,5,5)|level(14),wp_melee(106)|wp_throwing(115),knows_common|knows_riding_1|knows_shield_2|knows_weapon_master_2|knows_ironflesh_2|knows_athletics_2|knows_power_strike_2|knows_power_throw_1,swadian_face_young_1, swadian_face_old_2],
  ["swadian_infantry_rider","Swadian Mounted Infantry","Swadian Mounted Infantries",tf_mounted|tf_guarantee_all_armors_and_shield|tf_guarantee_polearm|tf_guarantee_horse,0,0,fac_kingdom_1,
   [itm_light_lance,itm_fighting_pick,itm_bastard_sword_a,itm_sword_medieval_a,itm_sword_medieval_b_small,itm_tab_shield_heater_c,itm_courser,
    itm_mail_with_surcoat,itm_haubergeon,itm_mail_chausses,itm_leather_boots,itm_segmented_helmet,itm_flat_topped_helmet,itm_helmet_with_neckguard],
   attr(15,13,6,6)|level(20),wp_melee(131)|wp_throwing(145),knows_common|knows_riding_2|knows_power_strike_3|knows_power_throw_2|knows_shield_3|knows_weapon_master_3|knows_ironflesh_2|knows_athletics_3,swadian_face_middle_1, swadian_face_old_2],
  ["swadian_sergeant_rider","Swadian Mounted Sergeant","Swadian Mounted Sergeants",tf_mounted|tf_guarantee_all_armors_and_shield|tf_guarantee_polearm|tf_guarantee_horse,0,0,fac_kingdom_1,
   [itm_heavy_lance,(itm_bastard_sword_b,imod_tempered),itm_morningstar,itm_sword_medieval_c,itm_tab_shield_heater_d,itm_hunter,
    itm_coat_of_plates,itm_brigandine_red,itm_mail_boots,itm_iron_greaves,itm_flat_topped_helmet,itm_guard_helmet,itm_mail_mittens,itm_gauntlets],
   attr(17,14,7,7)|level(25),wp_melee(170)|wp_throwing(185),knows_common|knows_riding_3|knows_shield_4|knows_weapon_master_4|knows_power_strike_4|knows_power_throw_3|knows_ironflesh_4|knows_athletics_4,swadian_face_middle_1, swadian_face_older_2], 
## CC
  ["swadian_infantry","Swadian Infantry","Swadian Infantries",tf_guarantee_all_armors_and_shield|tf_guarantee_polearm,0,0,fac_kingdom_1,
   [itm_pike,itm_fighting_pick,itm_bastard_sword_a,itm_sword_medieval_a,itm_sword_medieval_b_small,itm_tab_shield_heater_c,
    itm_mail_with_surcoat,itm_haubergeon,itm_mail_chausses,itm_leather_boots,itm_segmented_helmet,itm_flat_topped_helmet,itm_helmet_with_neckguard],
   attr(15,13,6,6)|level(20),wp_melee(131)|wp_throwing(145),knows_common|knows_riding_2|knows_power_strike_3|knows_power_throw_2|knows_shield_3|knows_weapon_master_3|knows_ironflesh_2|knows_athletics_3,swadian_face_middle_1, swadian_face_old_2],
  ["swadian_sergeant","Swadian Sergeant","Swadian Sergeants",tf_mounted|tf_guarantee_all_armors_and_shield|tf_guarantee_polearm,0,0,fac_kingdom_1,
   [itm_awlpike,(itm_bastard_sword_b,imod_tempered),itm_morningstar,itm_sword_medieval_c,itm_tab_shield_heater_d,
    itm_coat_of_plates,itm_brigandine_red,itm_mail_boots,itm_iron_greaves,itm_flat_topped_helmet,itm_guard_helmet,itm_mail_mittens,itm_gauntlets],
   attr(17,14,7,7)|level(25),wp_melee(170)|wp_throwing(185),knows_common|knows_riding_3|knows_shield_4|knows_weapon_master_4|knows_power_strike_4|knows_power_throw_3|knows_ironflesh_4|knows_athletics_4,swadian_face_middle_1, swadian_face_older_2], ## CC
  #["swadian_double_hander","Swadian Double Hander","Swadian Double Handers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   #[itm_sword_two_handed_b,itm_sword_two_handed_b,
    #itm_cuir_bouilli,itm_cuir_bouilli,itm_mail_chausses,itm_leather_boots,itm_segmented_helmet,itm_flat_topped_helmet,itm_helmet_with_neckguard],
   #def_attrib|level(20),wp_one_handed(105)|wp_two_handed(120)|wp_polearm(105),knows_common|knows_riding_3|knows_ironflesh_3|knows_power_strike_3|knows_ironflesh_3|knows_athletics_3,swadian_face_middle_1, swadian_face_old_2],
  # ["swadian_double_hander","Swadian Double Hander","Swadian Double Handers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_1,
   # [itm_sword_two_handed_a,itm_sword_two_handed_b,
    # itm_coat_of_plates,itm_coat_of_plates,itm_mail_boots,itm_iron_greaves,itm_flat_topped_helmet,itm_guard_helmet,itm_mail_mittens,itm_gauntlets],
   # def_attrib|level(25),wp_one_handed(135)|wp_two_handed(150)|wp_polearm(135),knows_common|knows_ironflesh_5|knows_power_strike_5|knows_ironflesh_4|knows_athletics_4,swadian_face_middle_1, swadian_face_older_2],

  # ["swadian_light_cavalry","Swadian Light Cavalry","Swadian Light Cavalry",tf_mounted|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   # [itm_light_lance,itm_sword_medieval_a,itm_sword_medieval_b_small,itm_tab_shield_heater_c,
    # itm_mail_with_tunic_red,itm_mail_with_tunic_red,itm_mail_chausses,itm_leather_boots,itm_segmented_helmet,itm_flat_topped_helmet,itm_helmet_with_neckguard,itm_courser],
   # def_attrib|level(20),wp_melee(105),knows_common|knows_riding_2|knows_ironflesh_2|knows_power_strike_2|knows_shield_2|knows_weapon_master_2|knows_ironflesh_2|knows_athletics_2,swadian_face_middle_1, swadian_face_old_2],
  #["swadian_veteran_light_cavalry","Swadian Light Cavalry","Swadian Light Cavalry",tf_mounted|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   #[itm_lance,itm_sword_medieval_b,itm_sword_medieval_c,itm_tab_shield_heater_d,
    #itm_mail_with_surcoat,itm_haubergeon,itm_mail_boots,itm_iron_greaves,itm_flat_topped_helmet,itm_guard_helmet,itm_mail_mittens,itm_gauntlets,itm_courser],
   #def_attrib|level(25),wp_melee(135),knows_common|knows_riding_3|knows_ironflesh_4|knows_power_strike_4|knows_shield_3|knows_weapon_master_3|knows_ironflesh_3|knows_athletics_3,swadian_face_middle_1, swadian_face_older_2],

  # ["swadian_infantry_thrower","Swadian Infantry (Thrower)","Swadian Infantries (Thrower)",tf_guarantee_ranged|tf_guarantee_all_armors_and_shield|tf_guarantee_polearm,0,0,fac_kingdom_1,
   # [itm_darts,itm_pike,itm_fighting_pick,itm_bastard_sword_a,itm_sword_medieval_a,itm_sword_medieval_b_small,itm_tab_shield_heater_c,
    # itm_mail_with_surcoat,itm_haubergeon,itm_mail_chausses,itm_leather_boots,itm_segmented_helmet,itm_flat_topped_helmet,itm_helmet_with_neckguard],
   # attr(15,13,6,6)|level(20),wp_melee(131)|wp_throwing(145),knows_common|knows_riding_2|knows_power_strike_3|knows_power_throw_2|knows_shield_3|knows_weapon_master_3|knows_ironflesh_2|knows_athletics_3,swadian_face_middle_1, swadian_face_old_2],
  # ["swadian_sergeant_thrower","Swadian Sergeant (Thrower)","Swadian Sergeants (Thrower)",tf_guarantee_ranged|tf_mounted|tf_guarantee_all_armors_and_shield|tf_guarantee_polearm,0,0,fac_kingdom_1,
   # [itm_war_darts,itm_awlpike,(itm_bastard_sword_b,imod_tempered),itm_morningstar,itm_sword_medieval_c,itm_tab_shield_heater_d,
    # itm_coat_of_plates,itm_brigandine_red,itm_mail_boots,itm_iron_greaves,itm_flat_topped_helmet,itm_guard_helmet,itm_mail_mittens,itm_gauntlets],
   # attr(17,14,7,7)|level(25),wp_melee(170)|wp_throwing(185),knows_common|knows_riding_3|knows_shield_4|knows_weapon_master_4|knows_power_strike_4|knows_power_throw_3|knows_ironflesh_4|knows_athletics_4,swadian_face_middle_1, swadian_face_older_2],

  # ["swadian_guard_knight","Swadian Guard Knight","Swadian Guard Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_1,
   # [itm_heavy_lance,itm_sword_two_handed_a,itm_sword_medieval_d_long,itm_morningstar,itm_morningstar,itm_sword_medieval_d_long,itm_tab_shield_heater_cav_b,
    # itm_plate_armor,itm_plate_armor,itm_plate_boots,itm_plate_boots,itm_winged_great_helmet,itm_winged_great_helmet,itm_charger,itm_charger,itm_gauntlets,itm_gauntlets],
   # def_attrib|level(32),wp_one_handed (180) | wp_two_handed (160) | wp_polearm (160) | wp_archery (100) | wp_crossbow (100) | wp_throwing (100),knows_common|knows_riding_6|knows_shield_6|knows_weapon_master_6|knows_ironflesh_6|knows_power_strike_6,swadian_face_middle_1, swadian_face_older_2],
   
  ["swadian_skirmisher","Swadian Skirmisher","Swadian Skirmishers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_1,
   [itm_bolts_2,itm_light_crossbow,itm_hunting_crossbow,itm_club,itm_voulge,itm_tab_shield_heater_a,
    itm_red_gambeson,itm_padded_cloth,itm_ankle_boots,itm_arming_cap,itm_arming_cap],
   attr(12,12,5,5)|level(14),wp(100),knows_riding_2|knows_ironflesh_1,swadian_face_young_1, swadian_face_middle_2],
  ["swadian_crossbowman","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_ranged|tf_guarantee_all_armors_and_shield,0,0,fac_kingdom_1,
   [itm_bolts_2,itm_crossbow,itm_light_crossbow,itm_fighting_pick,itm_sword_medieval_a,itm_voulge,itm_tab_shield_heater_b,
    itm_leather_jerkin,itm_red_gambeson,itm_leather_boots,itm_ankle_boots,itm_norman_helmet,itm_segmented_helmet],
   attr(14,13,6,6)|level(19),wp_one_handed (112) | wp_two_handed (112) | wp_polearm (112) | wp_archery (112) | wp_crossbow (125) | wp_throwing (112),knows_riding_2|knows_ironflesh_1|knows_athletics_1,swadian_face_young_1, swadian_face_old_2],
  ["swadian_sharpshooter","Swadian Sharpshooter","Swadian Sharpshooters",tf_mounted|tf_guarantee_ranged|tf_guarantee_all_armors_and_shield,0,0,fac_kingdom_1,
   [itm_steel_bolts_2,itm_steel_bolts_2,itm_crossbow,itm_crossbow,itm_heavy_crossbow,itm_sword_medieval_b_small,itm_sword_medieval_a,itm_voulge,itm_tab_shield_heater_c,
    itm_haubergeon,itm_arena_armor_red,itm_leather_boots,itm_mail_chausses,itm_kettle_hat,itm_helmet_with_neckguard,itm_leather_gloves],
   attr(15,15,7,7)|level(24),wp_one_handed (125) | wp_two_handed (125) | wp_polearm (125) | wp_archery (125) | wp_crossbow (150) | wp_throwing (125),knows_power_draw_3|knows_riding_2|knows_power_strike_1|knows_ironflesh_1|knows_athletics_2,swadian_face_middle_1, swadian_face_older_2],

  ["swadian_noble_lad","Swadian Squire","Swadian Squires",tf_mounted|tf_guarantee_horse|tf_guarantee_all_armors_and_shield|tf_guarantee_polearm,0,0,fac_kingdom_1,
   [itm_light_lance,itm_fighting_pick,itm_bastard_sword_a,itm_sword_medieval_a,itm_tab_shield_heater_cav_a,
    itm_mail_with_tunic_red,itm_ankle_boots,itm_mail_coif,itm_norman_helmet,itm_courser,itm_courser],
   attr(12,11,5,5)|level(13),wp_melee(100),knows_ironflesh_2|knows_riding_3|knows_shield_2|knows_weapon_master_2|knows_power_strike_1,swadian_face_young_1, swadian_face_old_2],

  ["swadian_man_at_arms","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_horse|tf_guarantee_all_armors_and_shield|tf_guarantee_polearm,0,0,fac_kingdom_1,
   [itm_lance,itm_heavy_lance,itm_fighting_pick,itm_bastard_sword_b,itm_sword_medieval_b,itm_sword_medieval_c_small,itm_tab_shield_heater_cav_a,
    (itm_haubergeon,imod_thick),(itm_mail_with_surcoat,imod_thick),itm_mail_chausses,itm_norman_helmet,itm_mail_coif,itm_flat_topped_helmet,itm_helmet_with_neckguard,itm_warhorse_r,itm_warhorse_r,itm_hunter],
   attr(15,14,6,6)|level(21),wp_melee(125),knows_ironflesh_3|knows_athletics_1|knows_riding_4|knows_shield_3|knows_weapon_master_3|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
  ["swadian_knight","Swadian Knight","Swadian Knights",tf_mounted|tf_guarantee_horse|tf_guarantee_all_armors_and_shield|tf_guarantee_polearm,0,0,fac_kingdom_1,
   [(itm_long_lance,imod_balanced),itm_long_lance,itm_sword_two_handed_b,itm_sword_medieval_d_long,itm_morningstar,itm_morningstar,itm_sword_medieval_d_long,itm_tab_shield_heater_cav_b,
    (itm_coat_of_plates_red,imod_reinforced),(itm_cuir_bouilli,imod_reinforced),itm_plate_boots,itm_guard_helmet,itm_great_helmet,itm_bascinet,itm_heavy_charger,itm_heavy_charger,itm_gauntlets,itm_mail_mittens],
   attr(18,16,7,7)|level(28),wp_one_handed (187) | wp_two_handed (162) | wp_polearm (162) | wp_archery (94) | wp_crossbow (94) | wp_throwing (94),knows_ironflesh_5|knows_athletics_2|knows_riding_5|knows_shield_5|knows_weapon_master_5|knows_power_strike_5,swadian_face_middle_1, swadian_face_older_2],

  ["swadian_messenger","Swadian Messenger","Swadian Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_1,
   [itm_sword_medieval_a,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_light_crossbow,itm_bolts],
   attr(7,21,4,4)|level(25),wp(162),knows_common|knows_riding_7|knows_horse_archery_5,swadian_face_young_1, swadian_face_old_2],
  ["swadian_deserter","Swadian Deserter","Swadian Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_bolts,itm_light_crossbow,itm_hunting_crossbow,itm_dagger,itm_club,itm_voulge,itm_wooden_shield,itm_leather_jerkin,itm_padded_cloth,itm_hide_boots,itm_padded_coif,itm_nasal_helmet,itm_footman_helmet],
   def_attrib|level(14),wp(100),knows_common|knows_riding_2|knows_ironflesh_1|knows_athletics_1,swadian_face_young_1, swadian_face_old_2],
  ["swadian_prison_guard","Prison Guard","Prison Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_awlpike,itm_pike,itm_great_sword,itm_morningstar,itm_sword_medieval_b,itm_tab_shield_heater_c,itm_coat_of_plates,itm_plate_armor,itm_plate_boots,itm_guard_helmet,itm_helmet_with_neckguard,itm_bascinet,itm_guard_helmet,itm_leather_gloves],
   def_attrib|level(25),wp(162),knows_common|knows_shield_3|knows_weapon_master_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
  ["swadian_castle_guard","Castle Guard","Castle Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_awlpike,itm_pike,itm_great_sword,itm_morningstar,itm_sword_medieval_b,itm_tab_shield_heater_c,itm_tab_shield_heater_d,itm_coat_of_plates,itm_plate_armor,itm_plate_boots,itm_guard_helmet,itm_helmet_with_neckguard,itm_bascinet,itm_guard_helmet,itm_leather_gloves],
   def_attrib|level(25),wp(162),knows_common|knows_shield_3|knows_weapon_master_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],

# Vaegir watchman?
  ["vaegir_recruit","Vaegir Recruit","Vaegir Recruits",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,
   [itm_scythe,itm_hatchet,itm_cudgel,itm_axe,itm_stones,itm_tab_shield_kite_a, itm_tab_shield_kite_a,
    itm_linen_tunic, itm_rawhide_coat,itm_nomad_boots],
   attr(8,6,5,5)|level(4),wp(75),knows_common, vaegir_face_younger_1, vaegir_face_middle_2],
  ["vaegir_footman","Vaegir Footman","Vaegir Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_spiked_club,itm_hand_axe,itm_sword_viking_1,itm_two_handed_axe,itm_tab_shield_kite_a,itm_tab_shield_kite_b,itm_spear,itm_nomad_cap,itm_vaegir_fur_cap,itm_rawhide_coat,itm_nomad_armor,itm_nomad_boots],
   attr(11,8,5,5)|level(9),wp(81),knows_common, vaegir_face_young_1, vaegir_face_middle_2],
  ["vaegir_skirmisher","Vaegir Skirmisher","Vaegir Skirmishers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,
   [itm_arrows,itm_arrows_back,itm_spiked_mace,itm_axe,itm_sword_khergit_1,itm_short_bow,itm_nomad_bow,itm_nomad_bow,itm_javelin,itm_javelin,itm_steppe_cap,itm_nomad_cap,itm_leather_vest,itm_leather_vest,itm_nomad_armor,itm_nomad_boots],
   attr(13,11,5,5)|level(14),wp(87),knows_ironflesh_1|knows_power_draw_2|knows_power_throw_1,vaegir_face_young_1, vaegir_face_old_2],
  ["vaegir_archer","Vaegir Archer","Vaegir Archers",tf_guarantee_ranged|tf_guarantee_all_armors,0,0,fac_kingdom_2,
   [itm_barbed_arrows_back,itm_vaegir_arrows,itm_axe,itm_sword_khergit_1,itm_nomad_bow,itm_strong_bow,itm_strong_bow,
    itm_leather_jerkin,itm_leather_vest,itm_nomad_boots,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet,itm_vaegir_fur_cap,itm_nomad_cap],
   attr(15,12,6,6)|level(19),wp_one_handed (96) | wp_two_handed (96) | wp_polearm (96) | wp_archery (150) | wp_crossbow (96) | wp_throwing (96),knows_power_draw_4|knows_ironflesh_1|knows_athletics_2|knows_power_strike_1|knows_power_throw_1,vaegir_face_young_1, vaegir_face_older_2],

  ["vaegir_marksman","Vaegir Marksman","Vaegir Marksmen",tf_guarantee_ranged|tf_guarantee_all_armors,0,0,fac_kingdom_2,
   [itm_vaegir_arrows_back,itm_vaegir_arrows,itm_axe,itm_voulge,itm_sword_khergit_2,(itm_nomad_bow,imod_masterwork),(itm_nomad_bow,imod_masterwork),itm_war_bow,
    itm_studded_leather_coat,itm_studded_leather_coat,itm_leather_boots,itm_vaegir_lamellar_helmet,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet],
   attr(17,13,7,7)|level(24),wp_one_handed (110) | wp_two_handed (110) | wp_polearm (110) | wp_archery (192) | wp_crossbow (110) | wp_throwing (110),knows_power_draw_6|knows_ironflesh_2|knows_athletics_3|knows_power_strike_2|knows_power_throw_1,vaegir_face_young_1, vaegir_face_older_2],
  # ["vaegir_eagleeye_archer","Vaegir EagleEye Archer","Vaegir EagleEye Archer",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_2,
   # [itm_barbed_arrows,itm_barbed_arrows,itm_war_bow,itm_war_bow,itm_long_bardiche,itm_long_bardiche,itm_scimitar_b,itm_scimitar_b,
    # itm_lamellar_vest,itm_lamellar_vest,itm_leather_boots,itm_leather_boots,itm_vaegir_lamellar_helmet,itm_vaegir_lamellar_helmet,itm_leather_gloves,itm_leather_gloves],
   # str_18 | agi_5 | int_4 | cha_4|level(28),wp_one_handed (100) | wp_two_handed (110) | wp_polearm (100) | wp_archery (170) | wp_crossbow (100) | wp_throwing (100),knows_ironflesh_3|knows_power_draw_6|knows_ironflesh_4|knows_athletics_4|knows_power_strike_2,vaegir_face_young_1, vaegir_face_older_2],

  ["vaegir_veteran","Vaegir Veteran","Vaegir Veterans",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_kingdom_2,
   [itm_spiked_mace,itm_two_handed_axe,itm_sword_viking_1,itm_tab_shield_kite_b,itm_tab_shield_kite_c,itm_spear,
    itm_steppe_cap,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet,itm_vaegir_fur_cap,itm_leather_jerkin,itm_studded_leather_coat,itm_nomad_boots], ## CC
   attr(14,10,5,5)|level(14),wp_melee(106)|wp_throwing(120),knows_ironflesh_1|knows_athletics_2|knows_power_strike_2|knows_power_throw_2|knows_shield_2|knows_weapon_master_2,vaegir_face_young_1, vaegir_face_old_2],
  ## CC
  ["vaegir_veteran_rider","Vaegir Mounted Veteran","Vaegir Mounted Veterans",tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_kingdom_2,
   [itm_light_lance,itm_spiked_mace,itm_two_handed_axe,itm_sword_viking_1,itm_tab_shield_kite_b,itm_tab_shield_kite_c,itm_saddle_horse,
    itm_steppe_cap,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet,itm_vaegir_fur_cap,itm_leather_jerkin,itm_studded_leather_coat,itm_nomad_boots], ## CC
   attr(14,10,5,5)|level(14),wp_melee(106)|wp_throwing(120),knows_riding_1|knows_ironflesh_1|knows_athletics_2|knows_power_strike_2|knows_power_throw_2|knows_shield_2|knows_weapon_master_2,vaegir_face_young_1, vaegir_face_old_2],
  ["vaegir_infantry_rider","Vaegir Mounted Infantry","Vaegir Mounted Infantries",tf_mounted|tf_guarantee_all_armors_and_shield|tf_guarantee_polearm|tf_guarantee_horse,0,0,fac_kingdom_2,
   [itm_light_lance,itm_battle_axe,itm_sword_viking_2,itm_sword_khergit_2,itm_tab_shield_kite_c,itm_steppe_horse,
    itm_mail_hauberk,itm_lamellar_vest,itm_leather_boots,itm_vaegir_lamellar_helmet,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet],
   attr(16,11,6,6)|level(19),wp_melee(125)|wp_throwing(140),knows_riding_2|knows_ironflesh_2|knows_athletics_3|knows_power_strike_3|knows_power_throw_3|knows_shield_2|knows_weapon_master_2,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_guard_rider","Vaegir Mounted Guard","Vaegir Mounted Guards",tf_mounted|tf_guarantee_all_armors_and_shield|tf_guarantee_polearm|tf_guarantee_horse,0,0,fac_kingdom_2,
   [itm_lance,itm_fighting_axe,(itm_bardiche,imod_heavy),(itm_battle_axe,imod_heavy),itm_fighting_axe,itm_tab_shield_kite_d,itm_hunter,
    (itm_banded_armor,imod_reinforced),(itm_lamellar_armor,imod_reinforced),itm_mail_chausses,itm_iron_greaves,itm_vaegir_war_helmet,itm_vaegir_war_helmet,itm_vaegir_lamellar_helmet,itm_leather_gloves],
   attr(18,12,7,7)|level(24),wp_one_handed(156)|wp_two_handed(187)|wp_polearm(156)|wp_archery(125)|wp_throwing(170),knows_riding_3|knows_ironflesh_3|knows_athletics_4|knows_shield_2|knows_weapon_master_2|knows_power_strike_4|knows_power_throw_4,vaegir_face_middle_1, vaegir_face_older_2],
  ## CC
  ["vaegir_infantry","Vaegir Infantry","Vaegir Infantries",tf_guarantee_all_armors_and_shield|tf_guarantee_polearm,0,0,fac_kingdom_2,
   [itm_pike,itm_battle_axe,itm_sword_viking_2,itm_sword_khergit_2,itm_tab_shield_kite_c,itm_spear,
    itm_mail_hauberk,itm_lamellar_vest,itm_leather_boots,itm_vaegir_lamellar_helmet,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet],
   attr(16,11,6,6)|level(19),wp_melee(125)|wp_throwing(140),knows_riding_2|knows_ironflesh_2|knows_athletics_3|knows_power_strike_3|knows_power_throw_3|knows_shield_2|knows_weapon_master_2,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_guard","Vaegir Guard","Vaegir Guards",tf_mounted|tf_guarantee_all_armors_and_shield|tf_guarantee_polearm,0,0,fac_kingdom_2,
   [itm_ashwood_pike,itm_fighting_axe,(itm_bardiche,imod_heavy),(itm_battle_axe,imod_heavy),itm_fighting_axe,itm_tab_shield_kite_d,
    (itm_banded_armor,imod_reinforced),(itm_lamellar_armor,imod_reinforced),itm_mail_chausses,itm_iron_greaves,itm_vaegir_war_helmet,itm_vaegir_war_helmet,itm_vaegir_lamellar_helmet,itm_leather_gloves],
   attr(18,12,7,7)|level(24),wp_one_handed(156)|wp_two_handed(187)|wp_polearm(156)|wp_archery(125)|wp_throwing(170),knows_riding_3|knows_ironflesh_3|knows_athletics_4|knows_shield_2|knows_weapon_master_2|knows_power_strike_4|knows_power_throw_4,vaegir_face_middle_1, vaegir_face_older_2], ## CC

  # ["vaegir_warrior","Vaegir Warrior","Vaegir Warrior",tf_guarantee_ranged|tf_guarantee_all_armors_and_shield,0,0,fac_kingdom_2,
   # [itm_barbed_arrows,itm_strong_bow,itm_nomad_bow,itm_strong_bow,itm_battle_axe,itm_fighting_axe,itm_sword_khergit_2,
    # itm_lamellar_vest,itm_lamellar_vest,itm_leather_boots,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet],
   # attr(16,13,7,13)|level(24),wp_one_handed (130)|wp_two_handed (145)|wp_polearm (130)|wp_archery (172)|wp_crossbow (130)|wp_throwing (130),knows_ironflesh_2|knows_power_draw_4|knows_ironflesh_3|knows_athletics_3|knows_power_strike_3|knows_power_throw_2,vaegir_face_young_1, vaegir_face_older_2],

  #["vaegir_berserker","Vaegir Berserker","Vaegir Berserker",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   #[itm_arrows,itm_arrows,itm_short_bow,itm_bardiche,itm_bardiche,
    #itm_mail_hauberk,itm_lamellar_vest,itm_leather_boots,itm_vaegir_lamellar_helmet,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet],
   #def_attrib|level(19),wp_one_handed(100)|wp_two_handed(120)|wp_polearm(100)|wp_archery(70),knows_common|knows_ironflesh_3|knows_athletics_3|knows_ironflesh_3|knows_power_draw_2|knows_power_strike_3,vaegir_face_young_1, vaegir_face_older_2],
  # ["vaegir_berserker","Vaegir Berserker","Vaegir Berserker",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_2,
   # [itm_barbed_arrows,itm_arrows,itm_strong_bow,itm_great_bardiche,itm_bardiche,
    # itm_banded_armor,itm_lamellar_vest,itm_lamellar_armor,itm_mail_chausses,itm_iron_greaves,itm_vaegir_war_helmet,itm_vaegir_war_helmet,itm_vaegir_lamellar_helmet,itm_leather_gloves],
   # def_attrib|level(24),wp_one_handed(125)|wp_two_handed(150)|wp_polearm(125)|wp_archery(100),knows_common|knows_ironflesh_4|knows_athletics_4|knows_ironflesh_4|knows_power_draw_3|knows_power_strike_4,vaegir_face_middle_1, vaegir_face_older_2],
  
  # ["vaegir_light_cavalry","Vaegir Light Cavalry","Vaegir Light Cavalry",tf_mounted|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   # [itm_light_lance,itm_fighting_axe,itm_sword_viking_2,itm_tab_shield_kite_c,
    # itm_studded_leather_coat,itm_studded_leather_coat,itm_leather_boots,itm_vaegir_lamellar_helmet,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet,itm_courser],
   # def_attrib|level(19),wp_melee(100),knows_common|knows_riding_2|knows_ironflesh_2|knows_athletics_2|knows_ironflesh_2|knows_power_strike_3|knows_shield_2|knows_weapon_master_2,vaegir_face_young_1, vaegir_face_older_2],
  #["vaegir_veteran_light_cavalry","Vaegir Light Cavalry","Vaegir Light Cavalry",tf_mounted|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_2,
   #[itm_lance,itm_battle_axe,itm_sword_khergit_2,itm_tab_shield_kite_d,
    #itm_mail_hauberk,itm_lamellar_vest,itm_mail_chausses,itm_iron_greaves,itm_vaegir_war_helmet,itm_vaegir_war_helmet,itm_vaegir_lamellar_helmet,itm_leather_gloves,itm_courser],
   #def_attrib|level(24),wp_melee(130),knows_common|knows_riding_3|knows_ironflesh_3|knows_athletics_3|knows_ironflesh_3|knows_power_strike_4|knows_shield_2|knows_weapon_master_2,vaegir_face_middle_1, vaegir_face_older_2],
  
  # ["vaegir_infantry_thrower","Vaegir Infantry (Thrower)","Vaegir Infantries (Thrower)",tf_guarantee_ranged|tf_guarantee_all_armors_and_shield|tf_guarantee_polearm,0,0,fac_kingdom_2,
   # [itm_pike,itm_battle_axe,itm_sword_viking_2,itm_sword_khergit_2,itm_tab_shield_kite_c,itm_spear,itm_light_throwing_axes,
    # itm_mail_hauberk,itm_lamellar_vest,itm_leather_boots,itm_vaegir_lamellar_helmet,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet],
   # attr(16,11,6,6)|level(19),wp_melee(125)|wp_throwing(140),knows_riding_2|knows_ironflesh_2|knows_athletics_3|knows_power_strike_3|knows_power_throw_3|knows_shield_2|knows_weapon_master_2,vaegir_face_young_1, vaegir_face_older_2],
  # ["vaegir_guard_thrower","Vaegir Guard (Thrower)","Vaegir Guards (Thrower)",tf_mounted|tf_guarantee_ranged|tf_guarantee_all_armors_and_shield|tf_guarantee_polearm,0,0,fac_kingdom_2,
   # [itm_ashwood_pike,itm_fighting_axe,(itm_bardiche,imod_heavy),(itm_battle_axe,imod_heavy),itm_fighting_axe,itm_tab_shield_kite_d,itm_throwing_axes,
    # (itm_banded_armor,imod_reinforced),(itm_lamellar_armor,imod_reinforced),itm_mail_chausses,itm_iron_greaves,itm_vaegir_war_helmet,itm_vaegir_war_helmet,itm_vaegir_lamellar_helmet,itm_leather_gloves],
   # attr(18,12,7,7)|level(24),wp_one_handed(156)|wp_two_handed(187)|wp_polearm(156)|wp_archery(125)|wp_throwing(170),knows_riding_3|knows_ironflesh_3|knows_athletics_4|knows_shield_2|knows_weapon_master_2|knows_power_strike_4|knows_power_throw_4,vaegir_face_middle_1, vaegir_face_older_2],
  
  
  ## CC
  ["vaegir_noble_lad","Vaegir Squire","Vaegir Squires",tf_mounted|tf_guarantee_horse|tf_guarantee_all_armors_and_shield|tf_guarantee_polearm,0,0,fac_kingdom_2,
   [itm_two_handed_axe,itm_sword_khergit_1,itm_light_lance,itm_tab_shield_kite_cav_a,
    itm_studded_leather_coat,itm_leather_jerkin,itm_leather_boots,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet,itm_steppe_horse,itm_steppe_horse],
   attr(12,11,5,5)|level(13),wp(100),knows_ironflesh_2|knows_riding_2|knows_power_strike_1,vaegir_face_young_1, vaegir_face_older_2],
  ## CC
  ["vaegir_horseman","Vaegir Horseman","Vaegir Horsemen",tf_mounted|tf_guarantee_horse|tf_guarantee_all_armors_and_shield|tf_guarantee_polearm,0,0,fac_kingdom_2,
   [itm_battle_axe,itm_sword_khergit_2,itm_lance,itm_lance,itm_tab_shield_kite_cav_a,
    itm_studded_leather_coat,itm_lamellar_vest,itm_leather_boots,itm_vaegir_lamellar_helmet,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet,itm_steppe_horse,itm_hunter,itm_warhorse_w],
   attr(15,14,6,6)|level(21),wp(125),knows_ironflesh_3|knows_athletics_1|knows_riding_3|knows_power_strike_3,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_knight","Vaegir Knight","Vaegir Knights",tf_mounted|tf_guarantee_horse|tf_guarantee_all_armors_and_shield|tf_guarantee_polearm,0,0,fac_kingdom_2,
   [itm_bardiche,itm_great_bardiche,itm_war_axe,itm_fighting_axe,itm_heavy_lance,itm_heavy_lance,itm_tab_shield_kite_cav_b,
    (itm_banded_armor,imod_reinforced),(itm_lamellar_armor,imod_reinforced),itm_mail_boots,itm_plate_boots,itm_vaegir_war_helmet,itm_vaegir_war_helmet,itm_vaegir_lamellar_helmet,itm_warhorse_w,itm_warhorse_w,itm_warhorse_vaegir,itm_leather_gloves],
   attr(17,15,7,7)|level(26),wp_one_handed (150) | wp_two_handed (175) | wp_polearm (150) | wp_archery (150) | wp_crossbow (150) | wp_throwing (150),knows_ironflesh_4|knows_athletics_2|knows_riding_4|knows_shield_2|knows_weapon_master_2|knows_power_strike_4,vaegir_face_middle_1, vaegir_face_older_2], ## CC warhorse_vaegir
  ["vaegir_messenger","Vaegir Messenger","Vaegir Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_2,
   [itm_sword_medieval_b,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_short_bow,itm_arrows],
   attr(7,21,4,4)|level(25),wp(162),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_deserter","Vaegir Deserter","Vaegir Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_arrows,itm_spiked_mace,itm_axe,itm_falchion,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_javelin,itm_javelin,itm_steppe_cap,itm_nomad_cap,itm_leather_vest,itm_leather_vest,itm_nomad_armor,itm_nomad_boots],
   def_attrib|level(14),wp(100),knows_ironflesh_1|knows_athletics_1|knows_power_draw_1,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_ashwood_pike,itm_battle_fork,itm_bardiche,itm_battle_axe,itm_fighting_axe,itm_tab_shield_kite_b,itm_studded_leather_coat,itm_lamellar_armor,itm_mail_chausses,itm_iron_greaves,itm_nordic_helmet,itm_nordic_helmet,itm_nordic_helmet,itm_spiked_helmet,itm_leather_gloves],
   def_attrib|level(24),wp(162),knows_ironflesh_3|knows_athletics_3|knows_shield_2|knows_weapon_master_2|knows_power_strike_3,vaegir_face_middle_1, vaegir_face_older_2],
  ["vaegir_castle_guard","Castle Guard","Castle Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_ashwood_pike,itm_battle_fork,itm_bardiche,itm_battle_axe,itm_fighting_axe,itm_tab_shield_kite_d,itm_studded_leather_coat,itm_lamellar_armor,itm_mail_chausses,itm_iron_greaves,itm_nordic_helmet,itm_nordic_helmet,itm_nordic_helmet,itm_spiked_helmet,itm_leather_gloves],
   def_attrib|level(24),wp(162),knows_ironflesh_3|knows_athletics_3|knows_shield_2|knows_weapon_master_2|knows_power_strike_3,vaegir_face_middle_1, vaegir_face_older_2],


  ["khergit_tribesman","Khergit Tribesman","Khergit Tribesmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_3,
   [itm_arrows,itm_club,itm_spear,itm_hunting_bow,
    itm_steppe_cap,itm_nomad_cap_b,itm_leather_vest,itm_steppe_armor,itm_nomad_boots,itm_khergit_leather_boots],
   attr(8,7,5,5)|level(5),wp(62),knows_riding_2|knows_power_draw_2|knows_horse_archery_2,khergit_face_younger_1, khergit_face_old_2],
  ["khergit_skirmisher","Khergit Skirmisher","Khergit Skirmishers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_3,
   [itm_arrows,itm_sword_khergit_1,itm_winged_mace,itm_spear,itm_nomad_bow,itm_javelin,itm_tab_shield_small_round_a,
    itm_steppe_cap,itm_nomad_cap_b,itm_leather_steppe_cap_a,itm_khergit_armor,itm_steppe_armor,itm_leather_vest,itm_nomad_boots,itm_khergit_leather_boots,itm_steppe_horse,itm_saddle_horse],
   attr(10,10,5,5)|level(10),wp_one_handed (75) | wp_two_handed (75) | wp_polearm (75) | wp_archery (100) | wp_crossbow (75) | wp_throwing (100),knows_riding_3|knows_power_draw_3|knows_power_throw_1|knows_power_strike_1|knows_horse_archery_3,khergit_face_younger_1, khergit_face_old_2],
  ["khergit_horseman","Khergit Horseman","Khergit Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_polearm,0,0,fac_kingdom_3,
  [itm_arrows,itm_light_lance,itm_nomad_bow,itm_sword_khergit_2,itm_tab_shield_small_round_a,itm_tab_shield_small_round_b,itm_spear,
   itm_leather_steppe_cap_a, itm_leather_steppe_cap_b,itm_nomad_robe,itm_nomad_vest,itm_khergit_leather_boots,itm_hide_boots,itm_spiked_helmet,itm_nomad_cap,itm_steppe_horse,itm_hunter],
   attr(12,13,5,5)|level(15),wp(100),knows_ironflesh_2|knows_athletics_1|knows_riding_4|knows_power_draw_3|knows_power_strike_2|knows_power_throw_2|knows_horse_archery_3|knows_shield_1|knows_weapon_master_1,khergit_face_young_1, khergit_face_older_2],
  ["khergit_lancer","Khergit Lancer","Khergit Lancers",tf_mounted|tf_guarantee_all_wo_ranged|tf_guarantee_polearm,0,0,fac_kingdom_3,
   [itm_sword_khergit_4,itm_spiked_mace,itm_one_handed_war_axe_b,itm_heavy_lance,itm_lance,itm_khergit_sword_two_handed_a,
    itm_khergit_cavalry_helmet,itm_khergit_cavalry_helmet,itm_khergit_war_helmet,(itm_lamellar_vest_khergit,imod_hardened),(itm_lamellar_armor,imod_reinforced),itm_khergit_leather_boots,itm_splinted_leather_greaves,itm_leather_gloves,itm_scale_gauntlets,itm_tab_shield_small_round_b,itm_tab_shield_small_round_c,itm_courser,(itm_warhorse_steppe,imod_champion),itm_warhorse_steppe],
   attr(13,16,7,7)|level(23),wp_one_handed (137) | wp_two_handed (137) | wp_polearm (187) | wp_archery (137) | wp_crossbow (137) | wp_throwing (137),knows_ironflesh_3|knows_athletics_2|knows_riding_6|knows_power_strike_4|knows_power_draw_3|knows_power_throw_2|knows_horse_archery_1|knows_shield_2|knows_weapon_master_2,khergit_face_middle_1, khergit_face_older_2],
  ## CC
  ["khergit_khan_guard","Khergit Khan's Guard","Khergit Khan's Guards",tf_mounted|tf_guarantee_all_wo_ranged|tf_guarantee_polearm,0,0,fac_kingdom_3,
   [(itm_long_lance,imod_balanced),itm_long_lance,itm_sword_khergit_4,itm_spiked_mace,itm_one_handed_war_axe_b,itm_khergit_sword_two_handed_b,
    itm_khergit_guard_helmet,(itm_khergit_guard_armor,imod_reinforced),itm_khergit_guard_boots,itm_khergit_guard_helmet,(itm_khergit_guard_armor,imod_reinforced),itm_khergit_guard_boots,itm_scale_gauntlets,itm_scale_gauntlets,
    itm_tab_shield_small_round_c,itm_tab_shield_small_round_c,(itm_warhorse_steppe,imod_champion),(itm_warhorse_steppe,imod_champion),itm_warhorse_steppe],
   attr(14,20,8,8)|level(30),wp_one_handed (175) | wp_two_handed (175) | wp_polearm (225) | wp_archery (175) | wp_crossbow (175) | wp_throwing (175),knows_ironflesh_4|knows_athletics_3|knows_riding_7|knows_power_strike_5|knows_power_draw_3|knows_power_throw_3|knows_horse_archery_2|knows_shield_4|knows_weapon_master_4,khergit_face_middle_1, khergit_face_older_2],
  # remove itm_javelin
  ["khergit_horse_archer","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_all_armors|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_kingdom_3,
   [itm_khergit_arrows,itm_bodkin_arrows_back,itm_arrows,itm_sword_khergit_2,itm_winged_mace,itm_spear,itm_khergit_bow,itm_tab_shield_small_round_a,itm_tab_shield_small_round_a,itm_tab_shield_small_round_b,
    itm_leather_steppe_cap_b,itm_nomad_cap_b,itm_tribal_warrior_outfit,itm_nomad_robe,itm_khergit_leather_boots,itm_tab_shield_small_round_a,itm_tab_shield_small_round_b,itm_steppe_horse,itm_steppe_horse],
   attr(12,13,5,5)|level(15),wp_one_handed (100) | wp_two_handed (100) | wp_polearm (100) | wp_archery (137) | wp_crossbow (100) | wp_throwing (137),knows_ironflesh_1|knows_athletics_1|knows_riding_4|knows_power_draw_4|knows_horse_archery_4|knows_power_throw_3|knows_power_strike_2,khergit_face_young_1, khergit_face_older_2],
  ["khergit_veteran_horse_archer","Khergit Veteran Horse Archer","Khergit Veteran Horse Archers",tf_mounted|tf_guarantee_all_armors|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_kingdom_3,
   [itm_flat_headed_arrows,itm_flat_headed_arrows_back,itm_khergit_arrows_back,itm_arrows,itm_strong_khergit_bow,itm_strong_khergit_bow,itm_khergit_bow,itm_nomad_bow,
   itm_tab_shield_small_round_b,itm_tab_shield_small_round_c,itm_sword_khergit_3,itm_winged_mace,itm_spear,
    itm_khergit_cavalry_helmet,itm_khergit_cavalry_helmet,itm_leather_warrior_cap,itm_lamellar_vest_khergit,itm_tribal_warrior_outfit,itm_khergit_leather_boots,itm_leather_gloves,itm_steppe_horse,(itm_courser,imod_champion)],
   attr(14,15,7,7)|level(23),wp_one_handed (112) | wp_two_handed (112) | wp_polearm (112) | wp_archery (162) | wp_crossbow (112) | wp_throwing (162),knows_ironflesh_3|knows_athletics_2|knows_riding_6|knows_power_draw_5|knows_horse_archery_7|knows_power_throw_4|knows_power_strike_3|knows_shield_1|knows_weapon_master_1,khergit_face_middle_1, khergit_face_older_2],
  ## CC
   
  # ## CC
  # ["khergit_dismounted_lancer","Khergit Dismounted Lancer","Khergit Dismounted Lancers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,0,0,fac_kingdom_3,
   # [itm_sword_khergit_4,itm_khergit_sword_two_handed_a,
    # itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_khergit_war_helmet,itm_lamellar_vest_khergit,itm_khergit_elite_armor,itm_khergit_leather_boots,itm_splinted_leather_greaves,itm_leather_gloves,itm_scale_gauntlets,itm_tab_shield_small_round_b,itm_tab_shield_small_round_c],
   # def_attrib|level(23),wp(130),knows_riding_3|knows_power_strike_6|knows_power_draw_4|knows_ironflesh_6|knows_horse_archery_1|knows_shield_3|knows_weapon_master_3,khergit_face_middle_1, khergit_face_older_2],
  # ## CC

  ["khergit_messenger","Khergit Messenger","Khergit Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_3,
   [itm_sword_khergit_2,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_short_bow,itm_arrows],
   attr(7,21,4,4)|level(25),wp(156),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,khergit_face_young_1, khergit_face_older_2],
  ["khergit_deserter","Khergit Deserter","Khergit Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_arrows,itm_spiked_mace,itm_axe,itm_sword_khergit_1,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_javelin,itm_javelin,itm_steppe_cap,itm_nomad_cap_b,itm_khergit_armor,itm_steppe_armor,itm_tribal_warrior_outfit,itm_nomad_boots],
   def_attrib|level(14),wp(100),knows_ironflesh_1|knows_athletics_1|knows_power_draw_1,khergit_face_young_1, khergit_face_older_2],
  ["khergit_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_sword_khergit_3,itm_tab_shield_small_round_b,itm_tab_shield_small_round_a,itm_lamellar_vest_khergit,itm_lamellar_armor,itm_khergit_leather_boots,itm_iron_greaves,itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_leather_warrior_cap],
   def_attrib|level(24),wp(162),knows_ironflesh_5|knows_athletics_5|knows_shield_2|knows_weapon_master_2|knows_power_strike_3,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_castle_guard","Castle Guard","Castle Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_sword_khergit_4,itm_tab_shield_small_round_b,itm_tab_shield_small_round_a,itm_lamellar_vest_khergit,itm_lamellar_armor,itm_khergit_leather_boots,itm_iron_greaves,itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_leather_warrior_cap],
   def_attrib|level(24),wp(162),knows_ironflesh_5|knows_athletics_5|knows_shield_2|knows_weapon_master_2|knows_power_strike_3,khergit_face_middle_1, khergit_face_older_2],


  ["nord_recruit","Nord Recruit","Nord Recruits",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_4,
   [itm_axe,itm_hatchet,itm_spear,itm_tab_shield_round_a,itm_tab_shield_round_a,
    itm_blue_tunic,itm_coarse_tunic,itm_hide_boots,itm_nomad_boots],
   attr(9,7,5,5)|level(6),wp(62),knows_power_strike_1|knows_power_throw_1|knows_riding_1|knows_athletics_1,nord_face_younger_1, nord_face_old_2],
  ["nord_footman","Nord Footman","Nord Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_4,
   [itm_fighting_axe,itm_one_handed_war_axe_a,itm_spear,itm_tab_shield_round_a,itm_tab_shield_round_b,itm_javelin,itm_light_throwing_axes,
    itm_leather_cap,itm_skullcap,itm_nomad_vest,itm_leather_boots,itm_nomad_boots],
   attr(11,9,5,5)|level(10),wp(87),knows_power_strike_2|knows_power_throw_2|knows_riding_1|knows_ironflesh_2|knows_athletics_2|knows_shield_1|knows_weapon_master_1,nord_face_young_1, nord_face_old_2],
  ["nord_trained_footman","Nord Trained Footman","Nord Trained Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_one_handed_war_axe_a,itm_one_handed_war_axe_b,itm_one_handed_battle_axe_a,itm_tab_shield_round_b,
    itm_skullcap,itm_nasal_helmet,itm_nordic_footman_helmet,itm_byrnie,itm_studded_leather_coat,itm_leather_boots],
   attr(13,11,5,5)|level(14),wp(125),knows_power_strike_3|knows_power_throw_2|knows_riding_1|knows_ironflesh_3|knows_athletics_3|knows_shield_2|knows_weapon_master_2,nord_face_young_1, nord_face_old_2],
   
  ["nord_scout","Nord Scout","Nord Scouts",tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_polearm,0,0,fac_kingdom_4,
   [itm_light_lance,itm_sword_viking_1,itm_one_handed_war_axe_b,itm_one_handed_battle_axe_a,itm_tab_shield_round_b,itm_javelin,itm_saddle_horse,
    itm_skullcap,itm_nasal_helmet,itm_nordic_footman_helmet,itm_byrnie,itm_studded_leather_coat,itm_leather_boots],
   attr(13,11,5,5)|level(14),wp(125),knows_power_strike_3|knows_power_throw_2|knows_riding_1|knows_ironflesh_3|knows_athletics_3|knows_shield_2|knows_weapon_master_2,nord_face_young_1, nord_face_old_2],
  ["nord_veteran_scout","Nord Veteran Scout","Nord Veteran Scouts",tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_polearm,0,0,fac_kingdom_4,
   [itm_lance,itm_sword_viking_2,itm_one_handed_war_axe_b,itm_one_handed_battle_axe_a,itm_tab_shield_round_c,itm_javelin,itm_javelin,itm_courser_b,itm_courser_b,
    itm_nordic_footman_helmet,itm_nordic_fighter_helmet,itm_mail_shirt,itm_studded_leather_coat,itm_hunter_boots,itm_leather_boots],
   attr(15,12,6,6)|level(19),wp(144),knows_power_strike_4|knows_power_throw_3|knows_riding_2|knows_ironflesh_4|knows_athletics_4|knows_shield_3|knows_weapon_master_3,nord_face_young_1, nord_face_older_2],
   
  ["nord_warrior","Nord Warrior","Nord Warriors",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_sword_viking_1,itm_one_handed_war_axe_b,itm_one_handed_battle_axe_a,itm_tab_shield_round_c,itm_javelin,itm_javelin,
    itm_nordic_footman_helmet,itm_nordic_fighter_helmet,itm_mail_shirt,itm_studded_leather_coat,itm_hunter_boots,itm_leather_boots],
   attr(15,12,6,6)|level(19),wp(144),knows_power_strike_4|knows_power_throw_3|knows_riding_2|knows_ironflesh_4|knows_athletics_4|knows_shield_3|knows_weapon_master_3,nord_face_young_1, nord_face_older_2],
  ["nord_veteran","Nord Veteran","Nord Veterans",tf_guarantee_all_armors_and_shield,0,0,fac_kingdom_4,
   [itm_sword_viking_2,itm_sword_viking_2_small,itm_one_handed_battle_axe_b,itm_spiked_mace,itm_tab_shield_round_d,itm_javelin,itm_throwing_axes,
    itm_nordic_helmet,itm_nordic_fighter_helmet,itm_mail_hauberk,itm_mail_shirt,itm_splinted_leather_greaves,itm_leather_boots,itm_leather_gloves],
   attr(17,13,7,7)|level(24),wp(181),knows_power_strike_5|knows_power_throw_4|knows_riding_2|knows_ironflesh_5|knows_athletics_5|knows_shield_4|knows_weapon_master_4,nord_face_young_1, nord_face_older_2],
  ["nord_champion","Nord Huscarl","Nord Huscarls",tf_guarantee_all_armors_and_shield,0,0,fac_kingdom_4,
   [itm_great_axe,itm_one_handed_battle_axe_c,itm_one_handed_battle_axe_c,itm_tab_shield_round_e,itm_throwing_spears,(itm_heavy_throwing_axes,imod_balanced),itm_heavy_throwing_axes,
    itm_nordic_huscarl_helmet,itm_nordic_warlord_helmet,itm_banded_armor,itm_mail_boots,itm_mail_chausses,itm_mail_mittens],
   attr(19,15,8,8)|level(30),wp(212),knows_power_strike_7|knows_power_throw_5|knows_riding_2|knows_ironflesh_7|knows_athletics_7|knows_shield_6|knows_weapon_master_6,nord_face_middle_1, nord_face_older_2],

  ## CC
  #["nord_thrower","Nord Thrower","Nord Throwers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_4,
   #[itm_throwing_axes,itm_throwing_axes,itm_long_axe,itm_long_axe,itm_tab_shield_round_c,
    #itm_nordic_footman_helmet,itm_nordic_fighter_helmet,itm_mail_shirt,itm_studded_leather_coat,itm_hunter_boots,itm_leather_boots],
   #def_attrib|level(19),wp(110)|wp_two_handed(120)|wp_throwing(130),knows_ironflesh_4|knows_power_strike_4|knows_riding_2|knows_ironflesh_4|knows_athletics_4|knows_shield_2|knows_weapon_master_2,nord_face_young_1, nord_face_older_2],
  #["nord_thrower","Nord Thrower","Nord Throwers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_4,
   #[itm_heavy_throwing_axes,itm_heavy_throwing_axes,itm_long_axe_b,itm_long_axe_b,itm_tab_shield_round_d,
    #itm_nordic_helmet,itm_nordic_fighter_helmet,itm_mail_hauberk,itm_mail_shirt,itm_splinted_leather_greaves,itm_leather_boots,itm_leather_gloves],
   #def_attrib|level(24),wp(140)|wp_two_handed(150)|wp_throwing(160),knows_ironflesh_5|knows_power_strike_5|knows_riding_3|knows_ironflesh_5|knows_athletics_5|knows_shield_3|knows_weapon_master_3,nord_face_young_1, nord_face_older_2],

  # ["nord_scout","Nord Scout","Nord Scouts",tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_4,
   # [itm_light_lance,itm_sword_viking_1,itm_tab_shield_round_c,itm_one_handed_battle_axe_a,
    # itm_nordic_footman_helmet,itm_nordic_fighter_helmet,itm_mail_shirt,itm_studded_leather_coat,itm_hunter_boots,itm_leather_boots,itm_courser],
   # def_attrib|level(19),wp(115),knows_ironflesh_4|knows_power_strike_3|knows_riding_2|knows_ironflesh_4|knows_athletics_4|knows_shield_2|knows_weapon_master_2,nord_face_young_1, nord_face_older_2],
  #["nord_veteran_scout","Nord Scout","Nord Scouts",tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_kingdom_4,
   #[itm_lance,itm_sword_viking_2,itm_tab_shield_round_d,itm_one_handed_battle_axe_b,
    #itm_nordic_helmet,itm_nordic_fighter_helmet,itm_mail_hauberk,itm_mail_shirt,itm_splinted_leather_greaves,itm_leather_boots,itm_leather_gloves,itm_courser],
   #def_attrib|level(24),wp(145),knows_ironflesh_5|knows_power_strike_4|knows_riding_3|knows_ironflesh_5|knows_athletics_5|knows_shield_3|knows_weapon_master_3,nord_face_young_1, nord_face_older_2],
  ## CC

  ["nord_huntsman","Nord Huntsman","Nord Huntsmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_4,
   [itm_arrows,itm_rawhide_coat,itm_hatchet,itm_hunting_bow,itm_hide_boots],
   attr(11,10,5,5)|level(11),wp_one_handed (75) | wp_two_handed (75) | wp_polearm (75) | wp_archery (87) | wp_crossbow (75) | wp_throwing (75),knows_power_strike_1|knows_power_draw_1|knows_ironflesh_1|knows_athletics_2,nord_face_young_1, nord_face_old_2],
  ["nord_archer","Nord Archer","Nord Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_4,
   [itm_arrows,itm_axe,itm_short_bow,itm_padded_leather,itm_leather_jerkin,itm_padded_leather,itm_leather_boots,itm_nasal_helmet,itm_nordic_archer_helmet,itm_leather_cap],
   attr(13,12,5,5)|level(15),wp_one_handed (100) | wp_two_handed (100) | wp_polearm (100) | wp_archery (119) | wp_crossbow (100) | wp_throwing (100),knows_power_strike_2|knows_power_draw_2|knows_ironflesh_2|knows_athletics_3,nord_face_young_1, nord_face_old_2],
  ["nord_veteran_archer","Nord Veteran Archer","Nord Veteran Archers",tf_guarantee_ranged|tf_guarantee_all_armors,0,0,fac_kingdom_4,
   [itm_bodkin_arrows,itm_sword_viking_2,itm_long_bow,itm_fighting_axe,itm_two_handed_axe,itm_mail_shirt,itm_mail_shirt,itm_byrnie,itm_leather_boots,itm_nordic_archer_helmet,itm_nordic_veteran_archer_helmet],
   attr(14,13,6,6)|level(19),wp_one_handed (118) | wp_two_handed (118) | wp_polearm (118) | wp_archery (150) | wp_crossbow (118) | wp_throwing (118),knows_power_strike_3|knows_power_draw_3|knows_ironflesh_4|knows_athletics_4,nord_face_middle_1, nord_face_older_2],
  ## CC
  # ["nord_champion_archer","Nord Champion Archer","Nord Champion Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
   # [itm_bodkin_arrows,itm_bodkin_arrows,itm_strong_bow,itm_strong_bow,itm_two_handed_battle_axe_2,itm_two_handed_battle_axe_2,
   # itm_banded_armor,itm_banded_armor,itm_leather_boots,itm_leather_boots,itm_nordic_helmet,itm_nordic_helmet],
   # str_15 | agi_7 | int_4 | cha_4|level(24),wp_one_handed (110) | wp_two_handed (135) | wp_polearm (110) | wp_archery (150) | wp_crossbow (110) | wp_throwing (110),knows_power_strike_5|knows_ironflesh_6|knows_power_draw_6|knows_ironflesh_8|knows_athletics_8,nord_face_middle_1, nord_face_older_2],
  ## CC
  ["nord_messenger","Nord Messenger","Nord Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_4,
   [itm_sword_viking_2,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_short_bow,itm_arrows],
   attr(7,21,4,4)|level(25),wp(162),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,nord_face_young_1, nord_face_older_2],
  ["nord_deserter","Nord Deserter","Nord Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_arrows,itm_spiked_mace,itm_axe,itm_falchion,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_javelin,itm_javelin,itm_steppe_cap,itm_nomad_cap,itm_leather_vest,itm_leather_vest,itm_nomad_armor,itm_nomad_boots],
   def_attrib|level(14),wp(100),knows_ironflesh_1|knows_athletics_1|knows_power_draw_1,nord_face_young_1, nord_face_older_2],
  ["nord_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_ashwood_pike,itm_battle_fork,itm_battle_axe,itm_fighting_axe,itm_tab_shield_round_d,itm_mail_hauberk,itm_mail_chausses,itm_iron_greaves,itm_nordic_helmet,itm_nordic_helmet,itm_nordic_helmet,itm_spiked_helmet,itm_leather_gloves],
   def_attrib|level(24),wp(162),knows_ironflesh_3|knows_athletics_3|knows_shield_2|knows_weapon_master_2|knows_power_strike_3,nord_face_middle_1, nord_face_older_2],
  ["nord_castle_guard","Castle Guard","Castle Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_ashwood_pike,itm_battle_fork,itm_battle_axe,itm_fighting_axe,itm_tab_shield_round_d,itm_tab_shield_round_e,itm_mail_hauberk,itm_heraldic_mail_with_tabard,itm_mail_chausses,itm_iron_greaves,itm_nordic_helmet,itm_nordic_helmet,itm_nordic_helmet,itm_spiked_helmet,itm_leather_gloves],
   def_attrib|level(24),wp(162),knows_ironflesh_3|knows_athletics_3|knows_shield_2|knows_weapon_master_2|knows_power_strike_3,nord_face_middle_1, nord_face_older_2],


  ["rhodok_tribesman","Rhodok Tribesman","Rhodok Tribesmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_5,
   [itm_pitch_fork,itm_pitch_fork,itm_tab_shield_pavise_a,
    itm_shirt,itm_coarse_tunic,itm_wrapping_boots,itm_nomad_boots,itm_head_wrappings,itm_straw_hat],
   attr(8,6,5,5)|level(4),wp(70),knows_power_draw_2|knows_ironflesh_1,rhodok_face_younger_1, rhodok_face_old_2],
  ["rhodok_spearman","Rhodok Spearman","Rhodok Spearmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_polearm,0,0,fac_kingdom_5,
   [itm_spear,itm_pike,itm_spear,itm_tab_shield_pavise_a,itm_falchion,
    itm_felt_hat_b,itm_common_hood,itm_leather_armor,itm_arena_tunic_green,itm_wrapping_boots,itm_nomad_boots],
   attr(11,8,5,5)|level(9),wp(100),knows_shield_1|knows_weapon_master_1|knows_power_strike_2|knows_ironflesh_2|knows_athletics_1,rhodok_face_young_1, rhodok_face_old_2],
  ["rhodok_trained_spearman","Rhodok Trained Spearman","Rhodok Trained Spearmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_kingdom_5,
   [itm_pike,itm_war_spear,itm_pike,itm_war_spear,itm_tab_shield_pavise_b,
    itm_footman_helmet,itm_padded_coif,itm_aketon_green,itm_aketon_green,itm_ragged_outfit,itm_nomad_boots,itm_leather_boots],
   attr(13,11,5,5)|level(14),wp_one_handed (131) | wp_two_handed (131) | wp_polearm (143) | wp_archery (131) | wp_crossbow (131) | wp_throwing (131),knows_shield_2|knows_weapon_master_2|knows_power_strike_3|knows_ironflesh_3|knows_athletics_2,rhodok_face_young_1, rhodok_face_older_2],
   
  ["rhodok_scout","Rhodok Scout","Rhodok Scouts",tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_kingdom_5,
   [itm_light_lance,itm_military_cleaver_b,itm_sword_medieval_a,itm_tab_shield_heater_cav_a,itm_saddle_horse,
    itm_footman_helmet,itm_padded_coif,itm_aketon_green,itm_aketon_green,itm_ragged_outfit,itm_nomad_boots,itm_leather_boots],
   attr(13,11,5,5)|level(14),wp_one_handed (131) | wp_two_handed (131) | wp_polearm (143) | wp_archery (131) | wp_crossbow (131) | wp_throwing (131),knows_shield_2|knows_weapon_master_2|knows_power_strike_3|knows_ironflesh_3|knows_athletics_2|knows_riding_1,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_veteran_scout","Rhodok Veteran Scout","Rhodok Veteran Scouts",tf_mounted|tf_guarantee_horse|tf_guarantee_all_armors_and_shield|tf_guarantee_polearm,0,0,fac_kingdom_5,
   [itm_lance,itm_military_cleaver_c,itm_sword_medieval_b,itm_tab_shield_heater_cav_b,itm_courser_g,itm_courser_g,
    itm_kettle_hat,itm_mail_coif,itm_mail_with_tunic_green,itm_leather_boots,itm_splinted_leather_greaves,itm_leather_gloves],
   attr(15,12,6,6)|level(19),wp_one_handed (143) | wp_two_handed (143) | wp_polearm (162) | wp_archery (143) | wp_crossbow (143) | wp_throwing (153),knows_shield_3|knows_weapon_master_3|knows_power_strike_4|knows_power_throw_2|knows_ironflesh_5|knows_athletics_3|knows_riding_2,rhodok_face_young_1, rhodok_face_older_2],
   
  ["rhodok_veteran_spearman","Rhodok Veteran Spearman","Rhodok Veteran Spearmen",tf_guarantee_all_armors_and_shield|tf_guarantee_polearm,0,0,fac_kingdom_5,
   [itm_ashwood_pike,itm_glaive,itm_military_cleaver_b,itm_military_cleaver_b,itm_tab_shield_pavise_c,
    itm_kettle_hat,itm_mail_coif,itm_mail_with_tunic_green,itm_leather_boots,itm_splinted_leather_greaves,itm_leather_gloves],
   attr(15,12,6,6)|level(19),wp_one_handed (143) | wp_two_handed (143) | wp_polearm (162) | wp_archery (143) | wp_crossbow (143) | wp_throwing (153),knows_shield_3|knows_weapon_master_3|knows_power_strike_4|knows_power_throw_2|knows_ironflesh_5|knows_athletics_3,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_sergeant","Rhodok Sergeant","Rhodok Sergeants",tf_guarantee_all_armors_and_shield|tf_guarantee_polearm,0,0,fac_kingdom_5,
   [itm_glaive,itm_military_hammer,itm_military_cleaver_c,itm_military_cleaver_c,itm_tab_shield_pavise_d,
    itm_full_helm, itm_bascinet_3,itm_bascinet_2,itm_surcoat_over_mail,itm_surcoat_over_mail,itm_heraldic_mail_with_surcoat,itm_mail_chausses,itm_leather_gloves,itm_mail_mittens],
   attr(17,14,7,7)|level(25),wp_one_handed (162) | wp_two_handed (143) | wp_polearm (200) | wp_archery (143) | wp_crossbow (143) | wp_throwing (182),knows_shield_5|knows_weapon_master_5|knows_power_strike_5|knows_power_throw_3|knows_ironflesh_6|knows_athletics_5|knows_riding_2,rhodok_face_middle_1, rhodok_face_older_2],
   
   
  # ["rhodok_veteran_spearman_thrower","Rhodok Veteran Spearman (Thrower)","Rhodok Veteran Spearmen (Thrower)",tf_guarantee_ranged|tf_guarantee_all_armors_and_shield|tf_guarantee_polearm,0,0,fac_kingdom_5,
   # [itm_throwing_hammers,itm_ashwood_pike,itm_glaive,itm_military_cleaver_b,itm_military_cleaver_b,itm_tab_shield_pavise_c,
    # itm_kettle_hat,itm_mail_coif,itm_mail_with_tunic_green,itm_leather_boots,itm_splinted_leather_greaves,itm_leather_gloves],
   # attr(15,12,6,6)|level(19),wp_one_handed (143) | wp_two_handed (143) | wp_polearm (162) | wp_archery (143) | wp_crossbow (143) | wp_throwing (153),knows_shield_3|knows_weapon_master_3|knows_power_strike_4|knows_power_throw_2|knows_ironflesh_5|knows_athletics_3,rhodok_face_young_1, rhodok_face_older_2],
  # ["rhodok_sergeant_thrower","Rhodok Sergeant (Thrower)","Rhodok Sergeants (Thrower)",tf_guarantee_ranged|tf_guarantee_all_armors_and_shield|tf_guarantee_polearm,0,0,fac_kingdom_5,
   # [itm_throwing_hammers,itm_glaive,itm_military_hammer,itm_military_cleaver_c,itm_military_cleaver_c,itm_tab_shield_pavise_d,
    # itm_full_helm, itm_bascinet_3,itm_bascinet_2,itm_surcoat_over_mail,itm_surcoat_over_mail,itm_heraldic_mail_with_surcoat,itm_mail_chausses,itm_leather_gloves,itm_mail_mittens],
   # attr(17,14,7,7)|level(25),wp_one_handed (162) | wp_two_handed (143) | wp_polearm (200) | wp_archery (143) | wp_crossbow (143) | wp_throwing (182),knows_shield_5|knows_weapon_master_5|knows_power_strike_5|knows_power_throw_3|knows_ironflesh_6|knows_athletics_5|knows_riding_2,rhodok_face_middle_1, rhodok_face_older_2],
   
  ## CC
  # ["rhodok_master_sergeant","Rhodok Master Sergeant","Rhodok Master Sergeants",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_5,
   # [itm_glaive,itm_two_handed_cleaver,itm_military_cleaver_c,itm_military_cleaver_c,itm_tab_shield_pavise_d,itm_throwing_spears,
    # itm_full_helm, itm_full_helm,itm_heraldic_mail_with_tabard,itm_heraldic_mail_with_tabard,itm_mail_chausses,itm_mail_chausses,itm_gauntlets,itm_gauntlets],
   # def_attrib|level(28),wp_one_handed (150) | wp_two_handed (140) | wp_polearm (165) | wp_archery (125) | wp_crossbow (125) | wp_throwing (140),knows_common|knows_ironflesh_7|knows_shield_6|knows_weapon_master_6|knows_power_strike_6|knows_ironflesh_6|knows_athletics_6,rhodok_face_middle_1, rhodok_face_older_2],
  ## CC
  
  ## CC
  #["rhodok_thrower","Rhodok Thrower","Rhodok Throwers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_5,
   #[itm_glaive,itm_tab_shield_pavise_c,itm_javelin,
    #itm_kettle_hat,itm_mail_coif,itm_mail_with_tunic_green,itm_leather_boots,itm_splinted_leather_greaves,itm_leather_gloves],
   #def_attrib|level(19),wp_melee(110)|wp_throwing(130),knows_common|knows_ironflesh_4|knows_shield_3|knows_weapon_master_3|knows_power_strike_3|knows_ironflesh_3|knows_athletics_3,rhodok_face_young_1, rhodok_face_older_2],
  #["rhodok_thrower","Rhodok Thrower","Rhodok Throwers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_5,
   #[itm_military_hammer,itm_military_cleaver_c,itm_tab_shield_pavise_d,itm_throwing_spears,
    #itm_full_helm, itm_bascinet_3,itm_bascinet_2,itm_surcoat_over_mail,itm_surcoat_over_mail,itm_heraldic_mail_with_surcoat,itm_mail_chausses,itm_leather_gloves,itm_mail_mittens],
   #def_attrib|level(25),wp_melee(120)|wp_throwing(150),knows_common|knows_ironflesh_5|knows_shield_5|knows_weapon_master_5|knows_power_strike_4|knows_ironflesh_5|knows_athletics_5,rhodok_face_middle_1, rhodok_face_older_2],
  
  # ["rhodok_scout","Rhodok Scout","Rhodok Scouts",tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_5,
   # [itm_light_lance,itm_sword_medieval_a,itm_military_cleaver_b,itm_tab_shield_heater_cav_a,
    # itm_kettle_hat,itm_mail_coif,itm_mail_with_tunic_green,itm_leather_boots,itm_splinted_leather_greaves,itm_leather_gloves,itm_courser],
   # def_attrib|level(19),wp_melee(100)|wp_polearm (110),knows_common|knows_ironflesh_5|knows_shield_3|knows_weapon_master_3|knows_power_strike_3|knows_ironflesh_2|knows_athletics_2|knows_riding_2,rhodok_face_young_1, rhodok_face_older_2],
  #["rhodok_veteran_scout","Rhodok Scout","Rhodok Scouts",tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_kingdom_5,
   #[itm_lance,itm_sword_medieval_b,itm_military_cleaver_c,itm_tab_shield_heater_cav_b,
    #itm_full_helm, itm_bascinet_3,itm_bascinet_2,itm_surcoat_over_mail,itm_surcoat_over_mail,itm_heraldic_mail_with_surcoat,itm_mail_chausses,itm_leather_gloves,itm_mail_mittens,itm_courser],
   #def_attrib|level(25),wp_melee(115)|wp_polearm (130),knows_common|knows_ironflesh_6|knows_shield_5|knows_weapon_master_5|knows_power_strike_4|knows_ironflesh_4|knows_athletics_4|knows_riding_3,rhodok_face_middle_1, rhodok_face_older_2],
  ## CC
   
  ["rhodok_crossbowman","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_5,
   [itm_sword_medieval_a,itm_falchion,itm_club_with_spike_head,itm_tab_shield_pavise_a,itm_crossbow,itm_bolts,
    itm_arena_tunic_green,itm_felt_hat_b,itm_common_hood,itm_nomad_boots,itm_wrapping_boots],
   attr(10,10,5,5)|level(10),wp(96),knows_shield_1|knows_weapon_master_1|knows_power_strike_1|knows_ironflesh_1|knows_athletics_2,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_trained_crossbowman","Rhodok Trained Crossbowman","Rhodok Trained Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_5,
   [itm_sword_medieval_a,itm_sword_medieval_b_small,itm_club_with_spike_head,itm_tab_shield_pavise_a,itm_crossbow,itm_bolts,
    itm_common_hood,itm_leather_armor,itm_arena_tunic_green,itm_nomad_boots],
   attr(13,12,5,5)|level(15),wp_one_handed (112) | wp_two_handed (112) | wp_polearm (112) | wp_archery (112) | wp_crossbow (131) | wp_throwing (112),knows_shield_2|knows_weapon_master_2|knows_power_strike_2|knows_ironflesh_1|knows_athletics_3,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_veteran_crossbowman","Rhodok Veteran Crossbowman","Rhodok Veteran Crossbowmen",tf_guarantee_ranged|tf_guarantee_all_armors_and_shield,0,0,fac_kingdom_5,
   [itm_sword_medieval_a,itm_sword_medieval_b_small,itm_fighting_pick,itm_club_with_spike_head,itm_tab_shield_pavise_b,itm_tab_shield_pavise_c,itm_heavy_crossbow,itm_bolts,
    itm_leather_cap,itm_felt_hat_b,itm_aketon_green,itm_leather_boots],
   attr(15,13,6,6)|level(20),wp_one_handed (125) | wp_two_handed (125) | wp_polearm (125) | wp_archery (125) | wp_crossbow (150) | wp_throwing (125),knows_shield_3|knows_weapon_master_3|knows_power_strike_3|knows_ironflesh_2|knows_athletics_4,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_sharpshooter","Rhodok Sharpshooter","Rhodok Sharpshooters",tf_guarantee_ranged|tf_guarantee_all_armors_and_shield,0,0,fac_kingdom_5,
   [itm_sword_medieval_b,itm_military_pick,itm_military_hammer,itm_tab_shield_pavise_c,itm_sniper_crossbow,itm_steel_bolts,itm_steel_bolts,
    itm_kettle_hat,itm_mail_coif,itm_mail_with_tunic_green,itm_leather_boots,itm_splinted_leather_greaves],
   attr(17,14,7,7)|level(25),wp_one_handed (137) | wp_two_handed (137) | wp_polearm (137) | wp_archery (125) | wp_crossbow (175) | wp_throwing (125),knows_shield_4|knows_weapon_master_4|knows_power_strike_4|knows_ironflesh_3|knows_athletics_6|knows_riding_2,rhodok_face_middle_1, rhodok_face_older_2],
   
  ["rhodok_messenger","Rhodok Messenger","Rhodok Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_5,
   [itm_sword_medieval_b,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_short_bow,itm_arrows],
   attr(7,21,4,4)|level(25),wp(162),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_deserter","Rhodok Deserter","Rhodok Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_arrows,itm_spiked_mace,itm_axe,itm_falchion,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_javelin,itm_javelin,itm_steppe_cap,itm_nomad_cap,itm_leather_vest,itm_leather_vest,itm_nomad_armor,itm_nomad_boots],
   def_attrib|level(14),wp(100),knows_ironflesh_1|knows_athletics_1|knows_power_draw_1,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_ashwood_pike,itm_battle_fork,itm_battle_axe,itm_fighting_axe,itm_tab_shield_pavise_b,itm_bascinet_2,itm_surcoat_over_mail,itm_mail_chausses,itm_iron_greaves,itm_leather_gloves],
   def_attrib|level(24),wp(162),knows_ironflesh_3|knows_athletics_3|knows_shield_2|knows_weapon_master_2|knows_power_strike_3,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_castle_guard","Castle Guard","Castle Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_ashwood_pike,itm_battle_fork,itm_battle_axe,itm_fighting_axe,itm_tab_shield_pavise_c,itm_bascinet_2,itm_surcoat_over_mail,itm_mail_chausses,itm_iron_greaves,itm_leather_gloves],
   def_attrib|level(24),wp(162),knows_ironflesh_3|knows_athletics_3|knows_shield_2|knows_weapon_master_2|knows_power_strike_3,rhodok_face_middle_1, rhodok_face_older_2],
#peasant - retainer - footman - man-at-arms -  knight


 ["sarranid_recruit","Sarranid Recruit","Sarranid Recruits",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_scythe,itm_hatchet,itm_pickaxe,itm_club,itm_stones,itm_tab_shield_heater_a,itm_sarranid_felt_hat,itm_turban,itm_sarranid_boots_a,
    itm_sarranid_cloth_robe, itm_sarranid_cloth_robe_b],
   attr(8,6,5,5)|level(4),wp(75),knows_common|knows_athletics_1,swadian_face_younger_1, swadian_face_middle_2],
 ["sarranid_footman","Sarranid Footman","Sarranid Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_6,
   [itm_bamboo_spear,itm_arabian_sword_a,itm_tab_shield_kite_a,itm_desert_turban,
    itm_skirmisher_armor,itm_turban,itm_sarranid_boots_a,itm_sarranid_boots_b],
   attr(11,8,5,5)|level(9),wp(93),knows_common|knows_athletics_2,swadian_face_young_1, swadian_face_old_2],
 ["sarranid_veteran_footman","Sarranid Veteran Footman","Sarranid Veteran Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_polearm,0,0,fac_kingdom_6,
   [itm_bamboo_spear,itm_arabian_sword_a,itm_arabian_sword_b,itm_tab_shield_kite_b,
    itm_sarranid_boots_b,itm_sarranid_warrior_cap,itm_sarranid_leather_armor,itm_javelin,itm_arabian_sword_a,itm_mace_3],
   attr(13,11,5,5)|level(14),wp_one_handed (106) | wp_two_handed (106) | wp_polearm (106) | wp_archery (93) | wp_crossbow (93) | wp_throwing (125),knows_ironflesh_1|knows_athletics_2|knows_power_throw_2|knows_power_strike_1|knows_shield_2|knows_weapon_master_2,swadian_face_young_1, swadian_face_old_2],
## CC
 ["sarranid_veteran_footman_rider","Sarranid Mounted Veteran Footman","Sarranid Mounted Veteran Footmen",tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_polearm,0,0,fac_kingdom_6,
   [itm_light_lance,itm_arabian_sword_a,itm_arabian_sword_b,itm_javelin,itm_arabian_sword_a,itm_mace_3,itm_tab_shield_kite_b,
    itm_sarranid_boots_b,itm_sarranid_warrior_cap,itm_sarranid_leather_armor,itm_saddle_horse],
   attr(13,11,5,5)|level(14),wp_one_handed (106) | wp_two_handed (106) | wp_polearm (106) | wp_archery (93) | wp_crossbow (93) | wp_throwing (125),knows_ironflesh_1|knows_athletics_2|knows_power_throw_2|knows_power_strike_1|knows_shield_2|knows_weapon_master_2,swadian_face_young_1, swadian_face_old_2],
 ["sarranid_infantry_rider","Sarranid Mounted Infantry","Sarranid Mounted Infantries",tf_mounted|tf_guarantee_all_armors_and_shield|tf_guarantee_polearm|tf_guarantee_horse,0,0,fac_kingdom_6,
   [itm_light_lance,itm_sarranid_axe_a,itm_arabian_sword_b,itm_mace_3,itm_jarid,itm_tab_shield_kite_c,
    itm_sarranid_mail_shirt,itm_sarranid_mail_coif,itm_sarranid_boots_c,itm_sarranid_boots_b,itm_arabian_horse_a],
   attr(16,12,6,6)|level(20),wp_one_handed (131) | wp_two_handed (131) | wp_polearm (131) | wp_archery (93) | wp_crossbow (93) | wp_throwing (137),knows_power_strike_2|knows_shield_3|knows_weapon_master_3|knows_power_throw_3|knows_ironflesh_2|knows_athletics_3|knows_riding_2,swadian_face_middle_1, swadian_face_old_2],
 ["sarranid_guard_rider","Sarranid Mounted Guard","Sarranid Mounted Guards",tf_mounted|tf_guarantee_all_armors_and_shield|tf_guarantee_polearm|tf_guarantee_horse,0,0,fac_kingdom_6,
   [itm_lance,itm_military_pick,itm_sarranid_two_handed_axe_a,itm_jarid,itm_scimitar_b,itm_mace_4,itm_tab_shield_kite_d,itm_arabian_horse_b,
    itm_sarranid_boots_d, itm_sarranid_boots_c,(itm_arabian_armor_b,imod_lordly),itm_sarranid_mail_coif,itm_sarranid_veiled_helmet,(itm_mail_mittens,imod_reinforced),(itm_leather_gloves,imod_hardened)],
   attr(18,13,7,7)|level(25),wp_one_handed (168) | wp_two_handed (168) | wp_polearm (168) | wp_archery (93) | wp_crossbow (93) | wp_throwing (175),knows_shield_3|knows_weapon_master_3|knows_power_strike_3|knows_power_throw_4|knows_ironflesh_3|knows_athletics_5|knows_riding_3,swadian_face_middle_1, swadian_face_older_2],
## CC
 ["sarranid_infantry","Sarranid Infantry","Sarranid Infantries",tf_guarantee_all_armors_and_shield|tf_guarantee_polearm,0,0,fac_kingdom_6,
   [itm_sarranid_axe_a,itm_arabian_sword_b,itm_mace_3,itm_jarid,itm_spear,itm_tab_shield_kite_c,
    itm_sarranid_mail_shirt,itm_sarranid_mail_coif,itm_sarranid_boots_c,itm_sarranid_boots_b],
   attr(16,12,6,6)|level(20),wp_one_handed (131) | wp_two_handed (131) | wp_polearm (131) | wp_archery (93) | wp_crossbow (93) | wp_throwing (137),knows_power_strike_2|knows_shield_3|knows_weapon_master_3|knows_power_throw_3|knows_ironflesh_2|knows_athletics_3|knows_riding_2,swadian_face_middle_1, swadian_face_old_2],
 ["sarranid_guard","Sarranid Guard","Sarranid Guards",tf_guarantee_all_armors_and_shield|tf_guarantee_polearm,0,0,fac_kingdom_6,
   [itm_military_pick,itm_sarranid_two_handed_axe_a,itm_jarid,itm_scimitar_b,itm_war_spear,itm_mace_4,itm_tab_shield_kite_d,
    itm_sarranid_boots_d, itm_sarranid_boots_c,(itm_arabian_armor_b,imod_lordly),itm_sarranid_mail_coif,itm_sarranid_veiled_helmet,(itm_mail_mittens,imod_reinforced),(itm_leather_gloves,imod_hardened)],
   attr(18,13,7,7)|level(25),wp_one_handed (168) | wp_two_handed (168) | wp_polearm (168) | wp_archery (93) | wp_crossbow (93) | wp_throwing (175),knows_shield_3|knows_weapon_master_3|knows_power_strike_3|knows_power_throw_4|knows_ironflesh_3|knows_athletics_5|knows_riding_3,swadian_face_middle_1, swadian_face_older_2],
  ## CC
 # ["sarranid_palace_guard","Sarranid Palace Guard","Sarranid Palace Guards",tf_mounted|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_6,
   # [itm_sarranid_two_handed_axe_a,itm_sarranid_two_handed_mace_1,itm_jarid,itm_scimitar_b,itm_scimitar_b,itm_tab_shield_kite_d,
    # itm_sarranid_boots_d, itm_sarranid_boots_d,itm_mamluke_mail,itm_sarranid_veiled_helmet,itm_sarranid_veiled_helmet,itm_mail_mittens,itm_mail_mittens],
   # def_attrib|level(29),wp_one_handed (160) | wp_two_handed (160) | wp_polearm (160) | wp_archery (90) | wp_crossbow (90) | wp_throwing (165),knows_common|knows_shield_4|knows_weapon_master_4|knows_ironflesh_5|knows_power_strike_6|knows_ironflesh_6|knows_athletics_6,swadian_face_middle_1, swadian_face_older_2],
  ## CC
## CC
 #["sarranid_axeman","Sarranid Axeman","Sarranid Axemen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,
   #[itm_sarranid_two_handed_axe_b,itm_sarranid_two_handed_axe_b,
   #itm_sarranid_mail_shirt,itm_sarranid_mail_coif,itm_sarranid_boots_c,itm_sarranid_boots_b],
   #def_attrib|level(20),wp_one_handed (90) | wp_two_handed (110) | wp_polearm (75) | wp_archery (75) | wp_crossbow (75) | wp_throwing (75),knows_common|knows_riding_3|knows_ironflesh_3|knows_power_strike_2|knows_ironflesh_3|knows_athletics_3,swadian_face_middle_1, swadian_face_old_2],
 # ["sarranid_axeman","Sarranid Axeman","Sarranid Axemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,
   # [itm_sarranid_two_handed_axe_a,itm_sarranid_two_handed_axe_b,
   # itm_sarranid_boots_d, itm_sarranid_boots_c,itm_sarranid_elite_armor,itm_sarranid_mail_coif,itm_sarranid_veiled_helmet,itm_mail_mittens,itm_leather_gloves],
   # def_attrib|level(25),wp_one_handed (120) | wp_two_handed (140) | wp_polearm (75) | wp_archery (75) | wp_crossbow (75) | wp_throwing (75),knows_common|knows_shield_3|knows_weapon_master_3|knows_ironflesh_5|knows_power_strike_4|knows_ironflesh_5|knows_athletics_5,swadian_face_middle_1, swadian_face_older_2],
   
 # ["sarranid_light_cavalry","Sarranid Light Cavalry","Sarranid Light Cavalry",tf_mounted|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,
   # [itm_light_lance,itm_sarranid_axe_a,itm_arabian_sword_b,itm_tab_shield_small_round_a,
   # itm_sarranid_leather_armor,itm_sarranid_mail_coif,itm_sarranid_boots_c,itm_sarranid_boots_b,itm_courser],
   # def_attrib|level(20),wp_one_handed (105) | wp_two_handed (105) | wp_polearm (115) | wp_archery (75) | wp_crossbow (75) | wp_throwing (75),knows_common|knows_riding_2|knows_ironflesh_2|knows_power_strike_2|knows_shield_2|knows_weapon_master_2| knows_ironflesh_2|knows_athletics_2,swadian_face_middle_1, swadian_face_old_2],
 #["sarranid_veteran_light_cavalry","Sarranid Light Cavalry","Sarranid Light Cavalry",tf_mounted|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_6,
   #[itm_lance,itm_sarranid_two_handed_axe_a,itm_scimitar_b,itm_tab_shield_small_round_b,
   #itm_sarranid_boots_d, itm_sarranid_boots_c,itm_sarranid_cavalry_robe,itm_sarranid_mail_coif,itm_sarranid_veiled_helmet,itm_mail_mittens,itm_leather_gloves,itm_courser],
   #def_attrib|level(25),wp_one_handed (135) | wp_two_handed (135) | wp_polearm (145) | wp_archery (75) | wp_crossbow (75) | wp_throwing (75),knows_common|knows_riding_3|knows_ironflesh_3|knows_power_strike_3|knows_shield_3|knows_weapon_master_3|knows_ironflesh_4|knows_athletics_4,swadian_face_middle_1, swadian_face_older_2],
## CC

 ["sarranid_skirmisher","Sarranid Skirmisher","Sarranid Skirmishers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_turban,itm_desert_turban,itm_skirmisher_armor,itm_jarid,itm_jarid,itm_arabian_sword_a,itm_spiked_club,itm_tab_shield_small_round_a,itm_sarranid_warrior_cap,itm_sarranid_boots_a],
   attr(12,12,5,5)|level(14),wp(100),knows_riding_2|knows_power_throw_2|knows_power_strike_2|knows_ironflesh_1|knows_athletics_3,swadian_face_young_1, swadian_face_middle_2],
 ["sarranid_archer","Sarranid Archer","Sarranid Archers",tf_guarantee_ranged|tf_guarantee_all_armors,0,0,fac_kingdom_6,
   [itm_arrows,itm_arrows_back,itm_arabian_sword_a,itm_triangle_bow,itm_triangle_bow,itm_archers_vest,itm_sarranid_boots_b,itm_sarranid_helmet1,itm_sarranid_warrior_cap,itm_turban,itm_desert_turban],
   attr(14,13,6,6)|level(19),wp_one_handed (112) | wp_two_handed (112) | wp_polearm (112) | wp_archery (125) | wp_crossbow (112) | wp_throwing (125),knows_power_draw_3|knows_power_strike_2|knows_ironflesh_2|knows_athletics_4|knows_power_throw_3,swadian_face_young_1, swadian_face_old_2],
 ["sarranid_master_archer","Sarranid Master Archer","Sarranid Master Archers",tf_guarantee_ranged|tf_guarantee_all_armors,0,0,fac_kingdom_6,
   [itm_bamboo_arrows_back,itm_bamboo_arrows,itm_arabian_sword_b,itm_mace_3,itm_strong_triangle_bow,itm_sarranid_bow,
    itm_arabian_armor_b,itm_sarranid_boots_c,itm_sarranid_boots_b,itm_sarranid_mail_coif],
   attr(15,15,7,7)|level(24),wp_one_handed (125) | wp_two_handed (125) | wp_polearm (125) | wp_archery (162) | wp_crossbow (125) | wp_throwing (162),knows_power_draw_4|knows_power_throw_4|knows_power_strike_2|knows_ironflesh_3|knows_athletics_5|knows_riding_2,swadian_face_middle_1, swadian_face_older_2],
  ## CC
 ["sarranid_noble_lad","Sarranid Squire","Sarranid Squires",tf_mounted|tf_guarantee_horse|tf_guarantee_all_armors_and_shield|tf_guarantee_polearm,0,0,fac_kingdom_6,
   [itm_light_lance,itm_arabian_sword_a,itm_scimitar,itm_spiked_club,itm_tab_shield_small_round_a,
    itm_sarranid_leather_armor,itm_sarranid_boots_a,itm_sarranid_boots_b, itm_sarranid_warrior_cap,itm_leather_gloves,itm_arabian_horse_a,itm_arabian_horse_b],
   attr(11,12,5,5)|level(13),wp_melee(100),knows_ironflesh_2|knows_athletics_1|knows_riding_3|knows_shield_2|knows_weapon_master_2|knows_power_strike_1,swadian_face_young_1, swadian_face_old_2],
  ## CC
 ["sarranid_horseman","Sarranid Horseman","Sarranid Horsemen",tf_mounted|tf_guarantee_horse|tf_guarantee_all_armors_and_shield|tf_guarantee_polearm,0,0,fac_kingdom_6,
   [itm_lance,itm_lance,itm_arabian_sword_b,itm_scimitar_b,itm_mace_4,itm_tab_shield_small_round_b,
    itm_sarranid_mail_shirt,itm_sarranid_boots_c,itm_sarranid_boots_b, itm_sarranid_horseman_helmet,itm_leather_gloves,itm_arabian_horse_a,itm_hunter,itm_warhorse_y],
   attr(13,15,6,6)|level(20),wp_melee(125),knows_ironflesh_3|knows_athletics_2|knows_riding_4|knows_shield_2|knows_weapon_master_2|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
 ["sarranid_mamluke","Sarranid Mamluke","Sarranid Mamlukes",tf_mounted|tf_guarantee_horse|tf_guarantee_all_armors_and_shield|tf_guarantee_polearm,0,0,fac_kingdom_6,
   [itm_heavy_lance,itm_heavy_lance,(itm_scimitar_b,imod_tempered),itm_sarranid_two_handed_mace_1,(itm_sarranid_cavalry_sword,imod_tempered),itm_tab_shield_small_round_c,
    itm_mamluke_mail,itm_sarranid_boots_d,itm_sarranid_boots_c,itm_sarranid_veiled_helmet,itm_heavy_warhorse_sarranid,itm_warhorse_sarranid,itm_scale_gauntlets,itm_mail_mittens],
   attr(15,18,7,7)|level(27),wp_one_handed (187) | wp_two_handed (162) | wp_polearm (162) | wp_archery (93) | wp_crossbow (93) | wp_throwing (137),knows_ironflesh_5|knows_athletics_3|knows_riding_6|knows_shield_5|knows_weapon_master_5|knows_power_strike_5,swadian_face_middle_1, swadian_face_older_2],

   ["sarranid_messenger","Sarranid Messenger","Sarranid Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_1,
   [itm_lance,itm_arabian_sword_b,itm_scimitar_b,itm_mace_4,itm_tab_shield_small_round_b,
    itm_sarranid_mail_shirt,itm_mail_chausses,itm_sarranid_helmet1,itm_courser,itm_hunter],
   def_attrib|level(20),wp_melee(125),knows_common|knows_riding_4|knows_ironflesh_2|knows_athletics_2|knows_shield_2|knows_weapon_master_2|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
  ["sarranid_deserter","Sarranid Deserter","Sarranid Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_lance,itm_arabian_sword_b,itm_scimitar_b,itm_mace_4,itm_tab_shield_small_round_b,
    itm_sarranid_mail_shirt,itm_mail_chausses,itm_desert_turban,itm_arabian_horse_a],
   def_attrib|level(20),wp_melee(125),knows_common|knows_riding_4|knows_ironflesh_2|knows_athletics_2|knows_shield_2|knows_weapon_master_2|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
  ["sarranid_prison_guard","Prison Guard","Prison Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_arabian_sword_b,itm_scimitar_b,itm_war_spear,itm_mace_4,itm_sarranid_boots_c,itm_arabian_armor_b,itm_sarranid_mail_coif,itm_sarranid_helmet1,itm_sarranid_horseman_helmet,itm_mail_boots,itm_iron_greaves,itm_mail_mittens,itm_leather_gloves,itm_tab_shield_kite_d],
   def_attrib|level(25),wp_melee(168)|wp_throwing(125),knows_common|knows_shield_3|knows_weapon_master_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_middle_1, swadian_face_older_2],
  ["sarranid_castle_guard","Castle Guard","Castle Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_arabian_sword_b,itm_scimitar_b,itm_war_spear,itm_mace_4,itm_sarranid_boots_c, itm_sarranid_boots_d,itm_arabian_armor_b,itm_sarranid_mail_coif,itm_sarranid_helmet1,itm_sarranid_horseman_helmet,itm_mail_boots,itm_iron_greaves,itm_mail_mittens,itm_leather_gloves,itm_tab_shield_kite_d],
   def_attrib|level(25),wp_melee(168)|wp_throwing(125),knows_common|knows_shield_3|knows_weapon_master_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_middle_1, swadian_face_older_2],


  ["looter","Looter","Looters",0,0,0,fac_outlaws,
   [itm_hatchet,itm_club,itm_butchering_knife,itm_falchion,itm_rawhide_coat,itm_stones,itm_nomad_armor,itm_nomad_armor,itm_woolen_cap,itm_woolen_cap,itm_nomad_boots,itm_wrapping_boots],
   attr(8,6,5,5)|level(4),wp(25),knows_common,bandit_face1, bandit_face2],
  ["bandit","Bandit","Bandits",tf_guarantee_armor,0,0,fac_outlaws,
   [itm_arrows,itm_spiked_mace,itm_sword_viking_1,itm_short_bow,itm_falchion,itm_nordic_shield,itm_rawhide_coat,itm_leather_cap,itm_leather_jerkin,itm_nomad_armor,itm_nomad_boots,itm_wrapping_boots,itm_saddle_horse],
   attr(11,9,5,5)|level(10),wp(75),knows_common|knows_power_draw_1|knows_ironflesh_1,bandit_face1, bandit_face2],
  ["brigand","Brigand","Brigands",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_outlaws,
   [itm_arrows_back,itm_spiked_mace,itm_sword_viking_1,itm_falchion,itm_wooden_shield,itm_hide_covered_round_shield,itm_long_bow,itm_leather_cap,itm_leather_jerkin,itm_nomad_boots,itm_saddle_horse],
   attr(14,12,5,5)|level(16),wp(112),knows_riding_2|knows_horse_archery_2|knows_power_draw_3|knows_ironflesh_2,bandit_face1, bandit_face2],
## CC
  ["forest_bandit","Forest Bandit","Forest Bandits", tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_boots,0,0,fac_outlaws,
   [itm_arrows,itm_axe,itm_hatchet,itm_quarter_staff,itm_short_bow,itm_strong_hunting_bow,
    itm_common_hood,itm_black_hood,itm_shirt,itm_green_tunic,itm_leather_jerkin,itm_ragged_outfit,itm_hide_boots,itm_nomad_boots],
   attr(12,9,5,5)|level(11),wp(87),knows_common|knows_power_draw_2,swadian_face_young_1, swadian_face_old_2],
  ["trained_forest_bandit","Trained Forest Bandit","Trained Forest Bandits",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,0,0,fac_outlaws,
   [itm_bodkin_arrows_back,itm_arrows,itm_battle_axe,itm_hand_axe,itm_iron_staff,itm_strong_short_bow,itm_long_bow,
    itm_leather_warrior_cap,itm_black_hood,itm_leather_jerkin,itm_aketon_green,itm_nomad_boots,itm_leather_boots],
   attr(13,11,5,5)|level(14),wp(112),knows_common|knows_ironflesh_2|knows_athletics_2|knows_power_draw_3|knows_power_throw_2,swadian_face_young_1, swadian_face_old_2],
  ["veteran_forest_bandit","Veteran Forest Bandit","Veteran Forest Bandits",tf_mounted|tf_guarantee_ranged|tf_guarantee_all_armors|tf_guarantee_horse,0,0,fac_outlaws,
   [itm_bodkin_arrows_back,itm_bodkin_arrows,itm_war_axe,itm_strong_bow,itm_strong_bow,itm_strong_nomad_bow,itm_voulge,itm_throwing_arrows,itm_war_darts,itm_darts,
    itm_leather_warrior_cap,itm_leather_warrior_cap,itm_tribal_warrior_outfit,itm_padded_leather,itm_leather_boots,itm_leather_boots,itm_saddle_horse],
   attr(14,12,6,6)|level(18),wp(137),knows_common|knows_riding_2|knows_horse_archery_2|knows_ironflesh_3|knows_athletics_3|knows_power_draw_4|knows_power_throw_3,swadian_face_young_1, swadian_face_old_2],
   
  
  ["taiga_bandit","Taiga Bandit","Taiga Bandits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_outlaws,
   [itm_arrows,itm_sword_khergit_1,itm_winged_mace,itm_spear, itm_light_lance,itm_nomad_bow,itm_nomad_bow,itm_short_bow,itm_vaegir_fur_cap,itm_leather_steppe_cap_c,itm_nomad_armor,itm_leather_jerkin,itm_hide_boots,itm_nomad_boots,itm_leather_covered_round_shield,itm_leather_covered_round_shield],
   attr(14,11,5,5)|level(15),wp(112),knows_common|knows_power_draw_3|knows_power_strike_2|knows_power_throw_2|knows_ironflesh_1|knows_athletics_2,vaegir_face_young_1, vaegir_face_old_2],
  ["trained_taiga_bandit","Trained Taiga Bandit","Trained Taiga Bandits",tf_guarantee_ranged|tf_guarantee_all_armors,0,0,fac_outlaws,
   [itm_barbed_arrows,itm_arrows_back,itm_sword_khergit_2,itm_spiked_mace,itm_boar_spear, itm_lance,itm_nomad_bow,itm_strong_short_bow,itm_strong_short_bow,itm_light_throwing_axes,
   itm_vaegir_fur_helmet,itm_vaegir_spiked_helmet,itm_tribal_warrior_outfit,itm_studded_leather_coat,itm_leather_boots,itm_nomad_boots,itm_tab_shield_kite_b,itm_tab_shield_round_b],
   attr(15,12,6,6)|level(19),wp(143),knows_common|knows_ironflesh_2|knows_athletics_3|knows_power_draw_4|knows_power_strike_3|knows_power_throw_3,vaegir_face_young_1, vaegir_face_old_2],
  ["veteran_taiga_bandit","Veteran Taiga Bandit","Veteran Taiga Bandits",tf_mounted|tf_guarantee_ranged|tf_guarantee_all_armors|tf_guarantee_horse,0,0,fac_outlaws,
   [itm_vaegir_arrows_back,itm_vaegir_arrows,itm_sword_khergit_3,itm_strong_bow,itm_strong_nomad_bow,itm_light_throwing_axes,itm_throwing_axes,itm_spiked_mace,itm_long_hafted_knobbed_mace,
   itm_vaegir_spiked_helmet,itm_vaegir_spiked_helmet,itm_studded_leather_coat,itm_studded_leather_coat,itm_leather_boots,itm_leather_boots,itm_tab_shield_kite_b,itm_tab_shield_round_b,itm_courser],
   attr(16,13,7,7)|level(23),wp(175),knows_common|knows_riding_3|knows_horse_archery_3|knows_ironflesh_3|knows_athletics_4|knows_power_draw_5|knows_power_strike_4|knows_power_throw_4,vaegir_face_young_1, vaegir_face_old_2],
   
  ["steppe_bandit","Steppe Bandit","Steppe Bandits",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_outlaws,
   [itm_arrows,itm_sword_khergit_1,itm_winged_mace,itm_spear, itm_light_lance,itm_nomad_bow,itm_nomad_bow,itm_short_bow,itm_leather_steppe_cap_a,itm_leather_steppe_cap_b,itm_nomad_cap,itm_nomad_cap_b,itm_khergit_armor,itm_steppe_armor,itm_leather_vest,itm_hide_boots,itm_nomad_boots,itm_leather_covered_round_shield,itm_leather_covered_round_shield,itm_saddle_horse,itm_steppe_horse,itm_steppe_horse],
   attr(10,12,5,5)|level(12),wp(100),knows_riding_3|knows_horse_archery_3|knows_power_draw_2|knows_power_strike_1|knows_power_throw_1,khergit_face_young_1, khergit_face_old_2],
  ["trained_steppe_bandit","Trained Steppe Bandit","Trained Steppe Bandits",tf_mounted|tf_guarantee_all,0,0,fac_outlaws,
   [itm_khergit_arrows,itm_arrows_back,itm_sword_khergit_2,itm_long_spiked_club,itm_boar_spear, itm_lance,itm_khergit_bow,itm_strong_short_bow,itm_nomad_bow,itm_leather_steppe_cap_b,itm_leather_steppe_cap_c,itm_leather_warrior_cap,itm_nomad_cap_b,itm_leather_jerkin,itm_nomad_robe,itm_tribal_warrior_outfit,itm_leather_boots,itm_khergit_leather_boots,itm_leather_covered_round_shield,itm_tab_shield_round_c,itm_courser,itm_steppe_horse,itm_steppe_horse],
   attr(11,14,5,5)|level(15),wp(131),knows_ironflesh_2|knows_athletics_1|knows_riding_3|knows_horse_archery_4|knows_power_draw_3|knows_power_strike_2|knows_power_throw_2,khergit_face_young_1, khergit_face_old_2],
  ["veteran_steppe_bandit","Veteran Steppe Bandit","Veteran Steppe Bandits",tf_mounted|tf_guarantee_all,0,0,fac_outlaws,
   [itm_khergit_arrows_back,itm_khergit_arrows,itm_sword_khergit_3,itm_khergit_bow,itm_strong_nomad_bow,itm_light_throwing_lances,itm_throwing_lances,itm_long_hafted_spiked_mace, itm_lance,itm_leather_steppe_cap_c,itm_leather_warrior_cap,itm_nomad_robe,itm_nomad_robe,itm_khergit_leather_boots,itm_khergit_leather_boots,itm_plate_covered_round_shield,itm_tab_shield_round_d, itm_courser, itm_courser],
   attr(12,15,6,6)|level(19),wp(162),knows_ironflesh_3|knows_athletics_2|knows_riding_5|knows_horse_archery_5|knows_power_draw_4|knows_power_strike_3|knows_power_throw_3,khergit_face_young_1, khergit_face_old_2],
   
   
  ["sea_raider","Sea Raider","Sea Raiders",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_outlaws,
   [itm_arrows,itm_sword_viking_1,itm_long_bow,itm_sword_viking_2,itm_fighting_axe,itm_battle_axe,itm_spear,itm_nordic_shield,itm_wooden_shield,itm_shield_heater_c,
    itm_nasal_helmet,itm_nordic_footman_helmet,itm_nomad_vest,itm_mail_shirt,itm_leather_boots, itm_nomad_boots],
   attr(14,12,5,5)|level(16),wp(112),knows_power_draw_3|knows_power_strike_2|knows_power_throw_2|knows_riding_1|knows_ironflesh_2|knows_athletics_2,nord_face_young_1, nord_face_old_2],
  ["trained_sea_raider","Trained Sea Raider","Trained Sea Raiders",tf_guarantee_all_armors_and_shield,0,0,fac_outlaws,
   [itm_bodkin_arrows,itm_sword_viking_2,itm_long_bow,itm_throwing_axes,itm_javelin,itm_one_handed_war_axe_a,itm_battle_axe,itm_boar_spear,itm_nordic_shield,itm_tab_shield_round_b,itm_tab_shield_heater_b,
    itm_nordic_footman_helmet,itm_nordic_fighter_helmet,itm_byrnie,itm_haubergeon,itm_splinted_leather_greaves, itm_leather_boots],
   attr(15,13,6,6)|level(20),wp(143),knows_power_draw_4|knows_power_strike_3|knows_power_throw_3|knows_riding_2|knows_ironflesh_3|knows_athletics_3,nord_face_young_1, nord_face_old_2],
  ["veteran_sea_raider","Veteran Sea Raider","Veteran Sea Raiders",tf_guarantee_all_armors_and_shield,0,0,fac_outlaws,
   [itm_bodkin_arrows_back,itm_sword_viking_3,itm_long_bow,itm_throwing_axes,itm_jarid,itm_one_handed_war_axe_b,itm_war_axe,itm_boar_spear,itm_nordic_shield,itm_nordic_shield,itm_tab_shield_round_c,itm_tab_shield_heater_c,
    itm_nordic_helmet,itm_nordic_helmet,itm_mail_hauberk,itm_mail_hauberk,itm_mail_chausses, itm_splinted_leather_greaves],
   attr(16,14,7,7)|level(24),wp(175),knows_power_draw_4|knows_power_strike_4|knows_power_throw_4|knows_riding_2|knows_ironflesh_4|knows_athletics_4,nord_face_young_1, nord_face_old_2],
   
   
  ["mountain_bandit","Mountain Bandit","Mountain Bandits",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_outlaws,
   [itm_arrows,itm_sword_viking_1,itm_spear,itm_winged_mace,itm_long_maul,itm_falchion,itm_short_bow,itm_fur_covered_shield,itm_hide_covered_round_shield,
    itm_felt_hat,itm_head_wrappings,itm_skullcap,itm_rawhide_coat,itm_leather_armor,itm_hide_boots,itm_nomad_boots,itm_wooden_shield,itm_nordic_shield],
   attr(11,10,5,5)|level(11),wp(87),knows_common|knows_power_draw_2|knows_power_strike_1|knows_power_throw_1,rhodok_face_young_1, rhodok_face_old_2],
  ["trained_mountain_bandit","Trained Mountain Bandit","Trained Mountain Bandits",tf_guarantee_all_armors,0,0,fac_outlaws,
   [itm_arrows_back,itm_sword_viking_2,itm_boar_spear,itm_spiked_mace,itm_long_sledgehammer,itm_throwing_hammers,itm_hand_axe,itm_strong_short_bow,itm_nomad_bow,itm_fur_covered_shield,itm_leather_covered_round_shield,
    itm_padded_coif,itm_leather_cap,itm_padded_cloth,itm_leather_jerkin,itm_nomad_boots,itm_leather_boots],
   attr(13,11,5,5)|level(14),wp(112),knows_common|knows_ironflesh_2|knows_athletics_2|knows_power_draw_3|knows_power_strike_2|knows_power_throw_2,rhodok_face_young_1, rhodok_face_old_2],
  ["veteran_mountain_bandit","Veteran Mountain Bandit","Veteran Mountain Bandits",tf_guarantee_all_armors,0,0,fac_outlaws,
   [itm_barbed_arrows_back,itm_sword_viking_3,itm_strong_bow,itm_strong_nomad_bow,itm_throwing_hammers,itm_throwing_hammers,itm_ashwood_pike,itm_spiked_mace,itm_long_warhammer,itm_plate_covered_round_shield,itm_leather_covered_round_shield,
    itm_leather_cap,itm_nasal_helmet,itm_ragged_outfit,itm_ragged_outfit,itm_leather_boots,itm_leather_boots],
   attr(14,12,6,6)|level(18),wp(137),knows_common|knows_ironflesh_3|knows_athletics_3|knows_power_draw_4|knows_power_strike_3|knows_power_throw_3,rhodok_face_young_1, rhodok_face_old_2],
   
   
  ["desert_bandit","Desert Bandit","Desert Bandits",tf_mounted|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_outlaws,
   [itm_arrows,itm_arabian_sword_a,itm_winged_mace,itm_spear, itm_light_lance,itm_triangle_bow,itm_nomad_bow,itm_sarranid_cloth_robe, itm_sarranid_cloth_robe, itm_skirmisher_armor, itm_desert_turban, itm_turban,itm_leather_steppe_cap_b,itm_sarranid_boots_a,itm_leather_covered_round_shield,itm_leather_covered_round_shield,itm_saddle_horse,itm_arabian_horse_a],
   attr(10,12,5,5)|level(12),wp(100),knows_ironflesh_1|knows_riding_3|knows_horse_archery_3|knows_power_draw_2|knows_power_strike_1|knows_power_throw_1,khergit_face_young_1, khergit_face_old_2],
  ["trained_desert_bandit","Trained Desert Bandit","Trained Desert Bandits",tf_mounted|tf_guarantee_all,0,0,fac_outlaws,
   [itm_bamboo_arrows,itm_arrows_back,itm_arabian_sword_b,itm_sarranid_mace_1,itm_war_spear, itm_lance,itm_triangle_bow,itm_triangle_bow, itm_archers_vest, itm_archers_vest, itm_desert_turban, itm_desert_turban,itm_sarranid_boots_a,itm_sarranid_boots_b,itm_leather_covered_round_shield,itm_tab_shield_small_round_a,itm_arabian_horse_a,itm_arabian_horse_b],
   attr(11,14,5,5)|level(15),wp(131),knows_ironflesh_2|knows_athletics_1|knows_riding_4|knows_horse_archery_3|knows_power_draw_3|knows_power_strike_2|knows_power_throw_2,swadian_face_young_1, swadian_face_old_2],
  ["veteran_desert_bandit","Veteran Desert Bandit","Veteran Desert Bandits",tf_mounted|tf_guarantee_all,0,0,fac_outlaws,
   [itm_bamboo_arrows_back,itm_bamboo_arrows,itm_arabian_sword_d,itm_strong_triangle_bow,itm_strong_triangle_bow,itm_sarranid_bow,itm_light_throwing_lances,itm_throwing_lances,itm_sarranid_mace_1, itm_lance, itm_sarranid_leather_armor, itm_sarranid_leather_armor, itm_sarranid_warrior_cap, itm_sarranid_warrior_cap,itm_sarranid_boots_b,itm_sarranid_boots_b,itm_tab_shield_small_round_b,itm_tab_shield_small_round_c,itm_arabian_horse_b,itm_arabian_horse_b],
   attr(12,15,6,6)|level(19),wp(162),knows_ironflesh_3|knows_athletics_2|knows_riding_5|knows_horse_archery_5|knows_power_draw_4|knows_power_strike_3|knows_power_throw_3,swadian_face_young_1, swadian_face_old_2],
   
   
  # bandit heroes
  ["forest_bandit_hero","Forster","forest bandits",tf_hero|tf_randomize_face,0,0,fac_outlaws,
   [itm_bodkin_arrows,itm_one_handed_war_axe_b,itm_war_axe,itm_war_bow, itm_nasal_helmet,itm_padded_leather,itm_ankle_boots],
   attr(20,16,13,13)|level(22),wp(225),knows_ironflesh_3|knows_athletics_3|knows_power_strike_3|knows_power_draw_6|knows_tactics_4|knows_leadership_4,swadian_face_young_1, swadian_face_old_2],
  ["taiga_bandit_hero","Theron","taiga bandits",tf_hero|tf_randomize_face,0,0,fac_outlaws,
   [itm_barbed_arrows,itm_sword_khergit_4,itm_strong_nomad_bow,itm_maul, itm_throwing_spears,itm_leather_warrior_cap,itm_lamellar_vest,itm_leather_boots,itm_leather_covered_round_shield],
   attr(18,16,18,18)|level(30),wp(275),knows_ironflesh_5|knows_athletics_5|knows_power_draw_6|knows_power_strike_5|knows_power_throw_5|knows_tactics_6|knows_leadership_6,vaegir_face_young_1, vaegir_face_old_2],
  ["steppe_bandit_hero","Ulysses","steppe bandits",tf_hero|tf_randomize_face|tf_mounted,0,0,fac_outlaws,
   [itm_flat_headed_arrows,itm_sword_khergit_4,itm_khergit_bow,itm_winged_mace, itm_heavy_lance,itm_leather_warrior_cap,itm_splinted_leather_greaves,itm_tribal_warrior_outfit,itm_leather_covered_round_shield,itm_hunter],
   attr(18,19,12,15)|level(24),wp(250),knows_ironflesh_3|knows_athletics_3|knows_riding_8|knows_power_strike_3|knows_horse_archery_6|knows_power_draw_6|knows_tactics_5|knows_leadership_5,khergit_face_young_1, khergit_face_old_2],
  ["sea_raider_hero","Milo","sea raiders",tf_hero|tf_randomize_face,0,0,fac_outlaws,
   [itm_bodkin_arrows,itm_sword_viking_3,itm_long_bow,itm_long_axe_c,itm_tab_shield_round_d,itm_throwing_axes,
    itm_nordic_huscarl_helmet,itm_mail_hauberk,itm_mail_mittens,itm_mail_boots],
   attr(21,15,18,18)|level(32),wp(275),knows_power_strike_6|knows_power_throw_6|knows_power_draw_6|knows_riding_2|knows_ironflesh_5|knows_athletics_5|knows_tactics_6|knows_leadership_6,nord_face_young_1, nord_face_old_2],
  ["mountain_bandit_hero","Kontar","mountain bandits",tf_hero|tf_randomize_face,0,0,fac_outlaws,
   [itm_barbed_arrows,itm_sword_viking_3,itm_strong_bow,itm_plate_covered_round_shield,
    itm_leather_cap,itm_nomad_robe,itm_hide_boots],
   attr(20,16,13,13)|level(22),wp(225),knows_ironflesh_3|knows_athletics_3|knows_power_strike_3|knows_power_draw_4|knows_tactics_4|knows_leadership_4,rhodok_face_young_1, rhodok_face_old_2],
  ["desert_bandit_hero","Ulric","desert bandits",tf_hero|tf_randomize_face|tf_mounted,0,0,fac_outlaws,
   [itm_bamboo_arrows,itm_sarranid_cavalry_sword,itm_strong_bow,itm_winged_mace, itm_lance,itm_throwing_lances,
   itm_sarranid_cavalry_robe, itm_sarranid_horseman_helmet,itm_sarranid_boots_b,itm_leather_covered_round_shield,itm_hunter],
   attr(18,19,12,15)|level(24),wp(250),knows_ironflesh_3|knows_athletics_3|knows_riding_8|knows_power_strike_3|knows_power_throw_4|knows_horse_archery_6|knows_power_draw_6|knows_tactics_5|knows_leadership_5,khergit_face_young_1, khergit_face_old_2],
   
  ["black_khergit_horseman","Black Khergit Horseman","Black Khergit Horsemen",tf_allways_fall_dead|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_black_khergits,
   [itm_khergit_arrows,itm_sword_khergit_2,itm_scimitar,itm_scimitar,itm_winged_mace,itm_spear,itm_lance,itm_khergit_bow,itm_khergit_bow,itm_nomad_bow,itm_nomad_bow,itm_steppe_cap,itm_nomad_cap,itm_khergit_war_helmet,itm_khergit_war_helmet,itm_mail_hauberk,itm_hide_boots,itm_plate_covered_round_shield,itm_plate_covered_round_shield,itm_saddle_horse,itm_steppe_horse],
   attr(13,16,6,6)|level(21),wp(125),knows_riding_3|knows_power_strike_2|knows_ironflesh_3|knows_athletics_2|knows_horse_archery_3|knows_power_draw_3,khergit_face_young_1, khergit_face_old_2],
  ["black_khergit_guard","Black Khergit Guard","Black Khergit Guard", tf_allways_fall_dead|tf_mounted|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_black_khergits,
  [itm_khergit_arrows,itm_scimitar,itm_winged_mace,itm_lance,itm_khergit_bow,itm_khergit_bow,
   itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_khergit_guard_boots,itm_khergit_guard_armor,itm_khergit_guard_boots,itm_khergit_guard_armor,itm_warhorse,itm_warhorse],
  attr(16,18,7,7)|level(28),wp(175),knows_riding_6|knows_power_strike_3|knows_ironflesh_4|knows_athletics_3|knows_horse_archery_6|knows_power_draw_6,khergit_face_middle_2, khergit_face_old_1],
  ["black_khergit_lancer","Black Khergit Lancer","Black Khergit Lancer", tf_allways_fall_dead|tf_mounted|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_black_khergits,
  [itm_lance,itm_heavy_lance,itm_scimitar,itm_winged_mace,
   itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_khergit_guard_boots,itm_khergit_guard_armor,itm_khergit_guard_boots,itm_khergit_guard_armor,itm_warhorse,itm_warhorse],
  attr(16,18,8,8)|level(30),wp(200),knows_riding_6|knows_ironflesh_4|knows_athletics_3|knows_power_strike_4,khergit_face_middle_1, khergit_face_old_1],
  ["dark_hunter","Dark Hunter","Dark Hunters",tf_allways_fall_dead|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_polearm,0,0,fac_dark_knights,
   [itm_lance,itm_battle_axe,itm_morningstar,itm_leather_jerkin,itm_iron_greaves,itm_guard_helmet,itm_steel_shield,itm_saddle_horse,itm_warhorse],
   attr(15,16,6,6)|level(23),wp(150),knows_riding_4|knows_shield_3|knows_weapon_master_3|knows_ironflesh_2|knows_athletics_1|knows_power_strike_2,swadian_face_middle_1, swadian_face_young_1],
  ["dark_sniper","Dark Sniper","Dark Snipers", tf_allways_fall_dead|tf_mounted|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,0,0,fac_dark_knights,
   [itm_sniper_crossbow,itm_sniper_crossbow, itm_heavy_bolts, itm_heavy_bolts, itm_sword_of_war,itm_morningstar,itm_great_axe,itm_steel_shield,
itm_black_armor,itm_black_greaves,itm_black_helmet,itm_gauntlets,itm_gauntlets],
   attr(17,17,8,8)|level(30),wp(212),knows_riding_4|knows_shield_4|knows_weapon_master_4|knows_power_strike_4|knows_ironflesh_5|knows_athletics_2, swadian_face_older_2, swadian_face_old_2],
  ["dark_knight","Dark Knight","Dark Knights", tf_allways_fall_dead|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_polearm,0,0,fac_dark_knights,
   [itm_heavy_lance,itm_heavy_lance,itm_great_sword,itm_sword_of_war,itm_morningstar,itm_great_axe,itm_steel_shield,
itm_black_armor,itm_black_greaves,itm_black_helmet,itm_warhorse,itm_warhorse,itm_gauntlets,itm_gauntlets],
   attr(17,20,8,8)|level(33),wp(225),knows_riding_6|knows_shield_5|knows_weapon_master_5|knows_ironflesh_6|knows_athletics_4|knows_power_strike_6,swadian_face_middle_2, swadian_face_older_2],
## CC
## CC

#  ["undead_walker","undead_walker","undead_walkers",tf_undead|tf_allways_fall_dead,0,0,fac_undeads,
#   [], 
#   def_attrib|level(3),wp(60),knows_common,undead_face1, undead_face2],
#  ["undead_horseman","undead_horseman","undead_horsemen",tf_undead|tf_allways_fall_dead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_undeads,
#   [], 
#   def_attrib|level(19),wp(100),knows_common,undead_face1, undead_face2],
#  ["undead_nomad","undead_nomad","undead_nomads",tf_undead|tf_allways_fall_dead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_black_khergits,
#   [], 
#   def_attrib|level(21),wp(100),knows_common|knows_riding_4,khergit_face1, khergit_face2],
#  ["undead","undead","undead",tf_undead|tf_allways_fall_dead,0,0,fac_undeads,
#   [], 
#   def_attrib|level(3),wp(60),knows_common,undead_face1, undead_face2],
#  ["hell_knight","hell_knight","hell_knights",tf_undead|tf_allways_fall_dead|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_undeads,
#   [], 
#   def_attrib|level(23),wp(100),knows_common|knows_riding_3,undead_face1, undead_face2],

  ["caravan_master","Caravan Master","Caravan Masters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_commoners,
   [itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,
    itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,
    itm_leather_jacket, itm_leather_cap],
   attr(8,11,5,5)|level(9),wp(125),knows_speechcraft_2|knows_inventory_management_2|knows_looting_2|knows_leadership_1|knows_riding_4|knows_ironflesh_3|knows_athletics_2,mercenary_face_1, mercenary_face_2],

  ["kidnapped_girl","Kidnapped Girl","Kidnapped Girls", tf_randomize_face|tf_female|tf_guarantee_boots|tf_guarantee_armor,0,reserved,fac_commoners,
   [itm_dress,itm_leather_boots],
   def_attrib|level(2),wp(62),knows_speechcraft_2|knows_inventory_management_2|knows_looting_2|knows_leadership_1|knows_riding_2,woman_face_1, woman_face_2], ## CC

#This troop is the troop marked as soldiers_end and town_walkers_begin
 ["town_walker_1","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic, itm_linen_tunic,itm_fur_coat, itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_arena_tunic_white, itm_leather_apron, itm_shirt, itm_arena_tunic_green, itm_arena_tunic_blue, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_hide_boots, itm_ankle_boots, itm_leather_boots, itm_fur_hat, itm_leather_cap, itm_straw_hat, itm_felt_hat],
   def_attrib|level(4),wp(60),knows_common,man_face_young_1, man_face_old_2],
 ["town_walker_2","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_blue_dress, itm_dress, itm_woolen_dress, itm_peasant_dress, itm_woolen_hose, itm_blue_hose, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
 ["khergit_townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_sarranid_felt_hat,itm_turban,itm_wrapping_boots,itm_khergit_leather_boots,itm_sarranid_cloth_robe, itm_sarranid_cloth_robe_b],
   def_attrib|level(4),wp(60),knows_common,swadian_face_younger_1, swadian_face_middle_2],
 ["khergit_townswoman","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_blue_dress, itm_dress, itm_woolen_dress, itm_peasant_dress, itm_woolen_hose, itm_blue_hose, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
 ["sarranid_townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_sarranid_felt_hat,itm_turban,itm_wrapping_boots,itm_sarranid_boots_a,itm_sarranid_cloth_robe, itm_sarranid_cloth_robe_b],
   def_attrib|level(4),wp(60),knows_common,swadian_face_younger_1, swadian_face_middle_2],
 ["sarranid_townswoman","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_sarranid_common_dress, itm_sarranid_common_dress_b,itm_woolen_hose,itm_sarranid_boots_a, itm_sarranid_felt_head_cloth, itm_sarranid_felt_head_cloth_b],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
  
#This troop is the troop marked as town_walkers_end and village_walkers_begin
 ["village_walker_1","Villager","Villagers",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic, itm_linen_tunic, itm_coarse_tunic, itm_leather_vest, itm_leather_apron, itm_shirt, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_hide_boots, itm_ankle_boots, itm_leather_boots, itm_fur_hat, itm_leather_cap, itm_straw_hat, itm_felt_hat],
   def_attrib|level(4),wp(60),knows_common,man_face_younger_1, man_face_older_2],
 ["village_walker_2","Villager","Villagers",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_blue_dress, itm_dress, itm_woolen_dress, itm_peasant_dress, itm_woolen_hose, itm_blue_hose, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],

#This troop is the troop marked as village_walkers_end and spy_walkers_begin
 ["spy_walker_1","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_short_tunic, itm_linen_tunic, itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_robe, itm_leather_apron, itm_shirt, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_hide_boots, itm_ankle_boots, itm_leather_boots, itm_fur_hat, itm_leather_cap, itm_straw_hat, itm_felt_hat],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_old_2],
 ["spy_walker_2","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_blue_dress, itm_dress, itm_woolen_dress, itm_peasant_dress, itm_woolen_hose, itm_blue_hose, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
# Ryan END

#This troop is the troop marked as spy_walkers_end
# Zendar
  ["tournament_master","Tournament Master","Tournament Master",tf_hero, scn_zendar_center|entry(1),reserved,  fac_commoners,[itm_nomad_armor,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common,0x000000000008414401e28f534c8a2d09],
  ["trainer","Trainer","Trainer",tf_hero, scn_zendar_center|entry(2),reserved,  fac_commoners,[itm_leather_jerkin,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x00000000000430c701ea98836781647f],
  ["Constable_Hareck","Constable Hareck","Constable Hareck",tf_hero, scn_zendar_center|entry(5),reserved,  fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,0x00000000000c41c001fb15234eb6dd3f],

# Ryan BEGIN
  ["Ramun_the_slave_trader","Ramun, the slave trader","Ramun, the slave trader",tf_hero, no_scene,reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,0x0000000fd5105592385281c55b8e44eb00000000001d9b220000000000000000],

  ["guide","Quick Jimmy","Quick Jimmy",tf_hero, no_scene,0,  fac_commoners,[itm_coarse_tunic,itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, 0x00000000000c318301f24e38a36e38e3],
# Ryan END


  ["Xerina","Xerina","Xerina",tf_hero|tf_female, scn_the_happy_boar|entry(5),reserved,  fac_commoners,[itm_leather_jerkin,itm_hide_boots],attr(27,32,10,10)|level(39),wp(390),knows_power_strike_5|knows_riding_6|knows_power_draw_4|knows_power_throw_4|knows_ironflesh_5|knows_athletics_8|knows_shield_3|knows_weapon_master_3,0x00000001ac0820074920561d0b51e6ed00000000001d40ed0000000000000000],
  ["Dranton","Dranton","Dranton",tf_hero, scn_the_happy_boar|entry(2),reserved,  fac_commoners,[itm_leather_vest,itm_hide_boots],attr(33,27,11,11)|level(42),wp(405),knows_power_strike_5|knows_riding_4|knows_power_draw_3|knows_power_throw_3|knows_ironflesh_7|knows_athletics_4|knows_shield_3|knows_weapon_master_3,0x0000000a460c3002470c50f3502879f800000000001ce0a00000000000000000],
  ["Kradus","Kradus","Kradus",tf_hero, scn_the_happy_boar|entry(3),reserved,  fac_commoners,[itm_padded_leather,itm_hide_boots],attr(34,27,11,11)|level(43),wp(337),knows_power_strike_5|knows_riding_4|knows_power_draw_3|knows_power_throw_3|knows_ironflesh_7|knows_athletics_4|knows_shield_3|knows_weapon_master_3,0x0000000f5b1052c61ce1a9521db1375200000000001ed31b0000000000000000],


#Tutorial
  ["tutorial_trainer","Training Ground Master","Training Ground Master",tf_hero, 0, 0, fac_commoners,[itm_robe,itm_nomad_boots],def_attrib|level(2),wp(25),knows_common,0x000000000008414401e28f534c8a2d09],
  ["tutorial_student_1","{!}tutorial_student_1","{!}tutorial_student_1",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_sword, itm_practice_shield, itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],
   def_attrib|level(2),wp(25),knows_common, swadian_face_young_1, swadian_face_old_2],
  ["tutorial_student_2","{!}tutorial_student_2","{!}tutorial_student_2",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_sword, itm_practice_shield, itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],
   def_attrib|level(2),wp(25),knows_common, swadian_face_young_1, swadian_face_old_2],
  ["tutorial_student_3","{!}tutorial_student_3","{!}tutorial_student_3",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_staff, itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],
   def_attrib|level(2),wp(25),knows_common, swadian_face_young_1, swadian_face_old_2],
  ["tutorial_student_4","{!}tutorial_student_4","{!}tutorial_student_4",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_staff, itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],
   def_attrib|level(2),wp(25),knows_common, swadian_face_young_1, swadian_face_old_2],

#Sargoth
  #halkard, hardawk. lord_taucard lord_caupard. lord_paugard

#Salt mine
  ["Galeas","Galeas","Galeas",tf_hero, 0, reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,0x000000000004718201c073191a9bb10c],

#Dhorak keep

  ["farmer_from_bandit_village","Farmer","Farmers",tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_linen_tunic,itm_coarse_tunic,itm_shirt,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_older_2],

  ["trainer_1","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_1|entry(6),reserved,  fac_commoners,[itm_leather_jerkin,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000d0d1030c74ae8d661b651c6840000000000000e220000000000000000],
  ["trainer_2","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_2|entry(6),reserved,  fac_commoners,[itm_nomad_vest,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e5a04360428ec253846640b5d0000000000000ee80000000000000000],
  ["trainer_3","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_3|entry(6),reserved,  fac_commoners,[itm_padded_leather,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e4a0445822ca1a11ab1e9eaea0000000000000f510000000000000000],
  ["trainer_4","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_4|entry(6),reserved,  fac_commoners,[itm_leather_jerkin,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e600452c32ef8e5bb92cf1c970000000000000fc20000000000000000],
  ["trainer_5","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_5|entry(6),reserved,  fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e77082000150049a34c42ec960000000000000e080000000000000000],

## CC
  ["mystic_merchant","Mystic Merchant","Mystic Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common|knows_inventory_management_10|knows_looting_10,merchant_face_1,merchant_face_2],
## CC
  
# Ransom brokers.
  ["ransom_broker_1","Ransom_Broke","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_2","Ransom_Broke","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_tabard,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_3","Ransom_Broke","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_4","Ransom_Broke","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_short_tunic,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_5","Ransom_Broke","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_6","Ransom_Broke","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_blue_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_7","Ransom_Broke","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_red_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_8","Ransom_Broke","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_blue_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],

# Tavern traveler.
  ["tavern_traveler_1","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_2","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_tabard,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_3","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_4","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_5","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_short_tunic,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_6","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_7","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_8","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_tabard,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_9","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_10","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_11","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_12","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
# Tavern traveler.
## CC
  ["tavern_bookseller_1","Haelbrad, the book merchant","{!}Book Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,
  [itm_book_speechcraft, itm_book_speechcraft, itm_book_leadership, itm_book_leadership, itm_book_intelligence, itm_book_intelligence, itm_book_spotting_reference, itm_book_spotting_reference, itm_book_training_reference, itm_book_training_reference, itm_fur_coat, itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_bookseller_2","Givea Alsev, the book merchant","{!}Book Merchant",tf_female|tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,
  [itm_book_tactics, itm_book_tactics, itm_book_wound_treatment_reference, itm_book_wound_treatment_reference,  itm_book_first_aid_reference, itm_book_first_aid_reference, itm_book_engineering, itm_book_engineering, itm_book_weapon_mastery, itm_book_weapon_mastery, itm_book_pathfinding_reference,itm_book_pathfinding_reference, itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1, merchant_face_2],
## CC

# Tavern minstrel.
  ["tavern_minstrel_1","Wandering Minstrel","Wandering Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_leather_jacket, itm_hide_boots, itm_lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #lute
  ["tavern_minstrel_2","Wandering Bard","Wandering Bard",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_tunic_with_green_cape, itm_hide_boots, itm_lyre],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],  #early harp/lyre
  ["tavern_minstrel_3","Wandering Ashik","Wandering Ashik",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_nomad_robe, itm_hide_boots, itm_lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #lute/oud or rebab
  ["tavern_minstrel_4","Wandering Skald","Wandering Skald",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_fur_coat, itm_hide_boots, itm_lyre],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #No instrument or lyre
  ["tavern_minstrel_5","Wandering Troubadour","Wandering Troubadour",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_short_tunic, itm_hide_boots, itm_lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #Lute or Byzantine/Occitan lyra
  
#NPC system changes begin
#Companions
  ["kingdom_heroes_including_player_begin",  "kingdom_heroes_including_player_begin",  "kingdom_heroes_including_player_begin",  tf_hero, 0,reserved,  fac_kingdom_1,[],          lord_attrib,wp(220),knows_lord_1, 0x000000000010918a01f248377289467d],

  ["npc1","Borcha","Borcha",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_khergit_armor,itm_nomad_boots,itm_knife],
   attr(11,9,14,9)|level(3),wp(60), 
   knows_ironflesh_1|knows_athletics_2|knows_power_strike_1|knows_riding_2|knows_weapon_master_1|knows_shield_1|knows_spotting_2|knows_tracking_2|knows_pathfinding_3|knows_inventory_management_2|knows_looting_2, #skills 2/3 player at that level
   0x00000004bf086143259d061a9046e23500000000001db52c0000000000000000],
  ["npc2","Marnid","Marnid", tf_hero|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,[itm_linen_tunic,itm_hide_boots,itm_club],
   attr(10,10,9,12)|level(1),wp(40),
   knows_ironflesh_1|knows_athletics_2|knows_riding_2|knows_weapon_master_1|knows_shield_1|knows_speechcraft_3|knows_inventory_management_3|knows_looting_3|knows_wound_treatment_1|knows_first_aid_1|knows_leadership_1,
   0x000000019d004001570b893712c8d28d00000000001dc8990000000000000000],
  ["npc3","Ymira","Ymira",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_dress,itm_woolen_hose,itm_knife],
   attr(9,11,12,9)|level(1),wp(20),
   knows_athletics_1|knows_riding_2|knows_wound_treatment_1|knows_first_aid_3|knows_surgery_1|knows_speechcraft_3|knows_inventory_management_3|knows_looting_3,
   0x0000000083040001583b6db8dec5925b00000000001d80980000000000000000],
  ["npc4","Rolf","Rolf",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_leather_jerkin,itm_nomad_boots, itm_sword_medieval_a],
   attr(16,14,11,9)|level(10),wp(110),
   knows_ironflesh_1|knows_athletics_2|knows_power_strike_2|knows_power_throw_2|knows_weapon_master_2|knows_shield_2|knows_riding_2|knows_inventory_management_2|knows_looting_2|knows_first_aid_1|knows_surgery_1|knows_tactics_2|knows_leadership_2,
   0x000000057f1074002c75c6a8a58ad72e00000000001e1a890000000000000000],
  ["npc5","Baheshtur","Baheshtur",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_nomad_vest,itm_nomad_boots, itm_sword_khergit_1, itm_arrows, itm_nomad_bow],
   attr(12,15,9,9)|level(5),wp(90),
   knows_weapon_master_2|knows_shield_2|knows_ironflesh_1|knows_athletics_1|knows_power_strike_2|knows_power_draw_3|knows_riding_2|knows_horse_archery_3|knows_inventory_management_2|knows_looting_2|knows_leadership_2,
   0x000000088910318b5c6f972328324a6200000000001cd3310000000000000000],
  ["npc6","Firentis","Firentis",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_tabard,itm_nomad_boots, itm_sword_medieval_a],
   attr(13,12,12,9)|level(6),wp(105),
   knows_weapon_master_2|knows_shield_2|knows_athletics_3|knows_power_strike_2|knows_riding_2|knows_inventory_management_2|knows_looting_2|knows_trainer_1|knows_leadership_1,
  0x00000002050052036a1895d0748f3ca30000000000000f0b0000000000000000],
  ["npc7","Deshavi","Deshavi",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_ragged_outfit,itm_wrapping_boots, itm_hunting_bow, itm_arrows, itm_quarter_staff],
   attr(12,12,9,9)|level(2),wp(80),
   knows_weapon_master_1|knows_shield_1|knows_ironflesh_1|knows_athletics_2|knows_power_draw_2|knows_spotting_2|knows_pathfinding_2|knows_tracking_2|knows_inventory_management_2|knows_looting_2,
   0x00000001fc08400533a15297634d44f400000000001e02db0000000000000000],
  ["npc8","Matheld","Matheld",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_tribal_warrior_outfit,itm_nomad_boots, itm_sword_viking_1],
   attr(13,13,9,12)|level(7),wp(90),
   knows_weapon_master_3|knows_shield_3|knows_ironflesh_1|knows_athletics_2|knows_power_strike_2|knows_riding_2|knows_inventory_management_2|knows_looting_2|knows_leadership_3|knows_tactics_1,
   0x00000005800c000637db8314e331e76e00000000001c46db0000000000000000],
  ["npc9","Alayen","Alayen",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_tabard,itm_nomad_boots, itm_sword_medieval_b_small],
   attr(13,12,8,9)|level(2),wp(100),
   knows_weapon_master_2|knows_shield_2|knows_ironflesh_1|knows_athletics_1|knows_power_strike_2|knows_riding_2|knows_inventory_management_2|knows_looting_2|knows_leadership_1|knows_tactics_1,
   0x000000030100300f499d5b391b6db8d300000000001dc2e10000000000000000],
  ["npc10","Bunduk","Bunduk",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_padded_leather,itm_nomad_boots, itm_crossbow, itm_bolts_2, itm_pickaxe],
   attr(15,12,13,9)|level(9),wp(105),
   knows_weapon_master_3|knows_shield_3|knows_ironflesh_3|knows_athletics_1|knows_power_strike_2|knows_riding_2|knows_inventory_management_2|knows_looting_2|knows_tactics_1|knows_leadership_1|knows_trainer_2|knows_first_aid_2,
   0x0000000a3f081006572c91c71c8d46cb00000000001e468a0000000000000000],
  ["npc11","Katrin","Katrin",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_leather_apron, itm_falchion, itm_wrapping_boots],
   attr(12,12,15,9)|level(8),wp(70),
   knows_weapon_master_1|knows_shield_1|knows_ironflesh_3|knows_riding_2|knows_speechcraft_3|knows_inventory_management_5|knows_looting_5|knows_first_aid_1|knows_wound_treatment_2,
   0x0000000d7f0400035915aa226b4d975200000000001ea49e0000000000000000],
  ["npc12","Jeremus","Jeremus",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_pilgrim_disguise,itm_nomad_boots, itm_staff],
   attr(9,11,15,9)|level(4),wp(30),    
   knows_ironflesh_1|knows_power_strike_1|knows_riding_2|knows_speechcraft_3|knows_inventory_management_3|knows_looting_3|knows_surgery_4|knows_wound_treatment_3|knows_first_aid_3,
   0x000000078000500e4f8ba62a9cd5d36d00000000001e36250000000000000000],
  ["npc13","Nizar","Nizar",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_nomad_robe,itm_nomad_boots, itm_scimitar, itm_courser],
   attr(12,10,9,12)|level(3),wp(80),
   knows_weapon_master_2|knows_shield_2|knows_ironflesh_2|knows_athletics_2|knows_power_strike_2|knows_riding_2|knows_inventory_management_2|knows_looting_2|knows_leadership_2,
   0x00000004bf0475c85f4e9592de4e574c00000000001e369c0000000000000000],
  ["npc14","Lezalit","Lezalit",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_nobleman_outfit,itm_nomad_boots, itm_sword_medieval_b_small],
   attr(11,12,13,9)|level(5),wp(100),
   knows_weapon_master_3|knows_shield_3|knows_ironflesh_1|knows_athletics_1|knows_power_strike_2|knows_riding_2|knows_inventory_management_2|knows_looting_2|knows_trainer_4|knows_leadership_2,
   0x00000001a410259144d5d1d6eb55e96a00000000001db0db0000000000000000],
  ["npc15","Artimenner","Artimenner",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_rich_outfit,itm_nomad_boots, itm_sword_medieval_b_small],
   attr(15,9,14,9)|level(7),wp(80),
   knows_weapon_master_2|knows_shield_2|knows_ironflesh_1|knows_athletics_1|knows_power_strike_2|knows_riding_2|knows_inventory_management_2|knows_looting_2|knows_tactics_2|knows_engineer_4|knows_speechcraft_3|knows_tracking_1|knows_spotting_1,
   0x0000000f2e1021862b4b9123594eab5300000000001d55360000000000000000],
  ["npc16","Klethi","Klethi",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_peasant_dress,itm_nomad_boots, itm_dagger, itm_throwing_knives],
   attr(13,12,8,9)|level(2),wp(80),
   knows_weapon_master_1|knows_shield_1|knows_ironflesh_1|knows_athletics_2|knows_power_throw_3|knows_power_strike_1|knows_spotting_2|knows_pathfinding_2|knows_tracking_2|knows_inventory_management_2|knows_looting_2,
   0x00000000000c100739ce9c805d2f381300000000001cc7ad0000000000000000],
#NPC system changes end


#governers olgrel rasevas                                                                        Horse          Bodywear                Footwear_in                     Footwear_out                    Armor                       Weapon                  Shield                  Headwaer
  ["kingdom_1_lord",  "King Harlaus",  "Harlaus",  tf_hero, 0,reserved,  fac_kingdom_1,[(itm_heavy_charger,imod_champion),   itm_rich_outfit,        itm_blue_hose,                  itm_plate_boots,               itm_plate_armor, itm_gauntlets,    (itm_bastard_sword_b,imod_masterwork),      (itm_tab_shield_heater_cav_b,imod_reinforced),       itm_great_helmet],          knight_attrib_5,wp(220),knight_skills_5|knows_trainer_5, 0x0000000f45041105241acd2b5a66a86900000000001e98310000000000000000,swadian_face_older_2],
  ["kingdom_2_lord",  "King Yaroglek",  "Yaroglek",  tf_hero, 0,reserved,  fac_kingdom_2,[(itm_heavy_warhorse_vaegir,imod_champion),    itm_courtly_outfit,      itm_leather_boots,              itm_plate_boots,              itm_heraldic_mail_with_surcoat, itm_gauntlets,      (itm_military_pick,imod_balanced),      (itm_tab_shield_kite_cav_b,imod_reinforced),      itm_vaegir_mask],    knight_attrib_5,wp(220),knight_skills_5|knows_trainer_4, 0x0000000ec50001400a2269f919dee11700000000001cc57d0000000000000000, vaegir_face_old_2],
  ["kingdom_3_lord",  "Sanjar Khan",  "Sanjar",  tf_hero, 0,reserved,  fac_kingdom_3,[(itm_heavy_warhorse_steppe,imod_champion),   itm_nomad_robe,             itm_leather_boots,              itm_splinted_greaves,           itm_khergit_guard_armor,  itm_lamellar_gauntlets,       (itm_sword_khergit_3,imod_masterwork),              (itm_tab_shield_small_round_c,imod_reinforced),       itm_guard_helmet],      knight_attrib_5,wp(220),knight_skills_5|knows_trainer_6, 0x0000000cee0051cc44be2d14d370c65c00000000001ed6df0000000000000000,khergit_face_old_2],
  ["kingdom_4_lord",  "King Ragnar",  "Ragnar",  tf_hero, 0,reserved,  fac_kingdom_4,[(itm_heavy_warhorse_b,imod_champion),    itm_nobleman_outfit,    itm_leather_boots,              itm_mail_boots,                 itm_cuir_bouilli,  itm_gauntlets,    (itm_great_axe,imodbit_heavy),           (itm_tab_shield_round_e,imod_reinforced),    itm_nordic_helmet],            knight_attrib_5,wp(220),knight_skills_5|knows_trainer_4, 0x0000000e2c0c028a068e8c18557b12a500000000001c0fe80000000000000000, nord_face_older_2],
  ["kingdom_5_lord",  "King Graveth",  "Graveth",  tf_hero, 0,reserved,  fac_kingdom_5,[(itm_heavy_warhorse_g,imod_champion),  itm_tabard,             itm_leather_boots,              itm_splinted_leather_greaves,   itm_heraldic_mail_with_tabard,  itm_gauntlets,         (itm_bastard_sword_b,imod_masterwork),         (itm_tab_shield_heater_cav_b,imod_reinforced),        itm_spiked_helmet],         knight_attrib_5,wp(220),knight_skills_4|knows_trainer_5, 0x0000000efc04119225848dac5d50d62400000000001d48b80000000000000000, rhodok_face_old_2],
  ["kingdom_6_lord",  "Sultan Hakim",  "Hakim",  tf_hero, 0,reserved,  fac_kingdom_6,[(itm_heavy_warhorse_sarranid,imod_champion),     itm_mamluke_mail,          itm_sarranid_boots_c,       itm_sarranid_mail_coif,  itm_mail_mittens,      (itm_sarranid_cavalry_sword,imod_masterwork),    (itm_tab_shield_small_round_c,imod_reinforced)],         knight_attrib_5,wp(220),knight_skills_4|knows_trainer_5, 0x0000000a4b103354189c71d6d386e8ac00000000001e24eb0000000000000000, rhodok_face_old_2],

#    Imbrea   Belinda Ruby Qaelmas Rose    Willow 
#  Alin  Ganzo            Zelka Rabugti
#  Qlurzach Ruhbus Givea_alsev  Belanz        Bendina  
# Dunga        Agatha     Dibus Crahask
  
#                                                                               Horse                   Bodywear                Armor                               Footwear_in                 Footwear_out                        Headwear                    Weapon               Shield
  #Swadian civilian clothes: itm_courtly_outfit itm_gambeson itm_blue_gambeson itm_red_gambeson itm_nobleman_outfit itm_rich_outfit itm_short_tunic itm_tabard
  #Older knights with higher skills moved to top
  ["knight_1_1", "Count Klargus", "Klargus", tf_hero, 0, reserved,  fac_kingdom_1, [itm_hunter,      itm_courtly_outfit,      itm_heraldic_mail_with_surcoat,   itm_nomad_boots, itm_splinted_greaves,       itm_great_helmet,           itm_sword_medieval_c,  itm_scale_gauntlets,         itm_tab_shield_heater_cav_a],   knight_attrib_5,wp(230),knight_skills_5|knows_trainer_3, 0x0000000c3e08601414ab4dc6e39296b200000000001e231b0000000000000000, swadian_face_older_2],
  ["knight_1_2", "Count Delinard", "Delinard", tf_hero, 0, reserved,  fac_kingdom_1, [itm_courser,           itm_red_gambeson,      itm_heraldic_mail_with_surcoat,               itm_nomad_boots,            itm_iron_greaves,                    itm_guard_helmet,  itm_gauntlets,        itm_bastard_sword_a,    itm_tab_shield_heater_cav_b],       knight_attrib_5,wp(240),knight_skills_5, 0x0000000c0f0c320627627238dcd6599400000000001c573d0000000000000000, swadian_face_young_2],
  ["knight_1_3", "Count Haringoth", "Haringoth", tf_hero, 0, reserved,  fac_kingdom_1, [itm_warhorse_r,          itm_nobleman_outfit,     itm_coat_of_plates,                 itm_leather_boots,          itm_splinted_leather_greaves,        itm_flat_topped_helmet, itm_gauntlets, itm_bastard_sword_b,   itm_tab_shield_heater_d],  knight_attrib_5,wp(260),knight_skills_5|knows_trainer_3, 0x0000000cb700210214ce89db276aa2f400000000001d36730000000000000000, swadian_face_young_2],
  ["knight_1_4", "Count Clais", "Clais", tf_hero, 0, reserved,  fac_kingdom_1, [itm_hunter,      itm_short_tunic,       itm_heraldic_mail_with_surcoat,           itm_leather_boots,          itm_mail_chausses,                   itm_winged_great_helmet, itm_gauntlets,       itm_bastard_sword_a,  itm_sword_two_handed_a,  itm_tab_shield_heater_d],    knight_attrib_5,wp(180),knight_skills_5|knows_trainer_4, 0x0000000c370c1194546469ca6c4e450e00000000001ebac40000000000000000, swadian_face_older_2],
  ["knight_1_5", "Count Deglan", "Deglan", tf_hero, 0, reserved,  fac_kingdom_1, [itm_hunter,            itm_rich_outfit,        itm_mail_hauberk,itm_woolen_hose, itm_mail_chausses, itm_guard_helmet, itm_gauntlets,         itm_sword_medieval_c,    itm_tab_shield_heater_d],      knight_attrib_4,wp(200),knight_skills_4|knows_trainer_6, 0x0000000c0c1064864ba34e2ae291992b00000000001da8720000000000000000, swadian_face_older_2],
  ["knight_1_6", "Count Tredian", "Tredian", tf_hero, 0, reserved,  fac_kingdom_1, [itm_hunter,            itm_tabard,      itm_heraldic_mail_with_surcoat,               itm_leather_boots,          itm_mail_boots,                      itm_winged_great_helmet, itm_gauntlets, itm_bastard_sword_b, itm_sword_two_handed_b,  itm_tab_shield_heater_cav_b], knight_attrib_5,wp(240),knight_skills_4|knows_trainer_4, 0x0000000c0a08038736db74c6a396a8e500000000001db8eb0000000000000000, swadian_face_older_2],
  ["knight_1_7", "Count Grainwad", "Grainwad", tf_hero, 0, reserved,  fac_kingdom_1, [itm_hunter,            itm_tabard,      itm_heraldic_mail_with_surcoat,               itm_leather_boots,          itm_mail_boots,                      itm_flat_topped_helmet, itm_gauntlets, itm_bastard_sword_b,   itm_sword_two_handed_b, itm_tab_shield_heater_cav_b], knight_attrib_5,wp(290),knight_skills_4|knows_trainer_4, 0x0000000c1e001500589dae4094aa291c00000000001e37a80000000000000000, swadian_face_young_2],
  ["knight_1_8", "Count Ryis", "Ryis", tf_hero, 0, reserved,  fac_kingdom_1, [itm_warhorse_r,          itm_nobleman_outfit,     itm_coat_of_plates,                 itm_leather_boots,          itm_splinted_leather_greaves,        itm_winged_great_helmet,  itm_gauntlets,itm_bastard_sword_b,  itm_sword_two_handed_a, itm_tab_shield_heater_d],  knight_attrib_4,wp(250),knight_skills_4, 0x0000000c330855054aa9aa431a48d74600000000001ed5240000000000000000, swadian_face_older_2],

#Swadian younger knights  
  ["knight_1_9", "Count Plais", "Plais", tf_hero, 0, reserved,  fac_kingdom_1, [itm_steppe_horse,      itm_gambeson,     itm_heraldic_mail_with_surcoat,                 itm_blue_hose,              itm_mail_boots,                      itm_nasal_helmet,  itm_scale_gauntlets,     itm_fighting_pick,   itm_tab_shield_heater_c],    knight_attrib_3,wp(160),knight_skills_3, 0x0000000c0f08000458739a9a1476199800000000001fb6f10000000000000000, swadian_face_old_2],
  ["knight_1_10", "Count Mirchaud", "Mirchaud", tf_hero, 0, reserved,  fac_kingdom_1, [itm_courser,           itm_blue_gambeson,        itm_mail_hauberk,                   itm_woolen_hose,            itm_mail_chausses,                   itm_guard_helmet,    itm_gauntlets,    itm_sword_two_handed_b,        itm_tab_shield_heater_cav_b],   knight_attrib_3,wp(190),knight_skills_3, 0x0000000c0610351048e325361d7236cd00000000001d532a0000000000000000, swadian_face_older_2],
  ["knight_1_11", "Count Stamar", "Stamar", tf_hero, 0, reserved,  fac_kingdom_1, [itm_courser,           itm_red_gambeson,      itm_heraldic_mail_with_surcoat,               itm_nomad_boots,            itm_iron_greaves,                    itm_guard_helmet,   itm_gauntlets,       itm_bastard_sword_a,    itm_tab_shield_heater_cav_b],       knight_attrib_3,wp(220),knight_skills_3, 0x0000000c03104490280a8cb2a24196ab00000000001eb4dc0000000000000000, swadian_face_older_2],
  ["knight_1_12", "Count Meltor", "Meltor", tf_hero, 0, reserved,  fac_kingdom_1, [itm_hunter,      itm_rich_outfit,        itm_heraldic_mail_with_surcoat,                    itm_nomad_boots,            itm_mail_boots,                      itm_guard_helmet,   itm_gauntlets,         itm_fighting_pick,   itm_tab_shield_heater_c],    knight_attrib_3,wp(130),knight_skills_3, 0x0000000c2a0805442b2c6cc98c8dbaac00000000001d389b0000000000000000, swadian_face_older_2],
  ["knight_1_13", "Count Beranz", "Beranz", tf_hero, 0, reserved,  fac_kingdom_1, [itm_hunter,      itm_ragged_outfit,      itm_heraldic_mail_with_surcoat,           itm_nomad_boots,            itm_splinted_greaves,                itm_guard_helmet,   itm_gauntlets,         itm_sword_medieval_c,  itm_sword_two_handed_a,     itm_tab_shield_heater_c],   knight_attrib_2,wp(160),knight_skills_2, 0x0000000c380c30c2392a8e5322a5392c00000000001e5c620000000000000000, swadian_face_older_2],
  ["knight_1_14", "Count Rafard", "Rafard", tf_hero, 0, reserved,  fac_kingdom_1, [itm_hunter,      itm_short_tunic,       itm_heraldic_mail_with_tabard,           itm_leather_boots,          itm_mail_chausses,                   itm_nasal_helmet,  itm_scale_gauntlets,     itm_bastard_sword_a,    itm_tab_shield_heater_cav_a],    knight_attrib_2,wp(190),knight_skills_3|knows_trainer_6, 0x0000000c3f10000532d45203954e192200000000001e47630000000000000000, swadian_face_older_2],
  ["knight_1_15", "Count Regas", "Regas", tf_hero, 0, reserved,  fac_kingdom_1, [itm_hunter,            itm_rich_outfit,        itm_mail_hauberk,                   itm_woolen_hose,            itm_mail_chausses,                   itm_great_helmet,   itm_gauntlets,       itm_sword_viking_3, itm_sword_two_handed_a,  itm_tab_shield_heater_d],      knight_attrib_4,wp(140),knight_skills_2, 0x0000000c5c0840034895654c9b660c5d00000000001e34530000000000000000, swadian_face_young_2],
  ["knight_1_16", "Count Devlian", "Devlian", tf_hero, 0, reserved,  fac_kingdom_1, [itm_hunter,      itm_courtly_outfit,      itm_heraldic_mail_with_surcoat,                     itm_nomad_boots,            itm_splinted_greaves,                itm_great_helmet,   itm_gauntlets,         itm_sword_medieval_c,           itm_tab_shield_heater_c],   knight_attrib_1,wp(130),knight_skills_2, 0x000000095108144657a1ba3ad456e8cb00000000001e325a0000000000000000, swadian_face_young_2],
  ["knight_1_17", "Count Rafarch", "Rafarch", tf_hero, 0, reserved,  fac_kingdom_1, [itm_steppe_horse,      itm_gambeson,     itm_heraldic_mail_with_surcoat,                 itm_blue_hose,              itm_mail_boots,                      itm_nasal_helmet,   itm_scale_gauntlets,    itm_fighting_pick,   itm_tab_shield_heater_cav_b],    knight_attrib_2,wp(190),knight_skills_1|knows_trainer_4, 0x0000000c010c42c14d9d6918bdb336e200000000001dd6a30000000000000000, swadian_face_young_2],
  ["knight_1_18", "Count Rochabarth", "Rochabarth", tf_hero, 0, reserved,  fac_kingdom_1, [itm_courser,           itm_blue_gambeson,        itm_mail_hauberk,                   itm_woolen_hose,            itm_mail_chausses,                   itm_winged_great_helmet,   itm_gauntlets,     itm_sword_two_handed_a,        itm_tab_shield_heater_cav_a],   knight_attrib_3,wp(210),knight_skills_1, 0x0000000c150045c6365d8565932a8d6400000000001ec6940000000000000000, swadian_face_young_2],
  ["knight_1_19", "Count Despin", "Despin", tf_hero, 0, reserved,  fac_kingdom_1, [itm_hunter,      itm_rich_outfit,        itm_heraldic_mail_with_surcoat,                    itm_nomad_boots,            itm_mail_boots,                      itm_great_helmet, itm_gauntlets,           itm_fighting_pick,  itm_sword_two_handed_a, itm_tab_shield_heater_cav_a],    knight_attrib_1,wp(120),knight_skills_1, 0x00000008200012033d9b6d4a92ada53500000000001cc1180000000000000000, swadian_face_young_2],
  ["knight_1_20", "Count Montewar", "Montewar", tf_hero, 0, reserved,  fac_kingdom_1, [itm_hunter,      itm_ragged_outfit,      itm_heraldic_mail_with_surcoat,           itm_nomad_boots,            itm_splinted_greaves,                itm_great_helmet, itm_gauntlets,           itm_sword_medieval_c,   itm_sword_two_handed_a,   itm_tab_shield_heater_cav_a],   knight_attrib_2,wp(150),knight_skills_1, 0x0000000c4d0840d24a9b2ab4ac2a332400000000001d34db0000000000000000, swadian_face_young_2],



  
#  ["knight_1_21", "Lord Swadian 21", "knight_1_7", tf_hero, 0, reserved,  fac_kingdom_1, [itm_saddle_horse,      itm_ragged_outfit,      itm_heraldic_mail_with_surcoat,           itm_nomad_boots,            itm_splinted_greaves,                itm_great_helmet, itm_gauntlets,           itm_sword_medieval_c,   itm_sword_two_handed_a,   itm_tab_shield_heater_cav_a],   knight_attrib_2,wp(150),knight_skills_2, 0x0000000c4d0840d24a9b2ab4ac2a332400000000001d34db0000000000000000, swadian_face_young_2],
 # ["knight_1_22", "Lord Swadian 22", "knight_1_8", tf_hero, 0, reserved,  fac_kingdom_1, [itm_saddle_horse,      itm_short_tunic,       itm_heraldic_mail_with_surcoat,           itm_leather_boots,          itm_mail_chausses,                   itm_winged_great_helmet, itm_gauntlets,       itm_bastard_sword_a,  itm_sword_two_handed_a,  itm_tab_shield_heater_d],    knight_attrib_3,wp(180),knight_skills_3|knows_trainer_4, 0x0000000c370c1194546469ca6c4e450e00000000001ebac40000000000000000, swadian_face_older_2],
#  ["knight_1_23", "Lord Swadian 23", "knight_1_9", tf_hero, 0, reserved,  fac_kingdom_1, [itm_hunter,            itm_rich_outfit,        itm_mail_hauberk,                   itm_woolen_hose,            itm_mail_chausses,                   itm_guard_helmet, itm_gauntlets,         itm_sword_medieval_c,    itm_tab_shield_heater_d],      knight_attrib_4,wp(200),knight_skills_4|knows_trainer_6, 0x0000000c0c1064864ba34e2ae291992b00000000001da8720000000000000000, swadian_face_older_2],
#  ["knight_1_24", "Lord Swadian 24", "knight_1_0", tf_hero, 0, reserved,  fac_kingdom_1, [itm_hunter,            itm_tabard,      itm_heraldic_mail_with_surcoat,               itm_leather_boots,          itm_mail_boots,                      itm_winged_great_helmet, itm_gauntlets, itm_bastard_sword_b, itm_sword_two_handed_b,  itm_tab_shield_heater_cav_b], knight_attrib_5,wp(240),knight_skills_5|knows_trainer_5, 0x0000000c0a08038736db74c6a396a8e500000000001db8eb0000000000000000, swadian_face_older_2],

  
  
  ["knight_2_1", "Boyar Vuldrat", "Vuldrat", tf_hero, 0, reserved,  fac_kingdom_2, [itm_hunter,      itm_fur_coat,     itm_vaegir_elite_armor,                   itm_nomad_boots,            itm_splinted_leather_greaves,        itm_vaegir_noble_helmet,    itm_mail_mittens,       itm_sword_viking_3,           itm_tab_shield_kite_c],    knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x00000005590011c33d9b6d4a92ada53500000000001cc1180000000000000000, vaegir_face_middle_2],
  ["knight_2_2", "Boyar Naldera", "Naldera", tf_hero, 0, reserved,  fac_kingdom_2, [itm_hunter,      itm_rich_outfit,        itm_lamellar_armor,               itm_woolen_hose,            itm_mail_chausses,                   itm_vaegir_noble_helmet,  itm_mail_mittens,      itm_shortened_military_scythe,    itm_tab_shield_kite_cav_a],    knight_attrib_2,wp(160),knight_skills_2, 0x0000000c2a0015d249b68b46a98e176400000000001d95a40000000000000000, vaegir_face_old_2],
  ["knight_2_3", "Boyar Meriga", "Meriga", tf_hero, 0, reserved,  fac_kingdom_2, [itm_warhorse_vaegir,            itm_short_tunic,        itm_mail_hauberk,                   itm_woolen_hose,            itm_mail_chausses,                   itm_vaegir_lamellar_helmet, itm_lamellar_gauntlets,           itm_great_bardiche,           itm_tab_shield_kite_cav_b],     knight_attrib_3,wp(190),knight_skills_3, 0x0000000c131031c546a38a2765b4c86000000000001e58d30000000000000000, vaegir_face_older_2],
  ["knight_2_4", "Boyar Khavel", "Khavel", tf_hero, 0, reserved,  fac_kingdom_2, [itm_hunter,      itm_courtly_outfit,     itm_lamellar_armor,               itm_leather_boots,          itm_mail_boots,                      itm_vaegir_noble_helmet, itm_lamellar_gauntlets,         itm_bastard_sword_b,   itm_tab_shield_kite_cav_b],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000c2f0832c748f272540d8ab65900000000001d34e60000000000000000, vaegir_face_older_2],
  ["knight_2_5", "Boyar Doru", "Doru", tf_hero, 0, reserved,  fac_kingdom_2, [itm_warhorse_vaegir,            itm_rich_outfit,        itm_haubergeon,                     itm_leather_boots,          itm_mail_chausses,                   itm_vaegir_noble_helmet, itm_scale_gauntlets,   itm_bastard_sword_b,   itm_tab_shield_kite_d],       knight_attrib_5,wp(250),knight_skills_5, 0x0000000e310061435d76bb5f55bad9ad00000000001ed8ec0000000000000000, vaegir_face_older_2],
  ["knight_2_6", "Boyar Belgaru", "Belgaru", tf_hero, 0, reserved,  fac_kingdom_2, [itm_hunter,      itm_nomad_vest,      itm_vaegir_elite_armor,                   itm_woolen_hose,            itm_mail_chausses,                   itm_vaegir_lamellar_helmet,  itm_mail_mittens,          itm_sword_viking_3,           itm_tab_shield_kite_c],   knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x0000000a0100421038da7157aa4e430a00000000001da8bc0000000000000000, vaegir_face_middle_2],
  ["knight_2_7", "Boyar Ralcha", "Ralcha", tf_hero, 0, reserved,  fac_kingdom_2, [itm_steppe_horse,      itm_leather_jacket,     itm_mail_hauberk,                   itm_leather_boots,          itm_mail_boots,                      itm_vaegir_noble_helmet,  itm_lamellar_gauntlets,          itm_great_bardiche,    itm_tab_shield_kite_cav_a],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000c04100153335ba9390b2d277500000000001d89120000000000000000, vaegir_face_old_2],
  ["knight_2_8", "Boyar Vlan", "Vlan", tf_hero, 0, reserved,  fac_kingdom_2, [itm_hunter,            itm_light_mail_and_plate,             itm_nomad_vest,                     itm_woolen_hose,            itm_mail_chausses,                   itm_vaegir_noble_helmet, itm_lamellar_gauntlets,       itm_shortened_military_scythe,    itm_tab_shield_kite_d],    knight_attrib_3,wp(200),knight_skills_3|knows_trainer_5, 0x0000000c00046581234e8da2cdd248db00000000001f569c0000000000000000, vaegir_face_older_2],
  ["knight_2_9", "Boyar Mleza", "Mleza", tf_hero, 0, reserved,  fac_kingdom_2, [itm_hunter,      itm_rich_outfit,        itm_vaegir_elite_armor,                     itm_leather_boots,          itm_mail_chausses,                   itm_vaegir_lamellar_helmet,  itm_lamellar_gauntlets,        itm_great_bardiche,   itm_tab_shield_kite_d],    knight_attrib_4,wp(230),knight_skills_4, 0x0000000c160451d2136469c4d9b159ad00000000001e28f10000000000000000, vaegir_face_older_2],
  ["knight_2_10", "Boyar Nelag", "Nelag", tf_hero, 0, reserved,  fac_kingdom_2, [itm_warhorse_vaegir,          itm_fur_coat,        itm_lamellar_armor,               itm_woolen_hose,            itm_mail_boots,                      itm_vaegir_noble_helmet,  itm_scale_gauntlets,      itm_military_pick,   itm_tab_shield_kite_cav_b],      knight_attrib_5,wp(260),knight_skills_5|knows_trainer_6, 0x0000000f7c00520e66b76edd5cd5eb6e00000000001f691e0000000000000000, vaegir_face_older_2],
  ["knight_2_11", "Boyar Crahask", "Crahask", tf_hero, 0, reserved,  fac_kingdom_2, [itm_hunter,      itm_leather_jacket,     itm_vaegir_elite_armor,                   itm_nomad_boots,            itm_splinted_leather_greaves,        itm_vaegir_noble_helmet, itm_scale_gauntlets,           itm_sword_viking_3,           itm_tab_shield_kite_cav_a],    knight_attrib_1,wp(130),knight_skills_1, 0x0000000c1d0821d236acd6991b74d69d00000000001e476c0000000000000000, vaegir_face_middle_2],
  ["knight_2_12", "Boyar Bracha", "Bracha", tf_hero, 0, reserved,  fac_kingdom_2, [itm_hunter,      itm_rich_outfit,        itm_lamellar_armor,               itm_woolen_hose,            itm_mail_chausses,                   itm_vaegir_noble_helmet,  itm_mail_mittens,      itm_great_bardiche,    itm_tab_shield_kite_cav_a],    knight_attrib_2,wp(170),knight_skills_2, 0x0000000c0f04024b2509d5d53944c6a300000000001d5b320000000000000000, vaegir_face_old_2],
  ["knight_2_13", "Boyar Druli", "Druli", tf_hero, 0, reserved,  fac_kingdom_2, [itm_hunter,            itm_short_tunic,        itm_mail_hauberk,                   itm_woolen_hose,            itm_mail_chausses,                   itm_vaegir_lamellar_helmet,  itm_lamellar_gauntlets,          itm_great_bardiche,           itm_tab_shield_kite_cav_b],     knight_attrib_3,wp(190),knight_skills_3, 0x0000000c680432d3392230cb926d56ca00000000001da69b0000000000000000, vaegir_face_older_2],
  ["knight_2_14", "Boyar Marmun", "Marmun", tf_hero, 0, reserved,  fac_kingdom_2, [itm_hunter,      itm_courtly_outfit,     itm_lamellar_armor,               itm_leather_boots,          itm_mail_boots,                      itm_vaegir_noble_helmet,  itm_lamellar_gauntlets,        itm_shortened_military_scythe,   itm_tab_shield_kite_cav_b],    knight_attrib_4,wp(220),knight_skills_4|knows_trainer_6, 0x0000000c27046000471bd2e93375b52c00000000001dd5220000000000000000, vaegir_face_older_2],
  ["knight_2_15", "Boyar Gastya", "Gastya", tf_hero, 0, reserved,  fac_kingdom_2, [itm_hunter,            itm_rich_outfit,        itm_haubergeon,                     itm_leather_boots,          itm_mail_chausses,                   itm_vaegir_lamellar_helmet, itm_lamellar_gauntlets,   itm_bastard_sword_b,  itm_shortened_military_scythe, itm_tab_shield_kite_cav_b],       knight_attrib_5,wp(250),knight_skills_5, 0x0000000de50052123b6bb36de5d6eb7400000000001dd72c0000000000000000, vaegir_face_older_2],
  ["knight_2_16", "Boyar Harish", "Harish", tf_hero, 0, reserved,  fac_kingdom_2, [itm_hunter,      itm_nomad_vest,      itm_vaegir_elite_armor,                   itm_woolen_hose,            itm_mail_chausses,                   itm_vaegir_noble_helmet,  itm_mail_mittens,          itm_great_bardiche,           itm_tab_shield_kite_c],   knight_attrib_1,wp(120),knight_skills_1, 0x000000085f00000539233512e287391d00000000001db7200000000000000000, vaegir_face_middle_2],
  ["knight_2_17", "Boyar Taisa", "Taisa", tf_hero, 0, reserved,  fac_kingdom_2, [itm_steppe_horse,      itm_leather_jacket,     itm_mail_hauberk,                   itm_leather_boots,          itm_mail_boots,                      itm_vaegir_noble_helmet,   itm_scale_gauntlets,         itm_great_bardiche,    itm_tab_shield_kite_cav_a],     knight_attrib_2,wp(150),knight_skills_2, 0x0000000a070c4387374bd19addd2a4ab00000000001e32cc0000000000000000, vaegir_face_old_2],
  ["knight_2_18", "Boyar Valishin", "Valishin", tf_hero, 0, reserved,  fac_kingdom_2, [itm_hunter,            itm_light_mail_and_plate,             itm_nomad_vest,                     itm_woolen_hose,            itm_mail_chausses,                   itm_vaegir_lamellar_helmet,  itm_lamellar_gauntlets,      itm_great_bardiche,    itm_tab_shield_kite_cav_a],    knight_attrib_3,wp(180),knight_skills_3, 0x0000000b670012c23d9b6d4a92ada53500000000001cc1180000000000000000, vaegir_face_older_2],
  ["knight_2_19", "Boyar Rudin", "Rudin", tf_hero, 0, reserved,  fac_kingdom_2, [itm_hunter,      itm_rich_outfit,        itm_vaegir_elite_armor,                     itm_leather_boots,          itm_mail_chausses,                   itm_vaegir_noble_helmet, itm_scale_gauntlets,         itm_fighting_pick,  itm_shortened_military_scythe, itm_tab_shield_kite_d],    knight_attrib_4,wp(210),knight_skills_4|knows_trainer_4, 0x0000000e070050853b0a6e4994ae272a00000000001db4e10000000000000000, vaegir_face_older_2],
  ["knight_2_20", "Boyar Kumipa", "Kumipa", tf_hero, 0, reserved,  fac_kingdom_2, [itm_warhorse_vaegir,          itm_fur_coat,        itm_lamellar_armor,               itm_woolen_hose,            itm_mail_boots,                      itm_vaegir_lamellar_helmet,  itm_lamellar_gauntlets,      itm_great_bardiche,   itm_tab_shield_kite_cav_b],      knight_attrib_5,wp(240),knight_skills_5|knows_trainer_5, 0x0000000f800021c63b0a6e4994ae272a00000000001db4e10000000000000000, vaegir_face_older_2],

#khergit civilian clothes: itm_leather_vest, itm_nomad_vest, itm_nomad_robe, itm_lamellar_vest,itm_tribal_warrior_outfit
  ["knight_3_1", "Alagur Noyan", "Alagur", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser, itm_leather_vest,  itm_studded_leather_coat,itm_nomad_boots,  itm_mail_boots, itm_khergit_guard_helmet, itm_lamellar_gauntlets, itm_leather_gloves,  itm_sword_khergit_3, itm_tab_shield_small_round_c, itm_khergit_bow, itm_khergit_arrows],  knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3|knows_power_draw_4, 0x000000043000318b54b246b7094dc39c00000000001d31270000000000000000, khergit_face_middle_2],
  ["knight_3_2", "Tonju Noyan",  "Tonju", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser, itm_nomad_vest,   itm_lamellar_armor, itm_hide_boots,  itm_mail_boots, itm_khergit_cavalry_helmet, itm_lamellar_gauntlets, itm_leather_gloves, itm_khergit_sword_two_handed_b,  itm_tab_shield_small_round_b, itm_khergit_bow, itm_khergit_arrows], knight_attrib_2,wp(160),knight_skills_2|knows_power_draw_4, 0x0000000c280461004929b334ad632aa200000000001e05120000000000000000, khergit_face_old_2],
  ["knight_3_3", "Belir Noyan",  "Belir", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser, itm_nomad_robe, itm_lamellar_armor,itm_nomad_boots,  itm_splinted_leather_greaves,  itm_khergit_guard_helmet, itm_lamellar_gauntlets, itm_fighting_pick,  itm_tab_shield_small_round_c, itm_khergit_bow, itm_khergit_arrows],  knight_attrib_3,wp(190),knight_skills_3|knows_trainer_5|knows_power_draw_4, 0x0000000e880062c53b0a6e4994ae272a00000000001db4e10000000000000000, khergit_face_older_2],
  ["knight_3_4", "Asugan Noyan", "Asugan", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser, itm_lamellar_vest_khergit,  itm_khergit_elite_armor, itm_hide_boots,  itm_splinted_greaves,   itm_khergit_cavalry_helmet, itm_lamellar_gauntlets, itm_khergit_sword_two_handed_b, itm_lance,  itm_tab_shield_small_round_c],  knight_attrib_4,wp(220),knight_skills_4|knows_power_draw_4, 0x0000000c23085386391b5ac72a96d95c00000000001e37230000000000000000, khergit_face_older_2],
  ["knight_3_5", "Brula Noyan",  "Brula", tf_hero, 0, reserved,  fac_kingdom_3, [itm_warhorse_steppe, itm_ragged_outfit,  itm_lamellar_vest_khergit, itm_hide_boots,  itm_mail_boots, itm_khergit_guard_helmet, itm_lamellar_gauntlets, itm_sword_khergit_3, itm_lance, itm_tab_shield_small_round_c],  knight_attrib_5,wp(250),knight_skills_5|knows_power_draw_4, 0x0000000efe0051ca4b377b4964b6eb6500000000001f696c0000000000000000, khergit_face_older_2],
  ["knight_3_6", "Imirza Noyan", "Imirza", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser, itm_tribal_warrior_outfit,itm_hide_boots, itm_splinted_leather_greaves,  itm_khergit_cavalry_helmet,  itm_lamellar_gauntlets, itm_sword_khergit_4,itm_lance,  itm_tab_shield_small_round_b], knight_attrib_1,wp(130),knight_skills_1|knows_power_draw_4, 0x00000006f600418b54b246b7094dc31a00000000001d37270000000000000000, khergit_face_middle_2],
  ["knight_3_7", "Urumuda Noyan","Urumuda", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser,  itm_leather_vest,itm_leather_boots, itm_hide_boots, itm_skullcap, itm_khergit_guard_helmet, itm_lamellar_gauntlets,  itm_sword_khergit_3, itm_tab_shield_small_round_b], knight_attrib_2,wp(160),knight_skills_2|knows_power_draw_4, 0x0000000bdd00510a44be2d14d370c65c00000000001ed6df0000000000000000, khergit_face_old_2],
  ["knight_3_8", "Kramuk Noyan", "Kramuk", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser,  itm_nomad_vest, itm_lamellar_armor, itm_woolen_hose, itm_splinted_greaves, itm_khergit_cavalry_helmet, itm_lamellar_gauntlets,   itm_great_bardiche,  itm_tab_shield_small_round_c],  knight_attrib_3,wp(190),knight_skills_3|knows_power_draw_4, 0x0000000abc00518b5af4ab4b9c8e596400000000001dc76d0000000000000000, khergit_face_older_2],
  ["knight_3_9", "Chaurka Noyan","Chaurka", tf_hero, 0, reserved,  fac_kingdom_3, [itm_hunter,  itm_nomad_robe, itm_lamellar_vest_khergit,  itm_leather_boots, itm_splinted_leather_greaves,  itm_khergit_guard_helmet, itm_lamellar_gauntlets,  itm_khergit_sword_two_handed_b,  itm_tab_shield_small_round_c],  knight_attrib_4,wp(220),knight_skills_4|knows_power_draw_4, 0x0000000a180441c921a30ea68b54971500000000001e54db0000000000000000, khergit_face_older_2],
  ["knight_3_10", "Sebula Noyan","Sebula", tf_hero, 0, reserved,  fac_kingdom_3, [itm_warhorse_steppe,  itm_lamellar_vest_khergit, itm_lamellar_armor, itm_hide_boots, itm_mail_chausses,  itm_khergit_guard_helmet, itm_lamellar_gauntlets,  itm_sword_khergit_4, itm_khergit_sword_two_handed_b,  itm_tab_shield_small_round_c], knight_attrib_5,wp(250),knight_skills_5|knows_trainer_6|knows_power_draw_4, 0x0000000a3b00418c5b36c686d920a76100000000001c436f0000000000000000, khergit_face_older_2],
  ["knight_3_11", "Tulug Noyan", "Tulug", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser, itm_leather_vest, itm_studded_leather_coat, itm_nomad_boots, itm_mail_boots,  itm_khergit_cavalry_helmet,  itm_leather_gloves, itm_sword_khergit_4,  itm_tab_shield_small_round_b, itm_khergit_bow, itm_khergit_arrows],  knight_attrib_1,wp(150),knight_skills_1|knows_power_draw_4, 0x00000007d100534b44962d14d370c65c00000000001ed6df0000000000000000, khergit_face_middle_2],
  ["knight_3_12", "Nasugei Noyan", "Nasugei", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser, itm_nomad_vest, itm_lamellar_armor, itm_hide_boots, itm_mail_boots,  itm_khergit_guard_helmet,  itm_leather_gloves, itm_sword_khergit_3,  itm_tab_shield_small_round_b], knight_attrib_2,wp(190),knight_skills_2|knows_power_draw_4, 0x0000000bf400610c5b33d3c9258edb6c00000000001eb96d0000000000000000, khergit_face_old_2],
  ["knight_3_13", "Urubay Noyan","Urubay", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser, itm_nomad_robe,  itm_lamellar_vest_khergit, itm_nomad_boots, itm_splinted_leather_greaves,  itm_khergit_cavalry_helmet, itm_lamellar_gauntlets, itm_fighting_pick,  itm_tab_shield_small_round_c, itm_khergit_bow, itm_flat_headed_arrows],  knight_attrib_3,wp(200),knight_skills_3|knows_trainer_3|knows_power_draw_4, 0x0000000bfd0061c65b6eb33b25d2591d00000000001f58eb0000000000000000, khergit_face_older_2],
  ["knight_3_14", "Hugu Noyan",  "Hugu", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser,  itm_lamellar_vest_khergit, itm_hide_boots, itm_splinted_greaves, itm_khergit_guard_helmet, itm_lamellar_gauntlets, itm_shortened_military_scythe,  itm_tab_shield_small_round_c, itm_khergit_bow, itm_flat_headed_arrows],  knight_attrib_4,wp(300),knight_skills_4|knows_trainer_6|knows_power_draw_4, 0x0000000b6900514144be2d14d370c65c00000000001ed6df0000000000000000, khergit_face_older_2],
  ["knight_3_15", "Tansugai Noyan", "Tansugai", tf_hero, 0, reserved,  fac_kingdom_3, [itm_warhorse_steppe,   itm_ragged_outfit, itm_lamellar_vest_khergit, itm_hide_boots, itm_mail_boots,  itm_khergit_cavalry_helmet, itm_sword_khergit_4, itm_khergit_sword_two_handed_b, itm_tab_shield_small_round_c],  knight_attrib_5,wp(240),knight_skills_5|knows_trainer_4|knows_power_draw_4, 0x0000000c360c524b6454465b59b9d93500000000001ea4860000000000000000, khergit_face_older_2],
  ["knight_3_16", "Tirida Noyan","Tirida", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser, itm_tribal_warrior_outfit,  itm_khergit_elite_armor,  itm_hide_boots,  itm_splinted_leather_greaves,  itm_khergit_guard_helmet, itm_leather_gloves,   itm_khergit_sword_two_handed_a,  itm_lance, itm_tab_shield_small_round_b, itm_khergit_bow, itm_khergit_arrows],  knight_attrib_1,wp(120),knight_skills_1|knows_power_draw_4, 0x0000000c350c418438ab85b75c61b8d300000000001d21530000000000000000, khergit_face_middle_2],
  ["knight_3_17", "Ulusamai Noyan", "Ulusamai", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser,  itm_leather_vest, itm_lamellar_vest_khergit, itm_leather_boots, itm_mail_boots, itm_khergit_guard_helmet, itm_leather_gloves,   itm_great_bardiche, itm_tab_shield_small_round_c, itm_khergit_bow, itm_khergit_arrows],  knight_attrib_2,wp(150),knight_skills_2|knows_power_draw_4, 0x0000000c3c0821c647264ab6e68dc4d500000000001e42590000000000000000, khergit_face_old_2],
  ["knight_3_18", "Karaban Noyan", "Karaban", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser,   itm_nomad_vest, itm_khergit_elite_armor, itm_hide_boots, itm_splinted_greaves,  itm_khergit_guard_helmet, itm_scale_gauntlets,   itm_war_axe, itm_tab_shield_small_round_c, itm_lance,  itm_khergit_bow, itm_khergit_arrows],   knight_attrib_3,wp(180),knight_skills_3|knows_trainer_4|knows_power_draw_4, 0x0000000c0810500347ae7acd0d3ad74a00000000001e289a0000000000000000, khergit_face_older_2],
  ["knight_3_19", "Akadan Noyan","Akadan", tf_hero, 0, reserved,  fac_kingdom_3, [itm_hunter,   itm_nomad_robe, itm_lamellar_vest_khergit, itm_leather_boots, itm_splinted_leather_greaves,  itm_khergit_cavalry_helmet, itm_lamellar_gauntlets, itm_sword_khergit_4, itm_shortened_military_scythe, itm_tab_shield_small_round_c],  knight_attrib_4,wp(210),knight_skills_4|knows_trainer_5|knows_power_draw_4, 0x0000000c1500510528f50d52d20b152300000000001d66db0000000000000000, khergit_face_older_2],
  ["knight_3_20", "Dundush Noyan","Dundush", tf_hero, 0, reserved,  fac_kingdom_3, [itm_warhorse_steppe, itm_lamellar_vest, itm_khergit_elite_armor, itm_hide_boots, itm_mail_chausses, itm_khergit_guard_helmet, itm_scale_gauntlets, itm_khergit_sword_two_handed_a, itm_tab_shield_small_round_c, itm_lance, itm_khergit_bow, itm_flat_headed_arrows],  knight_attrib_5,wp(240),knight_skills_5|knows_power_draw_4, 0x0000000f7800620d66b76edd5cd5eb6e00000000001f691e0000000000000000, khergit_face_older_2],

  ["knight_4_1", "Jarl Aedin", "Aedin", tf_hero, 0, reserved,  fac_kingdom_4, [itm_rich_outfit,  itm_banded_armor,   itm_woolen_hose,  itm_mail_boots,  itm_nordic_huscarl_helmet, itm_mail_mittens, itm_great_axe, itm_tab_shield_round_d, itm_throwing_axes], knight_attrib_1,wp(130),knight_skills_1, 0x0000000c13002254340eb1d91159392d00000000001eb75a0000000000000000, nord_face_middle_2],
  ["knight_4_2", "Jarl Irya", "Irya", tf_hero, 0, reserved,  fac_kingdom_4, [ itm_short_tunic,  itm_banded_armor, itm_blue_hose,  itm_splinted_greaves,  itm_nordic_warlord_helmet, itm_scale_gauntlets, itm_one_handed_battle_axe_c,  itm_tab_shield_round_d, itm_throwing_axes],  knight_attrib_2,wp(160),knight_skills_2|knows_trainer_3, 0x0000000c1610218368e29744e9a5985b00000000001db2a10000000000000000, nord_face_old_2],
  ["knight_4_3", "Jarl Olaf", "Olaf", tf_hero, 0, reserved,  fac_kingdom_4, [itm_warhorse_b, itm_rich_outfit,  itm_heraldic_mail_with_tabard,   itm_nomad_boots,  itm_mail_chausses, itm_scale_gauntlets,   itm_nordic_warlord_helmet,   itm_great_axe, itm_tab_shield_round_e, itm_throwing_axes],  knight_attrib_3,wp(190),knight_skills_3, 0x0000000c03040289245a314b744b30a400000000001eb2a90000000000000000, nord_face_older_2],
  ["knight_4_4", "Jarl Reamald", "Reamald", tf_hero, 0, reserved,  fac_kingdom_4, [itm_hunter,   itm_leather_vest,   itm_banded_armor,   itm_woolen_hose,  itm_mail_boots, itm_scale_gauntlets,  itm_nordic_huscarl_helmet, itm_fighting_pick, itm_tab_shield_round_e, itm_throwing_axes],  knight_attrib_4,wp(210),knight_skills_4, 0x0000000c3f1001ca3d6955b26a8939a300000000001e39b60000000000000000, nord_face_older_2],
  ["knight_4_5", "Jarl Turya", "Turya", tf_hero, 0, reserved,  fac_kingdom_4, [itm_courser_b,  itm_fur_coat,   itm_heraldic_mail_with_surcoat,   itm_leather_boots,  itm_splinted_leather_greaves,  itm_scale_gauntlets, itm_nordic_huscarl_helmet, itm_bastard_sword_b, itm_tab_shield_round_e, itm_throwing_axes, itm_throwing_axes], knight_attrib_5,wp(250),knight_skills_5, 0x0000000ff508330546dc4a59422d450c00000000001e51340000000000000000, nord_face_older_2],
  ["knight_4_6", "Jarl Gundur", "Gundur", tf_hero, 0, reserved,  fac_kingdom_4, [   itm_nomad_robe,   itm_banded_armor,  itm_nomad_boots,  itm_mail_chausses,   itm_nordic_warlord_helmet, itm_mail_mittens,   itm_war_axe, itm_tab_shield_round_d],   knight_attrib_1,wp(130),knight_skills_1, 0x00000005b00011813d9b6d4a92ada53500000000001cc1180000000000000000, nord_face_middle_2],
  ["knight_4_7", "Jarl Harald", "Harald", tf_hero, 0, reserved,  fac_kingdom_4, [  itm_fur_coat,   itm_studded_leather_coat,   itm_nomad_boots,  itm_mail_boots,  itm_nordic_warlord_helmet, itm_mail_mittens,   itm_sword_viking_3, itm_shortened_military_scythe,  itm_tab_shield_round_d],   knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x00000006690002873d9b6d4a92ada53500000000001cc1180000000000000000, nord_face_old_2],
  ["knight_4_8", "Jarl Knudarr", "Knudarr", tf_hero, 0, reserved,  fac_kingdom_4, [itm_courser_b, itm_rich_outfit,  itm_mail_and_plate,   itm_woolen_hose,  itm_mail_chausses,   itm_segmented_helmet, itm_scale_gauntlets, itm_war_axe,  itm_tab_shield_round_e, itm_throwing_axes],   knight_attrib_3,wp(190),knight_skills_3, 0x0000000f830051c53b026e4994ae272a00000000001db4e10000000000000000, nord_face_older_2],
  ["knight_4_9", "Jarl Haeda", "Haeda", tf_hero, 0, reserved,  fac_kingdom_4, [itm_warhorse_b, itm_nomad_robe,   itm_haubergeon, itm_blue_hose,  itm_mail_boots,  itm_guard_helmet, itm_scale_gauntlets, itm_bodkin_arrows, itm_long_bow,   itm_one_handed_battle_axe_c,  itm_tab_shield_round_e],  knight_attrib_4,wp(220),knight_skills_4|knows_trainer_5|knows_power_draw_4, 0x00000000080c54c1345bd21349b1b67300000000001c90c80000000000000000, nord_face_older_2],
  ["knight_4_10", "Jarl Turegor", "Turegor", tf_hero, 0, reserved,  fac_kingdom_4, [itm_hunter,   itm_courtly_outfit,   itm_coat_of_plates,   itm_nomad_boots,  itm_splinted_greaves, itm_scale_gauntlets,  itm_winged_great_helmet,itm_great_axe, itm_tab_shield_round_e],  knight_attrib_5,wp(250),knight_skills_5|knows_trainer_6, 0x000000084b0002063d9b6d4a92ada53500000000001cc1180000000000000000, nord_face_older_2],
  ["knight_4_11", "Jarl Logarson", "Logarson", tf_hero, 0, reserved,  fac_kingdom_4, [ itm_rich_outfit,  itm_banded_armor,   itm_woolen_hose,  itm_mail_boots,  itm_nordic_helmet,  itm_mail_mittens,  itm_great_bardiche, itm_tab_shield_round_d], knight_attrib_1,wp(140),knight_skills_1, 0x000000002d100005471d4ae69ccacb1d00000000001dca550000000000000000, nord_face_middle_2],
  ["knight_4_12", "Jarl Aeric", "Aeric", tf_hero, 0, reserved,  fac_kingdom_4, [ itm_short_tunic,  itm_banded_armor, itm_blue_hose,  itm_splinted_greaves,  itm_nordic_huscarl_helmet,  itm_mail_mittens,  itm_one_handed_battle_axe_c,  itm_tab_shield_round_d],  knight_attrib_2,wp(200),knight_skills_2, 0x0000000b9500020824936cc51cb5bb2500000000001dd4d80000000000000000, nord_face_old_2],
  ["knight_4_13", "Jarl Faarn", "Faarn", tf_hero, 0, reserved,  fac_kingdom_4, [itm_warhorse_b, itm_rich_outfit,  itm_heraldic_mail_with_tabard,   itm_nomad_boots,  itm_mail_chausses, itm_scale_gauntlets,   itm_nordic_warlord_helmet,   itm_war_axe, itm_tab_shield_round_e],  knight_attrib_3,wp(250),knight_skills_3|knows_trainer_3, 0x0000000a300012c439233512e287391d00000000001db7200000000000000000, nord_face_older_2],
  ["knight_4_14", "Jarl Bulba", "Bulba", tf_hero, 0, reserved,  fac_kingdom_4, [itm_courser_b, itm_leather_vest,   itm_banded_armor,   itm_woolen_hose,  itm_mail_boots,  itm_nordic_helmet, itm_scale_gauntlets, itm_fighting_pick, itm_tab_shield_round_e, itm_throwing_axes],  knight_attrib_4,wp(200),knight_skills_4, 0x0000000c0700414f2cb6aa36ea50a69d00000000001dc55c0000000000000000, nord_face_older_2],
  ["knight_4_15", "Jarl Rayeck", "Rayeck", tf_hero, 0, reserved,  fac_kingdom_4, [itm_hunter,   itm_leather_jacket,   itm_heraldic_mail_with_tabard,   itm_leather_boots, itm_scale_gauntlets,  itm_splinted_leather_greaves,  itm_nordic_huscarl_helmet, itm_shortened_military_scythe, itm_tab_shield_round_e], knight_attrib_5,wp(290),knight_skills_5|knows_trainer_6, 0x0000000d920801831715d1aa9221372300000000001ec6630000000000000000, nord_face_older_2],
  ["knight_4_16", "Jarl Dirigun", "Dirigun", tf_hero, 0, reserved,  fac_kingdom_4, [   itm_nomad_robe,   itm_banded_armor,  itm_nomad_boots,  itm_mail_chausses,   itm_nordic_huscarl_helmet, itm_mail_mittens,   itm_war_axe, itm_tab_shield_round_d, itm_throwing_axes],   knight_attrib_1,wp(120),knight_skills_1, 0x000000099700124239233512e287391d00000000001db7200000000000000000, nord_face_middle_2],
  ["knight_4_17", "Jarl Marayirr", "Marayirr", tf_hero, 0, reserved,  fac_kingdom_4, [  itm_fur_coat,   itm_banded_armor,   itm_nomad_boots,  itm_mail_boots,  itm_nordic_warlord_helmet, itm_mail_mittens,   itm_sword_viking_3,  itm_tab_shield_round_d, itm_throwing_axes],   knight_attrib_2,wp(150),knight_skills_2|knows_trainer_4, 0x0000000c2f0442036d232a2324b5b81400000000001e55630000000000000000, nord_face_old_2],
  ["knight_4_18", "Jarl Gearth", "Gearth", tf_hero, 0, reserved,  fac_kingdom_4, [itm_courser_b, itm_rich_outfit,  itm_mail_and_plate,   itm_woolen_hose,  itm_mail_chausses,   itm_segmented_helmet, itm_scale_gauntlets, itm_sword_viking_3, itm_shortened_military_scythe,  itm_tab_shield_round_d],   knight_attrib_3,wp(180),knight_skills_3, 0x0000000c0d00118866e22e3d9735a72600000000001eacad0000000000000000, nord_face_older_2],
  ["knight_4_19", "Jarl Surdun", "Surdun", tf_hero, 0, reserved,  fac_kingdom_4, [itm_warhorse_b, itm_nomad_robe,   itm_haubergeon, itm_blue_hose,  itm_mail_boots,  itm_guard_helmet, itm_scale_gauntlets,   itm_one_handed_battle_axe_c,  itm_tab_shield_round_e, itm_throwing_axes],  knight_attrib_4,wp(210),knight_skills_4|knows_trainer_5, 0x0000000c0308225124e26d4a6295965a00000000001d23e40000000000000000, nord_face_older_2],
  ["knight_4_20", "Jarl Gerlad", "Gerlad", tf_hero, 0, reserved,  fac_kingdom_4, [itm_hunter,   itm_courtly_outfit,   itm_coat_of_plates,   itm_nomad_boots,  itm_splinted_greaves, itm_scale_gauntlets,  itm_winged_great_helmet,itm_great_axe, itm_tab_shield_round_e, itm_throwing_axes],  knight_attrib_5,wp(240),knight_skills_5, 0x0000000f630052813b6bb36de5d6eb7400000000001dd72c0000000000000000, nord_face_older_2],

  ["knight_5_1", "Count Matheas", "Matheas", tf_hero, 0, reserved,  fac_kingdom_5, [itm_hunter,   itm_tabard,   itm_heraldic_mail_with_surcoat,       itm_leather_boots,    itm_mail_boots,    itm_guard_helmet, itm_leather_gloves,     itm_fighting_pick,   itm_tab_shield_heater_c],     knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x0000000a1b0c00483adcbaa5ac9a34a200000000001ca2d40000000000000000, rhodok_face_middle_2],
  ["knight_5_2", "Count Gutlans", "Gutlans", tf_hero, 0, reserved,  fac_kingdom_5, [itm_courser_g,    itm_red_gambeson,       itm_heraldic_mail_with_tabard,    itm_leather_boots,    itm_mail_boots,    itm_nasal_helmet, itm_leather_gloves,      itm_military_pick,  itm_sword_two_handed_a,   itm_tab_shield_heater_c],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
  ["knight_5_3", "Count Laruqen", "Laruqen", tf_hero, 0, reserved,  fac_kingdom_5, [itm_hunter,     itm_short_tunic,  itm_mail_and_plate,     itm_nomad_boots,      itm_splinted_leather_greaves,  itm_kettle_hat, itm_gauntlets, itm_shortened_military_scythe,  itm_tab_shield_heater_d],    knight_attrib_3,wp(190),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_5_4", "Count Raichs", "Raichs", tf_hero, 0, reserved,  fac_kingdom_5, [itm_hunter,     itm_leather_jacket,     itm_brigandine_red,       itm_woolen_hose,      itm_splinted_greaves,    itm_flat_topped_helmet, itm_gauntlets, itm_bastard_sword_a,    itm_tab_shield_heater_d],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
  ["knight_5_5", "Count Reland", "Reland", tf_hero, 0, reserved,  fac_kingdom_5, [itm_hunter,     itm_rich_outfit,  itm_heraldic_mail_with_tabard,     itm_leather_boots,    itm_mail_boots,    itm_great_helmet, itm_gauntlets, itm_shortened_military_scythe,  itm_tab_shield_heater_d], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_5_6", "Count Tarchias", "Tarchias", tf_hero, 0, reserved,  fac_kingdom_5, [itm_sumpter_horse,    itm_ragged_outfit,      itm_heraldic_mail_with_tabard,       itm_woolen_hose,      itm_splinted_greaves, itm_gauntlets,   itm_skullcap,     itm_sword_two_handed_b,   itm_tab_shield_heater_c],    knight_attrib_1,wp(130),knight_skills_1, 0x000000001100000648d24d36cd964b1d00000000001e2dac0000000000000000, rhodok_face_middle_2],
  ["knight_5_7", "Count Gharmall", "Gharmall", tf_hero, 0, reserved,  fac_kingdom_5, [itm_hunter,     itm_coarse_tunic,       itm_heraldic_mail_with_surcoat,   itm_leather_boots,    itm_mail_chausses,  itm_gauntlets,      itm_nasal_helmet,       itm_bastard_sword_a,    itm_tab_shield_heater_c],     knight_attrib_2,wp(160),knight_skills_2, 0x0000000c3a0455c443d46e4c8b91291a00000000001ca51b0000000000000000, rhodok_face_old_2],
  ["knight_5_8", "Count Talbar", "Talbar", tf_hero, 0, reserved,  fac_kingdom_5, [itm_hunter, itm_courtly_outfit,     itm_heraldic_mail_with_tabard,    itm_woolen_hose,      itm_mail_boots,    itm_nasal_helmet,  itm_gauntlets,      itm_military_pick, itm_sword_two_handed_b,  itm_tab_shield_heater_c],    knight_attrib_3,wp(190),knight_skills_3|knows_trainer_3, 0x0000000c2c0844d42914d19b2369b4ea00000000001e331b0000000000000000, rhodok_face_older_2],
  ["knight_5_9", "Count Rimusk", "Rimusk", tf_hero, 0, reserved,  fac_kingdom_5, [itm_warhorse_g,     itm_leather_jacket,     itm_heraldic_mail_with_tabard,   itm_leather_boots,    itm_splinted_leather_greaves,       itm_kettle_hat, itm_gauntlets,   itm_great_bardiche,   itm_tab_shield_heater_d],   knight_attrib_4,wp(220),knight_skills_4|knows_trainer_6, 0x00000000420430c32331b5551c4724a100000000001e39a40000000000000000, rhodok_face_older_2],
  ["knight_5_10", "Count Falsevor", "Falsevor", tf_hero, 0, reserved,  fac_kingdom_5, [itm_warhorse_g,     itm_rich_outfit,  itm_heraldic_mail_with_tabard,     itm_blue_hose,  itm_mail_chausses,       itm_great_helmet, itm_gauntlets,       itm_bastard_sword_a,   itm_tab_shield_heater_d],  knight_attrib_5,wp(250),knight_skills_5|knows_trainer_4, 0x00000008e20011063d9b6d4a92ada53500000000001cc1180000000000000000, rhodok_face_older_2],
  ["knight_5_11", "Count Etrosq", "Etrosq", tf_hero, 0, reserved,  fac_kingdom_5, [itm_hunter,     itm_tabard,       itm_heraldic_mail_with_surcoat,       itm_leather_boots,    itm_mail_boots,    itm_skullcap,  itm_leather_gloves,    itm_fighting_pick,   itm_tab_shield_heater_c],     knight_attrib_1,wp(130),knight_skills_1, 0x0000000c170c14874752adb6eb3228d500000000001c955c0000000000000000, rhodok_face_middle_2],
  ["knight_5_12", "Count Kurnias", "Kurnias", tf_hero, 0, reserved,  fac_kingdom_5, [itm_courser_g,    itm_red_gambeson,       itm_heraldic_mail_with_tabard,    itm_leather_boots,    itm_mail_boots,    itm_nasal_helmet,  itm_leather_gloves,      itm_military_pick,   itm_tab_shield_heater_c],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_5, 0x0000000c080c13d056ec8da85e3126ed00000000001d4ce60000000000000000, rhodok_face_old_2],
  ["knight_5_13", "Count Tellrog", "Tellrog", tf_hero, 0, reserved,  fac_kingdom_5, [itm_hunter,     itm_short_tunic,  itm_mail_and_plate,     itm_nomad_boots,      itm_splinted_leather_greaves,  itm_winged_great_helmet, itm_gauntlets,       itm_sword_two_handed_a,  itm_tab_shield_heater_d],    knight_attrib_3,wp(190),knight_skills_3, 0x0000000cbf10100562a4954ae731588a00000000001d6b530000000000000000, rhodok_face_older_2],
  ["knight_5_14", "Count Tribidan", "Tribidan", tf_hero, 0, reserved,  fac_kingdom_5, [itm_hunter,     itm_leather_jacket,     itm_brigandine_red,       itm_woolen_hose,      itm_splinted_greaves,    itm_flat_topped_helmet, itm_gauntlets, itm_bastard_sword_a,    itm_tab_shield_heater_d],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000c330805823baa77556c4e331a00000000001cb9110000000000000000, rhodok_face_older_2],
  ["knight_5_15", "Count Gerluchs", "Gerluchs", tf_hero, 0, reserved,  fac_kingdom_5, [itm_hunter,     itm_rich_outfit,  itm_heraldic_mail_with_tabard,     itm_leather_boots,    itm_mail_boots,    itm_great_helmet, itm_gauntlets,       itm_sword_two_handed_a,  itm_tab_shield_heater_d], knight_attrib_5,wp(250),knight_skills_5, 0x0000000d51000106370c4d4732b536de00000000001db9280000000000000000, rhodok_face_older_2],
  ["knight_5_16", "Count Fudreim", "Fudreim", tf_hero, 0, reserved,  fac_kingdom_5, [itm_sumpter_horse,    itm_ragged_outfit,      itm_heraldic_mail_with_tabard,       itm_woolen_hose,      itm_splinted_greaves,    itm_guard_helmet, itm_leather_gloves,     itm_fighting_pick,   itm_tab_shield_heater_c],    knight_attrib_1,wp(120),knight_skills_1, 0x0000000c06046151435b5122a37756a400000000001c46e50000000000000000, rhodok_face_middle_2],
  ["knight_5_17", "Count Nealcha", "Nealcha", tf_hero, 0, reserved,  fac_kingdom_5, [itm_hunter,     itm_coarse_tunic,       itm_heraldic_mail_with_surcoat,   itm_leather_boots,    itm_mail_chausses,       itm_nasal_helmet,  itm_leather_gloves,      itm_bastard_sword_a,    itm_tab_shield_heater_c],     knight_attrib_2,wp(150),knight_skills_2, 0x0000000c081001d3465c89a6a452356300000000001cda550000000000000000, rhodok_face_old_2],
  ["knight_5_18", "Count Fraichin", "Fraichin", tf_hero, 0, reserved,  fac_kingdom_5, [itm_hunter, itm_courtly_outfit,     itm_heraldic_mail_with_tabard,    itm_woolen_hose,      itm_mail_boots,    itm_nasal_helmet, itm_gauntlets,       itm_military_pick,   itm_tab_shield_heater_d],    knight_attrib_3,wp(180),knight_skills_3, 0x0000000a3d0c13c3452aa967276dc95c00000000001dad350000000000000000, rhodok_face_older_2],
  ["knight_5_19", "Count Trimbau", "Trimbau", tf_hero, 0, reserved,  fac_kingdom_5, [itm_warhorse_g,     itm_leather_jacket,     itm_heraldic_mail_with_tabard,   itm_leather_boots,    itm_splinted_leather_greaves,       itm_kettle_hat, itm_gauntlets,   itm_fighting_pick,  itm_sword_two_handed_a, itm_tab_shield_heater_d],   knight_attrib_4,wp(210),knight_skills_4|knows_trainer_5, 0x0000000038043194092ab4b2d9adb44c00000000001e072c0000000000000000, rhodok_face_older_2],
  ["knight_5_20", "Count Reichsin", "Reichsin", tf_hero, 0, reserved,  fac_kingdom_5, [itm_warhorse_g,     itm_rich_outfit,  itm_heraldic_mail_with_tabard,     itm_blue_hose,  itm_mail_chausses,       itm_great_helmet, itm_gauntlets,       itm_bastard_sword_b,   itm_tab_shield_heater_d],  knight_attrib_5,wp(240),knight_skills_5|knows_trainer_6, 0x000000003600420515a865b45c64d64c00000000001d544b0000000000000000, rhodok_face_older_2],

  ["knight_6_1", "Emir Uqais", "Uqais", tf_hero, 0, reserved,  fac_kingdom_6, [itm_arabian_horse_a,   itm_mamluke_mail,          itm_sarranid_boots_c,    itm_mail_boots,    itm_sarranid_warrior_cap, itm_leather_gloves,    itm_heavy_lance, itm_sarranid_cavalry_sword,   itm_tab_shield_small_round_c],     knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x00000000600c2084486195383349eae500000000001d16a30000000000000000, rhodok_face_middle_2],
  ["knight_6_2", "Emir Hamezan", "Hamezan", tf_hero, 0, reserved,  fac_kingdom_6, [itm_arabian_horse_b,    itm_sarranid_elite_armor,       itm_sarranid_boots_c,    itm_mail_boots,    itm_sarranid_warrior_cap, itm_leather_gloves,   itm_lance,   itm_military_pick,  itm_sword_two_handed_a,   itm_tab_shield_small_round_c],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x00000001380825d444cb68b92b8d3b1d00000000001dd71e0000000000000000, rhodok_face_old_2],
  ["knight_6_3", "Emir Atis", "Atis", tf_hero, 0, reserved,  fac_kingdom_6, [itm_arabian_horse_a,     itm_mamluke_mail,       itm_nomad_boots,      itm_sarranid_warrior_cap,  itm_shortened_military_scythe, itm_lamellar_gauntlets,  itm_tab_shield_small_round_c],    knight_attrib_3,wp(190),knight_skills_3, 0x000000002208428579723147247ad4e500000000001f14d40000000000000000, rhodok_face_older_2],
  ["knight_6_4", "Emir Nuwas", "Nuwas", tf_hero, 0, reserved,  fac_kingdom_6, [itm_hunter,     itm_sarranid_mail_shirt,            itm_sarranid_boots_c,          itm_sarranid_mail_coif,  itm_sarranid_cavalry_sword, itm_lamellar_gauntlets, itm_lance,   itm_tab_shield_small_round_c],    knight_attrib_4,wp(220),knight_skills_4, 0x00000009bf084285050caa7d285be51a00000000001d11010000000000000000, rhodok_face_older_2],
  ["knight_6_5", "Emir Mundhalir", "Mundhalir", tf_hero, 0, reserved,  fac_kingdom_6, [itm_arabian_horse_b,     itm_sarranid_cavalry_robe,       itm_sarranid_boots_c,    itm_sarranid_veiled_helmet,  itm_shortened_military_scythe,  itm_tab_shield_small_round_c], knight_attrib_5,wp(250),knight_skills_5, 0x000000002a084003330175aae175da9c00000000001e02150000000000000000, rhodok_face_older_2],
  ["knight_6_6", "Emir Ghanawa", "Ghanawa", tf_hero, 0, reserved,  fac_kingdom_6, [itm_arabian_horse_a,    itm_sarranid_elite_armor,            itm_sarranid_boots_c,      itm_splinted_greaves,    itm_sarranid_helmet1, itm_lance,      itm_sarranid_cavalry_sword,   itm_tab_shield_small_round_c],    knight_attrib_1,wp(130),knight_skills_1, 0x00000001830043834733294c89b128e200000000001259510000000000000000, rhodok_face_middle_2],
  ["knight_6_7", "Emir Nuam", "Nuam", tf_hero, 0, reserved,  fac_kingdom_6, [itm_arabian_horse_b,     itm_sarranid_mail_shirt,          itm_sarranid_boots_c,          itm_sarranid_mail_coif,       itm_sarranid_cavalry_sword,  itm_lamellar_gauntlets,  itm_tab_shield_small_round_c],     knight_attrib_2,wp(160),knight_skills_2, 0x0000000cbf10434020504bbbda9135d500000000001f62380000000000000000, rhodok_face_old_2],
  ["knight_6_8", "Emir Dhiyul", "Dhiyul", tf_hero, 0, reserved,  fac_kingdom_6, [itm_arabian_horse_a, itm_mamluke_mail,         itm_sarranid_boots_c,      itm_mail_boots,    itm_sarranid_helmet1,        itm_military_pick, itm_lance,  itm_sarranid_cavalry_sword,  itm_tab_shield_small_round_c],    knight_attrib_3,wp(190),knight_skills_3|knows_trainer_3, 0x0000000190044003336dcd3ca2cacae300000000001f47640000000000000000, rhodok_face_older_2],
  ["knight_6_9", "Emir Lakhem", "Lakhem", tf_hero, 0, reserved,  fac_kingdom_6, [itm_warhorse_sarranid,     itm_sarranid_mail_shirt,        itm_sarranid_boots_c,    itm_sarranid_helmet1, itm_lamellar_gauntlets,   itm_lance, itm_tab_shield_small_round_c],   knight_attrib_4,wp(220),knight_skills_4|knows_trainer_6, 0x0000000dde0040c4549dd5ca6f4dd56500000000001e291b0000000000000000, rhodok_face_older_2],
  ["knight_6_10", "Emir Ghulassen", "Ghulassen", tf_hero, 0, reserved,  fac_kingdom_6, [itm_warhorse_sarranid,     itm_sarranid_cavalry_robe,       itm_sarranid_boots_c,  itm_sarranid_boots_c,       itm_sarranid_helmet1, itm_lamellar_gauntlets,   itm_lance,     itm_sarranid_cavalry_sword,   itm_tab_shield_small_round_c],  knight_attrib_5,wp(250),knight_skills_5|knows_trainer_4, 0x00000001a60441c66ce99256b4ad4b3300000000001d392c0000000000000000, rhodok_face_older_2],
  ["knight_6_11", "Emir Azadun", "Azadun", tf_hero, 0, reserved,  fac_kingdom_6, [itm_arabian_horse_a,     itm_sarranid_mail_shirt,              itm_sarranid_boots_c,    itm_sarranid_boots_c,    itm_sarranid_mail_coif,  itm_leather_gloves,    itm_fighting_pick,   itm_tab_shield_small_round_c],     knight_attrib_1,wp(130),knight_skills_1, 0x0000000fff08134726c28af8dc96e4da00000000001e541d0000000000000000, rhodok_face_middle_2],
  ["knight_6_12", "Emir Quryas", "Quryas", tf_hero, 0, reserved,  fac_kingdom_6, [itm_courser,    itm_mamluke_mail,           itm_sarranid_boots_c,    itm_mail_boots,    itm_sarranid_helmet1, itm_lance,    itm_military_pick,   itm_tab_shield_small_round_c],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_5, 0x0000000035104084635b74ba5491a7a400000000001e46d60000000000000000, rhodok_face_old_2],
  ["knight_6_13", "Emir Amdar", "Amdar", tf_hero, 0, reserved,  fac_kingdom_6, [itm_arabian_horse_b,     itm_sarranid_mail_shirt,       itm_sarranid_boots_c,      itm_sarranid_boots_c,  itm_sarranid_helmet1,   itm_lamellar_gauntlets,     itm_sword_two_handed_a,  itm_tab_shield_small_round_c],    knight_attrib_3,wp(190),knight_skills_3, 0x00000000001021435b734d4ad94eba9400000000001eb8eb0000000000000000, rhodok_face_older_2],
  ["knight_6_14", "Emir Hiwan", "Hiwan", tf_hero, 0, reserved,  fac_kingdom_6, [itm_arabian_horse_b,     itm_sarranid_elite_armor,       itm_sarranid_boots_c,      itm_sarranid_boots_c,    itm_sarranid_mail_coif, itm_lance,  itm_sarranid_cavalry_sword,    itm_tab_shield_small_round_c],    knight_attrib_4,wp(220),knight_skills_4, 0x000000000c0c45c63a5b921ac22db8e200000000001cca530000000000000000, rhodok_face_older_2],
  ["knight_6_15", "Emir Muhnir", "Muhnir", tf_hero, 0, reserved,  fac_kingdom_6, [itm_hunter,     itm_sarranid_mail_shirt,       itm_sarranid_boots_c,    itm_mail_boots,    itm_sarranid_helmet1,  itm_sword_two_handed_a,  itm_tab_shield_small_round_c], knight_attrib_5,wp(250),knight_skills_5, 0x000000001b0c4185369a6938cecde95600000000001f25210000000000000000, rhodok_face_older_2],
  
  ["knight_6_16", "Emir Ayyam", "Ayyam", tf_hero, 0, reserved,  fac_kingdom_6, [itm_arabian_horse_a,    itm_mamluke_mail,             itm_sarranid_boots_c,      itm_sarranid_boots_c,    itm_sarranid_mail_coif, itm_leather_gloves,  itm_lance,    itm_fighting_pick,   itm_tab_shield_small_round_c],    knight_attrib_1,wp(120),knight_skills_1, 0x00000007770841c80a01e1c5eb51ffff00000000001f12d80000000000000000, rhodok_face_middle_2],
  ["knight_6_17", "Emir Raddoun", "Raddoun", tf_hero, 0, reserved,  fac_kingdom_6, [itm_arabian_horse_b,     itm_sarranid_mail_shirt,          itm_sarranid_boots_c,    itm_sarranid_boots_c,       itm_sarranid_mail_coif,  itm_leather_gloves,      itm_sarranid_cavalry_sword,    itm_tab_shield_small_round_c],     knight_attrib_2,wp(150),knight_skills_2, 0x000000007f0462c32419f47a1aba8bcf00000000001e7e090000000000000000, rhodok_face_old_2],
  ["knight_6_18", "Emir Tilimsan", "Tilimsan", tf_hero, 0, reserved,  fac_kingdom_6, [itm_arabian_horse_a,  itm_sarranid_elite_armor,     itm_sarranid_boots_c,      itm_mail_boots,    itm_sarranid_helmet1,  itm_lance,       itm_military_pick,   itm_tab_shield_small_round_c],    knight_attrib_3,wp(180),knight_skills_3, 0x000000003410410070d975caac91aca500000000001c27530000000000000000, rhodok_face_older_2],
  ["knight_6_19", "Emir Dhashwal", "Dhashwal", tf_hero, 0, reserved,  fac_kingdom_6, [itm_warhorse_sarranid,     itm_sarranid_mail_shirt,        itm_sarranid_boots_c,    itm_sarranid_boots_c,       itm_sarranid_mail_coif, itm_lamellar_gauntlets,   itm_fighting_pick,  itm_sword_two_handed_a, itm_tab_shield_small_round_c],   knight_attrib_4,wp(210),knight_skills_4|knows_trainer_5, 0x000000018a08618016ac36bc8b6e4a9900000000001dd45d0000000000000000, rhodok_face_older_2],
  ["knight_6_20", "Emir Biliya", "Biliya", tf_hero, 0, reserved,  fac_kingdom_6, [itm_warhorse_sarranid,     itm_sarranid_cavalry_robe,       itm_sarranid_boots_c,  itm_sarranid_boots_c,       itm_sarranid_veiled_helmet,   itm_lance,      itm_sarranid_cavalry_sword,   itm_tab_shield_small_round_c],  knight_attrib_5,wp(240),knight_skills_5|knows_trainer_6, 0x00000001bd0040c0281a899ac956b94b00000000001ec8910000000000000000, rhodok_face_older_2],
  


  
  ["kingdom_1_pretender",  "Lady Isolla of Suno",       "Isolla",  tf_hero|tf_female, 0,reserved,  fac_kingdom_1,[(itm_heavy_charger,imod_champion),   itm_rich_outfit,  itm_blue_hose,      itm_iron_greaves,         itm_mail_shirt,      (itm_sword_medieval_c_small,imod_masterwork),      (itm_tab_shield_small_round_c,imod_reinforced),       itm_bascinet],          lord_attrib,wp(220),knight_skills_5|knows_trainer_5, 0x00000000ef00000237dc71b90c31631200000000001e371b0000000000000000],
#claims pre-salic descent

  ["kingdom_2_pretender",  "Prince Valdym the Bastard", "Valdym",  tf_hero, 0,reserved,  fac_kingdom_2,[(itm_heavy_warhorse_w,imod_champion),    itm_courtly_outfit,      itm_leather_boots,              itm_mail_chausses,              itm_lamellar_armor,       (itm_military_pick,imodbit_balanced),      (itm_tab_shield_heater_b,imod_reinforced),      itm_flat_topped_helmet],    lord_attrib,wp(220),knight_skills_5|knows_trainer_5, 0x00000000200412142452ed631b30365c00000000001c94e80000000000000000, vaegir_face_middle_2],
#had his patrimony falsified

  ["kingdom_3_pretender",  "Dustum Khan",               "Dustum",  tf_hero, 0,reserved,  fac_kingdom_3,[(itm_heavy_warhorse_steppe,imod_champion),   itm_nomad_robe,             itm_leather_boots,              itm_splinted_greaves,           itm_khergit_guard_armor,         (itm_sword_khergit_2,imod_masterwork),              (itm_tab_shield_small_round_c,imod_reinforced),       itm_segmented_helmet],      lord_attrib,wp(220),knight_skills_5|knows_trainer_5, 0x000000065504310b30d556b51238f66100000000001c256d0000000000000000, khergit_face_middle_2],
#of the family

  ["kingdom_4_pretender",  "Lethwin Far-Seeker",   "Lethwin",  tf_hero, 0,reserved,  fac_kingdom_4,[(itm_heavy_warhorse_b,imod_champion),    itm_tabard,    itm_leather_boots,              itm_mail_boots,                 itm_brigandine_red,           (itm_sword_medieval_c,imod_masterwork),           (itm_tab_shield_heater_cav_a,imod_reinforced),    itm_kettle_hat],            lord_attrib,wp(220),knight_skills_5|knows_trainer_5, 0x00000004340c01841d89949529a6776a00000000001c910a0000000000000000, nord_face_young_2],
#dispossessed and wronged

  ["kingdom_5_pretender",  "Lord Kastor of Veluca",  "Kastor",  tf_hero, 0,reserved,  fac_kingdom_5,[(itm_heavy_warhorse_g,imod_champion),  itm_nobleman_outfit,             itm_leather_boots,              itm_splinted_leather_greaves,   itm_mail_hauberk,           (itm_sword_medieval_c,imod_masterwork),         (itm_tab_shield_heater_d,imod_reinforced),        itm_spiked_helmet],         lord_attrib,wp(220),knight_skills_5|knows_trainer_5, 0x0000000bed1031051da9abc49ecce25e00000000001e98680000000000000000, rhodok_face_old_2],
#republican

  ["kingdom_6_pretender",  "Arwa the Pearled One",       "Arwa",  tf_hero|tf_female, 0,reserved,  fac_kingdom_6,[(itm_heavy_warhorse_sarranid,imod_champion), itm_sarranid_mail_shirt, itm_sarranid_boots_c, (itm_sarranid_cavalry_sword,imod_masterwork),      (itm_tab_shield_small_round_c,imod_reinforced)],          lord_attrib,wp(220),knight_skills_5|knows_trainer_5, 0x000000050b003004072d51c293a9a70b00000000001dd6a90000000000000000],

##  ["kingdom_1_lord_a", "Kingdom 1 Lord A", "Kingdom 1 Lord A", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_b", "Kingdom 1 Lord B", "Kingdom 1 Lord B", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_c", "Kingdom 1 Lord C", "Kingdom 1 Lord C", tf_hero, 0,reserved,  fac_kingdom_3,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_d", "Kingdom 1 Lord D", "Kingdom 1 Lord D", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_e", "Kingdom 1 Lord E", "Kingdom 1 Lord E", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_f", "Kingdom 1 Lord F", "Kingdom 1 Lord F", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_g", "Kingdom 1 Lord G", "Kingdom 1 Lord G", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_h", "Kingdom 1 Lord H", "Kingdom 1 Lord H", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_i", "Kingdom 1 Lord I", "Kingdom 1 Lord I", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_j", "Kingdom 1 Lord J", "Kingdom 1 Lord J", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_k", "Kingdom 1 Lord K", "Kingdom 1 Lord K", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_l", "Kingdom 1 Lord L", "Kingdom 1 Lord L", tf_hero, 0,reserved,  fac_kingdom_3,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_m", "Kingdom 1 Lord M", "Kingdom 1 Lord M", tf_hero, 0,reserved,  fac_kingdom_3,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_n", "Kingdom 1 Lord N", "Kingdom 1 Lord N", tf_hero, 0,reserved,  fac_kingdom_3,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],



#  ["town_1_ruler_a", "King Harlaus",  "King Harlaus",  tf_hero, scn_town_1_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse,itm_courtly_outfit,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000010908101e36db44b75b6dd],
#  ["town_2_ruler_a", "Duke Taugard",  "Duke Taugard",  tf_hero, scn_town_2_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse,itm_courtly_outfit,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000000310401e06db86375f6da],
#  ["town_3_ruler_a", "Count Grimar",  "Count Grimar",  tf_hero, scn_town_3_castle|entry(9),reserved, fac_swadians,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000004430301e46136eb75bc0a],
#  ["town_4_ruler_a", "Count Haxalye", "Count Haxalye", tf_hero, scn_town_4_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000010918701e77136e905bc0e
#  ["town_5_ruler_a", "Count Belicha", "Count Belicha", tf_hero, scn_town_5_castle|entry(9),reserved, fac_swadians,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000000421c801e7713729c5b8ce],
#  ["town_6_ruler_a", "Count Nourbis", "Count Nourbis", tf_hero, scn_town_6_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000000c640501e371b72bcdb724],
#  ["town_7_ruler_a", "Count Rhudolg", "Count Rhudolg", tf_hero, scn_town_7_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000000c710201fa51b7286db721],
 
#  ["town_8_ruler_b", "King Yaroglek", "King_yaroglek", tf_hero, scn_town_8_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000000128801f294ca6d66d555],
#  ["town_9_ruler_b", "Count Aolbrug", "Count_Aolbrug", tf_hero, scn_town_9_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000004234401f26a271c8d38ea],
#  ["town_10_ruler_b","Count Rasevas", "Count_Rasevas", tf_hero, scn_town_10_castle|entry(9),reserved, fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000001032c201f38e269372471c],
#  ["town_11_ruler_b","Count Leomir",  "Count_Leomir",  tf_hero, scn_town_11_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000000c538001f55148936d3895],
#  ["town_12_ruler_b","Count Haelbrad","Count_Haelbrad",tf_hero, scn_town_12_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000000410c701f38598ac8aaaab],
#  ["town_13_ruler_b","Count Mira",    "Count_Mira",    tf_hero, scn_town_13_castle|entry(9),reserved, fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000004204401f390c515555594],
#  ["town_14_ruler_b","Count Camechaw","Count_Camechaw",tf_hero, scn_town_14_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000008318101f390c515555594],

##  ["kingdom_2_lord_a", "Kingdom 2 Lord A", "Kingdom 2 Lord A", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_b", "Kingdom 2 Lord B", "Kingdom 2 Lord B", tf_hero, 0,reserved,  fac_kingdom_11,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_c", "Kingdom 2 Lord C", "Kingdom 2 Lord C", tf_hero, 0,reserved,  fac_kingdom_12,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_d", "Kingdom 2 Lord D", "Kingdom 2 Lord D", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_e", "Kingdom 2 Lord E", "Kingdom 2 Lord E", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_f", "Kingdom 2 Lord F", "Kingdom 2 Lord F", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_g", "Kingdom 2 Lord G", "Kingdom 2 Lord G", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_h", "Kingdom 2 Lord H", "Kingdom 2 Lord H", tf_hero, 0,reserved,  fac_kingdom_11,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_i", "Kingdom 2 Lord I", "Kingdom 2 Lord I", tf_hero, 0,reserved,  fac_kingdom_11,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_j", "Kingdom 2 Lord J", "Kingdom 2 Lord J", tf_hero, 0,reserved,  fac_kingdom_11,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_k", "Kingdom 2 Lord K", "Kingdom 2 Lord K", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_l", "Kingdom 2 Lord L", "Kingdom 2 Lord L", tf_hero, 0,reserved,  fac_kingdom_12,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_m", "Kingdom 2 Lord M", "Kingdom 2 Lord M", tf_hero, 0,reserved,  fac_kingdom_12,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_n", "Kingdom 2 Lord N", "Kingdom 2 Lord N", tf_hero, 0,reserved,  fac_kingdom_12,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],



#Royal family members

  ["knight_1_1_wife","Error - knight_1_1_wife should not appear in game","knight_1_1_wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_commoners, [itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],

  #Swadian ladies - eight mothers, eight daughters, four sisters
  ["kingdom_1_lady_1","Lady Anna","Anna",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [          itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_1_lady_2","Lady Nelda","Nelda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
  ["knight_1_lady_3","Lady Bela","Bela",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,  [       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
  ["knight_1_lady_4","Lady Elina","Elina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,  [       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
  ["kingdom_l_lady_5","Lady Constanis","Constanis",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_6","Lady Vera","Vera",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
  ["kingdom_1_lady_7","Lady Auberina","Auberina",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_8","Lady Tibal","Tibal",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
  ["kingdom_1_lady_9","Lady Magar","Magar",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_10","Lady Thedosa","Thedosa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
  ["kingdom_1_lady_11","Lady Melisar","Melisar",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_12","Lady Irena","Irena",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
  ["kingdom_l_lady_13","Lady Philenna","Philenna",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_14","Lady Sonadel","Sonadel",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
  ["kingdom_1_lady_15","Lady Boadila","Boadila",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_16","Lady Elys","Elys",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],
  ["kingdom_1_lady_17","Lady Johana","Johana",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
  ["kingdom_1_lady_18","Lady Bernatys","Bernatys",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
  ["kingdom_1_lady_19","Lady Enricata","Enricata",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_1_lady_20","Lady Gaeta","Gaeta",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],
  
  #Vaegir ladies
  ["kingdom_2_lady_1","Lady Junitha","Junitha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_2","Lady Katia","Katia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_3","Lady Seomis","Seomis",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_4","Lady Drina","Drina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_lady_5","Lady Nesha","Nesha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_6","Lady Tabath","Tabath",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_7","Lady Pelaeka","Pelaeka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_8","Lady Haris","Haris",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_lady_9","Lady Vayen","Vayen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_10","Lady Joaka","Joaka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_11","Lady Tejina","Tejina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_12","Lady Olekseia","Olekseia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [      itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_lady_13","Lady Myntha","Myntha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_14","Lady Akilina","Akilina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_15","Lady Sepana","Sepana",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_16","Lady Iarina","Iarina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_lady_17","Lady Sihavan","Sihavan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_18","Lady Erenchina","Erenchina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [  itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_19","Lady Tamar","Tamar",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_20","Lady Valka","Valka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [itm_green_dress,   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],


  ["kingdom_3_lady_1","Lady Borge","Borge",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_1],
  ["kingdom_3_lady_2","Lady Tuan","Tuan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_green_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["kingdom_3_lady_3","Lady Mahraz","Mahraz",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [itm_red_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_2],
  ["kingdom_3_lady_4","Lady Ayasu","Ayasu",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_red_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
  ["kingdom_3_lady_5","Lady Ravin","Ravin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_green_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["kingdom_3_lady_6","Lady Ruha","Ruha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_green_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["kingdom_3_lady_7","Lady Chedina","Chedina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_3_lady_8","Lady Kefra","Kefra",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_3_lady_9","Lady Nirvaz","Nirvaz",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001940c3006019c925165d1129b00000000001d13240000000000000000],
  ["kingdom_3_lady_10","Lady Dulua","Dulua",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["kingdom_3_lady_11","Lady Selik","Selik",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000019b083005389591941379b8d100000000001e63150000000000000000],
  ["kingdom_3_lady_12","Lady Thalatha","Thalatha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
  ["kingdom_3_lady_13","Lady Yasreen","Yasreen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["kingdom_3_lady_14","Lady Nadha","Nadha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_1],
  ["kingdom_3_lady_15","Lady Zenur","Zenur",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_2],
  ["kingdom_3_lady_16","Lady Arjis","Zenur",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001ad003001628c54b05d2e48b200000000001d56e60000000000000000],
  ["kingdom_3_lady_17","Lady Atjahan", "Atjahan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001a700300265cb6db15d6db6da00000000001f82180000000000000000],
  ["kingdom_3_lady_18","Lady Qutala","Qutala",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["kingdom_3_lady_19","Lady Hindal","Hindal",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_3_lady_20","Lady Mechet","Mechet",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
  
  
  
  ["kingdom_4_lady_1","Lady Jadeth","Jadeth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_4_lady_2","Lady Miar","Miar",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_4_lady_3","Lady Dria","Dria",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress, itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_4_lady_4","Lady Glunde","Glunde",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_4_lady_5","Lady Loeka","Loeka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_4_lady_6","Lady Bryn","Bryn",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_4_lady_7","Lady Eir","Eir",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["knight_4_2b_daughter_1","Lady Thera","Thera",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_4_lady_9","Lady Hild","Hild",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,  itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["knight_4_2c_wife_1","Lady Endegrid","Endegrid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_4_lady_11","Lady Herjasa","Herjasa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["knight_4_2c_daughter","Lady Svipul","Svipul",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["knight_4_1b_wife","Lady Ingunn","Ingunn",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_4_lady_14","Lady Kaeteli","Kaeteli",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["knight_4_1b_daughter","Lady Eilif","Eilif",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["knight_4_2b_daughter_2","Lady Gudrun","Gudrun",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_4_lady_17","Lady Bergit","Bergit",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["knight_4_2c_wife_2","Lady Aesa","Aesa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["knight_4_1c_daughter","Lady Alfrun","Alfrun",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_4_lady_20","Lady Afrid","Afrid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],


  ["kingdom_5_lady_1","Lady Brina","Brina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_5_lady_2","Lady Aliena","Aliena",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_5_lady_3","Lady Aneth","Aneth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_lady_4","Lady Reada","Reada",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_5_5_wife","Lady Saraten","Saraten",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_5_2b_wife_1","Lady Baotheia","Baotheia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [itm_lady_dress_green,     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000bf0400035913aa236b4d975a00000000001eb69c0000000000000000],
  ["kingdom_5_1c_daughter_1","Lady Eleandra","Eleandra",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_2c_daughter_1","Lady Meraced","Meraced",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_5_1c_wife_1","Lady Adelisa","Adelisa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_5_2c_wife_1","Lady Calantina","Calantina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_5_1c_daughter_2","Lady Forbesa","Forbesa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_2c_daughter_2","Lady Claudora","Claudora",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_5_1b_wife","Lady Anais","Anais",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_5_2b_wife_2","Lady Miraeia","Miraeia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_5_1c_daughter_3","Lady Agasia","Agasia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_lady_16","Lady Geneiava","Geneiava",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_5_1c_wife_2","Lady Gwenael","Gwenael",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_5_2c_wife_2","Lady Ysueth","Ysueth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_5_1c_daughter_4","Lady Ellian","Ellian",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_lady_20","Lady Timethi","Timethi",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  
#Sarranid ladies
  ["kingdom_6_lady_1","Lady Rayma","Rayma",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,  itm_sarranid_head_cloth,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_6_lady_2","Lady Thanaikha","Thanaikha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
  ["kingdom_6_lady_3","Lady Sulaha","Sulaha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,  [itm_sarranid_lady_dress,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
  ["kingdom_6_lady_4","Lady Shatha","Shatha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,  [itm_sarranid_lady_dress,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
  ["kingdom_6_lady_5","Lady Bawthan","Bawthan",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_6","Lady Mahayl","Mahayl",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
  ["kingdom_6_lady_7","Lady Isna","Isna",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_8","Lady Siyafan","Siyafan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
  ["kingdom_6_lady_9","Lady Ifar","Ifar",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_10","Lady Yasmin","Yasmin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
  ["kingdom_6_lady_11","Lady Dula","Dula",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_12","Lady Ruwa","Ruwa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
  ["kingdom_6_lady_13","Lady Luqa","Luqa",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_14","Lady Zandina","Zandina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
  ["kingdom_6_lady_15","Lady Lulya","Lulya",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_16","Lady Zahara","Zahara",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],
  ["kingdom_6_lady_17","Lady Safiya","Safiya",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
  ["kingdom_6_lady_18","Lady Khalisa","Khalisa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
  ["kingdom_6_lady_19","Lady Janab","Janab",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_6_lady_20","Lady Sur","Sur",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],



  
#  ["kingdom_11_lord_daughter","kingdom_11_lord_daughter","kingdom_11_lord_daughter",tf_hero|tf_female,0,reserved,fac_kingdom_10,  [ itm_lady_dress_blue ,   itm_turret_hat_blue,    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008300701c08d34a450ce43],
#  ["kingdom_13_lord_daughter","kingdom_13_lord_daughter","kingdom_13_lord_daughter",tf_hero|tf_female,0,reserved,fac_kingdom_10,  [ itm_lady_dress_green,   itm_turret_hat_green,   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008000401db10a45b41d6d8],
##  ["kingdom_1_lady_a","kingdom_1_lady_a","kingdom_1_lady_a",tf_hero|tf_female,0,reserved,fac_kingdom_1, [   itm_lady_dress_blue ,   itm_turret_hat_blue,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008500201d8ad93708e4694],
##  ["kingdom_1_lady_b","kingdom_1_lady_b","kingdom_1_lady_b",tf_hero|tf_female,0,reserved,fac_kingdom_1, [   itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000004000101c3ae68e0e944ac],
##  ["kingdom_2_lady_a","Kingdom 2 Lady a","Kingdom 2 Lady a",tf_hero|tf_female,0,reserved,fac_kingdom_2, [               itm_lady_dress_green,   itm_turret_hat_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008100501d8ad93708e4694],
##  ["kingdom_2_lady_b","Kingdom 2 Lady b","Kingdom 2 Lady b",tf_hero|tf_female,0,reserved,fac_kingdom_2, [               itm_lady_dress_blue ,   itm_turret_hat_blue,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000004000401d8ad93708e4694],
##  ["kingdom_3_lady_a","Kingdom 3 Lady a","Kingdom 3 Lady a",tf_hero|tf_female,0,reserved,fac_kingdom_3, [               itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000010500301d8ad93708e4694],
##
##  ["kingdom_3_lady_b","Kingdom 3 Lady b","Kingdom 3 Lady b",tf_hero|tf_female,0,reserved,fac_kingdom_3,  [                         itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000000100601d8b08d76d14a24],
##  ["kingdom_4_lady_a","Kingdom 4 Lady a","Kingdom 4 Lady a",tf_hero|tf_female,0,reserved,fac_kingdom_4,  [                         itm_lady_dress_green,   itm_turret_hat_green,   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000010500601d8ad93708e4694],
##  ["kingdom_4_lady_b","Kingdom 4 Lady b","Kingdom 4 Lady b",tf_hero|tf_female,0,reserved,fac_kingdom_4,  [                         itm_lady_dress_blue ,   itm_turret_hat_blue,    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008500201d8ad93708e4694],

  ["heroes_end", "{!}heroes end", "{!}heroes end", tf_hero, 0,reserved,  fac_neutral,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000008318101f390c515555594],
#Merchants                                                                              AT                      SILAH                   ZIRH                        BOT                         Head_wear
##  ["merchant_1", "merchant_1_F", "merchant_1_F",tf_hero|tf_female,  0,0, fac_kingdom_1,[itm_courser,            itm_fighting_axe,       itm_leather_jerkin,         itm_leather_boots,          itm_straw_hat],              def_attrib|level(15),wp(100),knows_inventory_management_10|knows_looting_10, 0x000000000008200201e54c137a940c91],
##  ["merchant_2", "merchant_2", "merchant_2", tf_hero,               0,0, fac_kingdom_2,[itm_saddle_horse,       itm_arming_sword,       itm_light_leather,          itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10|knows_looting_10, 0x000000000000000601db6db6db6db6db],
##  ["merchant_3", "merchant_3", "merchant_3", tf_hero,               0,0, fac_kingdom_3,[itm_courser,            itm_nordic_sword,       itm_leather_jerkin,         itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10|knows_looting_10, 0x000000000008100701db6db6db6db6db],
##  ["merchant_4", "merchant_4_F", "merchant_4_F",tf_hero|tf_female,  0,0, fac_kingdom_4,[itm_saddle_horse,       itm_falchion,           itm_light_leather,          itm_blue_hose,                              ],              def_attrib|level(15),wp(100),knows_inventory_management_10|knows_looting_10, 0x000000000010500401e54c137a945c91],
##  ["merchant_5", "merchant_5", "merchant_5", tf_hero,               0,0, fac_kingdom_5,[itm_saddle_horse,       itm_sword,              itm_ragged_outfit,          itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10|knows_looting_10, 0x000000000008038001e54c135a945c91],
##  ["merchant_6", "merchant_6", "merchant_6", tf_hero,               0,0, fac_kingdom_1,[itm_saddle_horse,      itm_scimitar,           itm_leather_jerkin,         itm_leather_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10|knows_looting_10, 0x000000000000248e01e54c1b5a945c91],
##  ["merchant_7", "merchant_7_F", "merchant_7_F",tf_hero|tf_female,  0,0, fac_kingdom_2,[itm_hunter,            itm_arming_sword,       itm_padded_leather,         itm_blue_hose,                              ],              def_attrib|level(15),wp(100),knows_inventory_management_10|knows_looting_10, 0x000000000004200601c98ad39c97557a],
##  ["merchant_8", "merchant_8", "merchant_8", tf_hero,               0,0, fac_kingdom_3,[itm_saddle_horse,      itm_nordic_sword,       itm_light_leather,          itm_leather_boots,          itm_woolen_hood],              def_attrib|level(15),wp(100),knows_inventory_management_10|knows_looting_10, 0x00000000001095ce01d6aad3a497557a],
##  ["merchant_9", "merchant_9", "merchant_9", tf_hero,               0,0, fac_kingdom_4,[itm_saddle_horse,      itm_sword,              itm_padded_leather,         itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10|knows_looting_10, 0x000000000010519601ec26ae99898697],
##  ["merchant_10","merchant_10","merchant_10",tf_hero,               0,0, fac_merchants,[itm_hunter,             itm_bastard_sword,      itm_light_leather,          itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10|knows_looting_10, 0x00000000000884c401f6837d3294e28a],
##  ["merchant_11","merchant_11","merchant_11",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_sword,              itm_leather_jacket,         itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10|knows_looting_10, 0x00000000000c450501e289dd2c692694],
##  ["merchant_12","merchant_12","merchant_12",tf_hero,               0,0, fac_merchants,[itm_hunter,             itm_falchion,           itm_leather_jerkin,         itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10|knows_looting_10, 0x00000000000c660a01e5af3cb2763401],
##  ["merchant_13","merchant_13","merchant_13",tf_hero,               0,0, fac_merchants,[itm_sumpter_horse,      itm_nordic_sword,       itm_padded_leather,         itm_leather_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10|knows_looting_10, 0x00000000001001d601ec912a89e4d534],
##  ["merchant_14","merchant_14","merchant_14",tf_hero,               0,0, fac_merchants,[itm_courser,            itm_bastard_sword,      itm_light_leather,          itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10|knows_looting_10, 0x000000000004335601ea2c04a8b6a394],
##  ["merchant_15","merchant_15","merchant_15",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_sword,              itm_padded_leather,         itm_woolen_hose,            itm_fur_hat],              def_attrib|level(15),wp(100),knows_inventory_management_10|knows_looting_10, 0x000000000008358e01dbf27b6436089d],
##  ["merchant_16","merchant_16_F","merchant_16_F",tf_hero|tf_female, 0,0, fac_merchants,[itm_hunter,             itm_bastard_sword,      itm_light_leather,          itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10|knows_looting_10, 0x00000000000c300101db0b9921494add],
##  ["merchant_17","merchant_17","merchant_17",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_sword,              itm_leather_jacket,         itm_blue_hose,                              ],              def_attrib|level(15),wp(100),knows_inventory_management_10|knows_looting_10, 0x000000000008740f01e945c360976a0a],
##  ["merchant_18","merchant_18","merchant_18",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_nordic_sword,       itm_padded_leather,         itm_leather_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10|knows_looting_10, 0x000000000008020c01fc2db3b4c97685],
##  ["merchant_19","merchant_19","merchant_19",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_falchion,           itm_leather_jerkin,         itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10|knows_looting_10, 0x000000000008118301f02af91892725b],
##  ["merchant_20","merchant_20_F","merchant_20_F",tf_hero|tf_female, 0,0, fac_merchants,[itm_courser,            itm_arming_sword,       itm_padded_leather,         itm_leather_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10|knows_looting_10, 0x000000000010500401f6837d27688212],

  
#Seneschals
  ["town_1_seneschal", "{!}Town 1 Seneschal", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["town_2_seneschal", "{!}Town 2 Seneschal", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_padded_leather,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["town_3_seneschal", "{!}Town 3 Seneschal", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["town_4_seneschal", "{!}Town 4 Seneschal", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["town_5_seneschal", "{!}Town 5 Seneschal", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000000249101e7898999ac54c6],
  ["town_6_seneschal", "{!}Town 6 Seneschal", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_red_gambeson,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000010360b01cef8b57553d34e],
  ["town_7_seneschal", "{!}Town 7 Seneschal", "{!}Town7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000000018101f9487aa831dce4],
  ["town_8_seneschal", "{!}Town 8 Seneschal", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_red_gambeson,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["town_9_seneschal", "{!}Town 9 Seneschal", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["town_10_seneschal", "{!}Town 10 Seneschal", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000010230c01ef41badb50465e],
  ["town_11_seneschal", "{!}Town 11 Seneschal", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jacket,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["town_12_seneschal", "{!}Town 12 Seneschal", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["town_13_seneschal", "{!}Town 13 Seneschal", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["town_14_seneschal", "{!}Town 14 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_15_seneschal", "{!}Town 15 Seneschal", "{!}Town 15 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_16_seneschal", "{!}Town 16 Seneschal", "{!}Town 16 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_17_seneschal", "{!}Town17 Seneschal", "{!}Town 17 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_18_seneschal", "{!}Town 18 Seneschal", "{!}Town 18 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_19_seneschal", "{!}Town 19 Seneschal", "{!}Town 19 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_20_seneschal", "{!}Town 20 Seneschal", "{!}Town 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_21_seneschal", "{!}Town 21 Seneschal", "{!}Town 21 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_22_seneschal", "{!}Town 22 Seneschal", "{!}Town 22 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ## CC
  ["town_23_seneschal", "{!}Town 23 Seneschal", "{!}Town 23 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000000018101f9487aa831dce4],
  ["town_24_seneschal", "{!}Town 24 Seneschal", "{!}Town 24 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_25_seneschal", "{!}Town 25 Seneschal", "{!}Town 25 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jacket,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["town_26_seneschal", "{!}Town 26 Seneschal", "{!}Town 26 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_27_seneschal", "{!}Town 27 Seneschal", "{!}Town 27 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["town_28_seneschal", "{!}Town 28 Seneschal", "{!}Town 28 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_29_seneschal", "{!}Town 29 Seneschal", "{!}Town 29 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ## CC
  
  ["castle_1_seneschal", "{!}Castle 1 Seneschal", "{!}Castle 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x000000000010360b01cef8b57553d34e],
  ["castle_2_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_3_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_4_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_5_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_6_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_7_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_blue_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_8_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_9_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_10_seneschal", "{!}Castle 10 Seneschal", "{!}Castle 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_11_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_12_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_13_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_14_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_15_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_16_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_17_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_blue_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_18_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_19_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_20_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_21_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_22_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_23_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_24_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_25_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_26_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_27_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_blue_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_28_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_29_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_30_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_31_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_32_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_33_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_34_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_35_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_36_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_37_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_blue_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_38_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_39_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_40_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_41_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_42_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_43_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_44_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_45_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_46_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_47_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_48_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
## CC
  ["castle_49_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_50_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_51_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_52_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_53_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_54_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_55_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_56_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_57_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_58_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_59_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_60_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_61_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_62_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_63_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_64_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_65_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_66_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_67_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_68_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_69_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_70_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_71_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_72_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_73_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_74_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
## CC

#Arena Masters
  ["town_1_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_1_arena|entry(52),reserved,   fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_2_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_2_arena|entry(52),reserved,   fac_commoners,[itm_linen_tunic,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_3_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_3_arena|entry(52),reserved,   fac_commoners,[itm_nomad_armor,       itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_4_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_4_arena|entry(52),reserved,   fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_5_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_5_arena|entry(52),reserved,   fac_commoners,[itm_linen_tunic,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_6_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_6_arena|entry(52),reserved,   fac_commoners,[itm_leather_jerkin,    itm_leather_boots], def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_7_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_7_arena|entry(52),reserved,   fac_commoners,[itm_padded_leather,    itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_8_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_8_arena|entry(52),reserved,   fac_commoners,[itm_linen_tunic,       itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_9_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_9_arena|entry(52),reserved,   fac_commoners,[itm_padded_leather,    itm_leather_boots], def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_10_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_10_arena|entry(52),reserved,  fac_commoners,[itm_nomad_armor,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_11_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_11_arena|entry(52),reserved,  fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_12_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_12_arena|entry(52),reserved,  fac_commoners,[itm_leather_jerkin,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_13_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_13_arena|entry(52),reserved,  fac_commoners,[itm_coarse_tunic,      itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_14_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_14_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_15_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_15_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_16_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_16_arena|entry(52),reserved,  fac_commoners,[itm_fur_coat,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_17_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_17_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_18_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_18_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_19_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_19_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_20_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_20_arena|entry(52),reserved,  fac_commoners,[itm_fur_coat,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_21_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_21_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_22_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_22_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ## CC
  ["town_23_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_23_arena|entry(52),reserved,   fac_commoners,[itm_padded_leather,    itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_24_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_24_arena|entry(52),reserved,  fac_commoners,[itm_fur_coat,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_25_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_25_arena|entry(52),reserved,  fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_26_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_26_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_27_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_27_arena|entry(52),reserved,  fac_commoners,[itm_leather_jerkin,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_28_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_28_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_29_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_29_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ## CC
  
# Underground 

##  ["town_1_crook","Town 1 Crook","Town 1 Crook",tf_hero,                0,0, fac_neutral,[itm_linen_tunic,        itm_leather_boots       ],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, 0x000000000004428401f46e44a27144e3],
##  ["town_2_crook","Town 2 Crook","Town 2 Crook",tf_hero|tf_female,      0,0, fac_neutral,[itm_lady_dress_ruby,    itm_turret_hat_ruby     ],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, 0x000000000004300101c36db6db6db6db],
##  ["town_3_crook","Town 3 Crook","Town 3 Crook",tf_hero,                0,0, fac_neutral,[itm_leather_apron,      itm_hide_boots          ],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, 0x00000000000c530701f17944a25164e1],
##  ["town_4_crook","Town 4 Crook","Town 4 Crook",tf_hero,                0,0, fac_neutral,[itm_coarse_tunic,       itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, 0x00000000000c840501f36db6db7134db],
##  ["town_5_crook","Town 5 Crook","Town 5 Crook",tf_hero,                0,0, fac_neutral,[itm_red_gambeson,       itm_blue_hose           ],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, 0x00000000000c000601f36db6db7134db],
##  ["town_6_crook","Town 6 Crook","Town 6 Crook",tf_hero,                0,0, fac_neutral,[itm_coarse_tunic,       itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, 0x00000000000c10c801db6db6dd7598aa],
##  ["town_7_crook","Town 7 Crook","Town 7 Crook",tf_hero|tf_female,      0,0, fac_neutral,[itm_woolen_dress,       itm_woolen_hood         ],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, 0x000000000010214101de2f64db6db58d],
##  
##  ["town_8_crook","Town 8 Crook","Town 8 Crook",tf_hero,                0,0, fac_neutral,[itm_leather_jacket,     itm_leather_boots       ],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, 0x000000000010318401c96db4db6db58d],
##  ["town_9_crook","Town 9 Crook","Town 9 Crook",tf_hero,                0,0, fac_neutral,[itm_linen_tunic,        itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, 0x000000000008520501f16db4db6db58d],
##  ["town_10_crook","Town 10 Crook","Town 10 Crook",tf_hero,             0,0, fac_neutral,[itm_coarse_tunic,      itm_nomad_boots         ],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, 0x000000000008600701f35144db6db8a2],
##  ["town_11_crook","Town 11 Crook","Town 11 Crook",tf_hero|tf_female,   0,0, fac_neutral,[itm_blue_dress,        itm_wimple_with_veil    ],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, 0x000000000008408101f386c4db4dd514],
##  ["town_12_crook","Town 12 Crook","Town 12 Crook",tf_hero,             0,0, fac_neutral,[itm_coarse_tunic,      itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, 0x00000000000870c501f386c4f34dbaa1],
##  ["town_13_crook","Town 13 Crook","Town 13 Crook",tf_hero,             0,0, fac_neutral,[itm_blue_gambeson,     itm_nomad_boots         ],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, 0x00000000000c114901f245caf34dbaa1],
##  ["town_14_crook","Town 14 Crook","Town 14 Crook",tf_hero|tf_female,   0,0, fac_neutral,[itm_woolen_dress,      itm_turret_hat_ruby     ],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, 0x00000000001021c001f545a49b6eb2bc],

# Armor Merchants
  #arena_masters_end = zendar_armorer

  ["town_1_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,           itm_leather_boots   ],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_2_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,          itm_straw_hat       ],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, woman_face_1, woman_face_2],
  ["town_3_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_red,        itm_hide_boots      ],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_4_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_red_gambeson,         itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_5_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,          itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_6_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,       itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_7_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,       itm_blue_hose       ],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_8_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_leather,       itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_9_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_blue_gambeson,        itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_10_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_11_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,        itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_12_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_red_gambeson,         itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_13_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_14_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,         itm_headcloth       ],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, woman_face_1, woman_face_2],
  ["town_15_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_blue_gambeson,        itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_16_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,         itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_17_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_18_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,         itm_headcloth       ],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, woman_face_1, woman_face_2],
  ["town_19_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_blue_gambeson,        itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_20_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,         itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_21_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_22_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_sarranid_common_dress,         itm_sarranid_head_cloth       ],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, woman_face_1, woman_face_2],
  ## CC
  ["town_23_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,       itm_blue_hose       ],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_24_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,         itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_25_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,        itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_26_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,         itm_headcloth       ],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, woman_face_1, woman_face_2],
 ["town_27_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_red_gambeson,         itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_28_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_blue_gambeson,        itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_29_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ## CC
  
# Weapon merchants

  ["town_1_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,      itm_hide_boots,itm_straw_hat],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, woman_face_1, woman_face_2],
  ["town_2_weaponsmith", "Struga","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,     itm_nomad_boots],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_3_weaponsmith", "Dibus","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,   itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_4_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,            itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_5_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,   itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_6_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,      itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_7_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,            itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_8_weaponsmith", "Ganzo","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,     itm_wrapping_boots,itm_straw_hat],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, woman_face_1, woman_face_2],
  ["town_9_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,   itm_leather_boots],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_10_weaponsmith","Rabugti, the fletcher","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,     itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_11_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket,  itm_woolen_hose],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_12_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,           itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_13_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_red,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_14_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_blue,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_15_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket,  itm_woolen_hose],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_16_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,           itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_17_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_green,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_18_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_19_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket,  itm_sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_20_weaponsmith","Norskh, the shield collector","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,           itm_sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_21_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_green,     itm_sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_22_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,     itm_sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ## CC
  ["town_23_weaponsmith", "Qaelmas","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,            itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_24_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,           itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_25_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket,  itm_woolen_hose],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_26_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_27_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,           itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_28_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket,  itm_woolen_hose],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ["town_29_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_green,     itm_sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, mercenary_face_1, mercenary_face_2],
  ## CC
#Tavern keepers

  ["town_1_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_1_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_2_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_2_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_3_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_3_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,        itm_hide_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_4_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_4_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_5_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_5_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_hide_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_6_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_6_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,        itm_hide_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_7_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_7_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,        itm_leather_boots,      itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_8_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_8_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,      itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_9_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_9_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,        itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_10_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_10_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_hide_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_11_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_11_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_12_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_12_tavern|entry(9),0,  fac_commoners,[itm_leather_apron,       itm_hide_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_13_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_13_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_hide_boots,     itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_14_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_14_tavern|entry(9),0,  fac_commoners,[itm_shirt,               itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_15_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_15_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_16_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_16_tavern|entry(9),0,  fac_commoners,[itm_leather_apron,       itm_hide_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_17_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_17_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_hide_boots,     itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_18_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_18_tavern|entry(9),0,  fac_commoners,[itm_shirt,               itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_19_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_19_tavern|entry(9),0,  fac_commoners,[itm_sarranid_dress_a,        itm_sarranid_boots_a],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_20_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_20_tavern|entry(9),0,  fac_commoners,[itm_sarranid_cloth_robe,       itm_sarranid_boots_a],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_21_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_21_tavern|entry(9),0,  fac_commoners,[itm_sarranid_common_dress,        itm_sarranid_boots_a,     itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_22_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_22_tavern|entry(9),0,  fac_commoners,[itm_sarranid_cloth_robe_b,               itm_sarranid_boots_a],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ## CC
  ["town_23_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_23_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,        itm_leather_boots,      itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_24_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_24_tavern|entry(9),0,  fac_commoners,[itm_leather_apron,       itm_hide_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_25_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_25_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_26_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_26_tavern|entry(9),0,  fac_commoners,[itm_shirt,               itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_27_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_27_tavern|entry(9),0,  fac_commoners,[itm_leather_apron,       itm_hide_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_28_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_28_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_29_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_29_tavern|entry(9),0,  fac_commoners,[itm_sarranid_common_dress,        itm_sarranid_boots_a,     itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ## CC
#Goods Merchants

  ["town_1_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_1_store|entry(9),0, fac_commoners,     [itm_coarse_tunic,  itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_young_1, man_face_older_2],
  ["town_2_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_2_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_young_1, man_face_older_2],
  ["town_3_merchant", "Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_3_store|entry(9),0, fac_commoners,     [itm_dress,         itm_leather_boots,  itm_straw_hat   ],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, woman_face_1, woman_face_2],
  ["town_4_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_4_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_young_1, man_face_older_2],
  ["town_5_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_5_store|entry(9),0, fac_commoners,     [itm_nomad_armor,   itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_young_1, man_face_older_2],
  ["town_6_merchant", "Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_6_store|entry(9),0, fac_commoners,     [itm_woolen_dress,  itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_young_1, man_face_older_2],
  ["town_7_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_7_store|entry(9),0, fac_commoners,     [itm_leather_jerkin,itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_young_1, man_face_older_2],
  ["town_8_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_8_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_young_1, man_face_older_2],
  ["town_9_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_9_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_young_1, man_face_older_2],
  ["town_10_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_10_store|entry(9),0, fac_commoners,    [itm_leather_jerkin,itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_young_1, man_face_older_2],
  ["town_11_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_11_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_young_1, man_face_older_2],
  ["town_12_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_12_store|entry(9),0, fac_commoners,    [itm_woolen_dress,  itm_leather_boots,  itm_female_hood ],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, woman_face_1, woman_face_2],
  ["town_13_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_13_store|entry(9),0, fac_commoners,    [itm_dress,         itm_leather_boots,  itm_straw_hat   ],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, woman_face_1, woman_face_2],
  ["town_14_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_14_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_young_1, man_face_older_2],
  ["town_15_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_15_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_young_1, man_face_older_2],
  ["town_16_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_16_store|entry(9),0, fac_commoners,    [itm_woolen_dress,  itm_leather_boots,  itm_female_hood ],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, woman_face_1, woman_face_2],
  ["town_17_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_17_store|entry(9),0, fac_commoners,    [itm_dress,         itm_leather_boots,  itm_straw_hat   ],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, woman_face_1, woman_face_2],
  ["town_18_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_18_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_young_1, man_face_older_2],
  ["town_19_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_19_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_young_1, man_face_older_2],
  ["town_20_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_20_store|entry(9),0, fac_commoners,    [itm_sarranid_common_dress_b,  itm_sarranid_boots_a, itm_sarranid_felt_head_cloth_b  ],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, woman_face_1, woman_face_2],
  ["town_21_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_21_store|entry(9),0, fac_commoners,    [itm_sarranid_dress_a,         itm_sarranid_boots_a,  itm_sarranid_felt_head_cloth  ],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, woman_face_1, woman_face_2],
  ["town_22_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_22_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_young_1, man_face_older_2],
  ## CC
  ["town_23_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_23_store|entry(9),0, fac_commoners,     [itm_leather_jerkin,itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_young_1, man_face_older_2],
  ["town_24_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_24_store|entry(9),0, fac_commoners,    [itm_woolen_dress,  itm_leather_boots,  itm_female_hood ],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, woman_face_1, woman_face_2],
  ["town_25_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_25_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_young_1, man_face_older_2],
  ["town_26_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_26_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_young_1, man_face_older_2],
  ["town_27_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_27_store|entry(9),0, fac_commoners,    [itm_woolen_dress,  itm_leather_boots,  itm_female_hood ],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, woman_face_1, woman_face_2],
  ["town_28_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_28_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_young_1, man_face_older_2],
  ["town_29_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_29_store|entry(9),0, fac_commoners,    [itm_sarranid_dress_a,         itm_sarranid_boots_a,  itm_sarranid_felt_head_cloth  ],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, woman_face_1, woman_face_2],
  ## CC
  
  ["salt_mine_merchant","Barezan","Barezan",                tf_hero|tf_randomize_face|tf_is_merchant, scn_salt_mine|entry(1),0, fac_commoners,        [itm_leather_apron, itm_leather_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, merchant_face_1, merchant_face_2],

# Horse Merchants

  ["town_1_horse_merchant","Naldera, the horse merchant","{!}Town 1 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_blue_dress,           itm_blue_hose,      itm_female_hood],   def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, woman_face_1, woman_face_2],
  ["town_2_horse_merchant","Leomir, the horse merchant","{!}Town 2 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_linen_tunic,          itm_nomad_boots,],                      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, man_face_young_1, man_face_older_2],
  ["town_3_horse_merchant","Pelagn, the horse merchant","{!}Town 3 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_nomad_armor,          itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, man_face_young_1, man_face_older_2],
  ["town_4_horse_merchant","Qlurzach, the horse merchant","{!}Town 4 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_leather_jerkin,       itm_nomad_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, man_face_young_1, man_face_older_2],
  ["town_5_horse_merchant","Imbrea, the horse merchant","{!}Town 5 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_dress,                itm_woolen_hose,    itm_woolen_hood],   def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, woman_face_1, woman_face_2],
  ["town_6_horse_merchant","Prescan, the horse merchant","{!}Town 6 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,         itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, man_face_young_1, man_face_older_2],
  ["town_7_horse_merchant","Rhudolg, the horse merchant","{!}Town 7 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,         itm_leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, man_face_young_1, man_face_older_2],
  ["town_8_horse_merchant","Belicha, the horse merchant","{!}Town 8 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,         itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, man_face_young_1, man_face_older_2],
## CC
  # ["town_9_horse_merchant","Horse Merchant","{!}Town 9 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_leather_jerkin,       itm_woolen_hose],                       def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, man_face_young_1, man_face_older_2],
  # ["town_10_horse_merchant","Horse Merchant","{!}Town 10 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_blue_dress,          itm_blue_hose,      itm_straw_hat],     def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, woman_face_1, woman_face_2],
  # ["town_11_horse_merchant","Horse Merchant","{!}Town 11 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_nomad_armor,         itm_leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, man_face_young_1, man_face_older_2],
  # ["town_12_horse_merchant","Horse Merchant","{!}Town 12 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_leather_jacket,      itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, man_face_young_1, man_face_older_2],
  # ["town_13_horse_merchant","Horse Merchant","{!}Town 13 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_coarse_tunic,        itm_nomad_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, man_face_young_1, man_face_older_2],
  # ["town_14_horse_merchant","Horse Merchant","{!}Town 14 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_peasant_dress,       itm_blue_hose,      itm_headcloth],     def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, woman_face_1, woman_face_2],
  # ["town_15_horse_merchant","Horse Merchant","{!}Town 15 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_nomad_armor,         itm_leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, man_face_young_1, man_face_older_2],
  # ["town_16_horse_merchant","Horse Merchant","{!}Town 16 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_leather_jacket,      itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, man_face_young_1, man_face_older_2],
  # ["town_17_horse_merchant","Horse Merchant","{!}Town 17 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_coarse_tunic,        itm_nomad_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, man_face_young_1, man_face_older_2],
  # ["town_18_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_peasant_dress,       itm_blue_hose,      itm_headcloth],     def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, woman_face_1, woman_face_2],
  # ["town_19_horse_merchant","Horse Merchant","{!}Town 15 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_nomad_armor,         itm_sarranid_boots_a],                     def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, man_face_young_1, man_face_older_2],
  # ["town_20_horse_merchant","Horse Merchant","{!}Town 16 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_sarranid_cloth_robe,      itm_sarranid_boots_a],                        def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, man_face_young_1, man_face_older_2],
  # ["town_21_horse_merchant","Horse Merchant","{!}Town 17 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_sarranid_cloth_robe_b,        itm_sarranid_boots_a],                       def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, man_face_young_1, man_face_older_2],
  # ["town_22_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_sarranid_common_dress_b,       itm_blue_hose,      itm_sarranid_felt_head_cloth_b],     def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, woman_face_1, woman_face_2],
  # ## CC
  # ["town_23_horse_merchant","Horse Merchant","{!}Town 23 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,         itm_leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, man_face_young_1, man_face_older_2],
  # ["town_24_horse_merchant","Horse Merchant","{!}Town 24 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_leather_jacket,      itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, man_face_young_1, man_face_older_2],
  # ["town_25_horse_merchant","Horse Merchant","{!}Town 11 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_nomad_armor,         itm_leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, man_face_young_1, man_face_older_2],
  # ["town_26_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_peasant_dress,       itm_blue_hose,      itm_headcloth],     def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, woman_face_1, woman_face_2],
  # ["town_27_horse_merchant","Horse Merchant","{!}Town 12 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_leather_jacket,      itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, man_face_young_1, man_face_older_2],
  # ["town_28_horse_merchant","Horse Merchant","{!}Town 15 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_nomad_armor,         itm_leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, man_face_young_1, man_face_older_2],
  # ["town_29_horse_merchant","Horse Merchant","{!}Town 17 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_sarranid_cloth_robe_b,        itm_sarranid_boots_a],                       def_attrib|level(5),wp(20),knows_inventory_management_10|knows_looting_10, man_face_young_1, man_face_older_2],
  # ## CC
## CC
  
#Town Mayors    #itm_courtly_outfit itm_gambeson itm_blue_gambeson itm_red_gambeson itm_nobleman_outfit itm_rich_outfit
  ["town_1_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_courtly_outfit, itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["town_2_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_gambeson,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_3_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_blue_gambeson,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_4_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_fur_coat,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_5_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_nobleman_outfit,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_6_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_red_gambeson,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_7_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_rich_outfit,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_8_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_red_gambeson,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_9_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_courtly_outfit,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_10_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_11_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_leather_jacket,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_12_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_red_gambeson,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_13_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_nobleman_outfit,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_14_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_15_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_leather_jacket,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_16_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_fur_coat,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_17_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_nobleman_outfit,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_18_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_19_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,     itm_sarranid_boots_a],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_20_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,       itm_sarranid_boots_a], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_21_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,    itm_sarranid_boots_a],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_22_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,      itm_sarranid_boots_a],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ## CC
  ["town_23_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_rich_outfit,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_24_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_fur_coat,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_25_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_leather_jacket,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_26_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_27_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_red_gambeson,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_28_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_leather_jacket,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_29_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,    itm_sarranid_boots_a],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ## CC
  
#Village stores
  ["village_1_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,            man_face_old_1, man_face_older_2],
  ["village_2_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                              man_face_old_1, man_face_older_2],
  ["village_3_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                         man_face_old_1, man_face_older_2],
  ["village_4_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,        man_face_old_1, man_face_older_2],
  ["village_5_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                      man_face_old_1, man_face_older_2],
  ["village_6_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                          man_face_old_1, man_face_older_2],
  ["village_7_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                         man_face_old_1, man_face_older_2],
  ["village_8_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,        man_face_old_1, man_face_older_2],
  ["village_9_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,         man_face_old_1, man_face_older_2],
  ["village_10_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                              man_face_old_1, man_face_older_2],
  ["village_11_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                         man_face_old_1, man_face_older_2],
  ["village_12_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,             man_face_old_1, man_face_older_2],
  ["village_13_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                         man_face_old_1, man_face_older_2],
  ["village_14_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                              man_face_old_1, man_face_older_2],
  ["village_15_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,            man_face_old_1, man_face_older_2],
  ["village_16_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_17_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,             man_face_old_1, man_face_older_2],
  ["village_18_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_19_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots, itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,            man_face_old_1, man_face_older_2],
  ["village_20_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_21_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,             man_face_old_1, man_face_older_2],
  ["village_22_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,             man_face_old_1, man_face_older_2],
  ["village_23_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,            man_face_old_1, man_face_older_2],
  ["village_24_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                              man_face_old_1, man_face_older_2],
  ["village_25_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                      man_face_old_1, man_face_older_2],
  ["village_26_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,             man_face_old_1, man_face_older_2],
  ["village_27_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,        man_face_old_1, man_face_older_2],
  ["village_28_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                              man_face_old_1, man_face_older_2],
  ["village_29_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                          man_face_old_1, man_face_older_2],
  ["village_30_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,             man_face_old_1, man_face_older_2],
  ["village_31_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                         man_face_old_1, man_face_older_2],
  ["village_32_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                              man_face_old_1, man_face_older_2],
  ["village_33_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,             man_face_old_1, man_face_older_2],
  ["village_34_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,             man_face_old_1, man_face_older_2],
  ["village_35_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                              man_face_old_1, man_face_older_2],
  ["village_36_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                          man_face_old_1, man_face_older_2],
  ["village_37_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                              man_face_old_1, man_face_older_2],
  ["village_38_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                          man_face_old_1, man_face_older_2],
  ["village_39_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                         man_face_old_1, man_face_older_2],
  ["village_40_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                              man_face_old_1, man_face_older_2],
  ["village_41_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                         man_face_old_1, man_face_older_2],
  ["village_42_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                              man_face_old_1, man_face_older_2],
  ["village_43_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,             man_face_old_1, man_face_older_2],
  ["village_44_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,             man_face_old_1, man_face_older_2],
  ["village_45_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                              man_face_old_1, man_face_older_2],
  ["village_46_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                          man_face_old_1, man_face_older_2],
  ["village_47_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                              man_face_old_1, man_face_older_2],
  ["village_48_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                          man_face_old_1, man_face_older_2],
  ["village_49_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                         man_face_old_1, man_face_older_2],
  ["village_50_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                              man_face_old_1, man_face_older_2],
  ["village_51_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,             man_face_old_1, man_face_older_2],
  ["village_52_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,             man_face_old_1, man_face_older_2],
  ["village_53_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,            man_face_old_1, man_face_older_2],
  ["village_54_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                              man_face_old_1, man_face_older_2],
  ["village_55_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_56_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_57_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_58_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_59_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_60_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_61_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_62_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_63_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_64_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_65_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_66_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_67_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_68_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_69_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_70_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_71_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_72_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_73_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_74_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_75_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_76_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_77_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_78_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_79_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_80_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_81_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                         man_face_old_1, man_face_older_2],
  ["village_82_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                              man_face_old_1, man_face_older_2],
  ["village_83_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,             man_face_old_1, man_face_older_2],
  ["village_84_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,             man_face_old_1, man_face_older_2],
  ["village_85_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                              man_face_old_1, man_face_older_2],
  ["village_86_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                          man_face_old_1, man_face_older_2],
  ["village_87_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                              man_face_old_1, man_face_older_2],
  ["village_88_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                          man_face_old_1, man_face_older_2],
  ["village_89_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                         man_face_old_1, man_face_older_2],
  ["village_90_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                              man_face_old_1, man_face_older_2],
  ["village_91_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                         man_face_old_1, man_face_older_2],
  ["village_92_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                              man_face_old_1, man_face_older_2],
  ["village_93_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,             man_face_old_1, man_face_older_2],
  ["village_94_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,             man_face_old_1, man_face_older_2],
  ["village_95_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                              man_face_old_1, man_face_older_2],
  ["village_96_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                          man_face_old_1, man_face_older_2],
  ["village_97_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                              man_face_old_1, man_face_older_2],
  ["village_98_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                          man_face_old_1, man_face_older_2],
  ["village_99_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                         man_face_old_1, man_face_older_2],
  ["village_100_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                              man_face_old_1, man_face_older_2],
  ["village_101_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                         man_face_old_1, man_face_older_2],
  ["village_102_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                              man_face_old_1, man_face_older_2],
  ["village_103_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,             man_face_old_1, man_face_older_2],
  ["village_104_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,             man_face_old_1, man_face_older_2],
  ["village_105_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                              man_face_old_1, man_face_older_2],
  ["village_106_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                          man_face_old_1, man_face_older_2],
  ["village_107_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                              man_face_old_1, man_face_older_2],
  ["village_108_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                          man_face_old_1, man_face_older_2],
  ["village_109_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                         man_face_old_1, man_face_older_2],
  ["village_110_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                              man_face_old_1, man_face_older_2],
  ## CC
  ["village_111_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_112_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_113_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_114_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_115_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_116_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_117_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_118_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_119_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_120_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_121_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                         man_face_old_1, man_face_older_2],
  ["village_122_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                              man_face_old_1, man_face_older_2],
  ["village_123_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,             man_face_old_1, man_face_older_2],
  ["village_124_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,             man_face_old_1, man_face_older_2],
  ["village_125_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                              man_face_old_1, man_face_older_2],
  ["village_126_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                          man_face_old_1, man_face_older_2],
  ["village_127_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                              man_face_old_1, man_face_older_2],
  ["village_128_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                          man_face_old_1, man_face_older_2],
  ["village_129_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                         man_face_old_1, man_face_older_2],
  ["village_130_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                              man_face_old_1, man_face_older_2],
  ["village_131_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                         man_face_old_1, man_face_older_2],
  ["village_132_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                              man_face_old_1, man_face_older_2],
  ["village_133_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,             man_face_old_1, man_face_older_2],
  ["village_134_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,             man_face_old_1, man_face_older_2],
  ["village_135_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                              man_face_old_1, man_face_older_2],
  ["village_136_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                          man_face_old_1, man_face_older_2],
  ["village_137_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                              man_face_old_1, man_face_older_2],
  ["village_138_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                          man_face_old_1, man_face_older_2],
  ["village_139_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                         man_face_old_1, man_face_older_2],
  ["village_140_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                              man_face_old_1, man_face_older_2],
  ["village_141_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                              man_face_old_1, man_face_older_2],
  ["village_142_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,             man_face_old_1, man_face_older_2],
  
  ["village_143_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                         man_face_old_1, man_face_older_2],
  ["village_144_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_145_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                          man_face_old_1, man_face_older_2],
  ["village_146_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_147_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,             man_face_old_1, man_face_older_2],
  ["village_148_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,             man_face_old_1, man_face_older_2],
  ["village_149_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,             man_face_old_1, man_face_older_2],
  ["village_150_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,             man_face_old_1, man_face_older_2],
  ["village_151_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,             man_face_old_1, man_face_older_2],
  ["village_152_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                         man_face_old_1, man_face_older_2],
  ["village_153_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_154_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                              man_face_old_1, man_face_older_2],
  ["village_155_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,        man_face_old_1, man_face_older_2],
  ["village_156_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,         man_face_old_1, man_face_older_2],
  ["village_157_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                          man_face_old_1, man_face_older_2],
  ["village_158_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                          man_face_old_1, man_face_older_2],
  ["village_159_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                              man_face_old_1, man_face_older_2],
  ["village_160_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10, man_face_old_1, man_face_older_2],
  ["village_161_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                          man_face_old_1, man_face_older_2],
  ["village_162_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                         man_face_old_1, man_face_older_2],
  ["village_163_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,                         man_face_old_1, man_face_older_2],
  ## CC
# Place extra merchants before this point
  ["merchants_end","{!}merchants_end","{!}merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,0],

  #Used for player enterprises
  ["town_1_master_craftsman", "{!}Town 1 Craftsman", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_2_master_craftsman", "{!}Town 2 Craftsman", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_padded_leather,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x0000000f010811c92d3295e46a96c72300000000001f5a980000000000000000],
  ["town_3_master_craftsman", "{!}Town 3 Craftsman", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000001b083203151d2ad5648e52b400000000001b172e0000000000000000],
  ["town_4_master_craftsman", "{!}Town 4 Craftsman", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000001a10114f091b2c259cd4c92300000000000228dd0000000000000000],
  ["town_5_master_craftsman", "{!}Town 5 Craftsman", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000d1044c578598cd92b5256db00000000001f23340000000000000000],
  ["town_6_master_craftsman", "{!}Town 6 Craftsman", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000001f046285493eaf1b048abcdb00000000001a8aad0000000000000000],
  ["town_7_master_craftsman", "{!}Town 7 Craftsman", "{!}Town 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000002b0052c34c549225619356d400000000001cc6e60000000000000000],
  ["town_8_master_craftsman", "{!}Town 8 Craftsman", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x0000000fdb0c20465b6e51e8a12c82d400000000001e148c0000000000000000],
  ["town_9_master_craftsman", "{!}Town 9 Craftsman", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000009f7005246071db236e296a45300000000001a8b0a0000000000000000],
  ["town_10_master_craftsman", "{!}Town 10 Craftsman", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000009f71012c2456a921aa379321a000000000012c6d90000000000000000],
  ["town_11_master_craftsman", "{!}Town 11 Craftsman", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x00000009f308514428db71b9ad70b72400000000001dc9140000000000000000],
  ["town_12_master_craftsman", "{!}Town 12 Seneschal", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000009e90825863853a5b91cd71a5b00000000000598db0000000000000000],
  ["town_13_master_craftsman", "{!}Town 13 Seneschal", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000009fa0c708f274c8eb4c64e271300000000001eb69a0000000000000000],
  ["town_14_master_craftsman", "{!}Town 14 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000007590c3206155c8b475a4e439a00000000001f489a0000000000000000],
  ["town_15_master_craftsman", "{!}Town 15 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000007440022d04b2c6cb7d3723d5a00000000001dc90a0000000000000000],
  ["town_16_master_craftsman", "{!}Town 16 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000007680c3586054b8e372e4db65c00000000001db7230000000000000000],
  ["town_17_master_craftsman", "{!}Town 17 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x0000000766046186591b564cec85d2e200000000001e4cea0000000000000000],
  ["town_18_master_craftsman", "{!}Town 18 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x0000000e7e0075523a6aa9b6da61e8dd00000000001d96d30000000000000000],
  ["town_19_master_craftsman", "{!}Town 19 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000002408314852a432e88aaa42e100000000001e284e0000000000000000],
  ["town_20_master_craftsman", "{!}Town 20 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe_b,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000001104449136e44cbd1c9352bc000000000005e8d10000000000000000],
  ["town_21_master_craftsman", "{!}Town 21 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000000131032d3351c6e43226ec96c000000000005b5240000000000000000],
  ["town_22_master_craftsman", "{!}Town 22 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe_b,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000000200c658a5723b1a3148dc455000000000015ab920000000000000000],
  ## CC
  ["town_23_master_craftsman", "{!}Town 23 Craftsman", "{!}Town 23 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000002b0052c34c549225619356d400000000001cc6e60000000000000000],
  ["town_24_master_craftsman", "{!}Town 24 Seneschal", "{!}Town 24 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000007680c3586054b8e372e4db65c00000000001db7230000000000000000],
  ["town_25_master_craftsman", "{!}Town 25 Craftsman", "{!}Town 25 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x00000009f308514428db71b9ad70b72400000000001dc9140000000000000000],
  ["town_26_master_craftsman", "{!}Town 26 Seneschal", "{!}Town 26 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x0000000e7e0075523a6aa9b6da61e8dd00000000001d96d30000000000000000],
  ["town_27_master_craftsman", "{!}Town 27 Seneschal", "{!}Town 27 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000009e90825863853a5b91cd71a5b00000000000598db0000000000000000],
  ["town_28_master_craftsman", "{!}Town 28 Seneschal", "{!}Town 28 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000007440022d04b2c6cb7d3723d5a00000000001dc90a0000000000000000],
  ["town_29_master_craftsman", "{!}Town 29 Seneschal", "{!}Town 29 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000000131032d3351c6e43226ec96c000000000005b5240000000000000000],
  ## CC
  
# Chests
## CC
  ["zendar_chest","{!}Zendar Chest","{!}Zendar Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,
   [itm_sword_medieval_e_long,itm_steel_long_bow,itm_strong_steel_long_bow,itm_piercing_arrows_2,itm_piercing_arrows_2_back,itm_steel_lance,itm_double_axe,itm_zweihander,itm_repeat_crossbow],
  def_attrib|level(18),wp(60),knows_common|knows_inventory_management_10|knows_looting_10, 0],
  ["zendar_chest_backup","{!}Zendar Chest","{!}Zendar Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral, [], def_attrib|level(18),wp(60),knows_common|knows_inventory_management_10|knows_looting_10, 0],
  
  ["zendar_chest_2","{!}Zendar Chest","{!}Zendar Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,
   [itm_black_helmet,itm_black_armor,itm_black_greaves,itm_plate_armor,itm_warhorse_plate,itm_heavy_warhorse_plate,itm_tab_shield_pavise_e,itm_steel_shield],
  def_attrib|level(18),wp(60),knows_common|knows_inventory_management_10|knows_looting_10, 0],
  ["zendar_chest_backup_2","{!}Zendar Chest","{!}Zendar Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral, [], def_attrib|level(18),wp(60),knows_common|knows_inventory_management_10|knows_looting_10, 0],
  
  ["tutorial_chest_1","{!}Melee Weapons Chest","{!}Melee Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_tutorial_sword, itm_tutorial_axe, itm_tutorial_spear, itm_tutorial_club, itm_tutorial_battle_axe],def_attrib|level(18),wp(60),knows_common, 0],
  ["tutorial_chest_2","{!}Ranged Weapons Chest","{!}Ranged Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_tutorial_short_bow, itm_tutorial_arrows, itm_tutorial_crossbow, itm_tutorial_bolts, itm_tutorial_throwing_daggers],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_1","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_strange_helmet,itm_strange_armor,itm_strange_boots],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_2","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_strange_short_sword,itm_strange_sword,itm_strange_great_sword],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_3","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_flintlock_pistol,itm_cartridges],def_attrib|level(18),wp(60),knows_common, 0],
## CC

  ["household_possessions","{!}household_possessions","{!}household_possessions",tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10|knows_looting_10, 0],  
  
# These are used as arrays in the scripts.
## CC
  ["temp_array_a","{!}temp_array_a","{!}temp_array_a",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10|knows_looting_10, 0],
  ["temp_array_b","{!}temp_array_b","{!}temp_array_b",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10|knows_looting_10, 0],
  ["temp_array_c","{!}temp_array_c","{!}temp_array_c",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10|knows_looting_10, 0],
  ["temp_array_d","{!}temp_array_d","{!}temp_array_d",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10|knows_looting_10, 0],
  ["temp_array_e","{!}temp_array_e","{!}temp_array_e",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10|knows_looting_10, 0],
  ["temp_array_f","{!}temp_array_f","{!}temp_array_f",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10|knows_looting_10, 0],
  ["temp_array_g","{!}temp_array_g","{!}temp_array_g",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10|knows_looting_10, 0],
  ["temp_array_h","{!}temp_array_h","{!}temp_array_h",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10|knows_looting_10, 0],
  ["temp_array_i","{!}temp_array_i","{!}temp_array_i",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10|knows_looting_10, 0],
  ["temp_array_j","{!}temp_array_j","{!}temp_array_j",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10|knows_looting_10, 0],
  
  ["stack_selection_amounts","{!}stack_selection_amounts","{!}stack_selection_amounts",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_inventory_management_10|knows_looting_10,0],
  ["stack_selection_ids","{!}stack_selection_ids","{!}stack_selection_ids",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_inventory_management_10|knows_looting_10,0],

  ["notification_menu_types","{!}notification_menu_types","{!}notification_menu_types",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_inventory_management_10|knows_looting_10,0],
  ["notification_menu_var1","{!}notification_menu_var1","{!}notification_menu_var1",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_inventory_management_10|knows_looting_10,0],
  ["notification_menu_var2","{!}notification_menu_var2","{!}notification_menu_var2",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_inventory_management_10|knows_looting_10,0],

  ["banner_background_color_array","{!}banner_background_color_array","{!}banner_background_color_array",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_inventory_management_10|knows_looting_10,0],

  ["multiplayer_data","{!}multiplayer_data","{!}multiplayer_data",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_inventory_management_10|knows_looting_10,0],

##  ["black_khergit_guard","Black Khergit Guard","Black Khergit Guard",tf_mounted|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_black_khergits,
##   [itm_arrows,itm_nomad_sabre,itm_scimitar,itm_winged_mace,itm_lance,itm_khergit_bow,itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_khergit_guard_boots,itm_khergit_guard_armor,itm_nomad_shield,itm_steppe_horse,itm_warhorse],
##   def_attrib|level(28),wp(140),knows_riding_6|knows_ironflesh_4|knows_horse_archery_6|knows_power_draw_6,khergit_face1, khergit_face2],

  ["bookcase","Bookcase","Bookcase",tf_hero,0,reserved,fac_neutral,[],def_attrib,0,knows_inventory_management_10|knows_looting_10,0],
  ["entering_order","{!}Entering Order","{!}Entering Order",tf_hero,0,reserved,fac_neutral,[],def_attrib,0,knows_inventory_management_10|knows_looting_10,0],
  ["gallery","{!}Gallery","{!}Gallery",tf_hero,0,reserved,fac_neutral,[],def_attrib,0,knows_inventory_management_10|knows_looting_10,0],
  ["temp_troop_2","{!}Temp Troop","{!}Temp Troop",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10|knows_looting_10,0],
  ## CC
# Add Extra Quest NPCs below this point  

  ["local_merchant","Local Merchant","Local Merchants",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["tax_rebel","Peasant Rebel","Peasant Rebels",tf_guarantee_armor,0,reserved,fac_commoners,
   [itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_linen_tunic,itm_coarse_tunic,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,vaegir_face1, vaegir_face2],
  ["trainee_peasant","Peasant","Peasants",tf_guarantee_armor,0,reserved,fac_commoners,
   [itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_linen_tunic,itm_coarse_tunic,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,vaegir_face1, vaegir_face2],
  ["fugitive","Nervous Man","Nervous Men",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic,itm_linen_tunic,itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_wrapping_boots, itm_fur_hat, itm_leather_cap, itm_sword_medieval_b, itm_throwing_daggers],
   attr(20,12,7,7)|level(26),wp(180),knows_common|knows_power_throw_6|knows_power_strike_6|knows_ironflesh_9,man_face_middle_1, man_face_old_2],
   
  ["belligerent_drunk","Belligerent Drunk","Belligerent Drunks",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic,itm_linen_tunic,itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_wrapping_boots, itm_fur_hat, itm_leather_cap, itm_sword_viking_1],
   attr(18,7,5,5)|level(15),wp(120),knows_common|knows_power_strike_2|knows_ironflesh_9,    bandit_face1, bandit_face2],

  ["hired_assassin","Hired Assassin","Hired Assassin",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners, #they look like belligerent drunks
   [itm_short_tunic,itm_linen_tunic,itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_wrapping_boots, itm_fur_hat, itm_leather_cap, itm_sword_viking_1],
   attr(19,9,6,6)|level(20),wp(180),knows_common|knows_power_strike_5|knows_ironflesh_3|knows_athletics_3,    bandit_face1, bandit_face2],

  ["fight_promoter","Rough-Looking Character","Rough-Looking Character",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic,itm_linen_tunic,itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_wrapping_boots, itm_fur_hat, itm_leather_cap, itm_sword_viking_1],
   attr(16,12,6,6)|level(20),wp(180),knows_common|knows_power_strike_5|knows_ironflesh_3,    bandit_face1, bandit_face2],

   
   
  ["spy","Ordinary Townsman","Ordinary Townsmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
   [itm_sword_viking_1,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves],
   attr(16,12,6,6)|level(20),wp(130),knows_common,man_face_middle_1, man_face_older_2],
   
  ["spy_partner","Unremarkable Townsman","Unremarkable Townsmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
   [itm_sword_medieval_b,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves],
   attr(11,9,5,5)|level(10),wp(130),knows_common,vaegir_face1, vaegir_face2],

   ["nurse_for_lady","Nurse","Nurse",tf_female|tf_guarantee_armor,0,reserved,fac_commoners,
   [itm_robe, itm_black_hood, itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,woman_face_1, woman_face_2],   
   ["temporary_minister","Minister","Minister",tf_guarantee_armor|tf_guarantee_boots,0,reserved,fac_commoners,
   [itm_rich_outfit, itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_older_2],   
   
## CC
  ["cb_troop_0","F1","{!}F1", 0, 0, 0, 0,[],def_attrib|level(1),wp(0),0,0],
  ["cb_troop_1","A1","{!}A1", 0, 0, 0, 0,[],def_attrib|level(1),wp(0),0,0],
  ["cb_troop_2","B1","{!}B1", 0, 0, 0, 0,[],def_attrib|level(1),wp(0),0,0],
  ["cb_troop_3","C1","{!}C1", 0, 0, 0, 0,[],def_attrib|level(1),wp(0),0,0],
  ["cb_troop_4","D1","{!}D1", 0, 0, 0, 0,[],def_attrib|level(1),wp(0),0,0],
  ["cb_troop_5","E1","{!}E1", 0, 0, 0, 0,[],def_attrib|level(1),wp(0),0,0],
  ["cb_troop_total","Total","{!}Total", 0, 0, 0, 0,[],def_attrib|level(1),wp(0),0,0],
## CC

##  ["conspirator","Conspirator","Conspirators", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
##   [itm_sword,itm_leather_jerkin,itm_leather_boots,itm_hunter,itm_leather_gloves],
##   def_attrib|agi_11|level(10),wp(130),knows_common,vaegir_face1, vaegir_face2],
##  ["conspirator_leader","Conspirator","Conspirators", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
##   [itm_sword,itm_leather_jerkin,itm_leather_boots,itm_hunter,itm_leather_gloves],
##   def_attrib|agi_11|level(10),wp(130),knows_common,vaegir_face1, vaegir_face2],
##  ["peasant_rebel","Peasant Rebel","Peasant Rebels",tf_guarantee_armor,0,reserved,fac_peasant_rebels,
##   [itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_linen_tunic,itm_coarse_tunic,itm_nomad_boots,itm_wrapping_boots],
##   def_attrib|level(4),wp(60),knows_common,vaegir_face1, vaegir_face2],
##  ["noble_refugee","Noble Refugee","Noble Refugees",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_noble_refugees,
##   [itm_sword,itm_leather_jacket,itm_hide_boots, itm_saddle_horse, itm_leather_jacket, itm_leather_cap],
##   def_attrib|level(9),wp(100),knows_common,swadian_face1, swadian_face2],
##  ["noble_refugee_woman","Noble Refugee Woman","Noble Refugee Women",tf_female|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_noble_refugees,
##   [itm_knife,itm_dagger,itm_hunting_crossbow,itm_dress,itm_robe,itm_woolen_dress, itm_headcloth, itm_woolen_hood, itm_wrapping_boots],
##   def_attrib|level(3),wp(45),knows_common,refugee_face1,refugee_face2],

  ["quick_battle_6_player", "{!}quick_battle_6_player", "{!}quick_battle_6_player", tf_hero, 0, reserved,  fac_player_faction, [itm_padded_cloth,itm_nomad_boots, itm_splinted_leather_greaves, itm_skullcap, itm_sword_medieval_b,  itm_crossbow, itm_bolts, itm_plate_covered_round_shield],    knight_attrib_1,wp(130),knight_skills_1, 0x000000000008010b01f041a9249f65fd],

#Multiplayer ai troops
  ["swadian_crossbowman_multiplayer_ai","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_bolts,itm_crossbow,itm_sword_medieval_a,itm_tab_shield_heater_b,
    itm_leather_jerkin,itm_leather_armor,itm_ankle_boots,itm_footman_helmet],
   def_attrib|level(19),wp_melee(90)|wp_crossbow(100),knows_ironflesh_4|knows_athletics_6|knows_shield_5|knows_weapon_master_5|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
  ["swadian_infantry_multiplayer_ai","Swadian Infantry","Swadian Infantry",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_1,
   [itm_pike,itm_bastard_sword_a,itm_tab_shield_heater_c,
    itm_studded_leather_coat,itm_ankle_boots,itm_flat_topped_helmet],
   def_attrib|level(19),wp_melee(105),knows_shield_4|knows_weapon_master_4|knows_power_strike_5|knows_ironflesh_5|knows_athletics_4,swadian_face_middle_1, swadian_face_old_2],
  ["swadian_man_at_arms_multiplayer_ai","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_all_wo_ranged|tf_guarantee_polearm,0,0,fac_kingdom_1,
   [itm_lance,itm_bastard_sword_a,itm_tab_shield_heater_cav_a,
    itm_mail_with_surcoat,itm_hide_boots,itm_norman_helmet,itm_hunter],
   def_attrib|level(19),wp_melee(100),knows_riding_4|knows_shield_4|knows_weapon_master_4|knows_power_strike_4|knows_ironflesh_4|knows_athletics_1,swadian_face_young_1, swadian_face_old_2],
  ["vaegir_archer_multiplayer_ai","Vaegir Archer","Vaegir Archers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_arrows,itm_scimitar,itm_nomad_bow,
    itm_leather_vest,itm_nomad_boots,itm_spiked_helmet,itm_nomad_cap],
   def_int_cha|str_12|agi_5|level(19),wp_melee(70)|wp_archery(110),knows_power_draw_5|knows_ironflesh_4|knows_athletics_6|knows_shield_2|knows_weapon_master_2,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_spearman_multiplayer_ai","Vaegir Spearman","Vaegir Spearmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_2,
   [itm_padded_leather,itm_nomad_boots,itm_spiked_helmet,itm_nomad_cap, itm_spear, itm_tab_shield_kite_b, itm_mace_1, itm_javelin],
   def_int_cha|str_12|agi_5|level(19),wp_melee(90),knows_ironflesh_4|knows_athletics_6|knows_power_strike_3|knows_power_throw_3|knows_shield_2|knows_weapon_master_2,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_horseman_multiplayer_ai","Vaegir Horseman","Vaegir Horsemen",tf_mounted|tf_guarantee_all_wo_ranged|tf_guarantee_polearm,0,0,fac_kingdom_2,
   [itm_battle_axe,itm_scimitar,itm_lance,itm_tab_shield_kite_cav_a,
     itm_studded_leather_coat,itm_lamellar_vest,itm_nomad_boots,itm_spiked_helmet,itm_saddle_horse],
   def_attrib|level(19),wp(100),knows_riding_4|knows_ironflesh_4|knows_power_strike_4|knows_shield_3|knows_weapon_master_3,vaegir_face_young_1, vaegir_face_older_2],
  ["khergit_dismounted_lancer_multiplayer_ai","Khergit Dismounted Lancer","Khergit Dismounted Lancer",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_3,
   [itm_sword_khergit_4,itm_spiked_mace,itm_one_handed_war_axe_b,itm_one_handed_war_axe_a,itm_hafted_blade_a,itm_hafted_blade_b,itm_heavy_lance,itm_lance,
    itm_khergit_cavalry_helmet,itm_khergit_war_helmet,itm_lamellar_vest_khergit,itm_tribal_warrior_outfit,itm_khergit_leather_boots,itm_splinted_leather_greaves,itm_leather_gloves,itm_mail_mittens,itm_tab_shield_small_round_b,itm_tab_shield_small_round_c],
   def_attrib|level(19),wp(100),knows_riding_7|knows_power_strike_5|knows_power_draw_4|knows_power_throw_2|knows_ironflesh_5|knows_horse_archery_1,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_veteran_horse_archer_multiplayer_ai","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_3,itm_khergit_bow,itm_khergit_arrows,itm_tab_shield_small_round_b,
    itm_khergit_cavalry_helmet,itm_tribal_warrior_outfit,itm_khergit_leather_boots,itm_steppe_horse],
   def_attrib|level(19),wp(90)|wp_archery(100),knows_riding_6|knows_power_draw_5|knows_shield_2|knows_weapon_master_2|knows_horse_archery_5,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_lancer_multiplayer_ai","Khergit Lancer","Khergit Lancers",tf_guarantee_all_wo_ranged|tf_guarantee_polearm,0,0,fac_kingdom_3,
   [itm_sword_khergit_4,itm_spiked_mace,itm_one_handed_war_axe_b,itm_one_handed_war_axe_a,itm_hafted_blade_a,itm_hafted_blade_b,itm_heavy_lance,itm_lance,
    itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_khergit_war_helmet,itm_lamellar_vest_khergit,itm_lamellar_armor,itm_khergit_leather_boots,itm_splinted_leather_greaves,itm_leather_gloves,itm_mail_mittens,itm_scale_gauntlets,itm_tab_shield_small_round_b,itm_tab_shield_small_round_c,itm_courser],
   def_attrib|level(19),wp(100),knows_riding_7|knows_power_strike_5|knows_power_draw_4|knows_power_throw_2|knows_ironflesh_5|knows_horse_archery_1,khergit_face_middle_1, khergit_face_older_2],
  ["nord_veteran_multiplayer_ai","Nord Footman","Nord Footmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_4,
   [itm_sword_viking_2,itm_one_handed_battle_axe_b,itm_two_handed_axe,itm_tab_shield_round_d,itm_throwing_axes,
    itm_nordic_helmet,itm_nordic_fighter_helmet,itm_mail_hauberk,itm_splinted_leather_greaves,itm_leather_boots,itm_leather_gloves],
   def_attrib|level(19),wp(130),knows_power_strike_5|knows_power_throw_3|knows_ironflesh_3|knows_athletics_5|knows_shield_3|knows_weapon_master_3,nord_face_young_1, nord_face_older_2],
  ["nord_scout_multiplayer_ai","Nord Scout","Nord Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_javelin,itm_sword_viking_1,itm_two_handed_axe,itm_spear,itm_tab_shield_round_a,
    itm_skullcap,itm_nordic_archer_helmet,itm_leather_jerkin,itm_leather_boots,itm_saddle_horse],
   def_attrib|level(19),wp(100),knows_riding_5|knows_ironflesh_2|knows_power_strike_3|knows_shield_1|knows_weapon_master_1|knows_horse_archery_2|knows_power_throw_3,nord_face_young_1, nord_face_older_2],
  ["nord_archer_multiplayer_ai","Nord Archer","Nord Archers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_arrows,itm_two_handed_axe,itm_sword_viking_2,itm_short_bow,
    itm_leather_jerkin,itm_blue_tunic,itm_leather_boots,itm_nasal_helmet,itm_leather_cap],
   def_int_cha|str_11|agi_5|level(19),wp_melee(80)|wp_archery(110),knows_power_strike_2|knows_shield_1|knows_weapon_master_1|knows_power_draw_5|knows_ironflesh_4|knows_athletics_6,nord_face_young_1, nord_face_old_2],
  ["rhodok_veteran_crossbowman_multiplayer_ai","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_fighting_pick,itm_club_with_spike_head,itm_maul,itm_tab_shield_pavise_c,itm_heavy_crossbow,itm_bolts,
    itm_leather_cap,itm_padded_leather,itm_nomad_boots],
   def_attrib|level(19),wp_melee(100)|wp_crossbow(120),knows_shield_5|knows_weapon_master_5|knows_power_strike_3|knows_ironflesh_4|knows_athletics_6,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_veteran_spearman_multiplayer_ai","Rhodok Spearman","Rhodok Spearmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_5,
   [itm_ashwood_pike,itm_war_spear,itm_pike,itm_club_with_spike_head,itm_sledgehammer,itm_tab_shield_pavise_c,itm_sword_medieval_a,
    itm_leather_cap,itm_byrnie,itm_ragged_outfit,itm_nomad_boots],
   def_attrib|level(19),wp(115),knows_shield_3|knows_weapon_master_3|knows_power_strike_4|knows_ironflesh_5|knows_athletics_3,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_scout_multiplayer_ai","Rhodok Scout","Rhodok Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_5,
   #TODO: Change weapons, copied from Nord Scout
   [itm_sword_medieval_a,itm_tab_shield_heater_cav_a,itm_light_lance,itm_skullcap,itm_aketon_green,
    itm_ragged_outfit,itm_nomad_boots,itm_ankle_boots,itm_saddle_horse],
   def_attrib|level(19),wp(100),knows_riding_5|knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_weapon_master_1|knows_horse_archery_2|knows_power_throw_3,rhodok_face_young_1, rhodok_face_older_2],
  ["sarranid_infantry_multiplayer_ai","Sarranid Infantry","Sarranid Infantries",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,
   [itm_sarranid_mail_shirt,itm_sarranid_horseman_helmet,itm_sarranid_boots_b,itm_sarranid_boots_c,itm_splinted_leather_greaves,itm_arabian_sword_b,itm_mace_3,itm_spear,itm_tab_shield_kite_c],
   def_attrib|level(20),wp_melee(105),knows_riding_3|knows_ironflesh_2|knows_shield_3|knows_weapon_master_3,swadian_face_middle_1, swadian_face_old_2],
  ["sarranid_archer_multiplayer_ai","Sarranid Archer","Sarranid Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_arrows,itm_nomad_bow,itm_arabian_sword_a,itm_archers_vest,itm_sarranid_boots_b,itm_sarranid_helmet1,itm_turban,itm_desert_turban],
   def_attrib|level(19),wp_melee(90)|wp_archery(100),knows_riding_2|knows_ironflesh_1,swadian_face_young_1, swadian_face_old_2],
  ["sarranid_horseman_multiplayer_ai","Sarranid Horseman","Sarranid Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_polearm,0,0,fac_kingdom_6,
   [itm_lance,itm_arabian_sword_b,itm_scimitar_b,itm_mace_4,itm_tab_shield_small_round_b,
    itm_sarranid_mail_shirt,itm_sarranid_boots_b,itm_sarranid_boots_c,itm_sarranid_horseman_helmet,itm_courser,itm_hunter],
   def_attrib|level(20),wp_melee(100),knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_weapon_master_2|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],

   
   
#Multiplayer troops (they must have the base items only, nothing else)
  ["swadian_crossbowman_multiplayer","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_bolts,itm_crossbow,itm_sword_medieval_b_small,itm_tab_shield_heater_a,itm_red_shirt,itm_ankle_boots],
   str_14 | agi_15 |def_attrib_multiplayer|level(19),wpe(90,60,180,90),knows_common_multiplayer|knows_ironflesh_2|knows_athletics_5|knows_shield_5|knows_weapon_master_5|knows_power_strike_2|knows_riding_1,swadian_face_young_1, swadian_face_old_2],
  ["swadian_infantry_multiplayer","Swadian Infantry","Swadian Infantry",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_sword_medieval_a,itm_tab_shield_heater_a,itm_red_tunic,itm_ankle_boots],
   str_15 | agi_15 |def_attrib_multiplayer|level(20),wpex(105,130,110,40,60,110),knows_common_multiplayer|knows_shield_4|knows_weapon_master_4|knows_power_strike_4|knows_power_throw_2|knows_ironflesh_5|knows_athletics_6|knows_riding_1,swadian_face_middle_1, swadian_face_old_2],
  ["swadian_man_at_arms_multiplayer","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_lance,itm_sword_medieval_a,itm_tab_shield_heater_a,
    itm_red_tunic,itm_ankle_boots,itm_saddle_horse],
   str_14 | agi_16 |def_attrib_multiplayer|level(20),wp_melee(110),knows_common_multiplayer|knows_riding_5|knows_shield_2|knows_weapon_master_2|knows_power_throw_2|knows_power_strike_3|knows_ironflesh_3|knows_athletics_3,swadian_face_young_1, swadian_face_old_2],
#  ["swadian_mounted_crossbowman_multiplayer","Swadian Mounted Crossbowman","Swadian Mounted Crossbowmen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
#   [itm_bolts,itm_light_crossbow,itm_tab_shield_heater_cav_a,itm_bastard_sword_a,
#    itm_red_shirt,itm_hide_boots,itm_saddle_horse],
#   def_attrib_multiplayer|level(20),wp_melee(100)|wp_crossbow(120),knows_common_multiplayer|knows_riding_4|knows_shield_3|knows_weapon_master_3|knows_ironflesh_3|knows_horse_archery_2|knows_power_strike_3|knows_ironflesh_2|knows_athletics_2,swadian_face_young_1, swadian_face_old_2],
  ["vaegir_archer_multiplayer","Vaegir Archer","Vaegir Archers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_arrows,itm_mace_1,itm_nomad_bow,
    itm_linen_tunic,itm_hide_boots],
   str_14 | agi_14 |def_attrib_multiplayer|level(19),wpe(80,150,60,80),knows_common_multiplayer|knows_power_draw_7|knows_ironflesh_2|knows_athletics_4|knows_shield_2|knows_weapon_master_2|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_spearman_multiplayer","Vaegir Spearman","Vaegir spearman",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_spear, itm_tab_shield_kite_a, itm_mace_1,
    itm_linen_tunic,itm_hide_boots],
   str_15 | agi_15 |def_attrib_multiplayer|level(19),wpex(110,100,130,30,50,120),knows_common_multiplayer|knows_shield_2|knows_weapon_master_2|knows_power_throw_3|knows_power_strike_3|knows_ironflesh_4|knows_athletics_6|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_horseman_multiplayer","Vaegir Horseman","Vaegir Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_scimitar,itm_lance,itm_tab_shield_kite_cav_a,
    itm_linen_tunic,itm_hide_boots,itm_saddle_horse],
   str_16 | agi_15 |def_attrib_multiplayer|level(19),wpe(110,90,60,110),knows_common_multiplayer|knows_riding_5|knows_ironflesh_3|knows_power_strike_2|knows_shield_3|knows_weapon_master_3|knows_horse_archery_1|knows_power_throw_2,vaegir_face_young_1, vaegir_face_older_2],
  ["khergit_veteran_horse_archer_multiplayer","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_1,itm_nomad_bow,itm_arrows,
    itm_khergit_armor,itm_leather_steppe_cap_a,itm_hide_boots,itm_steppe_horse],
   str_15 | agi_18 |def_attrib_multiplayer|level(21),wpe(70,142,60,100),knows_common_multiplayer|knows_riding_2|knows_power_draw_3|knows_horse_archery_2|knows_athletics_4|knows_shield_1|knows_weapon_master_1,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_infantry_multiplayer","Khergit Infantry","Khergit Infantries",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_1,itm_spear,itm_tab_shield_small_round_a,
    itm_steppe_armor,itm_hide_boots,itm_leather_gloves],
   str_14 | agi_15 |def_attrib_multiplayer|level(19),wp(110),knows_common_multiplayer|knows_shield_4|knows_weapon_master_4|knows_power_strike_3|knows_ironflesh_3|knows_athletics_5|knows_riding_1,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_lancer_multiplayer","Khergit Lancer","Khergit Lancers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_1,itm_lance,itm_tab_shield_small_round_a,
    itm_khergit_armor,itm_leather_steppe_cap_a,itm_hide_boots,itm_steppe_horse],
   str_15 | agi_14 |def_attrib_multiplayer|level(21),wp(115),knows_common_multiplayer|knows_riding_6|knows_power_throw_3|knows_shield_4|knows_weapon_master_4|knows_power_strike_3|knows_ironflesh_3|knows_athletics_5,khergit_face_middle_1, khergit_face_older_2],
  ["nord_archer_multiplayer","Nord Archer","Nord Archers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_arrows,itm_sword_viking_2_small,itm_short_bow,
    itm_blue_tunic,itm_leather_boots],
   str_15 | agi_14 |def_attrib_multiplayer|level(15),wpe(90,150,60,80),knows_common_multiplayer|knows_power_strike_2|knows_shield_3|knows_weapon_master_3|knows_power_draw_5|knows_athletics_4|knows_riding_1,nord_face_young_1, nord_face_old_2],
  ["nord_veteran_multiplayer","Nord Huscarl","Nord Huscarls",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_sword_viking_1,itm_one_handed_war_axe_a,itm_tab_shield_round_a,
    itm_blue_tunic,itm_leather_boots],
   str_17 | agi_15 |def_attrib_multiplayer|level(24),wpex(110,135,100,40,60,140),knows_common_multiplayer|knows_power_strike_5|knows_power_throw_4|knows_ironflesh_4|knows_athletics_6|knows_shield_3|knows_weapon_master_3|knows_riding_1,nord_face_young_1, nord_face_older_2],
  ["nord_scout_multiplayer","Nord Scout","Nord Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_javelin,itm_sword_viking_1,itm_spear,itm_tab_shield_small_round_a,
    itm_blue_tunic,itm_leather_boots,itm_saddle_horse],
   str_16 | agi_15 |def_attrib_multiplayer|level(19),wp(105),knows_common_multiplayer|knows_riding_6|knows_power_strike_3|knows_shield_1|knows_weapon_master_1|knows_horse_archery_2|knows_ironflesh_2|knows_athletics_3|knows_power_throw_3,vaegir_face_young_1, vaegir_face_older_2],
  ["rhodok_veteran_crossbowman_multiplayer","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_crossbow,itm_bolts,itm_fighting_pick,itm_tab_shield_pavise_a,
    itm_tunic_with_green_cape,itm_ankle_boots],
   str_16 | agi_15 |def_attrib_multiplayer|level(20),wpe(100,60,180,90),knows_common_multiplayer|knows_shield_2|knows_weapon_master_2|knows_power_strike_2|knows_ironflesh_2|knows_athletics_5|knows_riding_1,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_sergeant_multiplayer","Rhodok Sergeant","Rhodok Sergeants",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_fighting_pick,itm_tab_shield_pavise_a,itm_spear,
    itm_green_tunic,itm_ankle_boots],
   str_16 | agi_14 |def_attrib_multiplayer|level(20),wpex(110,100,140,30,50,110),knows_common_multiplayer|knows_shield_5|knows_weapon_master_5|knows_power_strike_4|knows_power_throw_1|knows_ironflesh_4|knows_athletics_6|knows_riding_1,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_horseman_multiplayer","Rhodok Horseman","Rhodok Horsemen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_sword_medieval_a,itm_tab_shield_heater_cav_a, itm_light_lance, 
    itm_green_tunic,itm_ankle_boots,itm_saddle_horse],
   str_15 | agi_15 |def_attrib_multiplayer|level(20),wp(100),knows_common_multiplayer|knows_riding_4|knows_shield_2|knows_weapon_master_2|knows_power_strike_2|knows_ironflesh_3|knows_athletics_3|knows_power_throw_1,rhodok_face_middle_1, rhodok_face_older_2],
  ["sarranid_archer_multiplayer","Sarranid Archer","Sarranid Archers",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_arrows,itm_arabian_sword_a,itm_nomad_bow,
    itm_sarranid_cloth_robe, itm_sarranid_boots_b],
   str_15 | agi_16 |def_attrib_multiplayer|level(19),wpe(80,150,60,80),knows_common_multiplayer|knows_power_draw_5|knows_ironflesh_2|knows_athletics_5|knows_shield_2|knows_weapon_master_2|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
  ["sarranid_footman_multiplayer","Sarranid Footman","Sarranid footman",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_bamboo_spear, itm_tab_shield_kite_a, itm_arabian_sword_a,
    itm_sarranid_cloth_robe, itm_sarranid_boots_b],
   str_14 | agi_15 |def_attrib_multiplayer|level(19),wpex(110,100,130,30,50,120),knows_common_multiplayer|knows_shield_2|knows_weapon_master_2|knows_power_strike_3|knows_ironflesh_4|knows_athletics_6|knows_riding_1|knows_power_throw_3,vaegir_face_young_1, vaegir_face_older_2],
  ["sarranid_mamluke_multiplayer","Sarranid Mamluke","Sarranid Mamluke",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_arabian_sword_a,itm_lance,itm_tab_shield_small_round_a,
    itm_sarranid_cloth_robe, itm_sarranid_boots_b,itm_saddle_horse],
   str_15 | agi_14 |def_attrib_multiplayer|level(19),wpe(110,90,60,110),knows_common_multiplayer|knows_riding_5|knows_ironflesh_3|knows_power_strike_2|knows_shield_3|knows_weapon_master_3|knows_power_throw_2,vaegir_face_young_1, vaegir_face_older_2],

  ["multiplayer_end","{!}multiplayer_end","{!}multiplayer_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],

#Player history array
  ["log_array_entry_type",            "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_entry_time",            "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_actor",                 "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object",         "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object_lord",    "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object_faction", "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_troop_object",          "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_troop_object_faction",  "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_faction_object",        "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],

  ["quick_battle_troop_1","Rodrigo de Braganca","Rodrigo de Braganca", tf_hero,0,0,fac_kingdom_1,
   [itm_long_hafted_knobbed_mace, itm_wooden_shield, itm_iron_staff, itm_throwing_daggers,
    itm_felt_hat, itm_fur_coat, itm_light_leather_boots, itm_leather_gloves],
   attr(15,15,12,13)|level(15),wpex(109,33,132,15,32,100),knows_riding_3|knows_athletics_5|knows_shield_3|knows_weapon_master_3|knows_power_throw_3|knows_power_strike_2,0x0000000e240070cd598bb02b9556428c00000000001eabce0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_2","Usiatra","Usiatra", tf_hero|tf_female,0,0,fac_kingdom_1,
   [itm_nomad_bow, itm_barbed_arrows, itm_scimitar, itm_tab_shield_small_round_c, itm_sumpter_horse,
    itm_leather_armor, itm_splinted_greaves],
   attr(17,18,11,16)|level(22),wpex(182,113,112,159,82,115),knows_horse_archery_2|knows_riding_3|knows_ironflesh_4|knows_athletics_4|knows_shield_4|knows_weapon_master_4|knows_power_draw_2|knows_power_throw_1|knows_power_strike_3,0x000000007f004000719b69422165b71300000000001d5d1d0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_3","Hegen","Hegen", tf_hero,0,0,fac_kingdom_1,
   [itm_heavy_lance, itm_sword_two_handed_b, itm_sword_medieval_c, itm_tab_shield_heater_c, itm_warhorse,
    itm_guard_helmet, itm_coat_of_plates, itm_mail_mittens, itm_mail_boots],
   attr(20,18,12,14)|level(24),wpex(90,152,102,31,33,34),knows_riding_5|knows_ironflesh_6|knows_athletics_5|knows_shield_5|knows_weapon_master_5|knows_power_strike_6,0x000000018000324428db8a431491472400000000001e44a90000000000000000, swadian_face_old_2],
  ["quick_battle_troop_4","Konrad","Konrad", tf_hero,0,0,fac_kingdom_1,
   [itm_sword_two_handed_a, itm_mace_4, itm_tab_shield_kite_d,
    itm_bascinet_3, itm_scale_armor, itm_mail_mittens, itm_mail_boots],
   attr(22,16,12,14)|level(24),wpex(130,150,130,30,50,90),knows_riding_2|knows_ironflesh_6|knows_athletics_5|knows_shield_5|knows_weapon_master_5|knows_power_throw_3|knows_power_strike_6,0x000000081700205434db6df4636db8e400000000001db6e30000000000000000, swadian_face_old_2],
  ["quick_battle_troop_5","Sverre","Sverre", tf_hero,0,0,fac_kingdom_1,
   [itm_long_axe, itm_sword_viking_1, itm_light_throwing_axes, itm_tab_shield_round_d,
    itm_nordic_fighter_helmet, itm_byrnie, itm_leather_gloves, itm_leather_boots],
   attr(20,17,12,12)|level(21),wpex(110,130,110,80,15,110),knows_riding_1|knows_ironflesh_5|knows_athletics_5|knows_shield_5|knows_weapon_master_5|knows_power_draw_2|knows_power_throw_4|knows_power_strike_5,0x000000048a00024723134e24cb51c91b00000000001dc6aa0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_6","Borislav","Borislav", tf_hero,0,0,fac_kingdom_1,
   [itm_strong_bow, itm_barbed_arrows, itm_barbed_arrows_back, itm_shortened_spear,
    itm_leather_warrior_cap, itm_leather_jerkin, itm_leather_gloves, itm_ankle_boots],
   attr(18,15,13,12)|level(18),wpex(70,70,100,140,15,100),knows_horse_archery_2|knows_riding_2|knows_ironflesh_2|knows_athletics_5|knows_shield_3|knows_weapon_master_3|knows_power_draw_4|knows_power_throw_3|knows_power_strike_2,0x000000089e00444415136e36e34dc8e400000000001d46d90000000000000000, swadian_face_old_2],
  ["quick_battle_troop_7","Stavros","Stavros", tf_hero,0,0,fac_kingdom_1,
   [itm_heavy_crossbow, itm_bolts_2, itm_sword_medieval_b_small, itm_tab_shield_pavise_c,
    itm_nasal_helmet, itm_padded_leather, itm_leather_gloves, itm_leather_boots],
   attr(15,16,15,15)|level(21),wpex(100,70,70,30,140,80),knows_horse_archery_2|knows_riding_2|knows_ironflesh_4|knows_athletics_5|knows_shield_5|knows_weapon_master_5|knows_power_throw_2|knows_power_strike_4,0x0000000e1400659226e34dcaa46e36db00000000001e391b0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_8","Gamara","Gamara", tf_hero|tf_female,0,0,fac_kingdom_1,
   [itm_throwing_spears, itm_throwing_spears, itm_scimitar, itm_leather_covered_round_shield,
    itm_desert_turban, itm_skirmisher_armor, itm_leather_gloves, itm_sarranid_boots_b],
   attr(16,18,12,12)|level(18),wpex(100,40,100,85,15,130),knows_horse_archery_2|knows_riding_2|knows_ironflesh_2|knows_athletics_5|knows_shield_4|knows_weapon_master_4|knows_power_draw_2|knows_power_throw_4|knows_power_strike_2,0x000000015400300118d36636db6dc8e400000000001db6db0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_9","Aethrod","Aethrod", tf_hero,0,0,fac_kingdom_1,
   [itm_nomad_bow, itm_barbed_arrows, itm_barbed_arrows_back, itm_scimitar_b,
    itm_splinted_greaves, itm_lamellar_vest],
   attr(23,18,12,13)|level(26),wpex(182,113,112,159,82,115),knows_horse_archery_2|knows_riding_2|knows_ironflesh_4|knows_athletics_7|knows_shield_4|knows_weapon_master_4|knows_power_draw_7|knows_power_throw_3|knows_power_strike_3,0x000000000000210536db6db6db6db6db00000000001db6db0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_10","Zaira","Zaira", tf_hero|tf_female,0,0,fac_kingdom_1,
   [itm_sarranid_cavalry_sword, itm_strong_bow, itm_bodkin_arrows, itm_bodkin_arrows_back, itm_arabian_horse_b,
    itm_sarranid_felt_head_cloth_b, itm_sarranid_common_dress, itm_sarranid_boots_b],
   attr(15,20,12,11)|level(18),wpex(126,19,23,149,41,26),knows_horse_archery_6|knows_riding_6|knows_shield_2|knows_weapon_master_2|knows_power_draw_4|knows_power_throw_1|knows_power_strike_4|knows_ironflesh_1,0x0000000502003001471a6a24dc6594cb00000000001da4840000000000000000, swadian_face_old_2],
  ["quick_battle_troop_11","Argo Sendnar","Argo Sendnar", tf_hero,0,0,fac_kingdom_1,
   [itm_morningstar, itm_tab_shield_round_d, itm_war_spear, itm_courser,
    itm_leather_gloves, itm_fur_hat, itm_leather_boots, itm_leather_jacket],
   attr(21,18,14,15)|level(28),wpex(101,35,136,15,17,19),knows_riding_4|knows_ironflesh_5|knows_athletics_2|knows_shield_4|knows_weapon_master_4|knows_power_strike_5,0x0000000e800015125adb702de3459a9c00000000001ea6d00000000000000000, swadian_face_old_2],
  ["quick_battle_troops_end","{!}quick_battle_troops_end","{!}quick_battle_troops_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],

  ["tutorial_fighter_1","Novice Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic,itm_nomad_boots],
   def_attrib|level(1),wp_melee(10),knows_ironflesh_2|knows_athletics_1|knows_shield_2|knows_weapon_master_2,0x000000088c1073144252b1929a85569300000000000496a50000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_2","Novice Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_green_tunic,itm_nomad_boots],
   def_attrib|level(1),wp_melee(10),knows_ironflesh_2|knows_athletics_1|knows_shield_2|knows_weapon_master_2,0x000000088b08049056ab56566135c46500000000001dda1b0000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_3","Regular Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_green_tunic,itm_nomad_boots],
   def_attrib|level(9),wp_melee(50),knows_ironflesh_2|knows_athletics_1|knows_shield_2|knows_weapon_master_2,0x00000008bc00400654914a3b0d0de74d00000000001d584e0000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_4","Veteran Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic,itm_nomad_boots],
   def_attrib|level(16),wp_melee(110),knows_ironflesh_3|knows_athletics_1|knows_power_strike_1|knows_shield_2|knows_weapon_master_2,0x000000089910324a495175324949671800000000001cd8ab0000000000000000, vaegir_face_older_2],
  ["tutorial_archer_1","Archer","Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,
   [itm_leather_jerkin,itm_leather_vest,itm_nomad_boots,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet,itm_vaegir_fur_cap,itm_nomad_cap],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_power_draw_2|knows_ironflesh_1|knows_athletics_2|knows_power_throw_1,vaegir_face_young_1, vaegir_face_older_2],
  ["tutorial_master_archer","Archery Trainer","Archery Trainer",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic,itm_nomad_boots],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_power_draw_2|knows_ironflesh_1|knows_athletics_2|knows_power_throw_1,0x0000000ea508540642f34d461d2d54a300000000001d5d9a0000000000000000, vaegir_face_older_2],
  ["tutorial_rider_1","Rider","{!}Vaegir Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_green_tunic,itm_hunter, itm_saddle_horse,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_riding_4|knows_shield_2|knows_weapon_master_2|knows_ironflesh_3|knows_power_strike_2,vaegir_face_middle_1, vaegir_face_older_2],
  ["tutorial_rider_2","Horse archer","{!}Khergit Horse Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_kingdom_3,
   [itm_tribal_warrior_outfit,itm_nomad_robe,itm_hide_boots,itm_tab_shield_small_round_a,itm_steppe_horse],
   def_attrib|level(14),wp(80)|wp_archery(110),knows_riding_5|knows_power_draw_3|knows_ironflesh_1|knows_horse_archery_4|knows_power_throw_1,khergit_face_young_1, khergit_face_older_2],
  ["tutorial_master_horseman","Riding Trainer","Riding Trainer",tf_hero,0,0,fac_kingdom_2,
   [itm_leather_vest,itm_nomad_boots],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_power_draw_2|knows_ironflesh_1|knows_athletics_2|knows_power_throw_1,0x0000000ea0084140478a692894ba185500000000001d4af30000000000000000, vaegir_face_older_2],
   
  ["swadian_merchant", "Merchant of Praven", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_4, [itm_sword_two_handed_a, itm_courtly_outfit, itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["vaegir_merchant", "Merchant of Reyvadin", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_5, [itm_sword_two_handed_a, itm_nobleman_outfit, itm_woolen_hose], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["khergit_merchant", "Merchant of Tulga", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_1, [itm_sword_two_handed_a, itm_red_gambeson, itm_nomad_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["nord_merchant", "Merchant of Sargoth", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_2, [itm_sword_two_handed_a, itm_red_gambeson, itm_nomad_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["rhodok_merchant", "Merchant of Jelkala", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_3, [itm_sword_two_handed_a, itm_leather_jerkin, itm_blue_hose], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["sarranid_merchant", "Merchant of Shariz", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_6, [itm_sword_two_handed_a, itm_sarranid_cloth_robe, itm_sarranid_boots_a], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],       
  ["startup_merchants_end","{!}startup_merchants_end","{!}startup_merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,0],
 
  ["sea_raider_leader","Sea Raider Captain","Sea Raiders",tf_hero|tf_guarantee_all_wo_ranged,0,0,fac_outlaws,
   [itm_arrows,itm_sword_viking_1,itm_sword_viking_2,itm_fighting_axe,itm_battle_axe,itm_spear,itm_nordic_shield,itm_nordic_shield,itm_nordic_shield,itm_wooden_shield,itm_long_bow,itm_javelin,itm_throwing_axes,
    itm_nordic_helmet,itm_nordic_helmet,itm_nasal_helmet,itm_mail_shirt,itm_byrnie,itm_mail_hauberk,itm_leather_boots, itm_nomad_boots],
   def_attrib|level(24),wp(110),knows_power_strike_2|knows_power_draw_3|knows_power_throw_2|knows_riding_1|knows_ironflesh_2|knows_athletics_2,nord_face_young_1, nord_face_old_2],

  ["looter_leader","Robber","Looters",tf_hero,0,0,fac_outlaws,
   [itm_hatchet,itm_club,itm_butchering_knife,itm_falchion,itm_rawhide_coat,itm_stones,itm_nomad_armor,itm_nomad_armor,itm_woolen_cap,itm_woolen_cap,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(20),knows_common,0x00000001b80032473ac49738206626b200000000001da7660000000000000000, bandit_face2],
   
  ["bandit_leaders_end","{!}bandit_leaders_end","{!}bandit_leaders_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,0],   
  
  ["relative_of_merchant", "Merchant's Brother", "{!}Prominent",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic,itm_nomad_boots],
   def_attrib|level(1),wp_melee(10),knows_ironflesh_2|knows_athletics_1|knows_shield_2|knows_weapon_master_2, 0x00000000320410022d2595495491afa400000000001d9ae30000000000000000, mercenary_face_2],   
   
  ["relative_of_merchants_end","{!}relative_of_merchants_end","{!}relative_of_merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10|knows_looting_10,0],     
]


#Troop upgrade declarations

upgrade(troops,"farmer", "watchman")
#upgrade(troops,"townsman","watchman")
upgrade2(troops,"watchman","caravan_guard","mercenary_crossbowman")
upgrade2(troops,"caravan_guard","mercenary_swordsman","mercenary_horseman")
upgrade(troops,"mercenary_swordsman","hired_blade")
upgrade(troops,"mercenary_crossbowman","mercenary_sharpshooter")
upgrade(troops,"mercenary_horseman","mercenary_cavalry")

upgrade(troops,"swadian_recruit","swadian_militia")
upgrade2(troops,"swadian_militia","swadian_footman","swadian_skirmisher")

upgrade(troops,"swadian_footman","swadian_infantry")
upgrade(troops,"swadian_skirmisher","swadian_crossbowman")
upgrade(troops,"swadian_infantry","swadian_sergeant")
upgrade(troops,"swadian_crossbowman","swadian_sharpshooter")
## CC
# upgrade2(troops,"swadian_footman","swadian_infantry","swadian_crossbowman")
# upgrade2(troops,"swadian_skirmisher","swadian_crossbowman","swadian_infantry")
upgrade(troops,"swadian_footman_rider","swadian_infantry_rider")
upgrade(troops,"swadian_infantry_rider","swadian_sergeant_rider")
upgrade(troops,"swadian_noble_lad","swadian_man_at_arms") 
## CC
upgrade(troops,"swadian_man_at_arms","swadian_knight")

upgrade(troops,"vaegir_recruit","vaegir_footman")
upgrade2(troops,"vaegir_footman","vaegir_veteran","vaegir_skirmisher")

upgrade(troops,"vaegir_veteran","vaegir_infantry")
upgrade(troops,"vaegir_skirmisher","vaegir_archer")
upgrade(troops,"vaegir_infantry","vaegir_guard")
upgrade(troops,"vaegir_archer","vaegir_marksman")
## CC
# upgrade2(troops,"vaegir_veteran","vaegir_infantry","vaegir_archer")
# upgrade2(troops,"vaegir_skirmisher","vaegir_archer","vaegir_infantry")
upgrade(troops,"vaegir_veteran_rider","vaegir_infantry_rider")
upgrade(troops,"vaegir_infantry_rider","vaegir_guard_rider")
upgrade(troops,"vaegir_noble_lad","vaegir_horseman")
# upgrade2(troops,"vaegir_archer","vaegir_marksman","vaegir_warrior")
# upgrade2(troops,"vaegir_infantry","vaegir_guard","vaegir_warrior")
## CC
upgrade(troops,"vaegir_horseman","vaegir_knight")

upgrade(troops,"khergit_tribesman","khergit_skirmisher")
upgrade2(troops,"khergit_skirmisher","khergit_horseman","khergit_horse_archer")
upgrade(troops,"khergit_horseman","khergit_lancer")
upgrade(troops,"khergit_horse_archer","khergit_veteran_horse_archer")
upgrade(troops,"khergit_lancer","khergit_khan_guard")

upgrade2(troops,"nord_recruit","nord_footman","nord_huntsman")
upgrade(troops,"nord_footman","nord_trained_footman")
upgrade(troops,"nord_huntsman","nord_archer")

upgrade(troops,"nord_trained_footman","nord_warrior")
upgrade(troops,"nord_archer","nord_veteran_archer")
## CC
# upgrade2(troops,"nord_trained_footman","nord_warrior","nord_veteran_archer")
# upgrade2(troops,"nord_archer","nord_veteran_archer","nord_warrior")
## CC
upgrade(troops,"nord_warrior","nord_veteran")
upgrade(troops,"nord_veteran","nord_champion")


upgrade2(troops,"rhodok_tribesman","rhodok_spearman","rhodok_crossbowman") ## CC
upgrade(troops,"rhodok_spearman","rhodok_trained_spearman")
upgrade(troops,"rhodok_crossbowman","rhodok_trained_crossbowman")
upgrade(troops,"rhodok_trained_spearman","rhodok_veteran_spearman")
upgrade(troops,"rhodok_trained_crossbowman","rhodok_veteran_crossbowman") #new 1.126
## CC
# upgrade2(troops,"rhodok_trained_spearman","rhodok_veteran_spearman","rhodok_veteran_crossbowman")
# upgrade2(troops,"rhodok_trained_crossbowman","rhodok_veteran_crossbowman","rhodok_veteran_spearman")
## CC
upgrade(troops,"rhodok_veteran_spearman","rhodok_sergeant")
upgrade(troops,"rhodok_veteran_crossbowman","rhodok_sharpshooter")

upgrade(troops,"sarranid_recruit","sarranid_footman")
upgrade2(troops,"sarranid_footman","sarranid_veteran_footman","sarranid_skirmisher")

upgrade(troops,"sarranid_veteran_footman","sarranid_infantry")
upgrade(troops,"sarranid_skirmisher","sarranid_archer")
upgrade(troops,"sarranid_infantry","sarranid_guard")
upgrade(troops,"sarranid_archer","sarranid_master_archer")
## CC
# upgrade2(troops,"sarranid_veteran_footman","sarranid_infantry","sarranid_archer")
# upgrade2(troops,"sarranid_skirmisher","sarranid_archer","sarranid_infantry")
upgrade(troops,"sarranid_veteran_footman_rider","sarranid_infantry_rider")
upgrade(troops,"sarranid_infantry_rider","sarranid_guard_rider")
upgrade(troops,"sarranid_noble_lad","sarranid_horseman")
## CC
upgrade(troops,"sarranid_horseman","sarranid_mamluke")

## CC
# upgrade2(troops,"swadian_footman","swadian_infantry", "swadian_light_cavalry")
# upgrade2(troops,"swadian_infantry", "swadian_double_hander","swadian_sergeant")

# upgrade2(troops,"vaegir_veteran", "vaegir_infantry", "vaegir_light_cavalry")
# upgrade2(troops,"vaegir_infantry", "vaegir_berserker", "vaegir_guard")

# upgrade2(troops,"khergit_horseman","khergit_lancer", "khergit_dismounted_lancer")
# upgrade2(troops,"nord_trained_footman", "nord_warrior", "nord_scout")
# upgrade2(troops,"rhodok_trained_spearman","rhodok_veteran_spearman", "rhodok_scout")

# upgrade2(troops,"sarranid_veteran_footman","sarranid_infantry", "sarranid_light_cavalry")
# upgrade2(troops,"sarranid_infantry", "sarranid_axeman","sarranid_guard")
## CC


## CC

upgrade(troops,"mountain_bandit","trained_mountain_bandit")
upgrade(troops,"trained_mountain_bandit","veteran_mountain_bandit")
upgrade(troops,"forest_bandit","trained_forest_bandit")
upgrade(troops,"trained_forest_bandit","veteran_forest_bandit")
upgrade(troops,"steppe_bandit","trained_steppe_bandit")
upgrade(troops,"trained_steppe_bandit","veteran_steppe_bandit")
upgrade(troops,"taiga_bandit","trained_taiga_bandit")
upgrade(troops,"trained_taiga_bandit","veteran_taiga_bandit")
upgrade(troops,"sea_raider","trained_sea_raider")
upgrade(troops,"trained_sea_raider","veteran_sea_raider")
upgrade(troops,"desert_bandit","trained_desert_bandit")
upgrade(troops,"trained_desert_bandit","veteran_desert_bandit")
 
upgrade(troops,"looter","bandit")
upgrade(troops,"bandit","brigand")
upgrade2(troops,"brigand","mercenary_swordsman","mercenary_horseman")

# upgrade2(troops,"dark_hunter","dark_knight","dark_sniper")
# upgrade2(troops,"black_khergit_horseman","black_khergit_lancer","black_khergit_guard")
## CC

upgrade(troops,"manhunter","slave_driver")
upgrade(troops,"slave_driver","slave_hunter")
upgrade(troops,"slave_hunter","slave_crusher")
upgrade(troops,"slave_crusher","slaver_chief")

#upgrade(troops,"refugee","follower_woman")
upgrade(troops,"peasant_woman","follower_woman")
upgrade(troops,"follower_woman","hunter_woman")
upgrade(troops,"hunter_woman","fighter_woman")
upgrade(troops,"fighter_woman","sword_sister")

## CC
upgrade(troops,"hunter_woman_rider","fighter_woman_rider")
upgrade(troops,"fighter_woman_rider","sword_sister_rider")
upgrade(troops,"nord_scout","nord_veteran_scout")
upgrade(troops,"rhodok_scout","rhodok_veteran_scout")
## CC

