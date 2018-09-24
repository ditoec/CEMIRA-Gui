from PyQt5.QtCore import QProcess
from PyQt5 import QtWidgets
from control_panel_ui import Ui_MainWindow
import time
import subprocess

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
        self.process.start('tmux', ['send-keys', '-t', 'head', 'C-c'])
        self.process.waitForFinished()
        self.process.terminate()
        self.process.start('tmux', ['send-keys', '-t', 'arm', 'C-c'])
        self.process.waitForFinished()
        self.process.terminate()
        self.process.start('tmux', ['send-keys', '-t', 'faceOutput', 'C-c'])
        self.process.waitForFinished()
        self.process.terminate()
        self.process.start('tmux', ['send-keys', '-t', 'object', 'C-c'])
        self.process.waitForFinished()
        self.process.terminate()
        self.process.start('tmux', ['send-keys', '-t', 'faceInput', 'C-c'])
        self.process.waitForFinished()
        self.process.terminate()
        self.process.start('tmux', ['send-keys', '-t', 'leap', 'C-c'])
        self.process.waitForFinished()
        self.process.terminate()
        self.processTerm.terminate()

        self.process.start('tmux', ['send-keys', '-t', 'ros', 'C-c'])
        self.process.waitForFinished()
        self.process.terminate()

def setupControlPanel(ui):
    #connect events
    ui.pushHead.clicked.connect(pushHeadClickedHandler)
    ui.pushArm.clicked.connect(pushArmClickedHandler)
    ui.pushFaceOutput.clicked.connect(pushFaceOutputClickedHandler)
    ui.pushObject.clicked.connect(pushObjectClickedHandler)
    ui.pushFaceInput.clicked.connect(pushFaceInputClickedHandler)
    ui.pushLeap.clicked.connect(pushLeapClickedHandler)

def setupTmux():
    #setup tmux
    subprocess.run(['tmux','kill-session','-t','ros'])
    subprocess.run(['tmux','kill-session','-t','head'])
    subprocess.run(['tmux','kill-session','-t','arm'])
    subprocess.run(['tmux','kill-session','-t','faceOutput'])
    subprocess.run(['tmux','kill-session','-t','object'])
    subprocess.run(['tmux','kill-session','-t','faceInput'])
    subprocess.run(['tmux','kill-session','-t','leap'])
    
    subprocess.run(['tmux','new', '-s', 'head','-d'],cwd="/home/dito")
    subprocess.run(['tmux','new', '-s', 'arm','-d'],cwd="/home/dito")
    subprocess.run(['tmux','new', '-s', 'faceOutput','-d'],cwd="/home/dito")
    subprocess.run(['tmux','new', '-s', 'object','-d'],cwd="/home/dito")
    subprocess.run(['tmux','new', '-s', 'faceInput','-d'],cwd="/home/dito")
    subprocess.run(['tmux','new', '-s', 'leap','-d'],cwd="/home/dito")
    
    subprocess.run(['tmux', 'send-keys', '-t', 'ros', 'roscore', 'Enter'])
    
def pushHeadClickedHandler():
    subprocess.run(['tmux', 'send-keys', '-t', 'head', 'roslaunch cemira head.launch', 'Enter'])

def pushArmClickedHandler():
    subprocess.run(['tmux', 'send-keys', '-t', 'arm', 'roslaunch cemira arm.launch', 'Enter'])

def pushFaceOutputClickedHandler():
    subprocess.run(['tmux', 'send-keys', '-t', 'faceOutput', 'roslaunch cemira face_output.launch', 'Enter'])

def pushObjectClickedHandler():
    subprocess.run(['tmux', 'send-keys', '-t', 'object', 'roslaunch cemira object_rec.launch', 'Enter'])

def pushFaceInputClickedHandler():
    subprocess.run(['tmux', 'send-keys', '-t', 'faceInput', 'roslaunch cemira face_output.launch', 'Enter'])

def pushLeapClickedHandler():
    subprocess.run(['tmux', 'send-keys', '-t', 'leap', 'roslaunch cemira leap.launch', 'Enter'])

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