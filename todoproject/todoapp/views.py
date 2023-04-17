from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods

from .forms import TaskForm
from .models import ToDo


# Create your views here.
# from django.shortcuts import render
# from .models import TodoListItem
#
#
#
#
# def todoappView(request):
#     all_todo_items = TodoListItem.objects.all()
#     return render(request, 'todolist.html',
#     {'all_items':all_todo_items})
#
#
# def addTodoView(request):
#     x = request.POST['content']
#     new_item = TodoListItem(content = x)
#     new_item.save()
#     return HttpResponseRedirect('/todoapp/')
#
# def deleteTodoView(request, i):
#     y = TodoListItem.objects.get(id= i)
#     y.delete()
#     return HttpResponseRedirect('/todoapp/')
#
#
# class TodoForm:
#     pass
#
#
# def edit_task(request, task_id):
#     task = get_object_or_404(TodoListItem, id=task_id)
#     form = TodoForm(request.POST or None, instance=task)
#     if form.is_valid():
#         form.save()
#         return redirect('task_list')
#     context = {'form': form}
#     return render(request, 'edit_task.html', context)




#--------------
def index(request):
    todos = ToDo.objects.all()
    return render(request,'todoapp/index.html', {'todo_list':todos, 'title':'Главная страница'})



@require_http_methods(['POST'])
def add(request):
    title =request.POST['title']
    description = request.POST['description']
    todo = ToDo(title =title, description=description)
    todo.save()
    return redirect('index')


def update(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()
    if request.method == 'POST':
        todo.title = request.POST['title']
        todo.description = request.POST['description']
        todo.save()
    return redirect('index')

def delete(request, todo_id):
    todo=ToDo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')


@require_http_methods(['POST'])
def updateTask(request, todo_id):
	task = ToDo.objects.get(id=todo_id)

	form = TaskForm(instance=task)

	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('todoapp/update.html')

	context = {'form':form}

	return render(request, 'todoapp/index.html', context)