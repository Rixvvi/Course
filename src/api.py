import json

from src.api_abc import HhApiAbc
import requests


class HhApi(HhApiAbc):

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        self.__vacancies = []

    def _HhApiAbc__connection(self):
        response = requests.get(self.__url)
        if response.status_code != 200:
            return None
        else:
            return True

    def load_vacancies(self, keyword):
        self.__params['text'] = keyword
        if self._HhApiAbc__connection() is not None:
            while self.__params.get('page') != 20:
                response = requests.get(url=self.__url, params=self.__params)

                try:
                    data = response.json()['items']
                    for item in data:
                        vacancy = {
                            "name": item["name"],
                            "link": item["url"],
                            "salary": item["salary"],
                            "requirements": item["snippet"]["requirement"]
                        }
                        self.__vacancies.append(vacancy)
                    self.__params['page'] += 1
                    return self.__vacancies
                except Exception as e:
                    print(f'Ошибка при запросе: {e}')
                    break
        else:
            print('Возникла ошибка')
            return []

    def vacancies_json(self):
        data = self.__vacancies
        try:
            with open("vacancies.json", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f'Ошибка: {e}')


if __name__ == "__main__":
    a = HhApi()
    c = a.load_vacancies('повар')
    a.vacancies_json()
