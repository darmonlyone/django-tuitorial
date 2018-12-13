from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list, name='list_todo'),
    path('add_menu/', views.add_menu, name='add_menu'),
    path('add/', views.add, name='add_todo'),
    path('<int:todo_id>/', views.detail, name='detail'),
    path('set_done/<int:todo_id>', views.set_done, name="set_done"),
]
