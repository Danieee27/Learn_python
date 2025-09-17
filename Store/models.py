from django.db import models
import datetime 
from django.contrib.auth.models import User
from django.db.models.signals import post_save


#Create User Profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=20, default='', blank=True)
    address1 = models.CharField(max_length=20, default='', blank=True)
    address2 = models.CharField(max_length=20, default='', blank=True)
    city = models.CharField(max_length=20, default='', blank=True)
    state = models.CharField(max_length=20, default='', blank=True)
    zip_code = models.CharField(max_length=20, default='', blank=True)
    country = models.CharField(max_length=20, default='', blank=True)
    old_cart = models.CharField(max_length=20, default='', blank=True)

    def __str__(self):
        return self.user.username
    
#Create a user profile as soon as a user signs up or registers
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user = instance)
        user_profile.save()

#automate the profile thing
post_save.connect(create_profile, sender=User)



class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, default=0,decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='', blank=True, null=True)
    image = models.ImageField(upload_to = 'uploads/product/')

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=0)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default='')
    Quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', blank=False)
    phone =  models.CharField(max_length=20, default='', blank=True)
    Date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product