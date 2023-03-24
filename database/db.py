import motor.motor_asyncio
from aiogram.contrib.fsm_storage.redis import RedisStorage2

# MongoDB
MONGO_URI = f'mongodb://mongo:27017'
# Подключение к БД
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
# Создание БД и коллекций
db = client.filter
bad_words = db.bad_words
hellos = db.hellos
anecdotes = db.anecdotes
gifs = db.gifs
instructions = db.instructions
tops = db.tops

# Redis
host = 'redis'
port = 6379
redis = RedisStorage2(db=2, host=host, port=6379)
