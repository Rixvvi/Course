import json

from src.reader_abc import VacancyMethods


class ReaderJson(VacancyMethods):
    """Класс для добавления, получения и удаления вакансий"""

    def __init__(self, file_name='vacancies.json'):
        """Конструктор"""
        self.__file_name = file_name

    def _read_file(self):
        """Функция, которая читает файл"""
        try:
            with open(self.__file_name, 'r', encoding="utf-8") as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f'Возникла ошибка: {e}')
            return []

    def _save_file(self, data):
        """Функция, которая записывает в файл"""
        try:
            with open(self.__file_name, 'w', encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f'Возникла ошибка: {e}')

    def add_vacancies(self, vacancy):
        """Функция, которая добавляет вакансию"""
        data = self._read_file()
        if vacancy not in data:
            data.append(vacancy)
            self._save_file(data)

    def get_vacancies(self, name=None):
        """Функция, которая получает вакансии"""
        data = self._read_file()
        result = []
        if name is None:
            return data
        for item in data:
            for key, value in name.items():
                if item.get(key) != value:
                    break
            else:
                result.append(item)
        return result

    def delete_vacancies(self, vacancy):
        """Функция, которая удаляет вакансию"""
        data = self._read_file()
        new_data = []
        if not data:
            return []
        try:
            for vac in data:
                if vac != vacancy:
                    new_data.append(vac)
            self._save_file(new_data)
            return new_data
        except Exception as e:
            print(f'Возникла ошибка: {e}')
            return []

# if __name__ == "__main__":
#     storage = ReaderJson()
#     vac1 = {'name': "Уборщик", 'link': "ссылочка", 'salary': 50000, 'responsibility': "Трудоёмкий процесс",
#             'requirements': "Убирать дома и дворы"}
#     vac2 = {'name': "Повар", 'link': "ссылочка", 'salary': 70000, 'responsibility': "Любить вкусно кушать",
#             'requirements': "Готовить вкусную еду"}
#     vac3 = {'name': "Баба-Яга", 'link': "ссылочка", 'salary': 100000, 'responsibility': "Нужна ступа и метла",
#             'requirements': "Пугать детишек"}
#     storage.add_vacancies(vac1)
#     storage.add_vacancies(vac2)
#     storage.add_vacancies(vac3)
#     storage.get_vacancies()
#     storage.delete_vacancies(vac1)
