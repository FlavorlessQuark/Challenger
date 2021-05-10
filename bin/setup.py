import os
import json
from fileinput import FileInput as fp

def setup_config(config_name, cookies_name):

	directory = input(">> Now setting up", sitename, "Please enter the directory where you would like your files to be saved")
	while not os.path.dirname(directory):
		directory = input("Please enter a valid directory : ")
	directory = input("Please enter the value for cookie " + cookies_name)
	git = True if os.path.dirname(directory + "/.git") else False
	data = {
				"dir":directory,
				"git":git,
				"cookies":cookies,
				"solved":[],
				"skipped":[],
				"last":0
	}
	with open("config/euler.config", "w+") as f:
		f.write(json.dumps(data))
	return data

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
