from selenium import webdriver
from time import sleep
import password

class Aksje:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.browser = webdriver.Chrome()
		self.browser.get('https://trader.degiro.nl/login/#/login')
		# assert "DEGIRO" in self.browser.title
		sleep(1)
		self.browser.find_element_by_xpath('//*[@id="username"]').send_keys(username)
		self.browser.find_element_by_xpath('//*[@id="password"]').send_keys(password)
		self.browser.find_element_by_xpath('//*[@id="loginForm"]/div[3]/button').click()
		# username_form.clear()
		# username_form.send_keys(username)
		#
		# password_form.clear()
		# password_form.send_keys(password)
		#
		# login_form.send_keys(Keys.RETURN)
	def buy(self):
		pass



password = ""
username = ""
obj = Aksje(username, password)
