from PyQt5.QtCore import QProcess
from PyQt5 import QtWidgets
from control_panel_ui import Ui_MainWindow
import time,subprocess

class MyWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MyWindow, self).__init__(*args, **kwargs)
        self.processTerm = QProcess(self)

    def startTerminal(self):
        self.processTerm.setWorkingDirectory("/home/dito")
        self.processTerm.start('terminator',['-l', 'CEMIRA','-p','CEMIRA'])
        self.processTerm.waitForStarted()

    def closeEvent(self,event):
        self.process = QProcess()
        self.process.start('tmux', ['send-keys', '-t', 'cemira:head', 'C-c'])
        self.process.waitForFinished()
        self.process.terminate()
        self.process.start('tmux', ['send-keys', '-t', 'cemira:arm', 'C-c'])
        self.process.waitForFinished()
        self.process.terminate()

        self.processTerm.terminate()

def setupControlPanel(ui):
    #connect events
    ui.pushHead.clicked.connect(pushHeadClickedHandler)
    ui.pushArm.clicked.connect(pushArmClickedHandler)

def setupTmux():
    #setup tmux
    subprocess.call(['tmux','kill-session', '-t', 'cemira'])
    subprocess.call(['tmux','new', '-s', 'cemira','-n','head','-d'])
    subprocess.call(['tmux','new-window', '-t', 'cemira','-n','arm','-d'])
    
def pushHeadClickedHandler():
    subprocess.call(['tmux', 'send-keys', '-t', 'cemira:head', 'roslaunch head head.launch', 'Enter'])

def pushArmClickedHandler():
    subprocess.call(['tmux', 'send-keys', '-t', 'cemira:arm', 'roslaunch arm arm.launch', 'Enter'])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    setupControlPanel(ui)
    setupTmux()
    MainWindow.startTerminal()
    MainWindow.show()
    sys.exit(app.exec_())