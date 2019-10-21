# rasachatbot_zomato


In the Project we are using the environment variables for the credentials and we are accessing using

1. Required Environment Variables for Zomato:
    1. ZOMATO_API_KEY
       os.environ['ZOMATO_API_KEY']
2. Required Environment Variabled for Slack:
    1. OAuth_Access_Token
       os.environ['OAuth_Access_Token']
    2. Bot_User_OAuth_Access_Token
       os.environ['Bot_User_OAuth_Access_Token']
    3. verification_token
       os.environ['verification_token']
3. Required Environment Variables for Gmail:
    1. EMAIL
       os.environ['EMAIL']
    2. PASSWORD
       os.environ['PASSWORD']

## Setup py requirements
  jsonpickle==0.9.6
  six==1.11.0
  redis==2.10.6
  fakeredis==0.10.3
  future==0.16.0
  numpy==1.14.3
  typing==3.6.4
  ruamel.yaml==0.15.37
  requests==2.18.4
  graphviz==0.8.3
  keras==2.1.6
  tensorflow==1.8.0
  h5py==2.7.1
  apscheduler==3.5.1
  tqdm==4.23.3
  ConfigArgParse==0.13.0
  networkx==2.1
  fbmessenger==5.2.0
  pykwalify<=1.6.0
  coloredlogs==10.0
  flask==1.0.2
  flask_cors==3.0.4
  scikit-learn==0.19.1
  rasa_nlu~=0.12.3
  slackclient==1.2.1
  python-telegram-bot==10.1.0
  twilio==6.14.0
  mattermostwrapper==2.1
  colorhash==1.0.2

## additional
pypandoc==1.4
rasa_core==0.10.1
zomatopy==1.0.10


## How to run the application :

1. Train the Project
   python bot.py train-nlu

2. Dialogue Flow
   python bot.py train-dialogue

3. Run the Application
   python bot.py run

4. Interactive Learning (Train the Project using online)
   python bot.py train-online



