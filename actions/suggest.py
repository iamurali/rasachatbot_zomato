class ActionSuggest():
  def name(self):
    return 'action_suggest'

  def run(self, dispatcher, tracker, domain):
    dispatcher.utter_message("here's what I found:")
    dispatcher.utter_message(tracker.get_slot("matches"))
    dispatcher.utter_message("is it ok for you? "
                             "hint: I'm not going to "
                             "find anything else :)")
    return []