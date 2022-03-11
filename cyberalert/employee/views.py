from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def Employee_HomePage(request):
    return render(request, 'emp_home.html')

def AddTodoPage(request):
    try:
        if request.method== "POST":
            if "add" in request.POST:
                tf=TodoForm(request.POST)
                if (tf.is_valid()):
                    tf.save()
                    return redirect('addtodo')
                else:
                    return render(request, 'add_todo.html',{'error': tf.errors})
        todolist= Todo.objects.filter(emp_email=session['email'])
    except:
        return render(request, 'add_todo.html')
    return render(request, 'add_todo.html')

def ViewTodoPage(request):
    return render(request, 'view_todo.html')