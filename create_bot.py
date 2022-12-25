from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from tgbot.config import load_config



config = load_config(".env")
storage = RedisStorage2() if config.tg_bot.use_redis else MemoryStorage()
# storage = RedisStorage2(host=config.redis.host, port=6379)
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
dp = Dispatcher(bot, storage=storage)
scheduler = AsyncIOScheduler()
