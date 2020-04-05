from django.shortcuts import render
from django.http import HttpResponse
from .models import BD


def task(request):
    tasks = BD.objects.order_by('-date_posted')
    context = {'tasks': tasks}
    return render(request, 'generator_task/task.html', context)


def home(request):
    return HttpResponse("Home page")
