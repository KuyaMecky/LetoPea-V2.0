from PyQt5 import QtWidgets, QtCore
from loginUI import Ui_Form
from PyQt5.QtWidgets import QMessageBox,QInputDialog,QLineEdit
import bcrypt
import smtplib
import random
import string
import sys
import csv
import yagmail

#from main import SplashScreen
############### For SMTP ##############
def send_otp_email(email, otp):
    # Connect to your Gmail account
    yag = yagmail.SMTP('leto.pea1@gmail.com', 'dwxysjxnohngaaaz')
    # Compose the email
    subject = 'OTP for Password Reset'
    body = 'Your OTP for password reset is: {}'.format(otp)
    # Send the email
    yag.send(email, subject, body)
# email: leto.pea1@gmail.com    
# pass: P:nM6Kd5.AmDMHW
# SMTP: dwxysjxnohngaaaz
# SMTP: mail.google.com', 587
# You would need to replace 'smtp.example.com' and 'your_email_address' and 'your_email_password'
# with your own email server and email credentials.
# In this example, the smtplib.SMTP() method is used to establish a connection to the email server 
# using the server's address and port. The starttls() method is used to initiate a secure connection to the server. 
# The login() method is used to login to the email account using the provided email address and password. The sendmail() method is used to send the OTP email to the provided recipient email address. The quit() method is used to close the connection to the email server.
# Please note that this is a basic example, and that you may need to consult the documentation of the 
# email service that you are using to configure the SMTP settings.

class LoginApp(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.resetbttn)
    #### restebttn
    def resetbttn(self):
        email = self.lineEdit_3.text()
        email = self.lineEdit.text()
        # check if the email exists in the database
        with open('users.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['email'] == email:
                    # generate OTP
                    otp = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
                    # send OTP and password reset email
                    send_otp_email(email, otp)
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("A password reset OTP has been sent to {}".format(email))
                    msg.setWindowTitle("Password Reset")
                    msg.exec_()
                    # prompt user to enter OTP
                    entered_otp, ok = QInputDialog.getText(self, "OTP", "Enter the OTP received in the email:")
                    if ok:
                        if entered_otp == otp:
                            # prompt user to enter new password
                            new_password, ok = QInputDialog.getText(self, "New Password", "Enter your new password:", QLineEdit.Password)
                            if ok:
                                # update password
                                hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
                                with open('users.csv', 'r') as csvfile:
                                    data = list(csv.reader(csvfile))
                                    for i in range(len(data)):
                                        if data[i][0] == email:
                                            data[i][3] = hashed_password
                                with open('users.csv', 'w', newline='') as csvfile:
                                    csv.writer(csvfile).writerows(data)
                                msg = QMessageBox()
                                msg.setIcon(QMessageBox.Information)
                                msg.setText("Password reset successful!")
                                msg.setWindowTitle("Password Reset Success")
                                msg.exec_()
    #### LOGINbtn
    def login(self):
        email = self.lineEdit.text()
        password = self.lineEdit_2.text()
        first_name = self.lineEdit_2.text()
        # check if the email and password match a registered user
        with open('users.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['email'] == email and bcrypt.checkpw(password.encode('utf-8'), row['password'].encode()):
                    # log the user in
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Welcome, {}!".format(first_name))
                    msg.setWindowTitle("Login Success")
                    msg.exec_() 
                    # open the next window
                    # Show the splash screen
                    #MainWindow()
                    from main import MainWindow
                    import main
                    self.app 
                    self.show()
                    self.close()
                    return
                if row['email'] == '' and row['password'] == '':
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Error: Invalid username or password.")
                    msg.setWindowTitle("Input Error ")
                    msg.exec_()
            else:
                    # show error message
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Error: Invalid username or password.")
                    msg.setWindowTitle("Login Error")
                    msg.exec_()

    #connect the function with the button 
        self.pushButton.clicked.connect(self.login)
    #### REgisterbttn
    def register(self):
        email = self.lineEdit_3.text()
        first_name = self.lineEdit_4.text()
        last_name = self.lineEdit_5.text()
        password = self.lineEdit_6.text()
        confirm_password = self.lineEdit_7.text()
        if password != confirm_password:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error: Passwords don't match.")
            msg.setWindowTitle("Registration Error")
            msg.exec_()
            return
        if email == '' or password == '' or first_name=='' or last_name=='':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error: Please input all credentials.")
            msg.setWindowTitle("Registration Error")
            msg.exec_()
            return
        else:
            # check if the email already exists in the database
            with open('users.csv', 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row['email'] == email:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Critical)
                        msg.setText("Error: Email already exists.")
                        msg.setWindowTitle("Registration Error")
                        msg.exec_()
                        return
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            # Create the database file if it doesn't exist
            with open('users.csv', 'a') as csvfile:
                fieldnames = ['email', 'first_name', 'last_name', 'password']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                #write the headers 
                writer.writeheader()
                #write the data
                writer.writerow({'email': email, 'first_name': first_name, 'last_name': last_name, 'password': hashed_password.decode()})
                #show success message
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Registration Successful!")
                msg.setWindowTitle("Registration Success")
                msg.exec_()
            #Clear the lineEdit fields
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
            self.lineEdit_5.clear()
            self.lineEdit_6.clear()
            self.lineEdit_7.clear()
        ### exit window
    def exitbttn(self):
        self.close()
    def changeForm(self):
        if self.pushButton_7.isChecked():
            self.widget_2.hide()
            self.widget_3.show()
            self.pushButton_7.setText("<")
        else:
            self.widget_2.show()
            self.widget_3.hide()
            self.pushButton_7.setText(">")
    def __init__(self):
        super(LoginApp, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.pushButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
#############################################################
        self.pushButton_6.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        ### resetbttn
        self.pushButton_2.clicked.connect(self.resetbttn)
        ### loginbttn
        self.pushButton.clicked.connect(self.login)
        ### registerbttn
        self.pushButton_6.clicked.connect(self.register)
        ### exitbttn
        self.pushButton_3.clicked.connect(self.exitbttn)

        self.widget_3.hide()
        self.pushButton_7.clicked.connect(self.changeForm)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = LoginApp()
    Form.show()
    sys.exit(app.exec_())
