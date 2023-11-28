from GUI_source import *
from Music_Player import *

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


        self.startLvlTier = 0
        self.EndLvlTier = 1


        startLvlForm = QHBoxLayout()

        startLvlForm.addWidget(create_label("Starting Level:", RIGHT, LBL_FONT, HEADING_SZ))
        self.startTierDropdown = self.createTierDropdown()
        startLvlForm.addWidget(self.startTierDropdown)
        self.startLvlDropdown = self.createLvlDropdown()
        startLvlForm.addWidget(self.startLvlDropdown)
        self.generalLayout.addLayout(startLvlForm)

        endLvlForm = QHBoxLayout()
        endLvlForm.addWidget(create_label("Ending Level:", RIGHT, LBL_FONT, HEADING_SZ))
        self.endTierDropdown = self.createTierDropdown()
        endLvlForm.addWidget(self.endTierDropdown)
        self.endLvlDropdown = self.createLvlDropdown()
        endLvlForm.addWidget(self.endLvlDropdown)
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
        self.bexpCostLbl = create_label("TOTAL BEXP COST:", RIGHT, TITLE_FONT, HEADING_SZ)
        self.bexpCostDisplay.addWidget(self.bexpCostLbl)
        self.totalBexpCost = create_label(str(0), LEFT, TITLE_FONT, HEADING_SZ)
        self.bexpCostDisplay.addWidget(self.totalBexpCost)
        self.generalLayout.addLayout(self.bexpCostDisplay)

        # Music Player for BGM
        self.music_player = MusicPlayer(BGM)

        # self.center()
        self.show()
        self.music_player.play_BGM(BGM_VOL, BGM_LOOPS)

    def updateStartLvlTier(self):
        match self.sender().text():
            case "Tier 1":
                self.startLvlTier = 0
            case "Tier 2":
                self.startLvlTier = 1
            case "Tier 3":
                self.startLvlTier = 2

    def updateEndLvlTier(self):
        match self.sender().text():
            case "Tier 1":
                self.endLvlTier = 0
            case "Tier 2":
                self.endLvlTier = 1
            case "Tier 3":
                self.endLvlTier = 2

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
        start_lvl = convertToInternalLevel(int(self.startTierDropdown.currentText()[5:])-1, int(self.startLvlDropdown.currentText()[6:]))
        end_lvl = convertToInternalLevel(int(self.endTierDropdown.currentText()[5:])-1, int(self.endLvlDropdown.currentText()[6:]))
        self.totalBexpCost.setText(str(calc_bexp_cost(start_lvl, 
                                                      end_lvl, 
                                                      lvl_mod, 
                                                      self.diffMod)))
        
    def createLvlDropdown(self):
        lvlDropdown = QComboBox()
        for lvl in range(MAX_DISP_LEVEL):
            lvlDropdown.addItem("Level "+str(lvl+1))
        return lvlDropdown
    
    def createTierDropdown(self):
        tierDropdown = QComboBox()
        tierDropdown.addItem("Tier "+str(1))
        tierDropdown.addItem("Tier "+str(2))
        tierDropdown.addItem("Tier "+str(3))
        return tierDropdown
