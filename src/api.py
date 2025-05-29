from src.api_abc import HhApiAbc
import requests


class HhApi(HhApiAbc):

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        self.__vacancies = []

    def _connection(self):
        response = requests.get(self.__url, params=self.__params)
        if response.status_code != 200:
            return None
        else:
            return response

    def load_vacancies(self, keyword):
        self.__params['text'] = keyword
        while self.__params.get('page') != 20:
            response = self._connection()
            if response is None:
                print('Ошибка')
            try:
                vacancies = response.json()['items']
                self.__vacancies.extend(vacancies)
                self.__params['page'] += 1
            except Exception as e:
                print(f'Ошибка при запросе: {e}')
