
# Point export_dir to the folder you will be keeping your module
# Make sure you use forward slashes (/) and NOT backward slashes (\)

export_dir = "../"

# Several possible variants for export_dir variable:

# Warband being installed to C:/Games
#export_dir = "C:/Games/Mount&Blade Warband/Modules/Native/"

# Warband being installed to default path on Windows XP or Vista
#export_dir = "C:/Programs Files/Mount&Blade Warband/Modules/Native/"

# Warband being installed to default path on Windows 7+
#export_dir = "C:/Programs Files (x86)/Mount&Blade Warband/Modules/Native/"

# Likely paths for Steam Warband installation:
#export_dir = "C:/Programs Files/Steam/steamapps/common/Mount&Blade Warband/Modules/Native/"
#export_dir = "C:/Programs Files (x86)/Steam/steamapps/common/Mount&Blade Warband/Modules/Native/"



# Lav: ensure that the export_dir has a trailing slash
export_dir = '%s/' % export_dir.replace('\\', '/').rstrip('/')