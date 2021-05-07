import os
import subprocess

def setup_website(sitename):
	directory = ""

	print("Now setting up", sitename, "Please enter thhe directory where you would like your files to be saved")
	while not os.path.dirname(directory):
		print("Please enter a valid directory")
		directory = input()

	url = "none"
	if os.path.dirname(directory + "/.git"):
		os.chdir(directory)
		url = subprocess.check_output("git remote show origin | grep \"Fetch URL\" | sed \'s/ *Fetch URL: //\'")
	return [directory, url, ""]


def setup_workspace(data):
	if not os.path.dirname("Workspace"):
		os.mkdir("Workspace")
	if data[0] != "euler":
		with open("Workspace/input", 'w') as f:
			pass
	with open("Workspace/main" + data[1], 'w') as f:
		pass
	with open("Workspace/prompt.txt", 'w') as f:
		pass

