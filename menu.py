# create a menu called IsaacUtilities at the top toolbar
# replace this with whatever menu name you'd like
utilitiesMenu = nuke.menu('Nuke').addMenu('IsaacUtilities')

from extractSelectionStamps import *
utilitiesMenu.addCommand('Extract Selection and reconnect Stamps', 'extractSelectionStamps()', 'ctrl+shift+x', shortcutContext=2)
