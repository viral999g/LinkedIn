import requests, pymongo, json

myclient = pymongo.MongoClient("mongodb://localhost:27017/",
                                            connect=False)

MYDB = myclient['linkedIn']
PROFILECOLL = MYDB['profiles2']


agent = {'Host': 'www.linkedin.com',
'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0',
'Accept': 'application/vnd.linkedin.normalized+json+2.1',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'Referer': 'https://www.linkedin.com/mynetwork/invite-connect/connections/',
'x-li-lang': 'en_US',
'x-li-track': '{"clientVersion":"1.3.2830","osName":"web","timezoneOffset":5.5,"deviceFormFactor":"DESKTOP","mpName":"voyager-web"}',
'x-li-page-instance': 'urn:li:page:d_flagship3_people_connections;5kU2IHxMSI60eXlwzuT4nQ==',
'csrf-token': 'ajax:7027691122196337209',
'x-restli-protocol-version': '2.0.0',
'Connection': 'keep-alive',
'Cookie': 'bcookie="v=2&9385ef25-02e3-4777-8ce1-c0f7effaa469"; bscookie="v=1&2019040407091563d4e9f5-280f-4505-8c30-9bd6853d2510AQGS07T29AsEgpN7RIEvNPJc3H3vGKpd"; lidc="b=SB40:g=84:u=225:i=1562848145:t=1562907013:s=AQHu9iqSjA5mos9bYpKRg4zfAPt4kYWz"; UserMatchHistory=AQLuo2EQP5XnUwAAAWvhCOS17iYgFKZFCiSB2AqPYw99aKWeGkhuVODid2k3cAeRe3X0S1lzFohth1iitNxXAdf6WJh1_k6byHf8EevAQMU8Fiqz5IuspzsevCwABlEdwpL8wAliFguVKfeaKdP-S8l2Kw4NNZswv06Cglll5A; JSESSIONID="ajax:7027691122196337209"; lissc1=1; lissc2=1; sl=v=1&DgnLx; liap=true; li_at=AQEDASOjuAgAAkk3AAABa-ECLsgAAAFsBQ6yyFEArzsr7Bw7HHNAKmZ_siDsAFVXyM-cHtjVGubdIYLLgYQaiuHVny0UqfnQXxaxLjYLpdv9fBjWWoV83ru0Z8THH2w_r1J3p0ml3tdExm-VhM2lD3PN; lang=v=2&lang=en-us; _lipt=CwEAAAFr4QjcYtmyTbaMGsFsAaToEGTWJuzxevCNn3IWv59HuxX5OB3bAXvfa6CWFPqP3XKgskvxq3cECnw38mQJJITVtQ45V1QJiL1mGy0I4HwixT4JxDLc9Xsf4BnaLUxFlVtiJa6L6PNQPyMn-be5n95i1K9MY9s5_A7mkfoq24rNKi1F6dq0xGkw5rDK7Og3G1kUQndNfx5gFIu0oscvQlnYbQpT8UBPESiEUmrU3Q1wqQKLANSsulmABJmLpGjdVrcwLuIi7ECLWYRss1ejKHQXhWChuDQztRBjoXwP_-IQXb9t-PqXDs5GXvJnzu2M3ujtuceCgARxTQrX8SIE_CHQxb4; _ga=GA1.2.1663427579.1562848155; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-1303530583%7CMCIDTS%7C18089%7CMCMID%7C17337149683438522262679947931445074760%7CMCAAMLH-1563452959%7C12%7CMCAAMB-1563452959%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1562855359s%7CNONE%7CMCCIDH%7C1493197362%7CvVersion%7C3.3.0; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; aam_uuid=17835086685223831132737688628152068227; _gat=1',
'Pragma': 'no-cache',
'Cache-Control': 'no-cache',
'TE': 'Trailers'}

