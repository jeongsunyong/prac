#!/usr/bin/env python
#coding:utf8
import os
import subprocess
import sys

p = "/project/c/in"

#스앵님코드
#def searchItem(root):
#	result = []
#	for subdir in os.listdir(root):
#		for exr in or.listdir(root+"/"+subdir):
#			result.append("%/".join([root,subdir,exr]))
#		
#		result.sort()
#		return results


def genjpg(path):
	"""
	경로를 입력받으면 jpg를 만든다.
	"""
	
	if not os.path.exists("/usr/bin/convert"):
		return "", "ImageMagick이 설치되지 않았습니다."
	for i in os.listdir(p):
		for j in os.listdir(p+"/"+i):
			path=p+"/"+i+"/"+j
			for k in os.listdir(p+"/"+i+"/"+j):
				filename,ext = os.path.splitext(k)
				dst = path+"/"+filename+".jpg"
				cmds = "convert "+path+"/"+k+" "+dst
				os.system(cmds)
			print "test0"
			genmov(path)
			print "test1"
	return

def genmov(path):
	"""
	경로를 입력받으면 mov를 만든다.
	"""

	if not os.path.exists("/home/$USER/app/ffmpeg"):
		return "", "ffmpeg가 설치되지 않았습니다."

	if not os.path.exists("/tmp/mov"):
		os.makedirs("/tmp/mov")
	print "test"
	f = os.listdir(path)
	f.sort()
	filename_s,ext = os.path.splitext(f[0])
	filename_e,ext = os.path.splitext(f[-1])
	filename_s,startNum = os.path.splitext(filename_s)
	filename_e,frame = os.path.splitext(filename_e)
	startNum = int(startNum)
	frame = int(frame)-startNum

	cmds = ["ffmpeg", "-f", "image2", "-start_number", startNum, "-r", "24",
			"-i", path+filename+"%4d.jpg","-vframes","-vcodec","libx264","/tmp/mov/"+filename+".mov"]

	a = subprocess.Popen(cmds, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	return a.communicate()

if __name__=='__main__':

	p = "/project/c/in"
	genjpg(p)
	


#	src = "/project/circle/in/aces_exr/A003C025_150830_R0D0/A003C025_150830_R0D0.078727.exr"
#	stdOut, stdErr = genmov(src)
#	if stdErr:
#		sys.stderr.write(stdErr)
#	sys.stdout.write(stdOut)
