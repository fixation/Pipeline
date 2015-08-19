import maya.cmds as mc
# Customize the path below so that it points to the file where you have exported the keyframe data
myFileObject=open('/mydataDir/data.txt', 'r')
theLines = myFileObject.readlines()
count = 0
for line in theLines:
	theLine = theLines[count]
	theSplit = str.split(theLine)
	theValue = theSplit[0]
	theFrame = theSplit[1]
	theAttribute = theSplit[2]
	theName = theSplit[3]
	mc.setKeyframe( theName, v=float(theValue), at=theAttribute, t =float(theFrame))
	count +=1
myFileObject.close()
