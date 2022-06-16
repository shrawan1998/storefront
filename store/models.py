import email
from random import choices
from turtle import title
from django.db import models

# Create your models here.
# many-to-many relationship b/w Promotion-Product
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    # product_set will be created by Django automatically using reverse relationship
    # product_set will return the product for which the promotation is applied
    # product_set name is set by default, you can change it using related_to in Product


#Defining one-to-many relationship for Collection-Product, Customer-Order, Order-Item, Cart-Item
class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+') 
    # + sign prevent Djnago to create reverse relationship (resolve circular relationship)


class Product(models.Model):
    #sku = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=255)  # Instance of CharField class
    slug = models.SlugField()
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2) #9999.99
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT) # If Collection is deleted by mistake then Product will be protected from deleting
    promotions = models.ManyToManyField(Promotion) # Django will automatically create reverse relationship in Promotion class


class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    #Fixed List of values (like constant)
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'), # ('B', 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'), # ('S', 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold') # ('B', 'Gold')
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)


class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed'),
    ]
    placed_at = models.DateTimeField(auto_now_add=True) #First time when we create the order Django automatically populate this field
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField() # Quantity always +ve 
    unit_price = models.DecimalField(max_digits=6, decimal_places=2) 
    # unit_price already exist in Product 
    # but price of products can change over time so
    # we should always store the price of the product when order is placed.


# Defining one-to-one relationship b/w Customer and Address (parent-child relationship)
# customer is parent and address is child (parent must exist before child)
# For one Customer there will be only one Address
"""class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True) # If Customer is deleted then Address will also be deleted
"""
#One-to-Many Relationship (one customer with multiple address)
class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

