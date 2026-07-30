from os import getenv
import asyncio
from aiogram import Bot , Dispatcher

TOKEN = getenv("BOT_TOKEN")

db = Dispatcher()