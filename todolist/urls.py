from django.urls import path
from todolist.views import show_todolist
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import add_task
from todolist.views import add_ajax
from todolist.views import show_ajax
from todolist.views import show_json


app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('addTask/', add_task, name='add_task'),
    path('show-json/', show_json, name='show_json'),
    path('json/', show_ajax, name='show_ajax'),
    path('add/', add_ajax, name='add_ajax'),
]