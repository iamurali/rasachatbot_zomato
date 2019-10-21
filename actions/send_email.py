from rasa_core.events import Restarted
import smtplib

from rasa_core.actions.action import Action

class ActionSendEmail(Action):
  def name(self):
    return 'action_send_email'

  def run(self, dispatcher, tracker, domain):
    print(tracker.get_slot('email'), 'sending email')
    receiver = tracker.get_slot('email')
    dispatcher.utter_message("Sending email")
    self.send_email(receiver)
    return []


  def send_email(self, email):
    message = "List of restaurants to fetch:"
    global result
    sender = 'muralik@gmail.com'
    try:
      message += result
      server = smtplib.SMTP('smtp.gmail.com', 587)
      server.starttls()
      server.login(os.environ['EMAIL'], os.environ['PASSWORD'])
      server.sendmail(sender, email, message)
      return True
    except Exception as e:
      return False


class ActionRestartBot():
    def name(self):
        return 'action_restart_bot'

    def run(self, dispatcher, tracker, domain):
        return [Restarted()]