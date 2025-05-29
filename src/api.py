from src.api_abc import HhApiAbc
import requests


class HhApi(HhApiAbc):

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        self.__vacancies = []

    def __connection(self):
        response = requests.get(self.__url, params=self.__params)
        if response.status_code != 200:
            print(f"Ошибка! Код ответа: {response.status_code}")
        else:
            print('Запрос успешно отработал')

    def load_vacancies(self, keyword):
        self.__params['text'] = keyword
        while self.__params.get('page') != 20:
            self.__connection()
            try:
                response = requests.get(self.__url, params=self.__params)
                vacancies = response.json()['items']
                self.__vacancies.extend(vacancies)
                self.__params['page'] += 1
            except Exception as e:
                print(f'Ошибка при запросе: {e}')
