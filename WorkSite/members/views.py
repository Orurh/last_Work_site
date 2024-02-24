from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse

# Create your views here.

mmbrs = [
    {'id': 1, 'name': 'Денис Макаров', 'position': 'Начальник СПТ', 'reference': 'Справка-отзыв о Денисе',
     'is_public': True},
    {'id': 2, 'name': 'Максим Козинцев', 'position': 'Заместитель начальника СПТ/начальник 1й дежурной смены',
     'reference': 'Справка-отзыв о МаксимеСправка-отзыв о МаксимеСправка-отзыв о МаксимеСправка-отзыв о Максиме Справка-отзыв о Максиме Справка-отзыв о Максиме Справка-отзыв '
                  'о МаксимеСправка-отзыв о МаксимеСправка-отзыв о Максиме Справка-отзыв о Максиме Справка-отзыв о Максиме Справка-отзыв о Максиме Справка-отзыв о Максиме' , 'is_public': True},
    {'id': 3, 'name': 'Александр Метелев', 'position': 'Заместитель начальника СПТ/начальник 2й дежурной смены',
     'reference': 'Справка-отзыв о Александре', 'is_public': True},
    {'id': 4, 'name': 'Андрей Веркеев', 'position': 'Заместитель начальника СПТ/начальник 3й дежурной смены',
     'reference': 'Справка-отзыв о Андрее', 'is_public': True},
    {'id': 5, 'name': 'Артем Шеленко', 'position': 'Заместитель начальника СПТ/начальник 4й дежурной смены',
     'reference': 'Справка-отзыв о Артеме', 'is_public': True},
]

menu = [{'title': 'Служба пожаротушения', 'url_name': 'home'},
        {'title': 'Реагирование подразделений', 'url_name': 'fire_home'},
        {'title': 'Добавить статью', 'url_name': 'addpage'},
        {'title': 'Войти', 'url_name': 'login'},
        {'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
]

date = {'title': 'Главная страница',
        'menu': menu,
        'mmbrs': mmbrs,
        'pos_selected': 0,
        }

categors = [
    {'id': 1, 'name': 'Начальник СПТ'},
    {'id': 2, 'name': 'Начальники дежурных смен'},
    {'id': 3, 'name': 'Диспетчерский состав'},
    {'id': 4, 'name': 'Водительский состав'},
]

def index(request):
    return render(request, 'members/index.html', date)


def members(request, int_id):
    return render(request, 'members/index.html', date)

def categories(request, cat_id):
    date = {'title': 'Главная страница',
            'menu': menu,
            'mmbrs': mmbrs,
            'pos_selected': cat_id,
            }
    return render(request, 'members/index.html', date)

def about(request):
    return render(request, 'members/about.html', {'title2': 'О сайте', 'menu': menu})


def login(request):
    return HttpResponse(f'Авторизация')


def addpage(request):
    return HttpResponse(f'Добавить информацию')


def contact(request):
    return HttpResponse(f'Обратная связь')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена!</h1>')
