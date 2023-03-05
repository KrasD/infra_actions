import requests

from django.http import HttpResponse


def index(requests):
    return HttpResponse('У меня получилось!')


def second_page(requests):
    return HttpResponse('А это вторая страница')
