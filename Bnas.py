import time
from telegram import Bot
# Replace with your bot's API token
API_TOKEN = 'your_telegram_bot_token'
# The group chat ID (you can get this
from the bot when added to the group)
GROUP_CHAT_ID = 'your _group_chat_id'
# Create a Bot instance
bot = Bot (token=API_TOKEN)
# Define an array of messages
messages = [
"Hello, this is the first message!",
"This is the second message!",
"Here comes the third message!",
"Finally, the fourth message!"
]
def send_messages ():
for message in messages:
# Send each message in the
array
bot. send.
_message (chat_id=GROUP_CHAT_I
D, text=message)
time.sleep (60) # Wait for 60
seconds before sending the next message
# Start sending the messages
send_messages ()
