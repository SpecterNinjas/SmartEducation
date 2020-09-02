from django.urls import path
from main.views import contact,teachers,about
from .views import main

app_name = 'main'

urlpatterns = [
    path('', main, name='main'),
    path('teachers/flashcard/', teachers, name='teachers'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),

]
