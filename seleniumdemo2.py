from selenium import webdriver
import time, pymongo, random, string
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from selenium.webdriver.common.proxy import Proxy, ProxyType

myclient = pymongo.MongoClient("mongodb://localhost:27017/",
                                            connect=False)

MYDB = myclient['linkedIn']
PROFILECOLL = MYDB['profiles2']
ACCOUNTSCOLL = MYDB['accounts']

letters = string.ascii_lowercase

user_agent_list = [
   #Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    #Firefox
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
]

user = {'username': 'viral999g@gmail.com', 'password': '9898209177'}
random1 = random.randint(0, 9)
while True:
  random2 = random.randint(0, 9)
  if random1 != random2:
    break


users = []
for i in range(0,10):
  users.append({'username': ''.join(random.choice(letters) for i in range(random.randint(6, 10))), "password": ''.join(random.choice(letters) for i in range(random.randint(6, 10)))})

users[random1] = user
users[random2] = user
count = 0
for user in users:
  count += 1
  software_names = [SoftwareName.CHROME.value]
  operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   
  user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)


  user_a = user_agent_rotator.get_random_user_agent()

  options = webdriver.ChromeOptions()
  options.add_argument("user-agent=" + user_a)
  # options.add_argument("--proxy-server=198.50.147.158:3128")


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

  try:

    cookies_arr = []

    cookies_arr.append(driver.get_cookie("bscookie")) 
    cookies_arr.append(driver.get_cookie("bcookie")) 
    cookies_arr.append(driver.get_cookie("JSESSIONID"))
    cookies_arr.append(driver.get_cookie("_ga"))

    print(cookies_arr)

    cookies = ''
    for cookie in cookies_arr:
      cookies += cookie['name'] + "=" + cookie['value'] + "; "

    # ACCOUNTSCOLL.update({"username": user['username'], "password": user["password"]}, {"$set": {'cookies': cookies_arr}}, upsert = True)
    ACCOUNTSCOLL.insert({"username": user['username'], "password": user["password"],'cookies': cookies_arr, 'count': count})

  except:
    ACCOUNTSCOLL.insert({"username": user['username'], "password": user['password'], 'working': False, 'count': count})

  time.sleep(5)

  driver.close()

