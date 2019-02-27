#coding:utf8

import os
from PySide2.QtWidgets import *

class HelloWorld(QWidget):
	def __init__(self):
		super(HelloWorld, self).__init__()
		self.layout = QVBoxLayout()
		self.setLayout(self.layout)
		self.setEnv()

	def setEnv(self):
		self.layout.addWidget(QLabel("Hello World!"))

def main():
	global customApp
	try:
		customApp.close()
	except:
		pass
	customApp = HelloWorld()
	try:
		customApp.show()
	except:
		pass



