#!/usr/bin/env python
#coding:utf8
import os
import subprocess
import sys

def genThumb(path):
	"""
	경로를 입력받으면 썸네일을 만든다.
	"""
	#ImageMagick미설치시
	if not os.path.exists("/usr/bin/convert"):
		return "", "ImageMagick이 설치되지 않았습니다."

	size = "360x240"
	ext = ".jpg"
	p, filename_ext = os.path.split(path)
	filename,ext_t = os.path.splitext(filename_ext)

	target = p+"/"+filename+ext_t
	result = p+"/"+filename+ext
	#cmd = "convert %s -thumbnail %s -background black -gravity center -extent %s %s" % (target,size,size,result)

	#subprocess 리스트로 사용하기때문에 cmds 이용
	cmds = ["convert", target, "-thumbnail", size,
			"-background", "black", "-gravity", "center",
			"-extent", size, result]
			#command부분 list로 변경

	a = subprocess.Popen(cmds, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	return a.communicate()




	#os.system(cmd)

#스앵님코드
#d,f = os.path.split(src)
#notuse,ext = os.path.splitext(f)
#dst = d+"/"+f.replace(".ext",".jpg")
#cmd = "convert {src} -thumbnail {size} -background black -gravity center -extent {size} {dst}".format(src=src,dst=dst size="360x240")
# 위 : 삭제

#	cmds = ["convert", src, "-thumbnail", size,
#			"-background", "blakc", "-gravity", "center",
#			"-extent", size, dst]
#	a = subprocess.Popen(cmds, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#	return a.communicate()
# 처음코드
#p = "/project/circle/in"

#for i in os.listdir(p):
#	for j in os.listdir(p+"/"+i):
#		for k in os.listdir(p+"/"+i+"/"+j):
#			target = "/".join([p,i,j,k])
#			result = "/".join([p,i,j,k.replace(".dpx",".jpg").replace(".exr",".jpg")])
#			cmd = "convert %s -thumbnail 360x240 -background black -gravity center -extent 360x240 %s" % (target,result)
#			print target
#			print result
#			print cmd
#			os.system(cmd)
			
if __name__=='__main__':

	src = "/project/circle/in/aces_exr/A003C025_150830_R0D0/A003C025_150830_R0D0.078727.exr"
	stdOut, stdErr = genThumb(src)
	if stdErr:
		sys.stderr.write(stdErr)
	sys.stdout.write(stdOut)
