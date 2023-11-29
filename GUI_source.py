# Definitions for various imports/constants to be used by Inheritance_GUI

# Imports
from PyQt6.QtWidgets import (
    QApplication, 
    QLabel, 
    QMessageBox,
    QWidget,
    QMainWindow, 
    QGridLayout, 
    QHBoxLayout,
    QVBoxLayout,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
    QPushButton,
    QComboBox,
    QFrame,
    QSizePolicy,
    QDialog,
    QDialogButtonBox,
    QSpacerItem,
    QRadioButton,
    QCheckBox,
)
from PyQt6 import (
    QtGui, 
    QtWidgets
)
from PyQt6.QtCore import (
    Qt,
    QUrl,
    QTimer
)
from PyQt6.QtGui import (
    QPixmap,
    QPalette, 
    QFont
)
from PyQt6.QtMultimedia import (
    QSoundEffect,
    QMediaPlayer,
    QAudioOutput
)

import sys, time
from BEXP_calcs import *


# Various Constant Definitions
# Dimensions
WIDTH       =   600
HEIGHT      =   150
LINE_WIDTH  =   1
IMG_WIDTH   =   int(0.4*WIDTH)
IMG_HEIGHT  =   int(0.25*HEIGHT)

# Font
TITLE_FONT  =   'Helvetica'
TITLE_SIZE  =   24
LBL_FONT    =   'Helvetica'
LBL_SIZE    =   12
FORM_FONT   =   'Helvetica'
FORM_SIZE   =   8
HEADING_SZ  =   16

# Alignment flags
LEFT    =   Qt.AlignmentFlag.AlignLeft
CENTER  =   Qt.AlignmentFlag.AlignCenter
RIGHT   =   Qt.AlignmentFlag.AlignRight

# Colors for various buttons/fields
LTBLUE  =   "#b8e0f5"
LTTAN   =   "#faf2cd"

# Colors to be passed to QtQui.Color(R,G,B)
COL_LTGRAY      =   (212,212,212)
COL_WHT         =   (0,0,0)
COL_BEXP_GREEN  =   (2,249,2)

# Specific colors for various types of elements
SEP_COL     =   COL_WHT

# Music Defaults
BGM             =   'Resources/BGM.mp3'
BGM_VOL         =   0.1
BGM_LOOPS       =   -1      # Infinite Loops

# Images
APP_ICON        =   'Resources/AppIcon.png'

# Mode for button event handling
MODE_STATS      =   0
MODE_GROWTHS    =   1
MODE_BOTH       =   2

# For indexing into arrays
MOTHER  =   0
FATHER  =   1

LEVEL   =   0
PROMO   =   0
STATS   =   1

SON     =   0
DGHTR   =   1

# Misc Constants
DELAY   =   500     # ms

# Error Messages
PARENT_ERROR    =   "ERROR: Invalid Parent Combination"
STAT_ERROR      =   "ERROR: Invalid Stat Selection(s)"
LVL_ERROR       =   "ERROR: Invalid Level Selection(s)"

# Dialog Messages
WELCOME         =   """ Welcome to the FE10 BEXP Cost Calculator!
This program lets you calculate the total BEXP Cost for any (valid) pair of starting and ending levels! 
Apart from level range, you can also set difficulty, if they're laguz, and even mute the BGM if you want!
I hope you enjoy!"""

LVL_PROMPT      =   "Enter Level for which average stats will be calculated"
AVG_STAT_BTN    =   "Calculate Average Stats"