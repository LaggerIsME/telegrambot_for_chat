import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('localhost', 27017)
db = client.filters
bad_words = db.bad_words
hellos = db.hellos
anecdotes = db.anecdotes
