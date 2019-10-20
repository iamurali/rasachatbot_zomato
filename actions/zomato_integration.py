import requests
import json

base_url = "https://developers.zomato.com/api/v2.1/"

class ZomatoIntegration():

  def __init__(self, token):
    self.token = token

  def get_location(self, location='', limit=5):
    print('get_location', location, '----->')
    if str(limit).isalpha() == True:
      raise ValueError("limit is not a number")
    url = base_url + "locations?query=" + str(location) + "&count=" + str(limit)
    response = (requests.get(url, headers = self.__fetchheaders()).content).decode("utf-8")
    return json.loads(response)

  def restaurants_search(self, lat="", lon="", cuisines="", limit=10):
    url = base_url + "search?count=" + str(limit) + "&lat=" + str(lat) + '&lon=' + str(lon)
    if ((cuisines is not None) and (cuisines != 'None')):
      url = url + '&cuisines=' + str(cuisines)

    print(url, 'fettch url;::::')
    response = (requests.get(url, headers = self.__fetchheaders()).content).decode("utf-8")
    return (json.loads(response)["restaurants"])

  def __fetchheaders(self):
    return {'Accept': 'application/json', 'user-key': self.token}