from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from slack.rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurant_finder')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-802123317696-789341201010-789601485490-423f8c5e493b38e1a9700801d889a768', #app verification token
							'xoxb-802123317696-801919589748-zM2txMXdNETnkHDw6mJkVAdf', # bot verification token
							'QBVtotROW4GlL9RE5hwPU6sR', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))