from django.contrib import admin
from .models import Film

# admin.site.register(Film)

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    #fields = ["title",'description','year']  # uzywamy tylko tego co jest w []
    #exclude = ['year'] # uzywamy wszystkiego oprocz roku
    list_display = ["title","imdb_rating"] # co ma wyswietlac w panelu admina
    list_filter = ["title"]
