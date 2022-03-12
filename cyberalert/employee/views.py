from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def Employee_HomePage(request):
    return render(request, 'emp_home.html')

def AddTodoPage(request):
    try:
        if request.method== "POST":
            mutable = request.POST._mutable
            request.POST._mutable = True
            request.POST['emp_email']=request.session['email']
            request.POST._mutable = mutable
            tf=TodoForm(request.POST)
            if (tf.is_valid()):
                tf.save()
                return redirect('addtodo')
            else:
                return render(request, 'add_todo.html',{'error': tf.errors})
    except Exception as e:
        return render(request, 'add_todo.html',{'error': e})
    try:
        todolist= Todo.objects.filter(emp_email=request.session['email'])
        return render(request, 'add_todo.html',{'todolist':todolist})
    except Exception as e:
        return render(request, 'add_todo.html', {'error': e})

def ChangeStatus(request,id):
    try:
        print(id)
        print(request.POST['id'])
        td=Todo.objects.get(id=id)
        td.is_complete=not td.is_complete
        td.save()
        return redirect('addtodo')
    except Exception as e:
        return redirect('addtodo')


def ViewTodoPage(request):
    return render(request, 'view_todo.html')