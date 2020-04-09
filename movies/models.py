from django.db import models


class Category(models.Model):
    """Категории"""
    name = models.CharField("Категории",  max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категории"
