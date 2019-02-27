#coding:utf8
import os
#importPySide2 사용할때마다  PySide2.QtWidget.써줘야하니깐 아래줄이 나음
from PySide2.QtWidgets import *

class CheckEnv(QWidget):
	def __init__(self):
		super(CheckEnv,self).__init__()
	
		qmBox = QMessageBox(None)
		qmBox.setText("$USER : %s" % (os.environ['USER']))
		qmBox.setText("$NUKE_PATH : %s" % (os.environ['NUKE_PATH']))
		qmBox.setText("$NUKE_FONT_PATH : %s" % (os.environ['NUKE_FONT_PATH']))
		qmBox.setText("$OCIO : %s" % (os.environ['OCIO']))
		qmBox.show()
