from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils.text import slugify
from apps.base.models import TimeStampedModel


class Brand(TimeStampedModel):
    name = models.CharField(_('name'), max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('brand')
        verbose_name_plural = _('brands')


class Product(TimeStampedModel):
    is_active = models.BooleanField(_('active'), default=True)
    brand = models.ForeignKey(Brand, related_name='products', on_delete=models.SET_NULL, null=True)
    sku = models.CharField(_('sku'), max_length=10, unique=True)
    name = models.CharField(_('name'), max_length=200)
    price = models.DecimalField(_('price'), decimal_places=2, max_digits=12)
    times_visited = models.PositiveIntegerField(_('times visited'), default=0)
    slug = models.SlugField(_('slug'), max_length=150, unique=True)

    def __str__(self):
        return f'{self.name} | {self.sku}'

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
