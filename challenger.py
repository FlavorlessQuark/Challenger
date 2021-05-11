import os
import re
import bin.code_sessions as cs
import bin.setup
import bin.commands as cmd
import json

compile_lines = {
					".c": "gcc -g main.c && ./a.out",
					".py":"python3 main.py"
}

commands = {
				"end":cmd.stop,
				"start":cmd.start,
				"next":cmd.get_next,
				"submit":cmd.submit
}

sessions  = {
				"euler": cs.euler_session()
}


# ----------------------------------------------------------------#

print(">> Welcome user")
print(">> Exercises are available from the following: Project Euler (euler)")

# Setup the workspace and add information necessary to save files
info = {"id":1, "start_time":0, "mode":0}
session = sessions["euler"]
session.data["Answer"] = False
while True:
	answer = input().split(" ")
	if answer[0] not in commands:
		print(">? Invalid command: " + answer[0] + "| Available commands are : " + str(list(commands.keys())))
	else:
		commands[answer[0]](session)
