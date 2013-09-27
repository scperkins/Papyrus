#! /usr/bin/python
import sys
import os
from PyQt4 import QtGui

class Notepad(QtGui.QMainWindow):

	def __init__(self):
		super(Notepad, self).__init__()
		self.initUI()

	def initUI(self):
		closeAction = QtGui.QAction('Close', self)
		closeAction.setShortcut('Ctrl+Q')
		closeAction.setStatusTip('Close Notepad')
		closeAction.triggered.connect(self.close)

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(closeAction)

		newAction = QtGui.QAction('New', self)
		newAction.setShortcut('Ctrl+N')
		newAction.setStatusTip('Create new file')
		newAction.triggered.connect(self.newFile)

		saveAction = QtGui.QAction('Save', self)
		saveAction.setShortcut('Ctrl+S')
		saveAction.setStatusTip('Save current file')
		saveAction.triggered.connect(self.saveFile)

		openAction = QtGui.QAction('Open', self)
		openAction.setShortcut('Ctrl+O')
		openAction.setStatusTip("Open a file")
		openAction.triggered.connect(self.openFile)

		fileMenu.addAction(newAction)
		fileMenu.addAction(saveAction)
		fileMenu.addAction(openAction)

		self.text = QtGui.QTextEdit(self)
		self.setCentralWidget(self.text)

		self.setGeometry(300,300,300,300)
		self.setWindowTitle('Notepad')
		self.show()

	def newFile(self):
		self.text.clear()

	def saveFile(self):
		filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File', os.path.expanduser('~'))
		f = open(filename, 'w')
		filedata = self.text.toPlainText()
		f.write(filedata)
		f.close()

	def openFile(self):
		filename = QtGui.QFileDialog.getOpenFileName(self, 'Open', os.path.expanduser('~'))
		filedata = f.read()
		self.text.setText(filedata)
		f.close()

def main():
	app = QtGui.QApplication(sys.argv)
	notepad = Notepad()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()