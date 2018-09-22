from django.db import models
from django.contrib.auth.models import User
from django.template import defaultfilters
from django.urls import reverse

from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
# Create your models here.

Categoria = (
    ('Asterisk', 'Asterisk'),
    ('Python', 'Python'),
    ('Docker', 'Docker'),
    ('GCD', 'Google Cloud'),
    ('AWS', 'AWS'),
    ('Cursos', 'Cursos'),
    ('Tutorial', 'Tutorial'),
    ('Linux', 'Linux'),
    ('Hackers', 'Hackers'),
    ('Django', 'Django'),
    ('All', 'All'),
)

StatusPubli = (
    ('Publicada', 'Publicada'),
    ('Incompleta', 'Incompleta'),
    ('No_Publicada', 'No_Publicada'),
)

class Comments(models.Model):
    autor = models.OneToOneField(User, on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(max_length=400)
    likes = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.autor.username


#class Category(models.Model):
#    nombre = models.CharField(max_length=40, choices=Categoria)

#    def __str__(self):
#        return self.nombre

class Articles(models.Model):

    titulo = models.CharField(max_length=80)
    autor = models.OneToOneField(User, on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    contenido = MarkdownxField()
    likes = models.PositiveIntegerField(default=0)
    vistas = models.PositiveIntegerField(default=0)
    comentarios = models.ForeignKey(Comments, on_delete=models.CASCADE, null=True, blank=True)
    categoria = models.CharField(max_length=20, choices=Categoria, default='Tutorial')
    status = models.CharField(max_length=20, choices=StatusPubli, default='No_Publicada')
  #  categoria = models.CharField(max_length=100, choices=Categoria)
    slug = models.SlugField(max_length=80)

    def __str__(self):
        return self.titulo

    # Create a property that returns the markdown instead
    @property
    def formatted_markdown(self):
        return markdownify(self.contenido)

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.titulo)
        super(Articles, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("articulos:ver_articles", kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-id']
