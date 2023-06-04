from blog.models.category_models import Category
from blog.models.tag_models import Tag
from django.contrib.auth.models import User
from django.db import models
from utils.rands import new_slugify


class Post(models.Model):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    title = models.CharField(max_length= 65)
    slug = models.SlugField(
        unique= True,
        default= "",
        null= False,
        blank= True,
        max_length= 255,
    )
    excerpt = models.CharField(max_length= 150)
    is_published = models.BooleanField(
        default= False,
        help_text= (
            'Este campo precisará estar marcado '
            'para o post ser exibido publicamente'        
        ),
    )
    content = models.TextField()
    cover = models.ImageField(
        upload_to= 'post/%Y/%m/',
        blank= True,
        default= '',
    )
    cover_in_post_content = models.BooleanField(
        default= True,
        help_text= 'Exibir a imagem de capa tambem dentro do conteudo do post?',
    )
    created_at = models.DateTimeField(
        auto_now_add= True,
    )
    created_by = models.ForeignKey(
        User,
        on_delete= models.SET_NULL,
        blank= True,
        null= True,
        related_name= 'post_created_by',

    )
    updated_at = models.DateTimeField(
        auto_now= True,
    )
    updated_by = models.ForeignKey(
        User,
        on_delete= models.SET_NULL,
        blank= True,
        null= True,
        related_name= 'post_updated_by',

    )
    category = models.ForeignKey(
        Category,
        on_delete= models.SET_NULL,
        null= True,
        default= None,
    )
    tags = models.ManyToManyField(
        Tag,
        blank= True,
        default= '',
    )
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = new_slugify(self.title, 5)
        return super().save(*args, **kwargs)