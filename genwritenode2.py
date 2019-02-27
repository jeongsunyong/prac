#coding:utf8
import nuke

def checkError():
	nodes = nuke.selectedNodes()
	if len(nodes) == 0:
		nuke.message("please select node.")
		return 0;
	else:
		return 1;


def genNodes():
	nodes = nuke.selectedNodes()
	for e in nodes: 
		tail = e

		w = nuke.nodes.Write()
		r = nuke.nodes.Reformat()
		s = nuke.nodes.slate()
		m = nuke.nodes.AddTimeCode()

		w["file_type"].setValue("exr")
		w["create_directories"].setValue(True)
		w["file"].setValue("/test/test.####.exr")
		r["type"].setValue("to box")
		r["box_width"].setValue(2048)
		r["box_height"].setValue(968)
		r["box_fixed"].setValue(True)
		m["startcode"].setValue("01:00:00:00")
		m["useFrame"].setValue(True)
		m["frame"].setValue(1001)

		r.setInput(0,tail)
		m.setInput(0,r)
		s.setInput(0,m)
		w.setInput(0,s)


def main():
	result = checkError()
	if result==1:
		genNodes()
