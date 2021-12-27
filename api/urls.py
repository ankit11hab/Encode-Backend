from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('member-list/', views.memberList, name='member-list'),
    path('member-create/', views.memberCreate, name='member-create'),
    path('notes/', views.getNotes, name='notes'),
]
