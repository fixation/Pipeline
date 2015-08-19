import maya.cmds as mc
# Select all nodes with keys to export
# Customize the path below so that it points to, or creates, the file where you want to store the keyframe data
myFileObject=open('/mydataDir/data.txt', 'w')
obs = mc.ls(sl=True)
theData = []
minTime = mc.playbackOptions(query=True, minTime=True)
maxTime = mc.playbackOptions(query=True, maxTime=True)
attributes = ['translateX', 'translateY', 'translateZ', 'rotateX', 'rotateY', 'rotateZ', 'scaleX', 'scaleY', 'scaleZ', 'visibility']
for time in range(minTime -1, maxTime +1):
	mc.currentTime(time)
	count = 0
	for selection in obs:
		name = obs[count]
		count +=1
		for theAttribute in attributes:
			myAtF = mc.getAttr(selection + '.' + theAttribute)
			myAt = str(myAtF)
			myTime = str(time)
			theData.append(myAt + ' ' + myTime + ' ' + theAttribute + ' ' + name + ' \n')
for lines in theData:
	myFileObject.writelines(lines)
myFileObject.close()
