
from django.db import models
from django.utils.translation import gettext_lazy as _


def product_image_dir(instance, filename):
    return 'product/{0}/{1}'.format(instance.name, filename)

class Category(models.Model):
    name = models.CharField(_('Name'), max_length=255)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    name = models.CharField(_('Name'),max_length=255)
    description = models.TextField(_('Description'),blank=True, null=True)
    price = models.DecimalField(_('Price'), max_digits=8, decimal_places=2)
    discount_price = models.DecimalField(_('Discount Price'), max_digits=8, decimal_places=2, null=True, blank=True)
    image = models.ImageField(_('Profile Image'), null=True, blank=True, upload_to=product_image_dir)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Product'

    def __str__(self):
        return self.name
