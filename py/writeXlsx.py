#!/usr/bin/env python
#coding:utf8

from openpyxl import Workbook
wb = Workbook()
dest = 'output.xlsx'
ws1 = wb.active
ws1.title = "Sheet1"
ws1.append(["eq","seq","scene","shot","note"])
ws1.append(["1","CAR","FOO","0010","add cg car"])
ws1.append(["1","CAR","FOO","0020","add dust"])
ws1.append(["1","CAR","BAR","0010","add car, add dust"])
wb.save(filename = dest)
