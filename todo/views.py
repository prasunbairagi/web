from django.shortcuts import render,redirect,get_object_or_404
from todo.models import Todo # from models.py
from todo.forms import TodoForm # from forms.py
from todo.forms import TodoContact
from todo.models import Contact
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'home.html')
@login_required
def contact(request):
    contactform=TodoContact(request.POST or None) #Data input from user 
    if contactform.is_valid():
        contactform.save()
        return redirect('home') 
        # redirect routes to the next page
        # render connects backend to front end vicea versa
    return render(request,'contact.html',{'form':contactform})
    
@login_required
def about(request):
    return render(request,'about.html')
@login_required
def todoadd(request):
    todoform=TodoForm(request.POST or None) #Data input from user 
    if todoform.is_valid():
        todoform.save()
        return redirect('todolist') 
        # redirect routes to the next page
        # render connects backend to front end vicea versa
    return render(request,'todoadd.html',{'form':todoform})
    # form key entry leta hai user se
@login_required   
def todolist(request):
    allfeedback=Todo.objects.all() #Fetching the data from database db.sqlite(file)
    return render(request,'todolist.html',{'todos':allfeedback})
    #todos key entry ko show karega front end me all feedback wale page me

@login_required
def todoedit(request,pk):
    todo=get_object_or_404(Todo,pk=pk)
   # instance todo due to this data is alredy inserted in entry boxes todoadd.html
    todoform=TodoForm(request.POST or None,instance=todo)

    if todoform.is_valid():
        todoform.save()
        return redirect('todolist')
    return render(request,'todoadd.html',{'form':todoform})#todoadd page will get open
@login_required
def tododelete(request,pk):
    todo=get_object_or_404(Todo,pk=pk)
    
    if request.method=='POST':
        todo.delete()
        return redirect('todolist')
    return render(request,'tododelete.html',{'todo':todo})
