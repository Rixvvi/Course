class Vacancy:
    __slots__ = ('name', 'link', 'salary', 'requirements')

    def __init__(self, name, link, salary, requirements):
        self.name = name
        self.link = link
        self.salary = self.__validation(salary)
        self.requirements = requirements

    def __validation(self, salary):
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
        try:
            if isinstance(salary, dict):
                if salary.get('from') is not None:
                    salary_from = salary.get('from', 0)
                else:
                    salary_from = 0
                if salary.get('to') is not None:
                    salary_to = salary.get('to', 0)
                else:
                    salary_to = 0
                salary = (salary_from + salary_to) / 2
            return salary
        except Exception as e:
            print(f'Возникла ошибка: {e}')
            return 0

    def __lt__(self, other):
        return self.salary < other.salary

    def __le__(self, other):
        return self.salary <= other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __ge__(self, other):
        return self.salary >= other.salary


if __name__ == "__main__":
    vac1 = Vacancy("Дизайнер", "link1", 50000, "Требования для дизайнера")
    vac2 = Vacancy("Менеджер", "link2", 70000, "Требования для менеджера")
    print(vac1.__le__(vac2))
