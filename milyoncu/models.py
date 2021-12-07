from django.db import models
from django.conf  import settings
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=5555)
    description = models.TextField(max_length=5555)
    price = models.FloatField ()
    size = models.CharField(max_length=5555)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    logo = models.ImageField(upload_to="static/images", blank=True)

    def save(self):
        if not self.id:
            self.slug = slugify(self.name)
        super(Product, self).save()

    def __str__(self):
        return self.name
    slug = models.SlugField(editable=True) # hide from admin

class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User)
    product = models.ForeignKey('Product',on_delete=models.CASCADE, related_name="product")
    created = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.name+" => "+self.user.username

    def TotalPrice(self):
        return self.quantity * self.product.price
