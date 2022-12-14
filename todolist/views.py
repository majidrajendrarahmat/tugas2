from django.shortcuts import render
from todolist.forms import TaskAdderForm
from todolist.models import Task
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    task_data = Task.objects.filter(user=request.user)
    context = {
    'task_list': task_data,
    'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register_todolist.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login_todolist.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def add_task(request):
    form = TaskAdderForm()

    if request.method == "POST":
        form = TaskAdderForm(request.POST)
        if form.is_valid():
            todolist_data = Task(
                user = request.user,
                date = datetime.datetime.now(),
                title = form.cleaned_data["task_title"],
                description = form.cleaned_data["task_description"],
            )
            todolist_data.save()
            return redirect('todolist:show_todolist')
    
    context = {'form':form}
    return render(request, 'add_task_todolist.html', context)

def add_ajax(request):
    if request.method == 'POST':
        title = request.POST.get("judul")
        deskripsi = request.POST.get("deskripsi")

        new_todolist = Task(title=title, description=deskripsi, user=request.user)
        new_todolist.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def show_ajax(request):
    return render(request, "todolist_ajax.html")

def show_json(request):
    data_todolist = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data_todolist))
