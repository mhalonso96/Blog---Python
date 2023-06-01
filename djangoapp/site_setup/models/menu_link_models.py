from django.db import models

from .site_setup_models import SiteSetup


class MenuLink(models.Model):
    class Meta:
        verbose_name = 'Menu link'
        verbose_name_plural = 'Menu links'

    text = models.CharField(max_length=50)
    url_or_path = models.CharField(max_length=2048)
    new_tab = models.BooleanField(default=False)
    site_setup = models.ForeignKey(
        SiteSetup,
        on_delete= models.CASCADE,
        blank= True,
        null= True,
        default= None,
    )

    def __str__(self):
        return self.text