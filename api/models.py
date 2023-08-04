from django.db import models

# Create your models here.


class Tag(models.Model):
    tag = models.CharField(max_length=100, unique=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self) -> str:
        return self.tag


class Note(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    note = models.TextField()
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self) -> str:
        return self.title
