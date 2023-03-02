import asyncio
from db import bad_words, hellos


async def parse_data_to_bad_words():
    with open('bad_words.txt', 'r') as file:
        f = file.read()
    data = f.split('\n')
    for i in data:
        document = {'bad_word': i.lower()}
        await bad_words.insert_one(document)


async def parse_data_to_hello_words():
    with open('hellos.txt', 'r') as file:
        f = file.read()
    data = f.split('\n')
    for i in data:
        document = {'hello_word': i.lower()}
        await hellos.insert_one(document)


async def main():
    tasks = [asyncio.ensure_future(parse_data_to_bad_words()), asyncio.ensure_future(parse_data_to_hello_words())]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())


