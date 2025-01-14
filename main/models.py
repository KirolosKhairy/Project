import datetime

from django.db import models


# Create your models here

class Home(models.Model):
    title = models.CharField('Заголовок', max_length=100, default='homepage')
    text_1 = models.TextField('Текст 1', default=None)
    text_2 = models.TextField('Текст 2', default=None)
    image_1 = models.ImageField(
        'img 1', default=None,
        upload_to='home'
    )
    image_2 = models.ImageField(
        'img 2', default=None,
        upload_to='home'
    )


class Demand(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=100,
        default='demand'
    )
    text = models.TextField('Текст', default=None)
    graph_left = models.ImageField(
        'График №2',
        default=None,
        upload_to='demand'
    )
    graph_right = models.ImageField(
        'График №1',
        default=None,
        upload_to='demand'
    )


class Geography(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=100,
        default='geography'
    )
    text = models.TextField('Текст', default=None)
    table = models.TextField('Таблица', default=None)
    graph = models.ImageField(
        'График',
        default=None,
        upload_to='geography'
    )

class Skills(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=100,
        default='skills'
    )
    text = models.TextField('Текст', default=None)
    graph = models.ImageField(
        'График',
        default=None,
        upload_to='skills'
    )

class Statistics(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=100,
        default='Общая статистика'
    )
    salary_trend_graph = models.ImageField(
        'График динамики уровня зарплат',
        upload_to='statistics',
        default=None
    )
    vacancy_trend_graph = models.ImageField(
        'График динамики количества вакансий',
        upload_to='statistics',
        default=None
    )
    salary_city_table = models.TextField(
        'Таблица уровня зарплат по городам',
        default=None
    )
    vacancy_share_city_table = models.TextField(
        'Таблица доли вакансий по городам',
        default=None
    )
    top_skills_table = models.TextField(
        'ТОП-20 навыков по годам',
        default=None
    )
