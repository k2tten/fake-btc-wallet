import json, os, time
from PyQt5 import QtCore, QtGui, QtWidgets
from colorama import Fore, init
init()

with open('assets/data.json') as f:
    data = json.load(f)

dblue = Fore.BLUE
lblue = Fore.LIGHTBLUE_EX
white = Fore.WHITE
reset = Fore.RESET

main = [] #data[str(main)]['address']#
wc = [1, 2, 3]

def main_prog():
	class Ui_MainWindow(object):
	    def setupUi(self, MainWindow):
	        MainWindow.setObjectName("MainWindow")
	        MainWindow.setFixedSize(324, 500)
	        MainWindow.setStyleSheet("QWidget{\n"
	"    background-color: #1D2731;\n"
	"}")
	        self.centralwidget = QtWidgets.QWidget(MainWindow)
	        self.centralwidget.setObjectName("centralwidget")
	        self.old_hidden = QtWidgets.QLabel(self.centralwidget)
	        self.old_hidden.setGeometry(QtCore.QRect(12, 100, 300, 41))
	        font = QtGui.QFont()
	        font.setFamily("MS Shell Dlg 2")
	        font.setPointSize(24)
	        font.setBold(True)
	        font.setItalic(False)
	        font.setWeight(75)
	        self.old_hidden.setFont(font)
	        self.old_hidden.setStyleSheet("color: white;")
	        self.old_hidden.setAlignment(QtCore.Qt.AlignCenter)
	        self.old_hidden.setObjectName("old_hidden")
	        self.bal_usd = QtWidgets.QLabel(self.centralwidget)
	        self.bal_usd.setGeometry(QtCore.QRect(12, 210, 300, 21))
	        font = QtGui.QFont()
	        font.setFamily("MS Shell Dlg 2")
	        font.setPointSize(15)
	        font.setBold(False)
	        font.setItalic(False)
	        font.setWeight(50)
	        self.bal_usd.setFont(font)
	        self.bal_usd.setStyleSheet("color: white;")
	        self.bal_usd.setAlignment(QtCore.Qt.AlignCenter)
	        self.bal_usd.setObjectName("bal_usd")
	        self.receive_button = QtWidgets.QPushButton(self.centralwidget)
	        self.receive_button.setGeometry(QtCore.QRect(0, 270, 162, 30))
	        font = QtGui.QFont()
	        font.setPointSize(10)
	        font.setBold(True)
	        font.setWeight(75)
	        self.receive_button.setFont(font)
	        self.receive_button.setStyleSheet("border: none;\n"
	"background: none;\n"
	"background-color: #397eed;\n"
	"color: white;\n"
	"margin-left: 15px;\n"
	"margin-right: 5px;\n"
	"border-radius: 3px;")
	        self.receive_button.setObjectName("receive_button")
	        self.send_button = QtWidgets.QPushButton(self.centralwidget)
	        self.send_button.setGeometry(QtCore.QRect(162, 270, 162, 30))
	        font = QtGui.QFont()
	        font.setPointSize(10)
	        font.setBold(True)
	        font.setWeight(75)
	        self.send_button.setFont(font)
	        self.send_button.setStyleSheet("border: none;\n"
	"background: none;\n"
	"background-color: #397eed;\n"
	"color: white;\n"
	"margin-left: 5px;\n"
	"margin-right: 15px;\n"
	"border-radius: 3px;")
	        self.send_button.setObjectName("send_button")
	        self.bottom_bar = QtWidgets.QPushButton(self.centralwidget)
	        self.bottom_bar.setGeometry(QtCore.QRect(0, 390, 324, 121))
	        font = QtGui.QFont()
	        font.setPointSize(10)
	        font.setBold(True)
	        font.setWeight(75)
	        self.bottom_bar.setFont(font)
	        self.bottom_bar.setStyleSheet("border:none;\n"
	"background:none;")
	        self.bottom_bar.setText("")
	        icon = QtGui.QIcon()
	        icon.addPixmap(QtGui.QPixmap("assets/bottom.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	        self.bottom_bar.setIcon(icon)
	        self.bottom_bar.setIconSize(QtCore.QSize(324, 100))
	        self.bottom_bar.setAutoRepeatInterval(200)
	        self.bottom_bar.setObjectName("bottom_bar")
	        self.top_bar = QtWidgets.QPushButton(self.centralwidget)
	        self.top_bar.setGeometry(QtCore.QRect(0, 5, 324, 51))
	        font = QtGui.QFont()
	        font.setPointSize(10)
	        font.setBold(True)
	        font.setWeight(75)
	        self.top_bar.setFont(font)
	        self.top_bar.setStyleSheet("border:none;\n"
	"background:none;")
	        self.top_bar.setText("")
	        icon1 = QtGui.QIcon()
	        icon1.addPixmap(QtGui.QPixmap("assets/top.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	        self.top_bar.setIcon(icon1)
	        self.top_bar.setIconSize(QtCore.QSize(324, 100))
	        self.top_bar.setAutoRepeatInterval(200)
	        self.top_bar.setObjectName("top_bar")
	        self.btc = QtWidgets.QFrame(self.centralwidget)
	        self.btc.setGeometry(QtCore.QRect(0, 160, 324, 41))
	        self.btc.setMinimumSize(QtCore.QSize(324, 41))
	        self.btc.setMaximumSize(QtCore.QSize(324, 41))
	        self.btc.setFrameShape(QtWidgets.QFrame.StyledPanel)
	        self.btc.setFrameShadow(QtWidgets.QFrame.Raised)
	        self.btc.setObjectName("btc")
	        self.horizontalLayout = QtWidgets.QHBoxLayout(self.btc)
	        self.horizontalLayout.setContentsMargins(50, 0, 0, 0)
	        self.horizontalLayout.setSpacing(5)
	        self.horizontalLayout.setObjectName("horizontalLayout")
	        self.btc_balance = QtWidgets.QLabel(self.btc)
	        font = QtGui.QFont()
	        font.setFamily("MS Shell Dlg 2")
	        font.setPointSize(24)
	        font.setBold(True)
	        font.setItalic(False)
	        font.setWeight(75)
	        self.btc_balance.setFont(font)
	        self.btc_balance.setStyleSheet("color: white;")
	        self.btc_balance.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
	        self.btc_balance.setObjectName("btc_balance")
	        self.horizontalLayout.addWidget(self.btc_balance)
	        self.coin = QtWidgets.QLabel(self.btc)
	        font = QtGui.QFont()
	        font.setFamily("MS Shell Dlg 2")
	        font.setPointSize(14)
	        font.setBold(True)
	        font.setItalic(False)
	        font.setWeight(75)
	        self.coin.setFont(font)
	        self.coin.setStyleSheet("padding-top: 10px;\n"
	"color: white;")
	        self.coin.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
	        self.coin.setObjectName("coin")
	        self.horizontalLayout.addWidget(self.coin)
	        MainWindow.setCentralWidget(self.centralwidget)

	        self.retranslateUi(MainWindow)
	        QtCore.QMetaObject.connectSlotsByName(MainWindow)

	        self.old_hidden.hide()
	        self.receive_button.setEnabled(False)
	        self.send_button.setEnabled(False)

	    def retranslateUi(self, MainWindow):
	        _translate = QtCore.QCoreApplication.translate
	        MainWindow.setWindowTitle(_translate("MainWindow", "wallet"))
	        self.old_hidden.setText(_translate("MainWindow", str(data[str(main[0])]['btc'])))
	        self.bal_usd.setText(_translate("MainWindow", str(data[str(main[0])]['usd'])))
	        self.receive_button.setText(_translate("MainWindow", "RECEIVE"))
	        self.send_button.setText(_translate("MainWindow", "SEND"))
	        self.btc_balance.setText(_translate("MainWindow", str(data[str(main[0])]['btc'])))
	        self.coin.setText(_translate("MainWindow", "BTC"))


	if __name__ == "__main__":
	    import sys
	    app = QtWidgets.QApplication(sys.argv)
	    MainWindow = QtWidgets.QMainWindow()
	    ui = Ui_MainWindow()
	    ui.setupUi(MainWindow)
	    MainWindow.show()
	    sys.exit(app.exec_())


def ini():
	def show_wallets(): #gets all wallets in `assets/data.json`#
		count=1
		for i in data:
		    print(f"  `{lblue}{count}{reset}` | "+ lblue + data[str(count)]['address'] + reset)
		    count+= 1
		return

	def login(): #lets you choose wallet to log into#
		os.system('cls')
		print(f"\n{lblue}main@wallet{white}:{dblue}~{white}$ select a wallet:\n\n")
		show_wallets()
		selection = input(f"\n\n{lblue}main@wallet{white}:{dblue}~{white}# ")

		#not necessary#
		if "wallet -l -w" in selection:
			#check 1 == valid#
			selection = selection.replace("wallet -l -w ", "")

			if int(selection) in wc:
				main.append(selection)
				print(f"\n{lblue}main@wallet{white}:{dblue}~{white}$ launching gui.\n")
				time.sleep(0.3)
				print(F"{dblue}~{white}$ 3")
				time.sleep(0.3)
				print(F"{dblue}~{white}$ 2")
				time.sleep(0.3)
				print(F"{dblue}~{white}$ 1")
				time.sleep(0.3)
				print(f"\n{lblue}main@wallet{white}:{dblue}~{white}$ successfully launched gui using wallet `{lblue}{main[0]}{reset}`")
				main_prog()

			else:
				print(f"\n{lblue}main@wallet{white}:{dblue}~{white}$ invalid wallet!\n\n")
		else:
			print(f"\n{lblue}main@wallet{white}:{dblue}~{white}$ invalid command!\n\n")
	login()
os.system('mode con: cols=80 lines=25') #resizes terminal#
os.system('title Wallet') #renames terminal#
ini()