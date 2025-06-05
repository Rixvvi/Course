from src.api import HhApi
from src.help_file import get_search_str, top_transactions


def user_interaction():
    search_query = input("Введите профессию, по которой хотите отсортировать вакансии: ")

    filter_words = input("Введите ключевое слово в описании для фильтрации вакансий: ")

    while True:
        try:
            top_n = int(input("Введите количество вакансий для вывода в топ N по средней зарплате: "))
            break
        except Exception:
            print("Обязательно введите число")

    # фильтрация по профессии
    hh_api = HhApi()
    filtered_vacancies = hh_api.load_vacancies(search_query)

    # ключевое слово в описании
    sorted_vacancies = get_search_str(filtered_vacancies, filter_words)
    print(sorted_vacancies)

    # количество вакансий
    top_vacancies = top_transactions(filtered_vacancies, top_n)
    print(top_vacancies)


if __name__ == "__main__":
    user_interaction()
