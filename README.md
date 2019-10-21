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
       
       
## How to run the application :
    
1. Train the Project
   python bot.py train-nlu
   
2. Dialogue Flow
   python bot.py train-dialogue

3. Run the Application
   python bot.py run
   
4. Interactive Learning (Train the Project using online)
   python bot.py train-online
  
  

