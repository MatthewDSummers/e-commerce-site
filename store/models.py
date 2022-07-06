# from unicodedata import decimal
from django.db import models
from django.contrib.auth.models import User
# Create your models here.



# class Owner(models.Model):
    

class Shop(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="shop")
    # or OnetoOne if one shop per person


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=200, null=True)
    # favorites
    # order-history
    # my-recipes - not held accountable for how they use the product, we wanna just offer
    # the ability for them to share how they used it
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    # price = models.FloatField()
    # quantity = models.IntegerField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    desc = models.CharField(max_length=3000, default="")
    digital = models.BooleanField(default=False, null=True, blank=True)


    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length = 1000, null=True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.street

# class Wishlist(models.Model):
    # user = aosdijfaosidjf




# NOTES
    # link to resources - for plant info (wikipedia or sth)
    # SCHEDULED ORDERS FOR CUSTOMERS
    # PLUG-IN AN API FOR PLANT SALES DATA PER REGION

# class Image(models.Model):
#     name = models.CharField(max_length=255)
#     image = models.ImageField(upload_to='images/')
#     ticket = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)