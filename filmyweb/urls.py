from django.urls import path
from filmyweb.views import all_films

urlpatterns = [
    path('all/', all_films),
]
