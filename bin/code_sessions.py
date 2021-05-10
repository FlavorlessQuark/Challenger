from requests import Session
from bs4 import BeautifulSoup as bs
import base64
import json
import setup
import os

def get_data(config_name):
	if not os.path.isfile("config/" + config_name + ".config")
		return 1
	return json.loads("../config/euler.json")

class euler_session:
	def __init__(self, data):
		if (get_data("euler"))
			data = setup.setup_config("euler")

		self.url = "https://projecteuler.net/"
		self.data = data
		self.session = requests.Session()
		#Here code to check if successful login else need new cookies

	def get_problem(self, problem_no):
		response = self.session.get(self.url + "/problem=" + str(problem_no))
		html = bs(response.content, "html.parser")
		return html.find("div", {"class": "problem_content"})

	def check_answer(data):
		answer = input("Answer :")

	#  Code below

# url = "https://projecteuler.net/problem=4"
# cookies = {"PHPSESSID":"1d6b619ffc3c085c1005994454c0e593"}
# 	def save():

# with Session() as session:
# 	response = session.get(url, cookies=cookies)
# 	html = bs(response.content, "html.parser")
# 	token = html.findAll("input", {"name":"csrf_token"})[-1]["value"]
# 	payload = {"guess_4":"3", "csrf_token":token}
# 	# 42de3a0f57a4dfbca0e8ad629d1e49d01lZHtQUOMQrloqilLnznXBEKGJvXvxCj8Vpl+TzoDC29mXgsFC748hrVQhQO9S53bq5FeKIfOeM4X2ie
# 	# 1895d1367d4df4489267a6ea498e78caBI16mnM+mqy1tHySOJ0rjxb0Rj4Jiw/NcGcqsoqsLJMPuauAm2UR0TbWuG/Ym7VDiz2lYpzJOL0hkL2mp7HMoHyjyw==
# # 	# # # soup = bs(html, "lxml")
# 	response = session.post(url, data=payload, cookies=cookies)
# 	html = bs(response.content, "html.parser")
# # 	# action = html.find("form})
# 	# print(token)
# 	print(html.prettify())
# 	# # table = html.find("div",{"class": "problem_content"})
# 	# table = html.find("img",{"title": "wrong"})
# 	# for x in table:
# 	# 	print(x)

# 	# # print(response.text)
# 	# # print(html.find("div", {"class": "problem_content"}))
# 	# # response = session.get(url)
# 	# # print(html)
