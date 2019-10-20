from rasa_core.events import Restarted

class ActionSendEmail():
  def name(self):
    return 'action_send_email'

  def run(self, dispatcher, tracker, domain):
    dispatcher.utter_message("Sending email")
    return []

class ActionRestartBot():
    def name(self):
        return 'action_restart_bot'

    def run(self, dispatcher, tracker, domain):
        return [Restarted()]