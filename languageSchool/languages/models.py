from django.db import models

class Language(models.Model):

    language_name = models.CharField(max_length=250)
    language_family = models.CharField(max_length=250)
    region_origin = models.CharField(max_length=250)
    sentences = models.TextField()
    words = models.TextField()

    def __str__(self) -> str:
        return self.language_name

        