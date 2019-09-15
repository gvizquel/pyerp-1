# Librerias Django
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from .father import PyFather
from ..models import PyVariant


class PyAttribute(PyFather):
    name = models.CharField(_("Name"), max_length=255)
    variant_id = models.ForeignKey(PyVariant, null=True, blank=True, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('base:attribute-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
