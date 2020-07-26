from gui import MainPanel
import sys
from os import path


if getattr(sys, 'frozen', False):
    bundle_dir = getattr(sys, '_MEIPASS', path.abspath(path.dirname(__file__)))
    path_to_dat = path.abspath(path.join(bundle_dir, 'database.cwp'))
else:
    path_to_dat = 'database.cwp'

if __name__ == '__main__':
    gui = MainPanel(database_path=path_to_dat)
    gui.run()