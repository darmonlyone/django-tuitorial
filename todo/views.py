from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from todo.models import Todo


def index(request):
    return HttpResponse("Welcome to front page.")


def list(request):
    todos = Todo.objects.all()

    contexts = {"todo_list": todos}

    return render(request, 'todo/list.html', context=contexts)


def add(request):
    if request.method == "POST":
        named = request.POST.get('todo_name', '')
        bool = False

        todo = Todo(name=named, is_done=bool)
        todo.save()
        return HttpResponseRedirect(reverse('list_todo'))


def add_menu(request):
    return render(request, 'todo/add.html')


def detail(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    contexted = {'todo_detail': todo}
    return render(request, 'todo/detail.html', context=contexted)


def set_done(request, todo_id):
    if request.method == "POST":
        todo = Todo.objects.get(pk=todo_id)
        todo.is_done = True
        todo.save()
        return HttpResponseRedirect(reverse('list_todo'))
