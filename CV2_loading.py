

import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
# GUI FILE
from ui_cv_loading_screen import Ui_loadingScreen

# GLOBALS
counter = 0
jumper = 10
## ==> SPLASHSCREEN WINDOW
class loadingscreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_loadingScreen()
        self.ui.setupUi(self)

        ## ==>PANG SET NG INITIAL PROGRESS BAR TO (0) ZERO
        self.progressBarValue(0)

        ## ==> REMOVE STANDARD TITLE BAR
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) # Remove title bar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # Set background to transparent

        ## ==> APPLY DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.ui.circularBg.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(25)
 

        # Change Texts
        QtCore.QTimer.singleShot(1000, lambda: self.ui.labelLoadingInfo.setText("<strong>LOADING</strong> LANGUAGES"))
        QtCore.QTimer.singleShot(1500, lambda: self.ui.labelLoadingInfo.setText("<strong>LOADING</strong> LIBRARIES"))
        QtCore.QTimer.singleShot(2000, lambda: self.ui.labelLoadingInfo.setText("<strong>LOADING</strong> INTERFACE"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.labelLoadingInfo.setText("<strong>LOADING</strong> MODELS"))
        QtCore.QTimer.singleShot(6000, lambda: self.ui.labelLoadingInfo.setText("<strong>LOADING</strong> CAMERA IS OPENING"))
        
        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## DEF TO LOANDING
    ########################################################################
    def progress (self):
        global counter
        global jumper
        value = counter

        # HTML TEXT PERCENTAGE
        htmlText = """<p><span style=" font-size:69pt;">{VALUE}</span><span style=" font-size:40pt; vertical-align:super;">%</span></p>"""

        # REPLACE VALUE
        newHtml = htmlText.replace("{VALUE}", str(jumper))

        if(value > jumper):
            # APPLY NEW PERCENTAGE TEXT
            self.ui.labelPercentage.setText(newHtml)
            jumper += 1

        # SET VALUE TO PROGRESS BAR
        # fix max value error if > than 100
        if value >= 100: value = 1.000
        self.progressBarValue(value)

        # CLOSE SPLASH SCREE AND OPEN APP

        if counter > 100:
            # STOP TIMER
            self.timer.stop()
            import main_function
            self.close(self)     
        # INCREASE COUNTER
        counter += .5
      
       

    ## DEF PROGRESS BAR VALUE
    ########################################################################
    def progressBarValue(self, value):

        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
        QFrame{
        	border-radius: 150px;
        	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 150, 127, 0), stop:{STOP_2} rgba(255, 150, 50,255));
        }
        """

        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0

        # GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        # APPLY STYLESHEET WITH NEW VALUES
        self.ui.circularProgress.setStyleSheet(newStylesheet)

# IN THIS PART WHERE YOU LOAD THE ENTIRE WI
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = loadingscreen()
    sys.exit(app.exec_())
