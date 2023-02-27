# ///////////////////////////////////////////////////////////////
import sys
from PySide6 import QtCore
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from modules import ui_main
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget
import os
from PyQt6.QtWidgets import QListWidget, QListWidgetItem
import shutil
import speech_recognition as sr
import sys
import platform
from CV2_loading import loadingscreen
# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *

os.environ["QT_FONT_DPI"] = "90" # FIX Problem for High DPI and Scale above 100%
# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None
modules = None
#////////////////////////////////////////////////////////////////////
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # apng objects
        #///////////////////////////////////////////////////////////////
        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui
        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True
        #////////////////////////////////////////////////////////////////

        #self.ListView = self.ui.listWidget
        
        # train buton
        self.train_input = self.ui.inputwords
        self.ui.inputwords = QLineEdit()
        self.ui.Train_bttn.clicked.connect(self.train)#????????train to??????????

        # FSL BUTTON 
        self.ui.Start_FSL_Recognition.clicked.connect(self.Start_FSL_Recognition)
        # sa TTS function Buttons
        self.ui.Start_Voice_Dection.clicked.connect(self.start_voice_detection)
        self.ui.Stop_Voice_Detection.clicked.connect(self.stop_voice_detection)
        # CREATE A SPEECH RECOGNIZER OBJECT
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()
        #/////////////////////////////////////////////////////////////////////////////////////////
        # pang delete ng folder
        # ///////////////////////////////////////////////////////////////
        # Add_and_Train_words BUTTON
        # ...
        # ///////////////////////////////////////////////////////////////
        # ...
        #train function
        #/////// Start button ng/////////////////////////////////////////////////////////////////
        #////////////////////////////////////////////////////////////////////////////////////////
        # ///////////////////////////////////////////////////////////////
        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))
        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)
        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        #widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////s
        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_new.clicked.connect(self.buttonClick)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)
        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)
        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()
        # SET CUSTOM THEME
        useCustomTheme = False
        #themeFile = "themes\py_dracula_light.qss"
        themeFile = "themes\py_dracula_dark.qss"
        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)
            # SET HACKS
            AppFunctions.setThemeHack(self)
        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))
    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        self.ListView()
        btn = self.sender()
        btnName = btn.objectName()
        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        # SHOW NEW PAGE
        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU
            self.ListView() #this will refresh the new_page frame of the 
        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')
    # ///////////////////////////////////////////////////////////////
    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)
    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()
        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
    #///////////////////////////////////////////////////////////////////
    # pang FSL detection function
    def Start_FSL_Recognition(self):
       #import main_function  #and call desired function
        # PANG TAWAG NG EXTERNAL LOADING GUI PANG NA NAKA THREAD SA MAIN_MAINFUNCTION.PY
        from PySide2.QtWidgets import QApplication
        if __name__ == '__main__':
            app = QApplication([])
            loading_screen = loadingscreen()
            app.exec_()

        # Do your FSL Recognition tasks here
        
    #//////////////////////////////////////////////////////////////////
    #//////////////////////////////////////////////////////////////////
    #//////////////////////////////////////////////////////////////////
    # SA TTS function define dto    
    def start_voice_detection(self):
        self.ui.textbox.clear()
        with self.mic as source:
            self.r.adjust_for_ambient_noise(source)
            audio = self.r.listen(source)
            try:
                text = self.r.recognize_google(audio, language='tl')
                self.ui.textbox.appendPlainText(text)
            except sr.UnknownValueError:
                self.ui.textbox.appendPlainText("Could not understand audio")
            except sr.RequestError as e:
                self.ui.textbox.appendPlainText("Error; {0}".format(e))
    def stop_voice_detection(self):
        self.r.pause_threshold = 1
    

    # pang train
    def train(self):
        import data_collection
        #import panginputngwords
        text_input = self.train_input.text().strip()
        if text_input:
            actions = data_collection.train_pangwords(text_input)
            self.train_input.clear()
            import model
        else:
            QMessageBox.warning(self, "Bababala!", "Maaring ulitin at mag lagay ng impormasyon sa teksfield")
        
        self.ListView()
        

    # pang delete
    def ListView(self):
        # pang list view
        #self.ui.listWidget = QListWidget()
        data_path = os.path.join("data")
        folders = os.listdir(data_path)
        self.ui.listWidget.clear()
        for folder in folders:
            item = QListWidgetItem(folder)
            self.ui.listWidget.addItem(item)
        
        # pang delete button
        self.ui.pushButton.clicked.connect(self.delete)
   
        # babalikan kita, ung pang return ng value pang refresh ng folder 
        # after mag delete return sa buttun ng newpage for refresh
 # refresh the list of folders
    def delete(self):
        confirm = QMessageBox.question(self, 'Confirm', "Are you sure you want to delete the selected folder?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirm == QMessageBox.Yes:
            data_path = os.path.join("data")
            selected_folder = [self.ui.listWidget.item(i).text() for i in range(self.ui.listWidget.count()) if self.ui.listWidget.item(i).isSelected()]
            if selected_folder:
                folder = selected_folder[0]
                shutil.rmtree(os.path.join(data_path, folder))
                QMessageBox.information(self, "Deleted", "Selected folder has been deleted.")
                self.ListView()
            else:
                QMessageBox.warning(self, "Warning", "No folder selected.")
        

#/////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////
## ==> SPLASH SCREEN
from ui_splash_screen import Ui_SplashScreen
## ==> GLOBALS
counter = 0
# YOUR APPLICATION
class app(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = MainWindow()
        self.ui.setupUi(self)
# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        ## UI ==> INTERFACE CODES
        ########################################################################
        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)
        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(5)
        # CHANGE DESCRIPTION
        # Initial Text
        self.ui.label_description.setText("<strong>WELCOME</strong> TO LETOPEA")
        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> Languages"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))
        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##
    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):
        global counter
        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)
        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()
            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.close()
            # CLOSE SPLASH SCREEN
        # INCREASE COUNTER
        counter += 1
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec())
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    MainWindow()
    window = MainWindow()
    sys.exit(app.exec())
