from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from fires.models import Fire

menu = [{'title': 'Служба пожаротушения', 'url_name': 'home'},
        {'title': 'Реагирование подразделений', 'url_name': 'fire_home'},
        {'title': 'Добавить статью', 'url_name': 'addpage'},
        {'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        ]


def index(request):
    chapters = ['Пожары', 'ДТП']
    date = {'title': 'Главная страница',
            'menu': menu,
            'chapters': chapters,
            }
    return render(request, 'fires/reactions.html', date)

class FireHome(ListView):  # вместо функции index
#
    model = Fire # для работы ListView необходимо передать модель, но она будет показывать все открытые и закрытые данные
    template_name = 'fires/fire.html'
#     title_page = 'Главная страница'

