from django.forms import ModelForm
from .models import Film, AdditionalInformation

class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['title','description','year','premiera','imdb_rating','poster']

class AdditionalInfoForm(ModelForm):
    class Meta:
        model = AdditionalInformation
        fields = ['duration', 'type']