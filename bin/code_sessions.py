import requests
from bs4 import BeautifulSoup as bs
import base64
import json
import bin.setup as setup
import os

class euler_session:
	def __init__(self):
		if not os.path.isfile("./config/euler.config"):
			data = setup.setup_config("euler", "PHPSSESSID")
		else:
			with open("./config/euler.config") as f:
				data = json.loads(f.read())

		self.url = "https://projecteuler.net/"
		self.data = data
		self.session = requests.Session()
		self.extension = ".py"
		self.mode = 0
		self.id = data["last"]
		self.starttime = 0
		#Here code to check if successful login else need new cookies

	def get_problem(self, problem_no):
		response = self.session.get(self.url + "/problem=" + str(problem_no))
		html = bs(response.content, "html.parser")
		with open("Workspace/prompt.txt", 'w+') as f:
			r = html.find("div", {"class": "problem_content"})
			f.write(r.text)

	def check_answer(data):
		answer = input("Answer :")
		response = self.session.get(self.url + "/problem=" + str(problem_no))
		html = bs(response.content, "html.parser")
		token = html.findAll("input", {"name":"csrf_token"})[-1]["value"]
		payload = {"guess_" + str(self.id):answer, "csrf_token":token}
		response = session.post(url, data=payload, cookies=cookies)
		html = bs(response.content, "html.parser")
		if len(html.findAll("img", {"src":"images/clipart/answer_wrong.png"})) > 0:
			return False
		return True
	#  Code below
