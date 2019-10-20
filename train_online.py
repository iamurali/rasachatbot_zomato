from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.policies.memoization import MemoizationPolicy
from policy import RestaurantPolicy

class TrainOnline():

  def __init__(self):
    logging.basicConfig(level="INFO")
    self.nlu_intepreter = RasaNLUInterpreter(('./models/nlu/default/restaurant_finder'))


  def run(self, input_channel = ConsoleInputChannel(), training_data_file= 'data/babi_stories.md', domain_file='restaurant_domain.yml'):
    agent = Agent(domain_file, policies=[MemoizationPolicy(), RestaurantPolicy()], interpreter=self.nlu_intepreter)

    agent = Agent(domain_file, policies=[MemoizationPolicy(max_history=3), RestaurantPolicy()])
    agent.train_online(training_data_file, input_channel, max_history=3, batch_size=50, epochs=200)
    return agent
