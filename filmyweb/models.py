from django.db import models


class Film(models.Model):
    title = models.CharField(max_length=64, blank=False, unique=True)
    year = models.PositiveSmallIntegerField(default=2000)
    description = models.TextField(default="")
    premiera = models.DateField()


    def __str__(self):
        return self.title + ' (' + str(self.year) + ')'