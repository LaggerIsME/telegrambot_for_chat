import json
import asyncio
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression


# Класс для генератора ответов
class ReplicaGenerator:
    def __init__(self):
        self.alphabet = ' 1234567890-йцукенгшщзхъфывапролджэячсмитьбюёqwertyuiopasdfghjklzxcvbnm?%.,()!:;'
        self.vectorizer = CountVectorizer()
        self.clf = LogisticRegression()

    # Очистка стркои от мусора
    async def clean_str(self, r):
        r = r.lower()
        r = [c for c in r if c in self.alphabet]
        return ''.join(r)

    # Загрузка данных в модель
    async def update(self):
        with open('ai_for_chatting/dialogues.json', encoding='utf-8') as file:
            data = json.load(file)

        X_text = []
        y = []

        for block in data:
            if len(block) == 2:
                question = await self.clean_str(block['вопрос'])
                answers = block['ответ']
                if question and answers:
                    X_text += [question] * len(answers)
                    y += answers

        X = self.vectorizer.fit_transform(X_text)

        self.clf.fit(X, y)

    # Сгенерировать ответ
    async def get_generative_replica(self, text):
        text_vector = self.vectorizer.transform([text]).toarray()[0]
        question = self.clf.predict([text_vector])[0]
        return question


async def main(generator: ReplicaGenerator):
    await generator.update()
