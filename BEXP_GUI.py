from GUI_source import *
from Music_Player import *
from random import randint

def create_label(text, alignment, font, size):
    label = QLabel()
    label.setText(text)
    label.setFont(QFont(font, size))
    label.setAlignment(alignment)
    return label

class Welcome_Dialog(QDialog):
    def __init__(self, welcome_msg):
        super().__init__()
        layout = QGridLayout()

        # Create welcome message
        self.label = QLabel()
        self.label.setText(welcome_msg)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label, 0, 0, 1, 4)

        # Create confirmation button
        startBtn = QPushButton("Get Started")
        startBtn.clicked.connect(self.close)
        layout.addWidget(startBtn, 1, 1, 1, 2)

        self.setLayout(layout)
        self.setWindowTitle("Welcome")

class BEXP_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.welcome_dlg = Welcome_Dialog(WELCOME)
        self.initTimer()

    def initUI(self):
        # Initialize window and basic layout
        self.setWindowTitle('Radiant Dawn BEXP Calculator')
        # self.setStyleSheet(f"background-color: {LTGRAY};")
        self.setFixedSize(WIDTH, HEIGHT)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)


        self.startLvlTier = 0
        self.EndLvlTier = 1
        self.createDropdowns()


        startLvlForm = QHBoxLayout()
        startLvlForm.addWidget(create_label("Starting Level:", RIGHT, LBL_FONT, HEADING_SZ), 4)
        self.startTierDropdowns = QStackedWidget()
        # self.startTierDropdown = self.start_tier_dropdown_beorc
        self.startTierDropdowns.addWidget(self.start_tier_dropdown_beorc)
        self.startTierDropdowns.addWidget(self.start_tier_dropdown_laguz)
        startLvlForm.addWidget(self.startTierDropdowns, 2)
        # self.startLvlDropdown = self.start_lvl_dropdown_beorc
        self.startLvlDropdowns = QStackedWidget()
        self.startLvlDropdowns.addWidget(self.start_lvl_dropdown_beorc)
        self.startLvlDropdowns.addWidget(self.start_lvl_dropdown_laguz)
        startLvlForm.addWidget(self.startLvlDropdowns, 3)
        self.generalLayout.addLayout(startLvlForm)

        endLvlForm = QHBoxLayout()
        endLvlForm.addWidget(create_label("Ending Level:", RIGHT, LBL_FONT, HEADING_SZ), 4)
        self.endTierDropdowns = QStackedWidget()
        # self.endTierDropdown = self.end_tier_dropdown_beorc
        self.endTierDropdowns.addWidget(self.end_tier_dropdown_beorc)
        self.endTierDropdowns.addWidget(self.end_tier_dropdown_laguz)
        endLvlForm.addWidget(self.endTierDropdowns, 2)
        self.endLvlDropdowns = QStackedWidget()
        # self.endLvlDropdown = self.end_lvl_dropdown_beorc
        self.endLvlDropdowns.addWidget(self.end_lvl_dropdown_beorc)
        self.endLvlDropdowns.addWidget(self.end_lvl_dropdown_laguz)
        endLvlForm.addWidget(self.endLvlDropdowns, 3)
        self.generalLayout.addLayout(endLvlForm)

        # Create Difficulty Mode Options
        difficultyOptions = QHBoxLayout()

        diffLbl = create_label("Difficulty:", LEFT, LBL_FONT, LBL_SIZE)
        difficultyOptions.addWidget(diffLbl)

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
        self.laguzCheck.pressed.connect(self.updateDropdowns)
        difficultyOptions.addWidget(self.laguzCheck)

        # Check box to mute/unmute audio
        self.muteBox = QCheckBox(text="Mute Audio")
        self.muteBox.pressed.connect(self.updateAudio)
        difficultyOptions.addWidget(self.muteBox)

        self.generalLayout.addLayout(difficultyOptions)

        # Button to Calculate Final Bexp Cost
        calcBtn = QPushButton(text="Calculate Total BEXP Cost")
        calcBtn.clicked.connect(self.displayBexpCost)
        self.generalLayout.addWidget(calcBtn, 10)

        self.bexpCostDisplay = QHBoxLayout()
        self.bexpCostLbl = create_label("TOTAL BEXP COST:", RIGHT, TITLE_FONT, HEADING_SZ)
        self.bexpCostDisplay.addWidget(self.bexpCostLbl)
        self.totalBexpCost = create_label(str(0), LEFT, TITLE_FONT, HEADING_SZ)
        self.totalBexpCost.setStyleSheet("QLabel{color: #02db02;}")
        self.bexpCostDisplay.addWidget(self.totalBexpCost)
        self.generalLayout.addLayout(self.bexpCostDisplay)

        # Music Player for BGM
        if(randint(1,ODDS_OF_FUN) == 1):
            music = BACKUP
        else:
            music = BGM
        self.music_player = MusicPlayer(music)

        # self.center()
        self.show()
        # self.music_player.play_BGM(BGM_VOL, BGM_LOOPS)

    def initTimer(self):
        # Creates single-shot delay for welcome message
        QTimer.singleShot(DELAY, self.welcome_dlg.exec)
        QTimer.singleShot(DELAY, self.music_player.play_BGM)

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
            race = RACE_LAGUZ
            lvl_mod = LVL_MOD_LAGUZ
        else:
            race = RACE_BEORC
            lvl_mod = LVL_MOD_BEORC
        start_lvl = convertToInternalLevel(int(self.startTierDropdowns.currentWidget().currentText()[5:])-1, int(self.startLvlDropdowns.currentWidget().currentText()[6:]))
        end_lvl = convertToInternalLevel(int(self.endTierDropdowns.currentWidget().currentText()[5:])-1, int(self.endLvlDropdowns.currentWidget().currentText()[6:]))
        bexp_cost = calc_bexp_cost(start_lvl, end_lvl, lvl_mod, self.diffMod, race)
        if(bexp_cost < 0):
            display_error_msg("Invalid level range selected, please try again.")
            bexp_cost = 0
        self.totalBexpCost.setText(str(bexp_cost))
        
    def createLvlDropdown(self, max_lvl):
        lvlDropdown = QComboBox()
        for lvl in range(max_lvl):
            lvlDropdown.addItem("Level "+str(lvl+1))
        return lvlDropdown
    
    def createTierDropdown(self, max_tier):
        tierDropdown = QComboBox()
        for tier in range(max_tier):
            tierDropdown.addItem("Tier "+str(tier+1))
        return tierDropdown
    
    # Creates all lvl/tier dropdowns
    def createDropdowns(self):
        self.start_lvl_dropdown_beorc = self.createLvlDropdown(MAX_DISP_LVL_BEORC)
        self.start_lvl_dropdown_laguz = self.createLvlDropdown(MAX_DISP_LVL_LAGUZ)
        self.start_tier_dropdown_beorc = self.createTierDropdown(MAX_TIERS_BEORC)
        self.start_tier_dropdown_laguz = self.createTierDropdown(MAX_TIERS_LAGUZ)
        self.end_lvl_dropdown_beorc = self.createLvlDropdown(MAX_DISP_LVL_BEORC)
        self.end_lvl_dropdown_laguz = self.createLvlDropdown(MAX_DISP_LVL_LAGUZ)
        self.end_tier_dropdown_beorc = self.createTierDropdown(MAX_TIERS_BEORC)
        self.end_tier_dropdown_laguz = self.createTierDropdown(MAX_TIERS_LAGUZ)
    
    # Updates dropdown when switching between laguz and beorc
    def updateDropdowns(self):
        if(self.laguzCheck.isChecked()):
            # Switch to beorc
            self.startTierDropdowns.setCurrentIndex(RACE_BEORC)
            self.startLvlDropdowns.setCurrentIndex(RACE_BEORC)
            self.endTierDropdowns.setCurrentIndex(RACE_BEORC)
            self.endLvlDropdowns.setCurrentIndex(RACE_BEORC)
        else:
            # Switch to laguz
            self.startTierDropdowns.setCurrentIndex(RACE_LAGUZ)
            self.startLvlDropdowns.setCurrentIndex(RACE_LAGUZ)
            self.endTierDropdowns.setCurrentIndex(RACE_LAGUZ)
            self.endLvlDropdowns.setCurrentIndex(RACE_LAGUZ)
        self.resetDropdowns()

    # Resets dropdowns to have first item selected
    def resetDropdowns(self):
        self.start_tier_dropdown_beorc.setCurrentIndex(0)
        self.start_tier_dropdown_laguz.setCurrentIndex(0)
        self.start_lvl_dropdown_beorc.setCurrentIndex(0)
        self.start_lvl_dropdown_laguz.setCurrentIndex(0)
        self.end_tier_dropdown_beorc.setCurrentIndex(0)
        self.end_tier_dropdown_laguz.setCurrentIndex(0)
        self.end_lvl_dropdown_beorc.setCurrentIndex(0)
        self.end_lvl_dropdown_laguz.setCurrentIndex(0)
        

    def updateAudio(self):
        if(self.muteBox.isChecked()):
            self.music_player.audio_output.setVolume(BGM_VOL)
        else:
            self.music_player.audio_output.setVolume(0)

def display_error_msg(error_msg):
    msg_box = QMessageBox()
    msg_box.setText(error_msg)
    msg_box.exec()
