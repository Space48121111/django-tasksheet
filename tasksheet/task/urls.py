from django.urls import path
from . import views

app_name = 'task'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:room_id>/', views.detail, name='detail'),
    path('<int:room_id>/status/', views.status, name='status'),
]
