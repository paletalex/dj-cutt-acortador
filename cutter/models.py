from django.db import models
from .utils import generate_unique_key
from django.core.exceptions import ValidationError

def validate_dot_com(value):
    if not "com" in value:
        raise ValidationError("El enlace debe tener .com")
    return value

# Create your models here.
class Link(models.Model):
    url = models.CharField('Enlace', max_length=200, validators=[validate_dot_com])
    key = models.CharField('Clave', max_length=20, unique=True, blank=True)
    created = models.DateTimeField('Fecha de creacion', auto_now=True, auto_now_add=False)
    updated = models.DateTimeField('Fecha de modificacion', auto_now=False, auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.key is None or self.key == "":
            self.key = generate_unique_key(self)
        if not "http" in self.url:
            self.url = "http://" + self.url
        super(Link, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Enlace'
        verbose_name_plural = 'Enlaces'
        ordering =['-created']

    def __str__(self):
        return self.url