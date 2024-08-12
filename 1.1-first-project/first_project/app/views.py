import time

from django.http import HttpResponse
from django.shortcuts import render, reverse
from os import listdir
from os.path import isfile, join


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = time.ctime()
    msg = f'''
        <p>Текущее время:</p>
        <p>{current_time}</p>
        <p><a href="/"> На главную</a></p>
        '''
    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    files = [f for f in listdir('.') if isfile(join('.', f))]
    msg = f'''
        <p>Содержимое рабочей директории:</p>
        <p>{files}</p>
        <p><a href="/"> На главную</a></p>
        '''
    #raise NotImplemented
    return HttpResponse(msg)
