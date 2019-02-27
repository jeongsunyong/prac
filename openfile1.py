#coding:utf8
import nuke
import os
import re
#def main():
#	node = nuke.selectedNode()
#	path = node["file"].value()
#	os.system("nautilus %s" % (os.path.dirname(path)))
#
#
#def browser(path):
#	brws = "nautilus"
#	if sys.platform == "wind32":
#		brws = "start"
#	elif sys.platform == "darwin":
#		brws = "open"
#	p = subprocess.Popen([brws, path], stdout = subprocess.PIPE, stdout, stderr = p.communicate()
#	if stderr:
#		nuke.tprint(stderr, file=sys.stderr)


#def main():
#       node = nuke.selectedNode()
#       path = node["file"].value()
#       os.system("%s %s" % (brws, os.path.dirname(path)))

#def openFile():
def main():
	brws = "nautilus"
	nodes = nuke.selectedNodes()
	if len(nodes) != 1:
		nuke.message("please select one node.")
	else:
		r = re.findall('(\w+[^\d])',nodes[0].name())
		if r[0] != "Read" :
			nuke.message("No Read node.")
			return 0
		node = nodes[0]
		path = node["file"].value()
		os.system("%s %s" % (brws, os.path.dirname(path)))
	
#def main():

# 1.노드 1개선택 아니거나 Read노드아닌경우 에러판단
# 2.경로 윈도우/맥/리눅스 체크
# 3.파일오픈
