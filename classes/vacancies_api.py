import os
import requests

from abc import ABC, abstractmethod

class VacanciesApi(ABC):
    """Абстрактный класс"""
    @abstractmethod
    def get_vacancies(self, keyword: str):
        pass

    @abstractmethod
    def get_formatted_vacancies(self):
        pass


class HeadHunterApi(VacanciesApi):
    """Класс для работы с апи hh.ru"""
    def __init__(self, keyword: str):
        self.keyword = keyword
        self.vacancies = []

    def get_formatted_vacancies(self):
        """Формирует список исходя из нужных пунктов в вакансии"""
        formatted_vacancies = []
        for vacancy in self.vacancies:
            if vacancy['salary'] is None:
                continue
            if vacancy['salary']['from'] is None:
                continue
            else:
                formatted_vacancies.append({
                    'salary_from': vacancy['salary']['from'],
                    'salary_to': vacancy['salary']['to'],
                    'salary_currency': vacancy['salary']['currency'],
                    'title': vacancy['name'],
                    'area': vacancy['area']['name'],
                    'responsibility': vacancy['snippet']['responsibility'],
                    'url': vacancy['url']
                })
        return formatted_vacancies

    def get_vacancies(self):
        """Позволяет получить список вакансий по запросу"""

        params = {
            "text": self.keyword,
            "page": 1,
            "per_page": 100
        }

        data = requests.get(f'https://api.hh.ru/vacancies', params).json()
        for element in data['items']:
            self.vacancies.append(element)
        return self.vacancies

class SuperJobApi(VacanciesApi):
    """Класс для работы с апи superjob.ru"""
    def __init__(self, keyword: str):
        self.keyword = keyword
        self.vacancies = []

    def get_formatted_vacancies(self):
        formatted_vacancies = []
        for vacancy in self.vacancies:
            if vacancy['currency'] is None:
                continue
            if vacancy['payment_from'] is None:
                continue
            else:
                formatted_vacancies.append({
                    'salary_from': vacancy['payment_from'],
                    'salary_to': vacancy['payment_to'],
                    'salary_currency': vacancy['currency'],
                    'title': vacancy['profession'],
                    'area': vacancy['town']['title'],
                    'responsibility': vacancy['candidat'],
                    'url': vacancy['link']
                })
        return formatted_vacancies
    def get_vacancies(self):
        """Позволяет получить список вакансий по запросу"""
        sj_api_url = 'https://api.superjob.ru/2.0/vacancies/'
        sj_api_key = os.getenv('SJ_API_KEY')
        headers = {
            'X-Api-App-Id': sj_api_key,
        }

        params = {
            "keyword": self.keyword,
            "page": 1,
            "count": 100
        }

        data = requests.get(sj_api_url, headers=headers, params=params).json()
        for element in data['objects']:
            self.vacancies.append(element)
        return self.vacancies