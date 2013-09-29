#!/usr/bin/env python
import os
from PyQt4 import *
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from highlighter import MyHighlighter


class Papyrus(QtGui.QMainWindow):

	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		#super(Papyrus, self).__init__()
		self.initUI()		

	def center(self):
		frame = self.frameGeometry()
		cent = QtGui.QDesktopWidget().availableGeometry().center()
		frame.moveCenter(cent)
		self.move(frame.topLeft())

	def initUI(self):
		closeAction = QtGui.QAction('Close', self)
		closeAction.setShortcut('Ctrl+Q')
		closeAction.setStatusTip('Close Papyrus')
		closeAction.triggered.connect(self.close)

		'''menu bar items'''
		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		editMenu = menubar.addMenu('&Edit')
		viewMenu = menubar.addMenu('&View')
		
		'''file menu actions'''
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

		
		'''Edit Menu Actions '''
		edit = QtGui.QTextEdit(self)
		self.setCentralWidget(edit)

		#copy
		copyAction = QtGui.QAction("&Copy", self)
		copyAction.setShortcut("Ctrl+C")
		copyAction.setStatusTip('Copy text')
		copyAction.triggered.connect(edit.copy)

		#cut
		cutAction = QtGui.QAction('&Cut', self)
		cutAction.setShortcut('Ctrl+X')
		cutAction.setStatusTip("Cut text")
		cutAction.triggered.connect(edit.cut)

		#paste
		pasteAction = QtGui.QAction('&Paste', self)
		pasteAction.setShortcut('Ctrl+V')
		pasteAction.setStatusTip('Paste text')
		pasteAction.triggered.connect(edit.paste)

		editMenu.addAction(copyAction)
		editMenu.addAction(cutAction)
		editMenu.addAction(pasteAction)

		'''View Menu Actions'''
		syntaxMenu = QtGui.QAction('&Syntax', self)
		syntaxMenu.setStatusTip('Set syntax highlighting')
		syntaxMenu.triggered.connect(self.togglePython)

		viewMenu.addAction(syntaxMenu)

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

	def togglePython(self):
		font = QFont()
		font.setFamily( "Ubuntu" )
		font.setFixedPitch( True )
		font.setPointSize( 10 )
		editor = QTextEdit()
		editor.setFont( font )
		highlighter = MyHighlighter( editor, "Classic" )
		self.setCentralWidget( editor )
