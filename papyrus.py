#!/usr/bin/env python
import sys
import os
from PyQt4 import QtGui, QtCore

class Papyrus(QtGui.QMainWindow):

	def __init__(self):
		super(Papyrus, self).__init__()
		self.initUI()

	def initUI(self):
		closeAction = QtGui.QAction('Close', self)
		closeAction.setShortcut('Ctrl+Q')
		closeAction.setStatusTip('Close Papyrus')
		closeAction.triggered.connect(self.close)

		#menu bar items
		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		editMenu = menubar.addMenu('&Edit')
		
		#file menu actions
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
		fileMenu.addAction(closeAction)

		
		#Edit menu actions
		edit = QtGui.QTextEdit(self)
		edit.setStatusTip('Input Text Here')
		edit.setToolTip('Input Text Here')
		self.setCentralWidget(edit)

		copyAction = QtGui.QAction("Copy", self)
		copyAction.setShortcut("Ctrl+C")
		copyAction.setStatusTip('Copy text')
		copyAction.triggered.connect(edit.copy)

		editMenu.addAction(copyAction)

		#fontAction = QtGui.QAction('Choose font...', self)
		#fontAction.triggered.connect(self.selectFont)

		self.text = QtGui.QTextEdit(self)
		self.setCentralWidget(self.text)

		self.setGeometry(400,400,400,400)
		self.setWindowTitle('Papyrus')
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

	#def selectFont(self):


def main():
	app = QtGui.QApplication(sys.argv)
	papyrus = Papyrus()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()