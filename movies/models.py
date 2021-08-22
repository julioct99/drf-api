from django.db import models


class Actor(models.Model):
    """
    Represents an actor that participates in movies
    """

    dob = models.DateField()
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Director(models.Model):
    """
    Represents a movie director
    """

    dob = models.DateField()
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Movie(models.Model):
    """
    Represents a movie
    """

    year = models.IntegerField()
    title = models.CharField(max_length=50)
    description = models.TextField()
    available = models.BooleanField()

    # director = models.ForeignKey(
    #     Director, on_delete=models.CASCADE, related_name="movies"
    # )
    # actors = models.ManyToManyField(Actor, related_name="movies")

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"{self.title} ({self.year})"
