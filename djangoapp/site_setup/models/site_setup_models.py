from django.db import models


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

    def __str__(self):
        return self.title