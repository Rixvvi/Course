from src.reader_abc import VacancyMethods
import json


class ReaderJson(VacancyMethods):

    def __init__(self, file_name='vacancies.json'):
        self.__file_name = file_name

    def _read_file(self):
        try:
            with open(self.__file_name, 'r', encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_file(self, data):
        with open(self.__file_name, 'w', encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def add_vacancies(self, vacancy):
        data = self._read_file()
        if vacancy not in data:
            data.append(vacancy)
            self._save_file(data)

    def get_vacancies(self, name=None):
        data = self._read_file()
        result = []
        if not name:
            return data
        for item in data:
            for key, value in name.items():
                if item.get(key) != value:
                    break
            else:
                result.append(item)
        return result

    def delete_vacancies(self, vacancy):
        data = self._read_file()
        try:
            data.remove(vacancy)
            self._save_file(data)
        except Exception as e:
            print(f'Возникла ошибка: {e}')


if __name__ == "__main__":
    storage = ReaderJson()

    vac1 = ("Уборщик", "ссылочка", 50000, "Убирать дома и дворы")
    vac2 = ("Повар", "ссылочка", 70000, "Готовить вкусную еду")

    storage.add_vacancies(vac1)
    storage.add_vacancies(vac2)

    print(storage.get_vacancies())

    storage.delete_vacancies(vac1)
