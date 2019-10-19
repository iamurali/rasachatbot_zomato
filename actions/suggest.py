class ActionSuggest():
  def name(self):
    return 'action_suggest'

  def run(self, dispatcher, tracker, domain):
    # dispatcher.utter_message("here's what I found:")
    # dispatcher.utter_message(tracker.get_slot("matches"))
    # dispatcher.utter_message("is it ok for you? "
    #                          "hint: I'm not going to "
    #                          "find anything else :)")
    print('location', tracker.get_slot('location'))
    print('cuisine', tracker.get_slot('cuisine'))
    print('people', tracker.get_slot('people'))
    print('price', tracker.get_slot('price'))
    dispatcher.utter_message("BBQ")
    return []