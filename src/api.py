import json

import requests

from src.api_abc import HhApiAbc


class HhApi(HhApiAbc):
    """Класс для подключения к api и получения вакансий по ключевому слову"""

    def __init__(self):
        """Конструктор"""
        self.__url = "https://api.hh.ru/vacancies"
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        self.__vacancies = []

    def _HhApiAbc__connection(self) -> bool:
        """Функция, которая подключается к api и проверяет, корректен ли запрос"""
        response = requests.get(self.__url, params=self.__params)
        if response.status_code != 200:
            return False
        else:
            return True

    def load_vacancies(self, keyword: str):
        """Функция, которая получает вакансии по введённой профессии, приводит к красивому виду и записывает в файл"""
        self.__params['text'] = keyword
        if self._HhApiAbc__connection() is not False:
            while self.__params.get('page') != 20:
                response = requests.get(url=self.__url, params=self.__params)

                try:
                    data = response.json()['items']
                    for item in data:
                        vacancy = {
                            "name": item.get("name", ""),
                            "link": item.get("url", ""),
                            "salary": item.get("salary", ""),
                            "description": item.get("snippet", {}).get("responsibility", ""),
                            "requirements": item.get("snippet", {}).get("requirement", "")
                        }
                        self.__vacancies.append(vacancy)
                    self.__params['page'] += 1
                    try:
                        with open("vacancies.json", "w", encoding="utf-8") as file:
                            json.dump(self.__vacancies, file, indent=4, ensure_ascii=False)
                    except Exception as e:
                        print(f'Ошибка: {e}')
                except Exception as e:
                    print(f'Ошибка при запросе: {e}')
                    break
            return self.__vacancies
        else:
            print('Возникла ошибка')
            return []

# if __name__ == "__main__":
#     a = HhApi()
#     c = a.load_vacancies('повар')
