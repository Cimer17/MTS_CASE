from aiogram import Dispatcher, Bot, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import configparser
import logging

config = configparser.ConfigParser()
config.read("settings.ini")
tokenBot = config["bot"]["bot_token"]

bot = Bot(token=tokenBot)
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)
