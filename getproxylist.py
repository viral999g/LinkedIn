import requests, pymongo
from bs4 import BeautifulSoup
frm

myclient = pymongo.MongoClient("mongodb://localhost:27017/",
                                            connect=False)

MYDB = myclient['linkedIn']
PROFILECOLL = MYDB['profiles2']
ACCOUNTSCOLL = MYDB['accounts']
PROXIESCOLL = MYDB['proxies']

agent = {'Host': 'proxy6.net',
'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0',
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'Referer': 'https://proxy6.net/en/checker',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'X-Requested-With': 'XMLHttpRequest',
'Content-Length': '91',
'Connection': 'keep-alive',
'Cookie': 'PHPSESSID=8s1m1ii0pn03fkd2chelp3m415; lng=en; ref_url=https%3A%2F%2Fwww.google.com%2F; _ym_uid=156327052397031758; _ym_d=1563270523; _ym_wasSynced=%7B%22time%22%3A1563360123247%2C%22params%22%3A%7B%22eu%22%3A0%7D%2C%22bkParams%22%3A%7B%7D%7D; _ym_isad=2; _ym_hostIndex=0-2%2C1-0',
'Pragma': 'no-cache',
'Cache-Control': 'no-cache'}

def getproxieslist():
  soup = BeautifulSoup(requests.get("https://www.sslproxies.org/").text)
  div_table = soup.find("table", {"id": "proxylisttable"})
  tr_list = div_table.find_all("tr")

  count = 0
  proxies = []

  for tr in tr_list:
    try:
      rows = tr.find_all('td')
      ip = rows[0].text
      port = rows[1].text
      https_check = tr.find('td', {'class', 'hx'})
      if https_check.text == 'yes':
        PROXIESCOLL.update({"ip": ip}, {"$set": {"ip": ip, "port": port, "active": True}}, upsert=True)
    except:
      pass

def proxychecker(ip ,port):
  url = "https://proxy6.net/en/checker"
  soup = BeautifulSoup(requests.get(url).text)

  key = soup.find("input", {"name": "key"})['value']
  link1 = "https://proxy6.net/checker/pre"
  link2 = "https://proxy6.net/checker/check"
  link3 = "https://sockslist.net/request_check?i=" + ip + ":" + port + "&_=1563363247121"

  # print(requests.post(link1, headers=agent,data={"form_id": 'form-checker', "list": ip + ":" + port, 'hash': '', 'key': key}).text)
  print(requests.post(link2, headers=agent,data={"country_detect": 0, "item": [ip, port], 'key': key}).text)

proxychecker('171.25.164.123', '58363')
