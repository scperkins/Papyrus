#!/usr/bin/env python
import sys
from Papyrus import Papyrus
from PyQt4 import QtGui
from highlighter import *

def main():
	app = QtGui.QApplication(sys.argv)
	papyrus = Papyrus()
	papyrus.show()
	papyrus.raise_()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()