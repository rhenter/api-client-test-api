from django.db import models
from django.utils.translation import gettext_lazy as _


class Book(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    description = models.TextField(verbose_name=_('Description'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is Active'))

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')
        ordering = ['name']
