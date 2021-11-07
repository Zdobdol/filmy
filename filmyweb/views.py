from django.shortcuts import render
from django.http import HttpResponse
from .models import Film


def all_films(request):
    all = Film.objects.all()
    return render(request,'filmy.html',{ 'films': all })