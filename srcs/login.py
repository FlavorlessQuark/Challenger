from requests import Session
from bs4 import BeautifulSoup as bs
import base64

# class coding_session:
# 	def __init__(self, site, url):
# 		self.url = url
# 		self.cookies = {"PHPSESSID": "1d6b619ffc3c085c1005994454c0e593"}
# 		self.session = requests.Session()

# 	def get_problem(self, problem_no):
# 		response = self.session.get(self.url + "/" + problem_no)
# 		html = bs(response.content, "html.parser")
# 		return html.find("div", {"class": "problem_content"})
# def euler_log(data):
# 	#Check cookies for expiration
url = "https://projecteuler.net/problem=3"

cookies = {
	"PHPSESSID": "1d6b619ffc3c085c1005994454c0e593"
}

with Session() as session:
	response = session.get(url, cookies=cookies)
	html = bs(response.content, "html.parser")
	token = html.find("input", {"name":"csrf_token"})["value"]
	payload = {"guess_3":"42", "csrf_token":token}
	# soup = bs(html, "lxml")
	response = session.post(url, data=payload, cookies=cookies, )
	html = bs(response.content, "html.parser")
	# table = html.find("div",{"class": "problem_content"})
	table = html.find("img",{"title": "wrong"})
	print(table)
	# for x in table:
	# 	print(x)

	# print(response.text)
	# print(html.find("div", {"class": "problem_content"}))
	# response = session.get(url)
	# print(html)