agent2 = {'Host': 'www.linkedin.com',
'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0',
'Accept': 'application/vnd.linkedin.normalized+json+2.1',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'Referer': 'https://www.linkedin.com/in/vasudha-thirani-99b27129/',
'x-li-lang': 'en_US',
'x-li-track': '{"clientVersion":"1.3.2961","osName":"web","timezoneOffset":5.5,"deviceFormFactor":"DESKTOP","mpName":"voyager-web"}',
'x-li-page-instance': 'urn:li:page:d_flagship3_profile_view_base;j09E8OBiSOagQZjJunoX0Q==',
'csrf-token': 'ajax:1672710219561989399',
'x-restli-protocol-version': '2.0.0',
'Connection': 'keep-alive',
'Cookie': 'bcookie="v=2&9385ef25-02e3-4777-8ce1-c0f7effaa469"; bscookie="v=1&2019040407091563d4e9f5-280f-4505-8c30-9bd6853d2510AQGS07T29AsEgpN7RIEvNPJc3H3vGKpd"; UserMatchHistory=AQKc2oEoeU6VggAAAWv0mEy-i0Wolzs0ytdBtHM5CK8Vgt5_X_JY3fvoHTmXttNwYSObR_x-A5iu6OIOB-pOCze0r8sMJzbgWRzZPWKY9nuaJxT59Xbrp0S0IZJaCikeZe13yU7NMzxl-TyznwbsSNeL2ddUV6VKNTfeJuVkxl00p7svxpn5QdX4sCktFNwbASM8yWiNX9d-TbnhtYUmvqVaayiYNygozHTs; JSESSIONID="ajax:1672710219561989399"; lissc1=1; lissc2=1; _lipt=CwEAAAFr9JhE2jKS8HwLOVn3mgdH1v0PyJM-VM7VApekPfPX7Ir02yqQaHdxQ-I23xq8MHS8xZCVrQOFdnnMxpAjXMlVHV7rQBfgdsNcVUyjpQVHqEg6UC2SnyMRZ7gX-Vw90fyR-1pGgEtT_nyLloevfCuKnh1Ly82v_Wgbr6ywx1mIyDdE1l8wZZwzAV6ThA4xXyy_CKlYBSPnVJmkdgkMlbDtVzEqOp0Y6E_0ukNVqQzvwu6DWjLVepcItsq1Eh47dL-mtCcUMc3jDsH8ZbNTrexXeQUynZdJhJmgut_RmyASdbxFXlS2oKrkPRMWhqPwbtXH8dOX8XwLyRqMl6sU-MYft-0; _ga=GA1.2.1663427579.1562848155; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-1303530583%7CMCIDTS%7C18093%7CMCMID%7C17337149683438522262679947931445074760%7CMCAAMLH-1563776585%7C12%7CMCAAMB-1563776585%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1563178985s%7CNONE%7CMCCIDH%7C1493197362%7CvVersion%7C3.3.0; aam_uuid=17835086685223831132737688628152068227; _guid=30cd9896-a9c0-4e23-869e-9a2742aa9ccc; li_oatml=AQG3iFuP9OG6RgAAAWvlAocZxfrWZraiHellc3GHMfVsfjswCxIMGBylul_dsv3lW8zVrw6yLfI9LdIMjrwFsHR9bdSpsi9X; lidc="b=SB40:g=85:u=228:i=1563176745:t=1563187898:s=AQGR0-OrJiBpB9KpEPOFYqwlI2H7PkTl"; visit=v=1&M; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; sdsc=1%3A1SZM1shxDNbLt36wZwCgPgvN58iw%3D; sl=v=1&lXcem; li_at=AQEDASOjuAgAEdwXAAABa_SYOf0AAAFsGKS9_VEAnZ3vbq20CjfkQWao9IXRNtenWRSWym6zyBgtfqrdtKJ24dpwKRXVt7WO93wFN7tg4JiADCMzXVsRYRx4i24pPkOB0s242JlQA4YGe51ZpH6uGDKh; liap=true; lang=v=2&lang=en-us',
'Pragma': 'no-cache',
'Cache-Control': 'no-cache',
'TE': 'Trailers'}




