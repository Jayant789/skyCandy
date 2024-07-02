from django.db import models

class Package(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.CharField(max_length=50)
    popularity = models.IntegerField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    TIME_SLOTS = [
        ('sunrise', 'Sunrise'),
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('evening', 'Evening'),
    ]

    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.CharField(max_length=50, choices=TIME_SLOTS)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20)
    participants = models.IntegerField()
    status = models.CharField(max_length=20, default='pending')
    payment_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.customer_name} - {self.package.name} - {self.date}'

class Payment(models.Model):
    payment_id = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    ref_no = models.CharField(max_length=100, unique=True)
    extra = models.JSONField()

    def __str__(self):
        return self.payment_id
