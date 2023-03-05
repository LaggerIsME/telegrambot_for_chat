import asyncio
import json
from db import bad_words, hellos, anecdotes, gifs, instructions


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


async def parse_data_to_gifs():
    with open('database/gifs.json', 'r') as file:
        data = json.load(file)
    for i in data['gifs']:
        gif_doc = {'url': i}
        await gifs.insert_one(gif_doc)


async def parse_data_to_intsructions():
    with open('database/instructions.json', 'r') as file:
        data = json.load(file)
    for i in data:
        try:
            doc = {'_id': i, 'text': data[i]}
            await instructions.insert_one(doc)
        except:
            pass


async def main():
    tasks = [asyncio.ensure_future(parse_data_to_bad_words()), asyncio.ensure_future(parse_data_to_hello_words()),
             asyncio.ensure_future(parse_data_to_anecdotes()), asyncio.ensure_future(parse_data_to_gifs()),
             asyncio.ensure_future(parse_data_to_intsructions())]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())


