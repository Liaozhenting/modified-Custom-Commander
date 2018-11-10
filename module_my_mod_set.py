from header_operations import *
from ID_items import *
from ID_troops import *
from ID_strings import *
from module_constants import *
from module_items import *
from header_item_modifiers import *

###################################################
# module_my_mod_set.py
# This file contains many defines of my own mod.
###################################################


# def set_item_data():
  # item_data = []
  # for i_item in xrange(len(items)):
    
    # ## armor type
    # # if items[i_item][7] == imodbits_cloth:
      # # item_data.append((item_set_slot, i_item, slot_armor_type, armor_cloth))
    # # elif items[i_item][7] == imodbits_armor:
      # # item_data.append((item_set_slot, i_item, slot_armor_type, armor_armor))
    # # elif items[i_item][7] == imodbits_plate:
      # # item_data.append((item_set_slot, i_item, slot_armor_type, armor_plate))
    
    # ## item_best_modifier
    # if items[i_item][7] == imodbits_bow:
      # item_data.append((item_set_slot, i_item, slot_item_best_modifier, imod_masterwork))
    # elif items[i_item][7] == imodbits_pick:
      # item_data.append((item_set_slot, i_item, slot_item_best_modifier, imod_balanced))
    # elif items[i_item][7] == imodbits_none:
      # item_data.append((item_set_slot, i_item, slot_item_best_modifier, imod_plain))
    # else:
      # for i in xrange(43):
        # if items[i_item][7] >> i == 1:
          # item_data.append((item_set_slot, i_item, slot_item_best_modifier, i))
          
  ## item_modifier
  # for i_modifier in xrange(len(modifiers)):
    # item_data.append((item_set_slot, i_modifier, slot_item_modifier_multiplier, modifiers[i_modifier][1]))
  # return item_data[:]
  
# modifiers = [
  # (imod_plain, 100), 
  # (imod_cracked, 50), 
  # (imod_rusty, 55), 
  # (imod_bent, 65), 
  # (imod_chipped, 72), 
  # (imod_battered, 75), 
  # (imod_poor, 80), 
  # (imod_crude, 83), 
  # (imod_old, 86), 
  # (imod_cheap, 90), 
  # (imod_fine, 190), 
  # (imod_well_made, 250), 
  # (imod_sharp, 160), 
  # (imod_balanced, 350), 
  # (imod_tempered, 670), 
  # (imod_deadly, 850), 
  # (imod_exquisite, 1450), 
  # (imod_masterwork, 1750), 
  # (imod_heavy, 190), 
  # (imod_strong, 490), 
  # (imod_powerful, 320), 
  # (imod_tattered, 50), 
  # (imod_ragged, 70), 
  # (imod_rough, 60), 
  # (imod_sturdy, 170), 
  # (imod_thick, 260), 
  # (imod_hardened, 390), 
  # (imod_reinforced, 650), 
  # (imod_superb, 250), 
  # (imod_lordly, 1150), 
  # (imod_lame, 40), 
  # (imod_swaybacked, 60), 
  # (imod_stubborn, 90), 
  # (imod_timid, 180), 
  # (imod_meek, 180), 
  # (imod_spirited, 650), 
  # (imod_champion, 1450), 
  # (imod_fresh, 100), 
  # (imod_day_old, 100), 
  # (imod_two_day_old, 90), 
  # (imod_smelling, 40), 
  # (imod_rotten, 5), 
  # (imod_large_bag, 190),
# ]

def keys_array():
  keys_list = []
  for key_no in xrange(len(keys)):
    keys_list.append((troop_set_slot, "trp_temp_array_a", key_no, keys[key_no]))
    #keys_list.append((troop_set_slot, "trp_temp_array_b", key_no, str_key_0+key_no))
  return keys_list[:]
  
keys = [key_0, key_1, key_2, key_3, key_4, key_5, key_6, key_7, key_8, key_9, key_a, key_b, key_c, key_d, key_e, key_f, key_g, key_h, key_i, key_j, key_k, key_l, key_m, key_n, key_o, key_p, key_q, key_r, key_s, key_t, key_u, key_v, key_w, key_x, key_y, key_z, key_numpad_0, key_numpad_1, key_numpad_2, key_numpad_3, key_numpad_4, key_numpad_5, key_numpad_6, key_numpad_7, key_numpad_8, key_numpad_9, key_num_lock, key_numpad_slash, key_numpad_multiply, key_numpad_minus, key_numpad_plus, key_numpad_enter, key_numpad_period, key_insert, key_delete, key_home, key_end, key_page_up, key_page_down, key_up, key_down, key_left, key_right, key_f1, key_f2, key_f3, key_f4, key_f5, key_f6, key_f7, key_f8, key_f9, key_f10, key_f11, key_f12, key_space, key_escape, key_enter, key_tab, key_back_space, key_open_braces, key_close_braces, key_comma, key_period, key_slash, key_back_slash, key_equals, key_minus, key_semicolon, key_apostrophe, key_tilde, key_caps_lock, key_left_shift, key_right_shift, key_left_control, key_right_control, key_left_alt, key_right_alt]


