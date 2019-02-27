import nuke
r=nuke.nodes.Read(file="/project/circle/in/aces_exr/A003C025_150830_R0D0/A003C025_150830_R0D0.%04d.exr")
w=nuke.nodes.Write(file="/project/circle/in/aces_exr/A003C025_150830_R0D0/A003C025_150830_R0D0.%04d.jpg")
w["first"].setvalue(78471)
w["last"].setvalue(78472)
w.setInput(0,r)
nuke.execute("Write",78471,78472)
quit()

