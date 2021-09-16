import requests
import config


bot_token = config.bot_config["bot_token"]
bot_chat_id = config.bot_config["chat_id"]


def send_message(bot_message):
   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chat_id + '&parse_mode=Markdown&text=' + bot_message
   response = requests.get(send_text)
   return response.json()