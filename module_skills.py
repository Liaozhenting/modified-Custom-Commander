from header_common import *
from header_skills import *

####################################################################################################################
#  Each skill contains the following fields:
#  1) Skill id (string): used for referencing skills in other files. The prefix skl_ is automatically added before each skill-id .
#  2) Skill name (string).
#  3) Skill flags (int). See header_skills.py for a list of available flags
#  4) Maximum level of the skill (int).
#  5) Skill description (string): used in character window for explaining the skills.
# 
####################################################################################################################

# Hardcoded skills are {names (indexes, beginning with 0)}:
# Trade (1)
# Leadership (2)
# Prisoner Management (3)
# First Aid (9)
# Surgery (10)
# Wound Treatment (11)
# Inventory Management (12)
# Spotting (13)
# Pathfinding (14)
# Tactics (15)
# Tracking (16)
# Trainer (17)
# Engineer (18)
# Horse Archery (24)
# Riding (25)
# Athletics (26)
# Shield (27)
# Weapon Master (28)
# Power Draw (34)
# Power Throw (35)
# Power Strike (36)
# Ironflesh (37)
#
# The effects of these skills can only be removed if the skill is disabled with sf_inactive flag.
# If you want to add a new skill, use the reserved skills or use non-hardcoded skills.

## skill overhaul
# base_att_str: Power Strike, Power Draw, Ironflesh, Power Throw.
# base_att_agi: Weapon-master, Riding, Horse archery, Athletics, Looting, Shield.
# base_att_int: Path-finding, Spotting, Tracking, Wound treatment, Surgery, First-aid, Engineer, Tactics, trainer, Cooking.
# base_att_cha: Speechcraft, Leadership.
## skill overhaul

reserved_skill = ("Reserved Skill",sf_inactive,10,"This is a reserved skill.")

