import requests
from bs4 import BeautifulSoup


client = requests.Session()

HOMEPAGE_URL = 'https://www.linkedin.com'
LOGIN_URL = 'https://www.linkedin.com/uas/login-submit'

html = client.get(HOMEPAGE_URL).content
soup = BeautifulSoup(html, "html.parser")
csrf = soup.find("input", {"name": "loginCsrfParam"})['value']

print(csrf)


agent = {'Host': 'www.linkedin.com',
'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0',
'Accept': 'application/vnd.linkedin.normalized+json+2.1',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'Referer': 'https://www.linkedin.com/feed/?trk=guest_homepage-basic_nav-header-signin',
'x-li-lang': 'en_US',
'x-li-track': '{"clientVersion":"1.3.2961","osName":"web","timezoneOffset":5.5,"deviceFormFactor":"DESKTOP","mpName":"voyager-web"}',
'x-li-page-instance': 'urn:li:page:d_flagship3_profile_view_base;Db5LDSF7Rg6nerFvNtuotQ==',
'csrf-token': 'ajax:4219459705251760876',
'x-restli-protocol-version': '2.0.0',
'Connection': 'keep-alive',
'Cookie': 'bscookie="v=1&20190715111456eaa05bf5-5c57-40e5-8f15-5f1572539c6fAQGI7ymyVMJL73RkXkqw8YJlagPVCV3h"; bcookie="v=2&4b5d5057-2914-43bd-8843-66923732df9d"; JSESSIONID="ajax:4219459705251760876"; _ga=GA1.2.1346711522.1563189311;',
'Pragma': 'no-cache',
'Cache-Control': 'no-cache',
'TE': 'Trailers'}

# [{'secure': False, 'httpOnly': False, 'path': '/', 'domain': '.linkedin.com', 'value': 'bcb18c76-19cd-42c3-a8a6-6c0d19bcd9b4', 'name': 'spectroscopyId'}, {'secure': False, 'httpOnly': False, 'path': '/', 'expiry': 1626345476, 'domain': '.linkedin.com', 'value': '-1303530583%7CMCIDTS%7C18093%7CMCMID%7C68206286446291007123224831207109557192%7CMCAAMLH-1563791876%7C12%7CMCAAMB-1563791876%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1563194224s%7CNONE%7CvVersion%7C3.3.0%7CMCCIDH%7C1493197362', 'name': 'AMCV_14215E3D5995C57C0A495C55%40AdobeOrg'}, {'secure': False, 'httpOnly': False, 'path': '/', 'domain': '.linkedin.com', 'value': '1', 'name': 'AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg'}, {'secure': False, 'httpOnly': False, 'path': '/', 'expiry': 1563187617, 'domain': '.linkedin.com', 'value': '1', 'name': '_gat'}, {'secure': False, 'httpOnly': False, 'path': '/', 'expiry': 1626259075, 'domain': '.linkedin.com', 'value': 'GA1.2.923415915.1563187018', 'name': '_ga'}, {'secure': False, 'httpOnly': False, 'path': '/', 'expiry': 1563187904.924252, 'domain': '.linkedin.com', 'value': '"b=SB40:g=85:u=228:i=1563187006:t=1563187898:s=AQGDqe-lLr4kShDuoQZ0H1-K0657Uvfh"', 'name': 'lidc'}, {'secure': False, 'httpOnly': False, 'path': '/', 'domain': '.linkedin.com', 'value': 'v=2&lang=en-us', 'name': 'lang'}, {'secure': False, 'httpOnly': False, 'path': '/', 'expiry': 1565779077, 'domain': '.linkedin.com', 'value': 'AQKOHAEqfPCYhQAAAWv1NcYDNuMUlueu16LYbYtJL6gjz9lDLmxGukWSQdVuScqtxzPNiBzk3eLFBslZJ9on9iUjmojz5RiBa6myCC6Bucrbbloagv0RTR8GvDtKc1kXcMvF1ch2eCmLDJ0', 'name': 'UserMatchHistory'}, {'secure': False, 'httpOnly': False, 'path': '/', 'expiry': 1565779076, 'domain': '.linkedin.com', 'value': '68028484608040825313174978196645414915', 'name': 'aam_uuid'}, {'secure': True, 'httpOnly': False, 'path': '/', 'expiry': 1570963012.464049, 'domain': '.www.linkedin.com', 'value': '"ajax:8058862744467192425"', 'name': 'JSESSIONID'}, {'secure': False, 'httpOnly': False, 'path': '/', 'expiry': 1570963012.464035, 'domain': '.linkedin.com', 'value': 'true', 'name': 'liap'}, {'secure': True, 'httpOnly': True, 'path': '/', 'expiry': 1594723012.464011, 'domain': '.www.linkedin.com', 'value': 'AQEDASOjuAgCTVI7AAABa_U0yLgAAAFsGUFMuFEAbewmLSlNJbOsWwfogi0D_6HQOeoFi7uART30P75c26ersbxVXlB0cd0imXX1iwMVSk0zWq6QgUPk36PGkon7BeJPDL2FhxfuG2MhA44GDV8plb28', 'name': 'li_at'}, {'secure': False, 'httpOnly': False, 'path': '/', 'expiry': 1570963012.463944, 'domain': '.www.linkedin.com', 'value': 'v=1&pI2Q3', 'name': 'sl'}, {'secure': True, 'httpOnly': True, 'path': '/', 'expiry': 1626300860.428685, 'domain': '.www.linkedin.com', 'value': '"v=1&20190715103641c73189f2-26e8-493f-8aaa-cc88775b69c9AQHPNq4s2qtL-gFzpy_qE0eaHs4RmBEE"', 'name': 'bscookie'}, {'secure': False, 'httpOnly': False, 'path': '/', 'expiry': 1565779016.970317, 'domain': '.linkedin.com', 'value': 'CwEAAAFr9TTXSm6Ztk4iVVprR-2C4k81cimJqdNttAfHqCxfF_ZgmRDXw1X7eA1By2UwBfiyI9NLLQfKPsAz98zRbV4tpwyijLJy9XFpmRn6wQtP0nAJfITVTQC2pZsFwDTh9C6aE7OGIHAfSI5H24vG4lMCxFYu-enPJwsr08BExyEo__qgfP0LnDeDRYyNzIpHGrtWO8zJw1NvSOLkJZ5H3nCcnODZHLIQc2AOIMUJUOWea_oKY5kUDhZ55gauMTT_2c7SYX-G-pcozKTnwAbODVtmwGDdvP-YyFMh-G7o0hZJYa5si-GuHuYGcLlGoyTNYeZ64ncNp-8E2PtY_9guuZXqgQE', 'name': '_lipt'}, {'secure': False, 'httpOnly': False, 'path': '/', 'expiry': 1626300860.428658, 'domain': '.linkedin.com', 'value': '"v=2&b76afcad-80fb-4f91-8d79-5ca4595280d1"', 'name': 'bcookie'}]

# login_information = {
#     'session_key':'viral999g@gmail.com',
#     'session_password':'9898209177',
#     'loginCsrfParam': csrf,
#     'trk': 'guest_homepage-basic_sign-in-submit'

# }

# login = requests.post(LOGIN_URL, data=login_information)
# set_cookie_header = login.headers['Set-Cookie']
# cookie = str(set_cookie_header).replace('JSESSIONID="ajax:', '').replace('"; Path=/; Domain=.www.linkedin.com', '')
# print(cookie)

print(requests.get('https://www.linkedin.com/voyager/api/identity/profiles/harshal-davda-27161053/profileView', headers=agent ).json())