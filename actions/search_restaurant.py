from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import os
import pprint, json
from actions.zomato_integration import ZomatoIntegration

class ActionSearchRestaurants():
  def name(self):
    return 'action_search_restaurants'


  def run(self, dispatcher, tracker, domain):
    # print('people', tracker.get_slot('people'))
    # print('price', tracker.get_slot('price'))

    location = tracker.get_slot('location')
    cuisine_type = tracker.get_slot('cuisine')
    if not location:
      return []
    zomato = ZomatoIntegration(os.environ['ZOMATO_API_KEY'])
    longitude, latitude = self.__fetch_location_details(zomato, location)
    restaurants = self.__fetch_restaurants(longitude, latitude, cuisine_type)
    result = ""
    for restaurant in restaurants:
      result = response + "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+"\n"

    dispatcher.utter_message("-----" + result)
    return [SlotSet('location', location)]

  def __fetch_restaurants(self, zomato, longitude, latitude, cuisine_type):
    cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
    cuisines = str(cuisines_dict.get(cuisine_type))
    restaurants = zomato.restaurants_search(longitude, latitude, cuisines)

    if (len(restaurants) == 0):
      raise ValueError("No restaurants found with the input given")
    return restaurants


  def __fetch_location_details(self, zomato, location):
    location_details = zomato.get_location(location)

    if len(location_details['location_suggestions']) == 0:
      raise ValueError("Invalid location")

    latitude = location_details['location_suggestions'][0]['latitude']
    longitude = location_details['location_suggestions'][0]['longitude']
    return [longitude, latitude]