skills = [
  ## skill overhaul
  ("speechcraft","Speechcraft", sf_base_att_cha|sf_effects_party,10, "This skill helps you make other people accept your point of view. It also lowers the minimum level of relationship needed to get NPCs to do what you want (Personal skill). And every level of this skill reduces your trade penalty by 5%% (Party skill). Max level: 10"),
  ("leadership","Leadership", sf_base_att_cha,10,"Every point increases maximum number of troops you can command by 5, reduces troop wages by 5%%, increases your party morale and reduces the chance of the recruited prisoners escaping from your party. (Leader skill) Max level: 10"),
  ("prisoner_management", "Prisoner Management",sf_base_att_cha|sf_inactive,10,"Every level of this skill increases maximum number of prisoners by 5. (Leader skill) Max level: 10"), 
  ("tenacity","Tenacity",sf_base_att_cha|sf_inactive,10,"Each point to this skill reduces damage to every member of the party from enemy by 3%%. (Leader skill) Max level: 10"), 
  ("encouragement","Encouragement",sf_base_att_cha|sf_inactive,10,"Each point to this skill increases the damage of every member of the party by 3%%. (Leader skill) Max level: 10"), 
  ("tactics","Tactics",sf_base_att_int|sf_effects_party,10,"Every two levels of this skill increases starting battle advantage by 1. (Party skill) Max level: 10"),
  ("trainer","Trainer",sf_base_att_int,10,"Every day, each hero with this skill adds some experience to every other member of the party. Experience gained goes as: 0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60. The effective skill level is depend on the difference on troop level between this hero and other member. (Personal skill) Max level: 10"), 
  ("trade","Trade", sf_base_att_cha|sf_inactive,10,"Every level of this skill reduces your trade penalty by 5%%. (Party skill) Max level: 10"),
  ("engineer","Engineer",sf_base_att_int|sf_effects_party,10,"This skill allows you to construct siege equipment and fief improvements more efficiently. (Party skill) Max level: 10"),
  ("first_aid", "First Aid",sf_base_att_int|sf_effects_party,10,"Heroes regain 6%% per skill level of hit-points lost during mission. (Party skill) Max level: 10"), 
  ("surgery","Surgery",sf_base_att_int|sf_effects_party,4,"Each point to this skill gives a 4%% chance that a mortally struck party member will be wounded rather than killed. (Party skill) Max level: 10"),   
  ("wound_treatment","Wound Treatment",sf_base_att_int|sf_effects_party,10,"Party healing speed is increased by 20%% per level of this skill. (Party skill) Max level: 10"), 
  ("inventory_management","Inventory Management",sf_base_att_int|sf_inactive,10,"Increases inventory capacity by +6 (Party skill). Max level: 10"), 
  ("spotting","Spotting",sf_base_att_int|sf_effects_party,10,"Each point to this skill increases party seeing range by 10%%. (Party skill) Max level: 10"),
  ("reserved_1",) + reserved_skill, 
  ("pathfinding","Path-finding",sf_base_att_int|sf_effects_party,10,"Party map speed is increased by 4%% per skill level. (Party skill) Max level: 10"), 
  ("tracking","Tracking",sf_base_att_int|sf_effects_party,10,"Tracks become more informative. (Party skill) Max level: 10"),
  ("reserved_2",) + reserved_skill, 
  ("cooking","Cooking",sf_base_att_int|sf_effects_party,10,"Every level of this skill increases the food bonus to party morale by 10%%, reduces the consumption of foods by 5%%. (Party skill) Max level: 10"), 
  ("reserved_6",) + reserved_skill, 
  ("reserved_7",) + reserved_skill, 
  ("reserved_8",) + reserved_skill, 
  ("precise_shot","Precise Shot",sf_base_att_agi|sf_inactive,10,"Each point to this skill increases ranged damage by 4%% and increases shot accuracy by 2%% (excludes throwing weapons) . (Personal skill) Max level: 10"), 
  ("horse_archery","Horse Archery",sf_base_att_agi,10,"Reduces damage and accuracy penalties for archery and throwing from horseback. (Personal skill) Max level: 10"),
  ("riding","Riding",sf_base_att_agi,10,"Enables you to ride horses of higher difficulty levels and increases your riding speed and manuever. Reduces damage to you and your horse by 4%% per skill level when you are on horse.  (Personal skill) Max level: 10"),
  ("athletics","Athletics",sf_base_att_agi,10,"Improves your running speed. Reduces damage to you by 4%% per skill level when you are on foot. (Personal skill)"),
  ("shield","Shield",sf_base_att_agi|sf_inactive,10,"Reduces damage to shields (by 8%% per skill level) and improves shield speed and coverage. (Personal skill) Max level: 10"),
  ("weapon_master","Weapon Master",sf_base_att_agi,10,"Reduces damage to shields (by 8%% per skill level) and improves shield speed and coverage. Makes it easier to learn weapon proficiencies and increases the proficiency limits. Limits go as: 60, 100, 140, 180, 220, 260, 300, 340, 380, 420, 460. (Personal skill) Max level: 10"),
  ("reserved_9",) + reserved_skill, 
  ("looting","Looting",sf_base_att_agi|sf_effects_party,10,"This skill increases the amount of loot obtained by 10%% per skill level and increases the chance to get the special items (Party skill). Increases inventory capacity by +6 per skill level (Personal skill). Max level: 10"), 
  ("power_one_handed","Power One Handed",sf_base_att_str|sf_inactive,15,"Each point to this skill increases one handed weapon damage by 9%%. (Personal skill) Max level: 15"), 
  ("power_two_handed","Power Two Handed",sf_base_att_str|sf_inactive,15,"Each point to this skill increases two handed weapon damage by 8%%. (Personal skill) Max level: 15"), 
  ("power_polearm","Power Polearm",sf_base_att_str|sf_inactive,15,"Each point to this skill increases polearm damage by 10%%. (Personal skill) Max level: 15"), 
  ("power_draw","Power Draw",sf_base_att_str,15,"Lets character use more powerful bows. Each point to this skill (up to four plus power-draw requirement of the bow) increases bow damage by 14%%. (Personal skill) Max level: 15"),
  ("power_throw","Power Throw",sf_base_att_str,15,"Each point to this skill increases throwing damage by 10%%. (Personal skill) Max level: 15"),
  ("power_strike","Power Strike",sf_base_att_str,15,"Each point to this skill increases melee damage by 8%%. (Personal skill) Max level: 15"), 
  ("ironflesh","Ironflesh",sf_base_att_str,15,"Each point to this skill increases hit points by +2. Reduces 1 damage to you per skill level. For soldiers, each point to this skill gives a 3%% chance to be wounded rather than killed by a mortally struck. (Personal skill) Max level: 15"), 
  ("physique","Physique",sf_base_att_str|sf_inactive,10,"Reduces damage suffered by 4%% per skill level. (Personal skill) Max level: 10"), 
  ("reserved_3",) + reserved_skill, 
  ## skill overhaul
  ("reserved_16",) + reserved_skill, 
  ("reserved_17",) + reserved_skill, 
  ("reserved_18",) + reserved_skill, 
]