def get_all_connections(account_id):
  start = 0
  count = 500

  while True:
    url = "https://www.linkedin.com/voyager/api/relationships/connections?count=" + str(count) + "&sortType=RECENTLY_ADDED&start=" + str(start)
    response = requests.get(url, headers = agent).json()
    if response['included'] == []:
      break
    else:
      data = response['included']
      for node in data:
        if node['$type'] == 'com.linkedin.voyager.identity.shared.MiniProfile':
          del node['$type']
          del node['backgroundImage']
          del node['picture']
          node["_id"] = node["publicIdentifier"]
          node["entity_id"] = str(node["publicIdentifier"]).replace("urn:li:fs_miniProfile:", "")
          node['relationWith'] = account_id
          node['data'] = False
          try:
            PROFILECOLL.insert(node)
          except:
            pass


    start = start + count


def getSkills(id):
  skills = []
  url = "https://www.linkedin.com/voyager/api/identity/profiles/" + id + "/skillCategory?includeHiddenEndorsers=true"
  response = requests.get(url, headers=agent).json()
  data = response['included']

  for skill in data:
    if skill["$type"] == 'com.linkedin.voyager.identity.profile.Skill':
      skills.append(skill["name"])

  return skills

def getContactInfo(id):
  url = "https://www.linkedin.com/voyager/api/identity/profiles/" + id + "/profileContactInfo"
  data = requests.get(url, headers=agent).json()['data']
  return data

def getExperience(id):
  experience = []
  url = "https://www.linkedin.com/voyager/api/identity/profiles/" + id + "/positionGroups?start=0"
  data = requests.get(url, headers=agent).json()['included']
  for d in data:
    if d['$type'] == 'com.linkedin.voyager.identity.profile.Position':
      experience.append(d)

  return experience

def getEducation(id):
  education = []
  url = "https://www.linkedin.com/voyager/api/identity/profiles/" + id + "/educations?start=0"
  data = requests.get(url, headers=agent).json()['included']
  for d in data:
    if d['$type'] == 'com.linkedin.voyager.identity.profile.Education':
      education.append(d)

  return education

def getInterests(id):
  Interests = []
  url = "https://www.linkedin.com/voyager/api/identity/profiles/" + id + "/following?count=100&q=followedEntities"
  data = requests.get(url, headers=agent).json()['included']
  for d in data:
    if d['$type'] != 'com.linkedin.voyager.common.FollowingInfo':
      Interests.append(d)

  return Interests

def getUserData(id):
  obj = {}
  obj['licences'] = []
  url = "https://www.linkedin.com/voyager/api/identity/profiles/" + id + "/profileView"
  response = requests.get(url, headers=agent).json()
  included = response['included']
  data = response['data']

  for d in included:
    if d['$type'] == 'com.linkedin.voyager.identity.profile.Profile':
      print(d)
      obj['about'] = d['summary']
      obj['student'] = d['student']
      obj['headline'] = d['headline']
      obj['industryName'] = d['industryName']
      obj['locationName'] = d['locationName']
      obj['address'] = d['address']
      obj['geoCountryName'] = d['geoCountryName']
      obj['birthDate'] = d['birthDate']
      obj['countryCode'] = d['location']['basicLocation']['countryCode']

    if d['$type'] == 'com.linkedin.voyager.identity.profile.Certification':
      obj['licences'].append(d)

  return obj

def getData(account_id):
  users = PROFILECOLL.find({"relationWith": account_id, "data": False})
  for u in users:
    profileIdentifier = u['publicIdentifier']
    entity_id = u['entity_id']

    print(profileIdentifier)

    user_obj = getUserData(profileIdentifier)
    user_obj['skills'] = getSkills(profileIdentifier)
    user_obj['contactInfo'] = getContactInfo(profileIdentifier)
    user_obj['experience'] = getExperience(entity_id)
    user_obj['education'] = getEducation(entity_id)
    user_obj['interests'] = getInterests(profileIdentifier)

    user_str = json.dumps(user_obj)
    user_str = user_str.replace('$', '&')

    user_obj = json.loads(user_str)
    user_obj['data'] = True

    PROFILECOLL.update({"_id": profileIdentifier}, {"$set": user_obj})


# get_all_connections("viral-gandhi-5a02b5148")
# getData("viral-gandhi-5a02b5148")

print(requests.get("https://www.linkedin.com/voyager/api/identity/profiles/harshal-davda-27161053/profileView", headers=agent2))

