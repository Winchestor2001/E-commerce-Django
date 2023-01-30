from django.db import models
from django.urls import reverse


class Category(models.Model):
    slug = models.SlugField(unique=True)
    category_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    

    def get_url(self):
        return reverse('product_by_category', args=[self.slug])

    def __str__(self) -> str:
        return self.category_name
