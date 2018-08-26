# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot(
    'advobot trainer',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database='./advobot.sqlite3'
)

# Train based on the advobot corpus
bot.set_trainer(ChatterBotCorpusTrainer)
bot.train("chatterbot.corpus.advobot")
