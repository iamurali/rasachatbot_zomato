from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import yaml
import warnings
import argparse
import logging

from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.policies.memoization import MemoizationPolicy
from actions.search_restaurant import ActionSearchRestaurants
from actions.send_email import ActionSendEmail, ActionRestartBot
from policy import RestaurantPolicy
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.featurizers import (MaxHistoryTrackerFeaturizer, BinarySingleStateFeaturizer)
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.channels.console import ConsoleInputChannel
from train_online import TrainOnline

logger = logging.getLogger(__name__)


def train_nlu():
  from rasa_nlu.training_data import load_data
  from rasa_nlu import config
  from rasa_nlu.model import Trainer
  training_data = load_data('data/franken_data.json')
  trainer = Trainer(config.load('nlu_model_config.yml'))
  trainer.train(training_data)
  model_directory = trainer.persist('models/nlu', fixed_model_name='restaurant_finder')
  return model_directory

def train_dialogue(domain_file='restaurant_domain.yml',
                    model_path="models/dialogue",
                    training_data_file='data/babi_stories.md'):
  featurizer = MaxHistoryTrackerFeaturizer(BinarySingleStateFeaturizer(), max_history=5)
  agent = Agent(domain_file, policies=[MemoizationPolicy(max_history=5), KerasPolicy(featurizer)])
  training_data = agent.load_data(training_data_file)
  agent.train(training_data, epochs=400, batch_size=100, validation_split=0.2)
  agent.persist(model_path)
  return agent


def run(server_forver=True):
  interpreter = RasaNLUInterpreter('models/nlu/default/restaurant_finder')
  agent = Agent.load('models/dialogue', interpreter=interpreter)

  if server_forver:
    agent.handle_channel(ConsoleInputChannel())
  return agent

if __name__ == '__main__':
  utils.configure_colored_logging(loglevel='INFO')

  parser = argparse.ArgumentParser(description='Bot started')
  parser.add_argument('task', choices=['train-nlu', 'train-dialogue', 'run', 'train-online'], help='what the bot should do - e.g. run or train?')
  task = parser.parse_args().task

  if task == 'train-nlu':
    train_nlu()
  elif task == 'train-dialogue':
    train_dialogue()
  elif task == 'train-online':
    TrainOnline().run()
  elif task == 'run':
    run()




