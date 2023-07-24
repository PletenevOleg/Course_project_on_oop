class Vacancy:

    def __init__(self, salary_from: int, salary_to: int, salary_currency: str, title: str, area: str, responsibility: str, url: str):
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.salary_currency = salary_currency
        self.title = title
        self.area = area
        self.responsibility = responsibility
        self.url = url

    def __gt__(self, other):
        return self.salary_from > other.salary_from

    def __str__(self):
        return f"""
Название вакансии: {self.title}
Город: {self.area}
Зарплата от: {self.salary_from} {self.salary_currency} до: {self.salary_to} {self.salary_currency}
Требования: {self.responsibility}
Ссылка на вакансию: {self.url}
"""