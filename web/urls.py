from django.contrib import admin
from django.urls import path
from . import views
from .views import MyModelListCreate,MyModelRetrieveUpdateDestroy,MyModel2ListCreate,MyModel2RetrieveUpdateDestroy

urlpatterns = [
    path('', views.index, name='name'),
    path('index/',views.index,name='index'),   
    path('contact/',views.contact,name='contact'),
    path('destination/',views.destination,name='destination'),
    path('trips/',views.trips,name='single'),
    path("trips/<slug:slugvalue>/",views.getdata,name='getdata'),
    path('article/',views.article,name='article'),
    path('datainsert/',MyModelListCreate.as_view()),
    path('dataupdate/<int:pk>/', MyModelRetrieveUpdateDestroy.as_view()),
    path('sluginsert/',MyModel2ListCreate.as_view()),
    path('slugupdate/<int:pk>/', MyModel2RetrieveUpdateDestroy.as_view()),

    path("blogs/",views.blogs,name='blogs'),
    path("blogs/<slug:slugvalue>/",views.getdata,name='getdata'),
    
    path('<str:continent_name>/',views.continent_list,name='continent_list'),
   

]
