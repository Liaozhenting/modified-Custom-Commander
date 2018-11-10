@echo off
@del Process_Log.txt
echo Getting Misc Files .........
copy ".\misc files\*.*" ".\" >>Process_Log.txt
echo Start Processing...
echo ______________________________
echo.
py -2 process_init.py
py -2 process_global_variables.py
py -2 process_strings.py
py -2 process_skills.py
py -2 process_music.py
py -2 process_animations.py
py -2 process_meshes.py
py -2 process_sounds.py
py -2 process_skins.py
py -2 process_map_icons.py
py -2 process_factions.py
py -2 process_items.py
py -2 process_scenes.py
py -2 process_troops.py
py -2 process_particle_sys.py
py -2 process_scene_props.py
py -2 process_tableau_materials.py
py -2 process_presentations.py
py -2 process_party_tmps.py
py -2 process_parties.py
py -2 process_quests.py
py -2 process_info_pages.py
py -2 process_scripts.py
py -2 process_mission_tmps.py
py -2 process_game_menus.py
py -2 process_simple_triggers.py
py -2 process_dialogs.py
py -2 process_global_variables_unused.py
py -2 process_postfx.py
@del header_*.py
copy ".\ID_*.py" ".\misc files\" >>Process_Log.txt
@del ID_*.py
@del process_*.py
@del *.pyc
echo.
echo All Finish ...
echo Cleaning up...
echo ______________________________
echo.
echo Script processing has ended.
echo Press any key to exit. . .
pause>nul