class ActionSearchRestaurants():
  def name(self):
    return 'action_search_restaurants'


  def run(self, dispatcher, tracker, domain):
    dispatcher.utter_message('yes i will search')
    return []