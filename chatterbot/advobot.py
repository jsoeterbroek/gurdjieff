# -*- coding: utf-8 -*-
from chatterbot import ChatBot

import logging
#logging.basicConfig(level=logging.INFO)

bot = ChatBot(
    'terminal',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    database='./advobot.sqlite3'
)

# Get a response to an input statement
#response = advobot.get_response("Hello, how are you today?")
#print(response)

print(">> Welkom bij Advobot. Type iets om te beginnen")

while True:
    try:
        bot_input = bot.get_response(None)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
