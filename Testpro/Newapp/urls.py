from django.urls import path
from .views import NewsP, Home, Contact, NewsDate, register, addUSer, modelform, addModelForm





urlpatterns = [
	path('', Home, name='home'),
    path('news/', NewsP, name='news'),
    path('contact/', Contact, name='contact'),
    path('newsdate/<int:year>', NewsDate, name='newsdate'),
    path('sigup/', register, name='register'),
    path('addUser/', addUSer, name='addUser'),
    path('modelform/', modelform, name='form'),
    path('addmodelform/', addModelForm, name='modelform'),
]