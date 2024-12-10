from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)
    # Other fields...

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    productname = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    ordered_date = models.DateTimeField(auto_now_add=True)

class Coupon(models.Model):
    code = models.CharField(max_length=20)
    discount = models.DecimalField(max_digits=5, decimal_places=2)

class Report(models.Model):
    # Add fields relevant to reporting like sales, revenue, etc.
    pass
class Setting(models.Model):
    site_name = models.CharField(max_length=100)
    currency = models.CharField(max_length=10)
    tax_rate = models.DecimalField(max_digits=4, decimal_places=2)

    


# Create your models here.
