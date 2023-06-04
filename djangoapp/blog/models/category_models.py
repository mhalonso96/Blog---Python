from django.db import models
from utils.rands import new_slugify


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length= 255)
    slug = models.SlugField(
        unique= True,
        default= None,
        null= True,
        blank= True,
        max_length= 255,
    )
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = new_slugify(self.name, 5)
        return super().save(*args, **kwargs)