#def set_derivative_troops():
  #result_list = []
  #for row_no in xrange(len(derivative_troops)):
    #result_list.append((troop_set_slot, derivative_troops[row_no][0], slot_derivative_troop_cavalry_style,  derivative_troops[row_no][1]))
    #result_list.append((troop_set_slot, derivative_troops[row_no][0], slot_derivative_troop_infantry_style, derivative_troops[row_no][2]))
    #result_list.append((troop_set_slot, derivative_troops[row_no][0], slot_derivative_troop_center_style,   derivative_troops[row_no][3]))
    #result_list.append((troop_set_slot, derivative_troops[row_no][0], slot_derivative_troop_player_style,   derivative_troops[row_no][3]))
  #return result_list[:]

#derivative_troops = [
  #("trp_swadian_infantry", "trp_swadian_light_cavalry", "trp_swadian_double_hander", "trp_swadian_infantry"),
  #("trp_swadian_sergeant", "trp_swadian_veteran_light_cavalry", "trp_swadian_veteran_double_hander", "trp_swadian_sergeant"),
  #("trp_swadian_double_hander", "trp_swadian_light_cavalry", "trp_swadian_double_hander", "trp_swadian_infantry"),
  #("trp_swadian_veteran_double_hander", "trp_swadian_veteran_light_cavalry", "trp_swadian_veteran_double_hander", "trp_swadian_sergeant"),
  #("trp_swadian_light_cavalry", "trp_swadian_light_cavalry", "trp_swadian_double_hander", "trp_swadian_infantry"),
  #("trp_swadian_veteran_light_cavalry", "trp_swadian_veteran_light_cavalry", "trp_swadian_veteran_double_hander", "trp_swadian_sergeant"),

  #("trp_vaegir_infantry", "trp_vaegir_light_cavalry", "trp_vaegir_berserker", "trp_vaegir_infantry"),
  #("trp_vaegir_guard", "trp_vaegir_veteran_light_cavalry", "trp_vaegir_veteran_berserker", "trp_vaegir_guard"),
  #("trp_vaegir_berserker", "trp_vaegir_light_cavalry", "trp_vaegir_berserker", "trp_vaegir_infantry"),
  #("trp_vaegir_veteran_berserker", "trp_vaegir_veteran_light_cavalry", "trp_vaegir_veteran_berserker", "trp_vaegir_guard"),
  #("trp_vaegir_light_cavalry", "trp_vaegir_light_cavalry", "trp_vaegir_berserker", "trp_vaegir_infantry"),
  #("trp_vaegir_veteran_light_cavalry", "trp_vaegir_veteran_light_cavalry", "trp_vaegir_veteran_berserker", "trp_vaegir_guard"),

  #("trp_khergit_lancer", "trp_khergit_lancer", "trp_khergit_dismounted_lancer", "trp_khergit_dismounted_lancer"),
  #("trp_khergit_dismounted_lancer", "trp_khergit_lancer", "trp_khergit_dismounted_lancer", "trp_khergit_dismounted_lancer"),

  #("trp_nord_warrior", "trp_nord_scout", "trp_nord_thrower","trp_nord_warrior"),
  #("trp_nord_veteran", "trp_nord_veteran_scout", "trp_nord_veteran_thrower","trp_nord_veteran"),
  #("trp_nord_thrower", "trp_nord_scout", "trp_nord_thrower","trp_nord_warrior"),
  #("trp_nord_veteran_thrower", "trp_nord_veteran_scout", "trp_nord_veteran_thrower","trp_nord_veteran"),
  #("trp_nord_scout", "trp_nord_scout", "trp_nord_thrower","trp_nord_warrior"),
  #("trp_nord_veteran_scout", "trp_nord_veteran_scout", "trp_nord_veteran_thrower","trp_nord_veteran"),
  
  #("trp_rhodok_veteran_spearman", "trp_rhodok_scout", "trp_rhodok_thrower", "trp_rhodok_veteran_spearman"),
  #("trp_rhodok_sergeant", "trp_rhodok_veteran_scout", "trp_rhodok_veteran_thrower", "trp_rhodok_sergeant"),
  #("trp_rhodok_thrower", "trp_rhodok_scout", "trp_rhodok_thrower", "trp_rhodok_veteran_spearman"),
  #("trp_rhodok_veteran_thrower", "trp_rhodok_veteran_scout", "trp_rhodok_veteran_thrower", "trp_rhodok_sergeant"),
  #("trp_rhodok_scout", "trp_rhodok_scout", "trp_rhodok_thrower", "trp_rhodok_veteran_spearman"),
  #("trp_rhodok_veteran_scout", "trp_rhodok_veteran_scout", "trp_rhodok_veteran_thrower", "trp_rhodok_sergeant"),
  
  #("trp_sarranid_infantry", "trp_sarranid_light_cavalry", "trp_sarranid_axeman", "trp_sarranid_infantry"),
  #("trp_sarranid_guard", "trp_sarranid_veteran_light_cavalry", "trp_sarranid_veteran_axeman", "trp_sarranid_guard"),
  #("trp_sarranid_axeman", "trp_sarranid_light_cavalry", "trp_sarranid_axeman", "trp_sarranid_infantry"),
  #("trp_sarranid_veteran_axeman", "trp_sarranid_veteran_light_cavalry", "trp_sarranid_veteran_axeman", "trp_sarranid_guard"),
  #("trp_sarranid_light_cavalry", "trp_sarranid_light_cavalry", "trp_sarranid_axeman", "trp_sarranid_infantry"),
  #("trp_sarranid_veteran_light_cavalry", "trp_sarranid_veteran_light_cavalry", "trp_sarranid_veteran_axeman", "trp_sarranid_guard"),
