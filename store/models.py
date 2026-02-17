from django.db import models

# Create your models here.
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

class Customer(models.Model):
    first_name=models.Textfield(max_length=200)
    last_name=models.Textfield(max_length=200)
    email=model.EmailField(unique=True, max_length=200)
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
    place_at=medels.DateTimeField(auto_now=True)
    payment_status=models.CharField

