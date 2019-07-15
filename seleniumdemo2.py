from selenium import webdriver
import time
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem


software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   
user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
user_a = user_agent_rotator.get_random_user_agent()

print(user_a)

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_argument("user-agent=" + user_a )

driver = webdriver.Chrome(chrome_options=options)
driver.set_page_load_timeout(5)
driver.get('https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin')
# print(driver.get_cookies())

username_input = driver.find_element_by_id('username')
username_input.send_keys("viral999g@gmail.com")

password_input = driver.find_element_by_id('password')
password_input.send_keys("9898209177")

submit_button = driver.find_element_by_xpath('//div[@class="login__form_action_container "]/button')

try:
  submit_button.click()
except:
  pass

print(driver.execute_script("return navigator.userAgent;"))

cookies_arr = []

cookies_arr.append(driver.get_cookie("bscookie")) 
cookies_arr.append(driver.get_cookie("bcookie")) 
cookies_arr.append(driver.get_cookie("JSESSIONID"))
cookies_arr.append(driver.get_cookie("_ga"))

print(cookies_arr)

cookies = ''
for cookie in cookies_arr:
  cookies += cookie['name'] + "=" + cookie['value'] + "; "

print(cookies)
