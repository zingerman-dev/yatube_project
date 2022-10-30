from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template: str = 'posts/index.html'
    return render(request, template, context={'title': 'Это главная страница проекта Yatube'})

# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def group_posts(request, slug):
    return HttpResponse(f'Посты группы {slug}')

def group_list(request):
    template: str = 'posts/group_list.html'
    return render(request, template, context={'title': 'Здесь будет информация о группах проекта Yatube'})

