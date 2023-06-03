from typing import Iterable, Optional

from django.db import models
from utils.images import resize_image
from utils.model_validators import validade_png


class SiteSetup(models.Model):
    class Meta:
        verbose_name = 'Setup'
        verbose_name_plural = 'Setup'

    title = models.CharField(max_length= 65)
    description = models.CharField (max_length= 255)

    show_header = models.BooleanField (default= True)
    show_search = models.BooleanField(default= True)
    show_menu = models.BooleanField(default= True)
    show_description = models.BooleanField(default= True)
    show_pagination = models.BooleanField(default= True)
    show_footer = models.BooleanField(default= True)
    favicon = models.ImageField(
        upload_to= 'assents/favicon/%Y/%m/',
        blank= True, default= '',
        validators= [
            validade_png,
        ]
    )

    def save(self, *args, **kwargs):
        
        current_favicon_name = str(self.favicon.name) # antes de salvar
        super().save(*args, **kwargs)
        favicon_changed = False
        if self.favicon:
            favicon_changed = current_favicon_name != self.favicon.name
            
        if favicon_changed:
            resize_image(self.favicon, 32)

    def __str__(self):
        return self.title