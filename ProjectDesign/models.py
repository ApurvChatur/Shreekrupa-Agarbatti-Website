from django.shortcuts import reverse
from django.db import models
from django.utils.text import slugify
from ckeditor import fields

TAG_CHOICES = [
    ('Featured', 'Featured'),
    ('Recent', 'Recent'),
]
CATEGORY_CHOICES = [
    ('Agarbatti', 'Agarbatti'),
    ('Dhoopbatti', 'Dhoopbatti'),
    ('Perfume', 'Perfume'),
]


class Home(models.Model):
    title = models.CharField(max_length=255, unique=True, default='Shreekrupa Agarbatti')
    subtitle = models.CharField(max_length=255, default='Best Place for Fragrance Agarbatti!')
    image = models.ImageField(upload_to='Home/', default='default.jpg')
    description = fields.RichTextField()
    slug = models.SlugField(unique=True, blank=True)

    # Some Common Methods
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug

    def get_class_name(self):
        return self.__class__.__name__

    # ProjectDesign
    def get_object_list_url(self):
        return reverse('ProjectDesign:home-list-page')

    def get_object_create_url(self):
        return reverse('ProjectDesign:home-create-page')

    def get_object_retrieve_url(self):
        return reverse('ProjectDesign:home-retrieve-page',
                       kwargs={
                           'slug': self.slug
                       })

    def get_object_update_url(self):
        return reverse('ProjectDesign:home-update-page',
                       kwargs={
                           'slug': self.slug
                       })

    def get_object_delete_url(self):
        return reverse('ProjectDesign:home-delete-page',
                       kwargs={
                           'slug': self.slug
                       })


class Category(models.Model):
    title = models.CharField(max_length=20, unique=True, default='Agarbatti')
    subtitle = models.CharField(max_length=50, default='Check our agarbattis')
    slug = models.SlugField(unique=True, blank=True)

    # Some Common Methods
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug

    def get_class_name(self):
        return self.__class__.__name__

    # Project Model
    def get_category_url(self):
        return reverse('ProjectModel:category-page',
                       kwargs={
                           'slug': self.slug
                       })


class Product(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=255)
    actual_price = models.DecimalField(decimal_places=2, max_digits=5)
    discount_price = models.DecimalField(decimal_places=2, max_digits=5, blank=True, null=True)
    description = fields.RichTextField()
    #
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    tag = models.CharField(choices=(
                                ('featured', 'featured'),
                                ('recent', 'recent'),
                            ), max_length=20, default='featured')
    #
    related_home = models.ForeignKey(Home, on_delete=models.CASCADE, default=f'shreekrupa-agarbatti')
    slug = models.SlugField(unique=True, blank=True)

    # Some Common Methods
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug

    def get_class_name(self):
        return self.__class__.__name__

    def get_final_price(self):
        if self.discount_price:
            final_price = self.actual_price - self.discount_price
            return final_price
        else:
            final_price = self.actual_price
            return final_price

    # ProjectDesign
    def get_object_list_url(self):
        return reverse('ProjectDesign:product-list-page')

    def get_object_create_url(self):
        return reverse('ProjectDesign:product-create-page')

    def get_object_retrieve_url(self):
        return reverse('ProjectDesign:product-retrieve-page',
                       kwargs={
                           'slug': self.slug
                       })

    def get_object_update_url(self):
        return reverse('ProjectDesign:product-update-page',
                       kwargs={
                           'slug': self.slug
                       })

    def get_object_delete_url(self):
        return reverse('ProjectDesign:product-delete-page',
                       kwargs={
                           'slug': self.slug
                       })

    # Product Model
    def get_home_url(self):
        return reverse('ProjectModel:home-page')

    def get_products_url(self):
        return reverse('ProjectModel:products-page')

    def get_product_url(self):
        return reverse('ProjectModel:product-page',
                       kwargs={
                           'slug': self.slug
                       })


class ProductImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='ProductImage/')
    related_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True)

    # Some Common Methods
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug

    def get_class_name(self):
        return self.__class__.__name__

    # ProjectDesign
    def get_object_list_url(self):
        return reverse('ProjectDesign:product-image-list-page')

    def get_object_create_url(self):
        return reverse('ProjectDesign:product-image-create-page')

    def get_object_retrieve_url(self):
        return reverse('ProjectDesign:product-image-retrieve-page',
                       kwargs={
                           'slug': self.slug
                       })

    def get_object_update_url(self):
        return reverse('ProjectDesign:product-image-update-page',
                       kwargs={
                           'slug': self.slug
                       })

    def get_object_delete_url(self):
        return reverse('ProjectDesign:product-image-delete-page',
                       kwargs={
                           'slug': self.slug
                       })

