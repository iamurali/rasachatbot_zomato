from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
import os
import pprint, json
from actions.zomato_integration import ZomatoIntegration
from rasa_core.events import SlotSet

class ActionSearchRestaurants(Action):
  def name(self):
    return 'action_search_restaurants'


  def run(self, dispatcher, tracker, domain):
    location = tracker.get_slot('location')
    cuisine_type = tracker.get_slot('cuisine')
    print('price reader', tracker.get_slot('budget'))
    print("______________", cuisine_type, location, 'location')
    if not location:
      return []
    zomato = ZomatoIntegration(os.environ['ZOMATO_API_KEY'])
    longitude, latitude = self.__fetch_location_details(zomato, location)
    restaurants = self.__fetch_restaurants(zomato, longitude, latitude, cuisine_type)

    global result
    result = ""
    for restaurant in restaurants:
      result = result + "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+ " has been rated "+ restaurant['restaurant']['user_rating']['aggregate_rating'] + "\n"

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