#]


#def set_commensalism_troops():
  #result_list = []
  #for row_no in xrange(len(commensalism_troops)):
    #if len(commensalism_troops[row_no]) == 3:
      #result_list.append((troop_set_slot, commensalism_troops[row_no][0], slot_troop_commensalism_troop, commensalism_troops[row_no][2]))
      #result_list.append((troop_set_slot, commensalism_troops[row_no][1], slot_troop_commensalism_troop, commensalism_troops[row_no][2]))
    #else:
      #result_list.append((troop_set_slot, commensalism_troops[row_no][0], slot_troop_commensalism_troop, commensalism_troops[row_no][1]))
      #result_list.append((troop_set_slot, commensalism_troops[row_no][1], slot_troop_commensalism_troop, commensalism_troops[row_no][0]))
  #return result_list[:]

#commensalism_troops = [
  #("trp_bandit", "trp_brigand"),
  #("trp_forest_bandit", "trp_chief_forest_bandit"),
  #("trp_taiga_bandit", "trp_chief_taiga_bandit"),
  #("trp_steppe_bandit", "trp_chief_steppe_bandit"),
  #("trp_sea_raider", "trp_chief_sea_raider"),
  #("trp_mountain_bandit", "trp_chief_mountain_bandit"),
  #("trp_desert_bandit", "trp_chief_desert_bandit"),
  #("trp_swadian_infantry", "trp_swadian_sergeant"),
  #("trp_swadian_crossbowman", "trp_swadian_sharpshooter"),
  #("trp_swadian_man_at_arms", "trp_swadian_knight"),
  #("trp_vaegir_archer", "trp_vaegir_marksman"),
  #("trp_vaegir_infantry", "trp_vaegir_guard"),
  #("trp_vaegir_horseman", "trp_vaegir_knight"),
  #("trp_khergit_horse_archer", "trp_khergit_veteran_horse_archer", 0),
  #("trp_khergit_horseman", "trp_khergit_lancer", 0),
  #("trp_nord_veteran", "trp_nord_champion"),
  #("trp_nord_archer", "trp_nord_veteran_archer", 0),
  #("trp_rhodok_veteran_spearman", "trp_rhodok_sergeant"),
  #("trp_rhodok_veteran_crossbowman", "trp_rhodok_sharpshooter"),
  #("trp_sarranid_infantry", "trp_sarranid_guard"),
  #("trp_sarranid_archer", "trp_sarranid_master_archer"),
  #("trp_sarranid_horseman", "trp_sarranid_mamluke"),
  #("trp_ranger_warden", "trp_ranger_huntmaster"),
  #("trp_ranger_shieldmaiden", "trp_ranger_huntress"),
#]