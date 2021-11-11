from django.shortcuts import render, get_object_or_404, redirect
from .models import Film
from .forms import FilmForm
from django.contrib.auth.decorators import login_required


def all_films(request):
    all = Film.objects.all()
    return render(request,'filmy.html',{ 'films': all })

@login_required
def new_films(request):
    form = FilmForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(all_films)

    return render(request, 'film_form.html', {'form': form, 'new':True})

@login_required
def edit_film(request, id):
    film = get_object_or_404(Film, pk=id)
    form = FilmForm(request.POST or None, request.FILES or None, instance=film)

    if form.is_valid():
        form.save()
        return redirect(all_films)

    return render(request, 'film_form.html', {'form': form, 'new':False})

@login_required
def delete_film(request, id):
    film = get_object_or_404(Film, pk=id)

    if request.method == 'POST':
        film.delete()
        return redirect(all_films)

    return render(request, 'confirm.html', {'film': film})


