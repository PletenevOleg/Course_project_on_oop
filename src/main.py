from classes.vacancies_api import HeadHunterApi, SuperJobApi

def main():
    """"Взаимодействие с пользователем"""
    keyword = input('Введите слово для поиска вакансии: \n')
    hh = HeadHunterApi()
    sj = SuperJobApi()

    vacancies = []
    for api in (hh, sj):
        api.get_vacancies()
        vacancies.extend(api.get_formatted_vacancies())

if __name__ == "__main__":
    main()