import os
import random
import time
import bin.code_sessions
import bin.setup

emojis = [":sunny:",":umbrella:",":cloud:",":snowflake:",":snowman:",":zap:",":cyclone:",":foggy:",":ocean:",":cat:",":dog:",
":rabbit2:",":dragon:",":goat:",":rooster:",":dog2:",":pig2:",":mouse2:",":ox:",":dragon_face:",":blowfish:",":crocodile:",
":dromedary_camel:",":leopard:",":cat2:",":poodle:",":paw_prints:",":bouquet:",":cherry_blossom:",":tulip:",":four_leaf_clover:",
":rose:",":sunflower:",":hibiscus:",":maple_leaf:",":leaves:",":fallen_leaf:",":herb:",":mushroom:",":cactus:",":palm_tree:",
":evergreen_tree:",":deciduous_tree:",":chestnut:",":seedling:",":blossom:",":ear_of_rice:",":shell:",":globe_with_meridians:",
":volcano:",":milky_way:",":partly_sunny:",":octocat:",":squirrel:",":bamboo:",":gift_heart:",":dolls:",":school_satchel:",
":cd:",":dvd:",":floppy_disk:",":camera:",":video_camera:",":movie_camera:",":computer:",":tv:",":iphone:",":phone:",":telephone:",
":telephone_receiver:",":pager:",":fax:",":minidisc:",":vhs:",":sound:",":speaker:",":mute:",":loudspeaker:",":mega:",":hourglass:",
":hourglass_flowing_sand:",":alarm_clock:",":watch:",":radio:",":satellite:",":loop:",":mag:",":mag_right:",":unlock:",":lock:",
":lock_with_ink_pen:",":closed_lock_with_key:",":key:",":bulb:",":flashlight:",":high_brightness:",":low_brightness:",":electric_plug:",
":battery:",":calling:",":email:",":mailbox:",":postbox:",":bath:",":bathtub:",":shower:",":toilet:",":wrench:",":nut_and_bolt:",":hammer:",
":envelope:",":incoming_envelope:",":postal_horn:",":mailbox_closed:",":mailbox_with_mail:",":mailbox_with_no_mail:",":package:",":door:",
":chart_with_upwards_trend:",":chart_with_downwards_trend:",":scroll:",":clipboard:",":calendar:",":date:",":card_index:",":file_folder:",
":open_file_folder:",":scissors:",":pushpin:",":paperclip:",":black_nib:",":pencil2:",":straight_ruler:",":triangular_ruler:",":closed_book:",
":green_book:",":blue_book:",":orange_book:",":notebook:",":notebook_with_decorative_cover:",":ledger:",":books:",":bookmark:",":name_badge:",
":microscope:",":telescope:"]

def save_work(data, state):
	if not os.stat("Workspace/main" + data.extension) == 0:
		os.rename("Workspace/main" + data.extension,
						data.data["dir"] + "/problem_" + str(data.id) + data.extension)
	if state:
		os.chdir(data["dir"])
		os.system("git add .")
		os.system("git commit -m \"Problem_" + str(data.id) + emojis[random.random() % len(emojis)] + "Automated save")
		os.system("git push")

def submit(data):
	answer = input("Type your answer: ")
	if (data.check_answer(answer)):
		print("Correct answer")
		data.data["solved"]
		with open(data["dir"] + "/timelog", "a") as f:
			t = divmod((time.time() - data.starttime) / 60)
			f.write("Problem " + data.id + " : " + str(t[0]) + "min " + str(t[1]) + "sec\n")
		return
	print("Incorrect answer")

def get_next(data):
	if (data.id not in data.data["solved"]):
		save_work(data, False)
		data.data["skipped"].append(data.id)
	else:
		save_work(data, True)
	data.starttime = time.time()
	data.id += 1

def start(data):
	extension = input("enter file extension: ")
	data.id = int(data.data["last"]) + 1
	data.starttime = time.time()
	data.extension = extension
	bin.setup.setup_workspace(("euler", data.extension))
	data.get_problem(data.id)

def stop(data):
	save_work(data, state)
	exit()
