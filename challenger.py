import os
import re
from srcs import setup


compile_lines = {
					".c": "gcc -g main.c && ./a.out",
					".py":"python3 main.py"

}

commands = {
				"end":"save()",
				"test":"test()",
				"start":"start(answer)",
				"pause":"pause()",
				"submit":"submit()"
}

def start(answer):
	match = re.match(r'^start (leetcode|aoc|euler) (\..+)$', answer)
	if match and config[match.groups()[0]]:
		print("workspace")
		setup.setup_workspace(match.groups())
		break
	elif match:
		print("setup all")
		setup.setup_website(match.groups()[0])
		setup.setup_workspace(match.groups())
		break
	else:
		print("Invalid optiions. Usage: start website language_extension")


# ----------------------------------------------------------------#
# Check if config file exist, else run setup
if not os.path.dirname("challenger.config"):
	with open("challenger.config", 'w+') as f:
			f.write("leetcode:\naoc:\neuler:\n")

with open ("challenger.config") as f:
	config = {line.split(":")[0]:line.strip().split(",")[1:] for line in  f }


print(">> Welcome user")
print(">> Exercises are available from the following: Leetcode (leetcode) | Advent of Code (aoc) | Project Euler (euler)")

# Setup the workspace and add information necessary to save files

while True:
	answer = input().split(" ")
	if answer[0] not in commands:
		print(">? Invalid command: " + answer[0] + "| Available commands are : start, pause, finish")
	else:
		eval(commands[answer[0]])
