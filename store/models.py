from django.db import models

# Create your models here.

class promotion(models.Model):
    description = models.CharField(max_length=200)
    discount = models.FloatField()

class Collection(models.Model):
    title = models.CharField(max_length=200)

class Product(models.Model):
    MEMBERSHIP_BRONZE='B'
    MEMBERSHIP_SILVER='S'
    MEMBERSHIP_GOLD='G'

    MEMBERSHIP_CHOICES=[
        ('MEMBERSHIP_BRONZE', 'Bronze'),
        ('MEMBERSHIP_SILVER', 'Silver'),
        ('MEMBERSHIP_GOLD', 'Gold')
    ]
    title = models.CharField(max_length=255)
    discription = models.Textfield()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory= models.IntergerField()
    last_update = models.DateTimeField(auto_now=True)
    collection=models.ForeignKey(collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)

class Customer(models.Model):
    first_name=models.Textfield(max_length=200)
    last_name=models.Textfield(max_length=200)
    email=models.EmailField(unique=True, max_length=200)
    phone=models.CharField(max_length=200)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default-'MEMBERSHIP_BRONZE')

class Order(models.Model):
    PAYMENT_STATUS_PENDING ='P'
    PAYMENT-STATUS_COMPLETE='C'
    PAYMENT_STATUS_FAILED = 'F'

    PAYMENT_STATUS_CHOICES=[
        ('PAYMENT_STATUS_PENDING', 'Pending')
        ('PAYMENT-STATUS_COMPLETE', 'Complete')
        ('PAYMENT_STATUS_FAILED', 'Failed')
    ]
    place_at=medels.DateTimeField(auto_now_add=True)
    payment_status=models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default= PAYMENT_STATUS_PENDING  )
    Customer= models.ForeignKey(Customer, on_delete=models.PROTECT)


class Adresss(models.Models):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class OrderItem(models.Model):
    Order=models.ForeignKey(order, on_delete=models.PROTECT)
    Prod=models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntergerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Cart(models.Model):
    created_at= models.DateTimeField(auto_now_add=true)

class cartItems(models.Model):
    product= models.ForeignKey(product, on_delete=models.CASCADE)
    cart=models.ForeignKey(card, on_delete=models.CASCADE)
    quantity= models.PositiveSmallIntergerField()