from django.db import models

class AdditionalInformation(models.Model):

    TYPE = {
        (0, "Inne"),
        (1, "Horror"),
        (2, "Komedia"),
        (3, "Sci-fi"),
        (4, "Drama"),

    }

    duration = models.PositiveSmallIntegerField(default=0)
    type = models.PositiveSmallIntegerField(default=0, choices=TYPE)


class Film(models.Model):
    title = models.CharField(max_length=64, blank=False, unique=True)
    year = models.PositiveSmallIntegerField(default=2000)
    description = models.TextField(default="")
    premiera = models.DateField(null=True, blank=True)
    imdb_rating = models.DecimalField(max_digits=4,decimal_places=2, null=True,blank=True)
    poster = models.ImageField(upload_to="posters", null=True, blank=True)
    additional = models.OneToOneField(AdditionalInformation, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.title_with_year()

    def title_with_year(self):
        return "{} ({})".format(self.title,self.year)

class Rating(models.Model):
    review = models.TextField(default="", blank=True)
    stars = models.PositiveSmallIntegerField(default=5)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)

class Actor(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    films = models.ManyToManyField(Film)