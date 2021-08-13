from . import views
from django.urls import path,include
from django.conf import settings

urlpatterns =[
    path('', views.index,name='landing'),
    path('index/',views.projects,name='index'),
    path('projects/',views.projects,name='projects'),
    path('resume/',views.resume,name='resume'),
    path('contact/',views.contact,name='contact'),
]