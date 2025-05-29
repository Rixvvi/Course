from abc import ABC, abstractmethod


class HhApiAbc(ABC):

    @abstractmethod
    def __connection(self):
        pass

    @abstractmethod
    def load_vacancies(self, keyword):
        pass
