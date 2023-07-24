import json

from classes.vacancies_api import HeadHunterApi, SuperJobApi
from classes.vacancy import Vacancy

class JSONSaver:

    def __init__(self, vacancies):
        self.create_file(vacancies)
        self.vacancy_data = []

    def create_file(self, vacancies):
        """Записывает вакансии в файл"""
        with open("../classes/vacancies.json", "w", encoding="utf-8") as file:
            json.dump(vacancies, file, indent=2, ensure_ascii=False)

    def select_all(self):
        """Достаёт вакансии из файла и создает экземпляры класса Vacancy"""
        with open("../classes/vacancies.json", 'r', encoding="utf-8") as file:
            data = json.load(file)
            for vacancy in data:
                self.vacancy_data.append(Vacancy(**vacancy))
            return self.vacancy_data
    #
    # def sorted_by(self):
    #     """Сортировка вакансий"""
    #     vacancy_data = self.select_all()
    #     s_vacancies = sorted(vacancy_data)
    #     return s_vacancies

sj = SuperJobApi('python')
sj.get_vacancies()
op = sj.get_formatted_vacancies()
jopa = JSONSaver(op)
hui = jopa.select_all()
for i in hui:
    print(i)
