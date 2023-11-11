
from django.contrib import admin
from django.urls import path,include

from .views import list,save,deleteTodo,updateTodo,get_csrf_token

urlpatterns = [
    path('list/',list,name='todolist'),
    path('save/',save,name='savetodo'),
    path('deleteTodo/',deleteTodo,name='deleteTodo'),
    path('updateTodo/',updateTodo,name='updateTodo'),
    path('get-csrf-token/',get_csrf_token),
]



