# Telegram_monitoring
A python program which monitors telegram message

Steps for setup : 
1) Create an app on https://my.telegram.org/apps. To login, use your mobile number with country code
2) Populate values 'api_id' and 'api_hash' in config-template file.
3) Sign up on Twilio. Complete the setup for Programmable Voice and Programmable Messaging
4) Populate the values of Twilio section(i.e. - account_sid,auth_token,from_number,to_number )
5) Change the name of config-template.ini to config.ini
6) Download the requirements using command "pip install -r requirements.txt"
7) The program doesn't run on Spyder as there is some compatibility issue due to async nature of program. To run use "python message_handler.py".
8) The first time it runs, it would require login. On console, it would ask your mobile number with country code. An OTP would be sent to you from 'Telegram' account.
9) (Optional) You can deploy the script on cloud services(AWS,GCP).The script is killed after logging out. So use 'nohup' command to keep it alive. (Ref - https://stackoverflow.com/questions/2975624/how-to-run-a-python-script-in-the-background-even-after-i-logout-ssh) I had used 2 instances on AWS for redundancy and as fail-safe mechanism.

For documentation, refer https://docs.telethon.dev/en/latest/
