from selenium import webdriver
import time, pymongo
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from selenium.webdriver.common.proxy import Proxy, ProxyType

myclient = pymongo.MongoClient("mongodb://localhost:27017/",
                                            connect=False)

MYDB = myclient['linkedIn']
PROFILECOLL = MYDB['profiles2']
ACCOUNTSCOLL = MYDB['accounts']

software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   
user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
user_a = user_agent_rotator.get_random_user_agent()

# options.add_argument("--headless")

options = webdriver.ChromeOptions()
options.add_argument("user-agent=" + user_a)
# options.add_argument("--proxy-server=138.197.216.112:8118")

user = {'username': 'viral999g@gmail.com', 'password': '9898209177'}

driver = webdriver.Chrome(chrome_options=options)
driver.set_page_load_timeout(20)
driver.get('https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin')
# print(driver.get_cookies())

username_input = driver.find_element_by_id('username')
username_input.send_keys(user['username'])

password_input = driver.find_element_by_id('password')
password_input.send_keys(user['password'])

submit_button = driver.find_element_by_xpath('//div[@class="login__form_action_container "]/button')

try:
  submit_button.click()
except:
  pass

cookies_arr = []

cookies_arr.append(driver.get_cookie("bscookie")) 
cookies_arr.append(driver.get_cookie("bcookie")) 
cookies_arr.append(driver.get_cookie("JSESSIONID"))
cookies_arr.append(driver.get_cookie("_ga"))

print(cookies_arr)

cookies = ''
for cookie in cookies_arr:
  cookies += cookie['name'] + "=" + cookie['value'] + "; "

ACCOUNTSCOLL.update({"username": user['username']}, {"$set": {'cookies': cookies_arr}}, upsert = True)
