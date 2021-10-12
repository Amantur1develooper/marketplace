from django.db import models
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='shop/image' , null=True , blank=True)

    def str(self):
        return self.name

    def get_all_product(self):
        return Product.objects.all()