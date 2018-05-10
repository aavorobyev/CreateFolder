import os
path = "/Users/alexandervorobyev/Desktop/"
projectname = "Project1"
folders = \
["input", 
"output", 
"scenes",
"assets"]
def CreateFolder(path):
	if not os.path.exists(path):
		os.mkdir(path)

fullPath = os.path.join(path, projectname)
CreateFolder(fullPath)

for f in folders:
	folder = os.path.join(fullPath, f)	
	CreateFolder(folder)


