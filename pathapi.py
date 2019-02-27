#!/usr/bin/env python
#coding:utf8
import re
path = "/project/circle/shot/FOO/0010/comp/FOO_0010_comp_v001.nk"

def project(path):
	"""
	경로를 넣으면 project이름을 반환한다.
	"""
	p = re.findall('/project/(\w[^/]+)',path.replace("\\","/"))
	if len(p) != 1:
		return "", "경로에서 project정보를 가지고 올 수 없습니다."
	return p[0],None


def seq(path):
	"""
	경로를 넣으면 sequence이름을 반환한다.
	"""
	p = re.findall('/shot/(\S[^/]+)',path.replace("\\","/"))
	if len(p) != 1:
		return "", "경로에서 sequence정보를 가지고 올 수 없습니다."
	return p[0],None

def shot(path):
	"""
	경로를 넣으면 shot이름을 반환한다.
	"""
	p = re.findall('/shot/\w+/(\w[^/]+)',path.replace("\\","/"))
	if len(p) != 1:
		return "", "경로에서 shot정보를 가지고 올 수 없습니다."
	return p[0],None

def task(path):
	"""
	경로를 넣으면 task이름을 반환한다.
	"""
	p = re.findall('/shot/\w[^/]+/\w[^/]+/(\D[^/]+)',path.replace("\\","/"))
	if len(p) != 1:
		return "", "경로에서 task정보를 가지고 올 수 없습니다."
	return p[0],None

def ver(path):
	"""
	경로를 넣으면 version 넘버를 반환한다.
	"""
	p = re.findall("_v(\d+)",path.replace("\\","/"))
	if len(p) != 1:
		return -1, "경로에서 version정보를 가지고 올 수 없습니다."
	return int(p[0]),None

def seqNum(path):
	"""
	경로를 넣으면 sequence넘버를 반환한다.
	"""
	p = re.findall("[.](\d+)[.]",path.replace("\\","/"))
	if len(p) != 1:
		return -1,"경로에서 sequence number정보를 가지고 올 수 없습니다."
	return int(p[0]),None



