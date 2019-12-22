from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QStatusBar, QMessageBox
from PyQt5.QtCore import Qt
from board import Board
from score_board import ScoreBoard

class Go(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def getBoard(self):
        return self.board

    def getScoreBoard(self):
        return self.scoreBoard


    def initUI(self):
        '''initiates application UI'''
        self.board = Board(self)
        self.setCentralWidget(self.board)
        self.scoreBoard = ScoreBoard()
        self.addDockWidget(Qt.RightDockWidgetArea, self.scoreBoard)
        self.scoreBoard.make_connection(self.board)
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage('Message in statusbar.')
        self.resize(900, 900)
        self.center()
        self.setWindowTitle('Go')
        self.show()

    def center(self):
        '''centers the window on the screen'''
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,(screen.height() - size.height()) / 2)


    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_R:
            print("Excaaaa")
            self.getBoard().resetGame()
            self.update()
        if event.key() == QtCore.Qt.Key_P:
            print("Pass")
            if self.getBoard().passEvent() == True:
                self.close()

            self.update()
            #self.close()
