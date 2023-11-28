from GUI_source import *
from Music_Player import *

class LevelForm():
    def __init__(self):
        self.Lvl = QLineEdit()

def create_label(text, alignment, font, size):
    label = QLabel()
    label.setText(text)
    label.setFont(QFont(font, size))
    label.setAlignment(alignment)
    return label

class BEXP_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Initialize window and basic layout
        self.setWindowTitle('Radiant Dawn BEXP Calculator')
        self.setFixedSize(WIDTH, HEIGHT)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)

        # Take Input for Starting/Final Level
        startLvlForm = QFormLayout()
        self.startLvlVal = LevelForm()
        startLvlForm.addRow(create_label("Starting Level:", LEFT, TITLE_FONT, HEADING_SZ), self.startLvlVal.Lvl)
        self.generalLayout.addLayout(startLvlForm)

        endLvlForm = QFormLayout()
        self.endLvlVal = LevelForm()
        endLvlForm.addRow(create_label("Ending Level:", LEFT, TITLE_FONT, HEADING_SZ), self.endLvlVal.Lvl)
        self.generalLayout.addLayout(endLvlForm)

        # Create Difficulty Mode Options
        difficultyOptions = QHBoxLayout()
        self.radio = QRadioButton("Easy", self)
        self.radio.toggled.connect(self.updateDifficulty)
        difficultyOptions.addWidget(self.radio)

        self.radio = QRadioButton("Normal", self)
        self.radio.toggled.connect(self.updateDifficulty)
        self.radio.toggle()
        difficultyOptions.addWidget(self.radio)

        self.radio = QRadioButton("Hard", self)
        self.radio.toggled.connect(self.updateDifficulty)
        difficultyOptions.addWidget(self.radio)

        self.diffMod = DIFF_MOD_NORMAL

        self.laguzCheck = QCheckBox(text="Laguz?")
        difficultyOptions.addWidget(self.laguzCheck)

        self.generalLayout.addLayout(difficultyOptions)

        # Button to Calculate Final Bexp Cost
        calcBtn = QPushButton(text="Calculate Total BEXP Cost")
        calcBtn.clicked.connect(self.displayBexpCost)
        self.generalLayout.addWidget(calcBtn)

        self.bexpCostDisplay = QHBoxLayout()
        self.bexpCostLbl = create_label("TOTAL BEXP COST:", LEFT, TITLE_FONT, HEADING_SZ)
        self.bexpCostDisplay.addWidget(self.bexpCostLbl)
        self.totalBexpCost = create_label(str(0), RIGHT, TITLE_FONT, HEADING_SZ)
        self.bexpCostDisplay.addWidget(self.totalBexpCost)
        self.generalLayout.addLayout(self.bexpCostDisplay)

        # Music Player for BGM
        self.music_player = MusicPlayer(BGM)

        # self.center()
        self.show()
        self.music_player.play_BGM(BGM_VOL, BGM_LOOPS)

    def updateDifficulty(self):
        match self.sender().text():
            case "Easy":
                self.diffMod = DIFF_MOD_EASY
            case "Normal":
                self.diffMod = DIFF_MOD_NORMAL
            case "Hard":
                self.diffMod = DIFF_MOD_HARD

    def displayBexpCost(self):
        if(self.laguzCheck.isChecked()):
            lvl_mod = LVL_MOD_LAGUZ
        else:
            lvl_mod = LVL_MOD_BEORC
        self.totalBexpCost.setText(str(calc_bexp_cost(int(self.startLvlVal.Lvl.text()), 
                                                      int(self.endLvlVal.Lvl.text()), 
                                                      lvl_mod, 
                                                      self.diffMod)))
        