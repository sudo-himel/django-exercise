from django.db import models

# Create your models here.
class Category(models.Model):
     title = models.CharField(max_length=50)
     featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')

class Customer(models.Model):
    BRONZE = 'B'
    SILVER = 'S'
    GOLD = 'G'
    MEMBERSHIP_OPTIONS = [
         (BRONZE, 'Bronze'),
         (SILVER, 'Silver'),
         (GOLD, 'Gold') 
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, max_length=254)
    phone = models.CharField(max_length=14)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10, null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_OPTIONS, default=None)

class Address(models.Model):
     street = models.CharField(max_length=255)
     city = models.CharField(max_length=50)
     zip = models.CharField(max_length=10)
     customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)

class Promotion(models.Model):
     descirption = models.CharField(max_length=255)
     discount = models.FloatField()

class Product(models.Model):
     sku = models.CharField(max_length=15, primary_key=True)
     title = models.CharField(max_length=255)
     slug = models.SlugField(default='-')
     description = models.TextField()
     price = models.DecimalField(max_digits=6, decimal_places=2)
     quantity = models.IntegerField()
     created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
     category = models.ForeignKey(Category, on_delete=models.CASCADE)
     promotions = models.ManyToManyField(Promotion)

class Order(models.Model):
    PENDING = 'P'
    COMPLETED = 'C'
    FAILED = 'F'
    CASH_ON_DELIVERY = 'COD'
    PREPAID_DELIVERY = 'PD'
    ORDER_STATUS_OPTIONS = [
         (CASH_ON_DELIVERY, 'Cash On Delivery'),
         (PREPAID_DELIVERY, 'Prepaid Delivery')
    ]
    PAYMENT_STATUS_OPTIONS = [
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
        (FAILED, 'Failed')
    ]
    placed_at = models.DateField(auto_now_add=True)
    order_status = models.CharField(max_length=3, choices=ORDER_STATUS_OPTIONS)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_OPTIONS, default=PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

class OrderItem(models.Model):
     order = models.ForeignKey(Order, on_delete=models.CASCADE)
     product = models.ForeignKey(Product, on_delete=models.CASCADE)
     quantity = models.PositiveSmallIntegerField()
     unit_price = models.DecimalField(max_digits=6, decimal_places=2)

class Cart(models.Model):
     created_at = models.DateField(auto_now_add=True)

class CartItem(models.Model):
     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
     product = models.ForeignKey(Product, on_delete=models.CASCADE)
     quantity = models.PositiveSmallIntegerField()

