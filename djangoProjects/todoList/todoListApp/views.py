from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItems

# Create your views here.
def todoHome(request):
    # dict_text = {'list_a':'temporary todo item A',
    #             'list_b':'temporary todo item B'
    #     }
    all_items = TodoItems.objects.all()
    return render(request, 'todoListApp/index.html',{'all_items':all_items})

def addTodo(request):
    # Create a new todo_items
    new_item = TodoItems(content = request.POST['content'])
    new_item.save()
    #Redirect the browser to addTodo
    return HttpResponseRedirect('/todo/')

def deleteTodo(request, todo_id):
    item_to_delete = TodoItems.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')
