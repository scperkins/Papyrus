from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Python(QSyntaxHighlighter):

	def __init__(self, parent, theme):
		QSyntaxHighlighter.__init__(self, parent)
		self.parent = parent
		self.highlightingRules = []

		keyword = QTextCharFormat()
		keyword.setForeground(Qt.darkBlue)
		keyword.setFontWeight(Qt.Bold)

		reservedClasses = QTextCharFormat()
		reservedClasses.setForeground(Qt.darkRed)
		reservedClasses.setFontWeight(QFont.Bold)

		keywords = QStringList(['and','del','from','not','while','as','elif','global','or','with',
			'assert','else','if','pass','yield','break','except','import','print','class','exec','in',
			'raise','continue','finally','is','return','def','for','lambda','try'])

		operators = [ '=',
	        # Comparison
	        '==', '!=', '<', '<=', '>', '>=',
	        # Arithmetic
	        '\+', '-', '\*', '/', '//', '\%', '\*\*',
	        # In-place
	        '\+=', '-=', '\*=', '/=', '\%=',
	        # Bitwise
	        '\^', '\|', '\&', '\~', '>>', '<<']

	        braces = ['\{', '\}', '\(', '\)', '\[', '\]']

	        for word in keywords:
	        	pattern = QRegExp("\\b" + word + "\\b")
		     	rule = HighlightingRule(pattern, reservedClasses)
		     	self.highlightingRules.append(rule)

	     	assignmentOperator = QTextCharFormat()
	     	pattern = QRegExp( "(<){1,2}-")
	     	assignmentOperator.setForeground(Qt.green)

