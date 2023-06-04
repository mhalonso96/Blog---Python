from django.db import models


class Page(models.Model):
    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'

    name = models.CharField(max_length= 255)
    slug = models.SlugField(
        unique= True,
        default= None,
        null= True,
        blank= True,
        max_length= 255,
    )
    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)