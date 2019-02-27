#!/usr/bin/env python
#coding:utf8
import os
import subprocess
import sys

p = "/project/b/in"

#스앵님코드
#def searchItem(root):
#	result = []
#	for subdir in os.listdir(root):
#		for exr in or.listdir(root+"/"+subdir):
#			result.append("%/".join([root,subdir,exr]))
#		
#		result.sort()
#		return results

#스앵님코드2
#seq = []
#	for subdir in os.listdir(root):
#		shot = []
#		for f in or.listdir(root+"/"+subdir):
#			shot.append("/".join([root,subdir,f]))
#	shot.sort()
#	seqs.append(shot)
#	return seqs

#code3
#def proxyPath(p):
#	return p+"_proxy"


def genmov(path_list):
	"""
	경로를 입력받으면 mov를 만든다.
	"""
	if os.path.exists("/home/$USER/app/ffmpeg/ffmpeg"):
		return "", "ffmpeg가 설치되지 않았습니다."

	for i in path_list:
		f = os.listdir(i)
		f.sort()
		filename_s,ext = os.path.splitext(f[0])
		filename_e,ext = os.path.splitext(f[-1])
		filename,startNum = os.path.splitext(filename_s)
		filename,frames = os.path.splitext(filename_e)
		print startNum.replace(".","")
		startNum = int(startNum.replace(".",""))
		frames = int(frames.replace(".","")) - startNum
		print frames

		cmds = ("/home/$USER/app/ffmpeg/ffmpeg -f image2 -start_number "
			+str(startNum)+" -r 24 -i "+i+"/"+filename+
			".%d.jpg -vframes "+str(frames)+" -vcodec libx264 /"+i+"/"+filename+".mov")
		print(cmds)	
		os.system(cmds)
		return

def genjpg(p):

	if not os.path.exists("/usr/bin/convert"):
		return "", "ImageMagick이 설치되지 않았습니다."
	for i in os.listdir(p):
		for j in os.listdir(p+"/"+i):
			path_list=[]
			if not os.path.exists(p+"/"+i+"/"+j+"/"+j+"_proxy"):
				os.makedirs(p+"/"+i+"/"+j+"/"+j+"_proxy")
			path_list.append(p+"/"+i+"/"+j+"/"+j+"_proxy")
			for k in os.listdir(p+"/"+i+"/"+j):
				filename,ext = os.path.splitext(k)
				dst = p+"/"+i+"/"+j+"/"+j+"_proxy/"+filename+".jpg"
				cmds = "convert "+p+"/"+i+"/"+j+"/"+k+" "+dst
				os.system(cmds)
			print path_list

	return path_list

def rmjpg(path_list):
	for i in path_list:
		cmds = "rm " +i+"/*.jpg"
		os.system(cmds)
	return 

if __name__=='__main__':

	p = "/project/b/in"
	path_list = genjpg(p)
	genmov(path_list)
	rmjpg(path_list)

#	src = "/project/circle/in/aces_exr/A003C025_150830_R0D0/A003C025_150830_R0D0.078727.exr"
#	stdOut, stdErr = genmov(src)
#	if stdErr:
#	sys.stderr.write(stdErr)
#	sys.stdout.write(stdOut)
