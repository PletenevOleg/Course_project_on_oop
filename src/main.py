from classes.vacancies_api import HeadHunterApi, SuperJobApi
from classes.utils import filter_vacancies, get_top_vacancies
from classes.json_saver import JSONSaver

def main():
    """"Взаимодействие с пользователем"""
    # Ввод ключевого слова для поиска вакансий
    keyword = input('Введите слово для поиска вакансии: \n')

    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh = HeadHunterApi(keyword)
    sj = SuperJobApi(keyword)

    # Получение вакансий с разных платформ
    hh_vacancies = hh.get_vacancies()
    sj_vacancies = sj.get_vacancies()

    # Получение вакансий в требуемом формате
    formatted_hh = hh.get_formatted_vacancies()
    formatted_sj = sj.get_formatted_vacancies()

    # Ввод выбора сайта для поиска вакансий
    get_api = ""
    choice_api = input("Выберите вакансии с сайта\n1 - Вакансии с HeadHunter\n2 - Вакансии с SuperJob\n3 - Вакансии с "
                       "HeadHunter и SuperJob\n")

    if choice_api == "1":
        get_api = formatted_hh
    elif choice_api == "2":
        get_api = formatted_sj
    elif choice_api == "3":
        get_api = formatted_hh + formatted_sj
    else:
        print("Не верный ввод")

    # Ввод пользователя города, в котором интересует вакансия
    user_keyword = input("Введите интересующий город (Пропустить - Enter)\n")
    if len(user_keyword) > 1:
        filtered_vac = filter_vacancies(get_api, user_keyword)
    else:
        filtered_vac = get_api

    # Сохранение информации о вакансиях в файл
    json_saver = JSONSaver(get_api)
    save_in_file = json_saver.create_file(filtered_vac)

    # Бесконечный цикл для работы с пользователем
    while True:

        command = input("Выберите критерии вакансий\n1 - Показать все вакансии\n2 - Показать вакансии сортированные по "
                        "ЗП\nexit - Завершение программы\n")

        if command.lower() == "exit":
            break
        elif command == "1":
            vacancies = json_saver.select_all()
        elif command == "2":
            top_n = int(input("Выберете количество интересующих вакансий\n"))
            vacancies = get_top_vacancies(sorted(json_saver.select_all(), reverse=True), top_n)
        else:
            print("Не верный ввод")
            break

        for vacancy in vacancies:
            print(vacancy)

if __name__ == "__main__":
    main()