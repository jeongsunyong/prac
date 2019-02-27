#!usr/bin/env python
#coding:utf8

import csv

with open('test.csv', mode='w') as csvFile:
	title = ['ep','swq','scene','shot','note']
	writer = csv.DictWriter(csvFile, fieldnames=title)
	writer.writerheader()
	writer.writerow({'ep':'1','seq':'CAR', 'scene':'FOO','shot':'0010','note':'cg car'})
	writer.writerow({'ep':'1','seq':'CAR', 'scene':'FOO','shot':'0020','note':'add dust'})
	writer.writerow({'ep':'1','seq':'CAR', 'scene':'BAR','shot':'0010','note':'cg car, add dust'})

