# Challenger
Unleash the Code
-----
````
Once upon a time there lived a mage

Wanting to solve problems made by his pairs

These were scattered across lands and ages

Through times and addresses

Shortcuts are never the same anywhere

Environments always differ

But he smiles, for he knows... He can automate that

"Ei, zwei, drei!"
````

# What even ..?

Challenger is a command line tool that lets you easily solve coding problems from different places - Currently getting problems from : Project Euler

## ETC

This will be a longer and more complete tool than ones i've previousy done, and it is likely to take weeks if not months to complete.

## Usage

When ran for the first time, you will need to supply which directory you want your files saved to as well as a Cookie that will be used to log into Project Euler

Commands :


```
start [extension] : Starts from the last solved problem withn $extension as the file extension used
next			  : Skips the current problem if unsolved or starts the next problem if solved. Work will be saved
stop			  : Saves your work and ends the program
submit			  : Submits your answer to project Euler and returns whateher it is correct or not

```
**BEWARE** Saved work is automatically pushed to github if the specified directory is a git repo. As of now there are no options to disable this except editing the config file


# TODO

Test it more thorougly, add the option to redo skipped problem | Do random problems

Add AoC support

Add w3Ressources (https://www.w3resource.com/python-exercises/) Python / C

