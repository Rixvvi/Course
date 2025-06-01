from abc import ABC, abstractmethod


class HhApiAbc(ABC):
    """Абстрактный класс для подключения к api и получения вакансий по ключевому слову"""

    @abstractmethod
    def __connection(self):
        pass

    @abstractmethod
    def load_vacancies(self, keyword):
        pass
