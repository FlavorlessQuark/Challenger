import os
from fileinput import FileInput as fp

def setup_website(sitename):
	
	print(">> Now setting up", sitename, "Please enter the directory where you would like your files to be saved")
	directory = input()
	while not os.path.dirname(directory):
		print("Please enter a valid directory")
		directory = input()

	git = True if os.path.dirname(directory + "/.git") else False
	with fp("challenger.config", inplace = True) as f:
		for line in f:
			if line.startswith(sitename):
				print(sitename + ":" + directory + "," + str(git), end="\n")
			else:
				print(line, end="")
	return directory

def setup_workspace(data):
	if not os.path.dirname("Workspace"):
		os.mkdir("Workspace")
	if data[0] != "euler":
		with open("Workspace/input", 'w+') as f:
			pass
	with open("Workspace/main" + data[1], 'w+') as f:
		pass
	with open("Workspace/prompt.txt", 'w+') as f:
		pass
