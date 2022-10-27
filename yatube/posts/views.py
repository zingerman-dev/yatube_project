from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template: str = 'posts/index.html'
    return render(request, template)

# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def group_posts(request, slug):
    return HttpResponse(f'Посты группы {slug}')

