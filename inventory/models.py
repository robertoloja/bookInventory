from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)

    def __str__(self):
        return '%s, by %s' % (self.title, self.author)
