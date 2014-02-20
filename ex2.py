def connectBlendUI():
	import maya.cmds as mc

	win = "connectBlendUI"
	if mc.window(win, exists=True):
		mc.deleteUI(win)


	mc.window(win, title="Connect Blend")
	mc.columnLayout(adj=True)

	tfg1 = mc.textFieldButtonGrp(l="Object 1 (blender=0):",bl="Load Sel")
	tfg2 = mc.textFieldButtonGrp(l="Object 2 (blender=1):",bl="Load Sel")

	mc.text(l="")
	tfg3 = mc.textFieldButtonGrp(l="Target Object:",bl="Load Sel")
	tfg5 = mc.textFieldGrp(l="Attribute:")
	mc.text(l="")
	tfg4 = mc.textFieldGrp(l="Driver (optinal):")
	#mis a command
	mc.button(l="Go")
	mc.textFieldButtonGrp(tfg1,e=True,bc="loadSelIntoTFBG(tfg1)")
	mc.showWindow(win)

def loadSelIntoTFBG(tfbg):
	objs = mc.ls(sl=True)

	if len(objs)>0:
		mc.textFieldButtonGrp(tfbg,e=True,tx=objs[0])
	
	print mc.textFieldButtonGrp(tfbg,q=True,tx=True)

loadSelIntoTFBG(tfg1)	
def prepConnectBlend(*args):
	obj1 = mc.textFieldButtonGrp(tfbg1,tx=True)
	obj2 = mc.textFieldButtonGrp(tfbg2,tx=True)
	target = mc.textFieldButtonGrp(tfbg3,tx=True)
	drivers = mc.textFieldButtonGrp(tfbg4,tx=True)
	attribute = mc.textFieldButtonGrp(tfg5,tx=True)		