from django.shortcuts import render

# Create your views here.
from .models import course, teacher, faculty

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    #Генерация "количеств" некоторых главных объектов
    num_course=course.objects.all().count()
    num_teacher=teacher.objects.count()
    num_faculty=faculty.objects.count() #Метод 'all()" применен по умолчанию.

    #Отрисовка HTML-шаблона index.html с данными внутри
    #Переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_course':num_course,'num_teacher':num_teacher, 'num_faculty':num_faculty},
    )
from django.views import generic

class courseListView(generic.ListView):
    model = course
class courseDetailView(generic.DetailView):
    model = course
class teacherListView(generic.ListView):
    model = teacher
class teacherDetailView(generic.DetailView):
    model = teacher
