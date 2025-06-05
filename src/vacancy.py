from typing import Union


class Vacancy:
    """Класс для создания вакансий"""
    __slots__ = ('name', 'link', 'salary', 'responsibility', 'requirements')

    def __init__(self, name: str, link: str, salary: Union[int, float, dict, None], responsibility: Union[str, None], requirements: Union[str, None]):
        """Конструктор"""
        self.name = name
        self.link = link
        self.salary = self.__validation(salary)
        self.responsibility = responsibility
        self.requirements = requirements

    def __validation(self, salary):
        """Функция, которая валидирует зарплату"""
        try:
            if salary is None:
                return 0
            if isinstance(salary, dict):
                return self.__validation_avg(salary)
            if isinstance(salary, (int, float)) and salary >= 0:
                return salary
            return 0
        except Exception as e:
            print(f'Возникла ошибка: {e}')
            return 0

    @staticmethod
    def __validation_avg(salary):
        """Функция, которая валидирует зарплату и находит среднее значение"""
        try:
            if isinstance(salary, dict):
                salary_from = salary.get('from')
                salary_to = salary.get('to')
                if salary_from is not None and salary_to is not None:
                    salary = (salary_from + salary_to) / 2
                    return salary
                elif salary_from is not None:
                    return salary_from
                elif salary_to is not None:
                    return salary_to
                else:
                    return 0
        except Exception as e:
            print(f'Возникла ошибка: {e}')
            return 0

    def __lt__(self, other):
        """Магический метод для сравнения"""
        return self.salary < other.salary

    def __le__(self, other):
        """Магический метод для сравнения"""
        return self.salary <= other.salary

    def __gt__(self, other):
        """Магический метод для сравнения"""
        return self.salary > other.salary

    def __ge__(self, other):
        """Магический метод для сравнения"""
        return self.salary >= other.salary

    def _to_dict(self) -> dict:
        """Функция, которая превращает объект класса в вакансию формата dict"""
        return {
            "name": self.name,
            "link": self.link,
            "salary": self.salary,
            "responsibility": self.responsibility,
            "requirements": self.requirements
        }

# if __name__ == "__main__":
#     vac1 = Vacancy("Дизайнер", "ссылочка", 50000, 'Много рисовать', "Требования для дизайнера")
#     vac2 = Vacancy("Менеджер", "ссылочка", 70000, 'Много разговаривать', "Требования для менеджера")
#     print(vac1._to_dict())
