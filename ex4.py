import maya.cmds as mc
import re
win = "connectBlendUI"
if mc.window(win, exists=True):
	mc.deleteUI(win)


mc.window(win, title="Connect Blend")
mc.columnLayout(adj=True)

tfg9 = mc.textFieldButtonGrp(l="Object 1 (blender=0):",bl="Load Sel")
print tfg9
mc.textFieldButtonGrp(tfg9,e=True,l="hah")
tmp = mc.textFieldButtonGrp(tfg9,q=True,l=True)
print tmp
mc.textFieldButtonGrp(tfg9,e=True,bc='loadSelIntoTFBG(arg="'+tfg9+'")')
mc.showWindow(win)

def testPrint(a,b,c,d,e):
	print a
	print b
	print c
	print d
	print e

testPrint(1,'2','foo',-9,'*')	

def testPrint1(*args):
	listargs = ['obj1','obj2','target','drivers','attribute']
	for i in range(len(args)):
		#listargs[i] = mc.textFieldButtonGrp(args[i],q=True,tx=True)
		listargs[i] = args[i]
		print listargs

testPrint1(1,'2','foo',-9,'*')
print obj1
args=[1,2,3,4]
print len(args)
for i in range(len(args)):
	print args[i]

strin = '165ayzLJOt.kleX'
strinResult=re.match(r'([a-zA-Z0-9]*)\.([a-zA-Z]+)',strin)
if strinResult:
	print 'OK!'
print strin