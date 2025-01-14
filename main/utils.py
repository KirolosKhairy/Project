import pandas as pd
import requests

def load_vacancies_csv(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None


def clean_vacancy(vacancy):
    if vacancy['salary'] is None:
        vacancy['salary'] = 'Нет данных'
    elif vacancy['salary']['from'] and vacancy['salary']['to'] and vacancy['salary']['from'] != vacancy['salary']['to']:
        vacancy['salary'] = f"от {'{0:,}'.format(vacancy['salary']['from']).replace(',', ' ')} до {'{0:,}'.format(vacancy['salary']['to']).replace(',', ' ')} {vacancy['salary']['currency']}"
    elif vacancy['salary']['from']:
        vacancy['salary'] = f"{'{0:,}'.format(vacancy['salary']['from']).replace(',', ' ')} {vacancy['salary']['currency']}"
    elif vacancy['salary']['to']:
        vacancy['salary'] = f"{'{0:,}'.format(vacancy['salary']['to']).replace(',', ' ')} {vacancy['salary']['currency']}"
    else:
        vacancy['salary'] = 'Нет данных'

    vacancy['key_skills'] = ', '.join(skill['name'] for skill in vacancy['key_skills'])
    vacancy['published_at'] = vacancy['published_at'].replace('T', ' ')
    return vacancy


def get_vacancies():
    try:
        params = {
            'text': 'python',
            'specialization': 1,
            'page': 1,
            'per_page': 10,
        }
        response = requests.get('https://api.hh.ru/vacancies', params=params).json()
        vacancies = []
        for item in response['items']:
            if 'python' in item['name'].lower():
                vacancy_data = requests.get(f"https://api.hh.ru/vacancies/{item['id']}").json()
                vacancies.append(clean_vacancy(vacancy_data))
        return vacancies
    except Exception as e:
        print(f"Error fetching vacancies: {e}")
        return []
