import re


def get_search_str(data: list[dict], string_search: str) -> list[dict]:
    """Функция, которая принимает строку пользователя и возвращает ответ,
    в описании которого находится переданная пользователем строка"""
    result = []
    try:
        for vacancy in data:
            description = vacancy.get("description") or ""
            description_match = re.search(rf"{string_search}", description, flags=re.IGNORECASE)
            if description_match:
                result.append(vacancy)
        return result
    except Exception as e:
        print(e.__class__.__name__)
        return []


def top_transactions(data: list[dict], n) -> list[dict]:
    """Функция, которая возвращает топ-n вакансий по средней зарплате"""

    def get_avg_salary(vacancy):
        salary_info = vacancy.get('salary')
        if not salary_info:
            return 0
        salary_from = salary_info.get('from')
        salary_to = salary_info.get('to')
        if salary_from is not None and salary_to is not None:
            return (salary_from + salary_to) / 2
        elif salary_from is not None:
            return salary_from
        elif salary_to is not None:
            return salary_to
        return 0

    sorted_data = sorted(data, key=get_avg_salary, reverse=True)
    return sorted_data[:n]
