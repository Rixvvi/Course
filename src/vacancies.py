class Vacancies():
    def __init__(self, name, link, salary, requirements):
        self.name = name
        self.link = link
        self.salary = self.__validation(salary)
        self.requirements = requirements

    def __validation(self, salary):
        if salary is None:
            salary = 0
        return salary

    def __validation_avg(self, salary):
        if isinstance(salary, dict):
            salary_from = salary.get('from', 0)
            salary_to = salary.get('to', 0)
            average = (salary_from + salary_to) / 2
            salary = average
            return salary
        return 0

    def __lt__(self, other):
        return self.salary < other.salary

    def __le__(self, other):
        return self.salary <= other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __ge__(self, other):
        return self.salary >= other.salary
