from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from slack.rasa_slack_connector import SlackInput

import os
nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurant_finder')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput(os.environ['OAuth_Access_Token'],#app verification token
							os.environ['Bot_User_OAuth_Access_Token'],# bot verification token
							os.environ['verification_token'], # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))