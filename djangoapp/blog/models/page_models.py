from django.db import models
from django.urls import reverse
from utils.rands import new_slugify


class Page(models.Model):
    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'

    title = models.CharField(max_length= 65,)
    slug = models.SlugField(
        unique= True,
        default= '',
        null = False,
        blank= True,
        max_length= 255
    )
    is_published = models.BooleanField(
        default= False,
        help_text= (
            'Este campo precisará estar marcado '
            'para a página ser exibida publicamente'        
        ),
    )
    content = models.TextField()

    def get_absolute_url(self):
        if not self.is_published:
            return reverse('blog:index')
        return reverse('blog:page', args=(self.slug,))
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = new_slugify(self.title, 5)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
