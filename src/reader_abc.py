from abc import ABC, abstractmethod


class VacancyMethods(ABC):

    @abstractmethod
    def add_vacancies(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self, name):
        pass

    @abstractmethod
    def delete_vacancies(self, vacancy):
        pass
