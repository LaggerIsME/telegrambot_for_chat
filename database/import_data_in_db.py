import asyncio
import json
from db import bad_words, hellos, anecdotes, gifs


async def parse_data_to_bad_words():
    with open('database/bad_words.txt', 'r') as file:
        f = file.read()
    data = f.split('\n')
    for i in data:
        document = {'bad_word': i.lower()}
        await bad_words.insert_one(document)


async def parse_data_to_hello_words():
    with open('database/hellos.txt', 'r') as file:
        f = file.read()
    data = f.split('\n')
    for i in data:
        document = {'hello_word': i.lower()}
        await hellos.insert_one(document)


async def parse_data_to_anecdotes():
    with open('database/anecdotes.json', 'r') as file:
        data = json.load(file)
    for i in data['anecdotes']:
        document = {'anecdote': i}
        await anecdotes.insert_one(document)


async def parse_data_to_gif():
    gif_doc = {'name': 'mygif', 'url': "https://tenor.com/ru/view/hello-anime-girl-gif-22450365"}
    await gifs.insert_one(gif_doc)


async def main():
    tasks = [asyncio.ensure_future(parse_data_to_bad_words()), asyncio.ensure_future(parse_data_to_hello_words()),
             asyncio.ensure_future(parse_data_to_anecdotes()), asyncio.ensure_future(parse_data_to_gif())]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())


