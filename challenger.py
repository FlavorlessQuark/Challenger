import os
import re
from srcs import setup

# Check if config file exist, else run setup

with open ("srcs/challenger.config") as f:
	config = {line.split(":")[0]:line.split(",")[0:] for line in  f }

print(config)
print("Welcome user")
print("Exercises are available from the following: Leetcode, Advent of Code, Project Euler.")

while True:
	answer = input()
	match = re.match(r'^start (leetcode|aoc|euler) (\..+)$', answer)
	if match and config[match.groups(0)[0]][0] != "":
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

