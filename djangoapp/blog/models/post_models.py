from blog.models.category_models import Category
from blog.models.tag_models import Tag
from django.db import models


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
        max_length= 255
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
        default= ''
    )
    cover_in_post_content = models.BooleanField(
        default= True,
        help_text= 'Exibir a imagem de capa tambem dentro do conteudo do post?'
    )
    create_at = models.DateTimeField(
        auto_now_add= True
    )
    update_at = models.DateTimeField(
        auto_now= True
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
        default= ''
    )
    def __str__(self):
        return self.title