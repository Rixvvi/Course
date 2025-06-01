from src.vacancy import Vacancy


def test_vacancy_init_with_int_salary():
    vacancy = Vacancy("Dev", "https://example.com", 100000, "Coding", "Python")
    assert vacancy.salary == 100000


def test_vacancy_init_with_none_salary():
    vacancy = Vacancy("Dev", "https://example.com", None, "Coding", "Python")
    assert vacancy.salary == 0


def test_vacancy_init_with_dict_salary_avg():
    salary_dict = {"from": 100000, "to": 200000}
    vacancy = Vacancy("Dev", "https://example.com", salary_dict, "Coding", "Python")
    assert vacancy.salary == 150000


def test_vacancy_init_with_salary_from_only():
    salary_dict = {"from": 120000}
    vacancy = Vacancy("Dev", "https://example.com", salary_dict, "Coding", "Python")
    assert vacancy.salary == 120000


def test_vacancy_init_with_salary_to_only():
    salary_dict = {"to": 80000}
    vacancy = Vacancy("Dev", "https://example.com", salary_dict, "Coding", "Python")
    assert vacancy.salary == 80000


def test_vacancy_comparison_operators():
    v1 = Vacancy("A", "link1", 50000, "resp", "req")
    v2 = Vacancy("B", "link2", 70000, "resp", "req")

    assert v1 < v2
    assert v1 <= v2
    assert v2 > v1
    assert v2 >= v1


def test_vacancy_to_dict():
    v = Vacancy("Backend", "link", 120000, "Backend work", "Django")
    d = v._to_dict()
    assert d == {
        "name": "Backend",
        "link": "link",
        "salary": 120000,
        "responsibility": "Backend work",
        "requirements": "Django"
    }


def test_vacancy_negative_salary_defaults_to_zero():
    v = Vacancy("Dev", "link", -5000, "test", "reqs")
    assert v.salary == 0


def test_vacancy_invalid_salary_type():
    v = Vacancy("Dev", "link", "not_a_number", "test", "reqs")
    assert v.salary == 0
