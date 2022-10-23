from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')

# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def group_posts(request, pk):
    return HttpResponse(f'Посты группы {pk}')

