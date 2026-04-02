from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    PRODUCT_STATUS={
        'available':'Available',
        'unavailable':'Unavailable',
        'out_of_stock':'Out of Stock',
        'discontinued':'Discontinued'
    }
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(upload_to='products/')
    description=models.TextField()
    created_at=models.DateTimeField(default=timezone.now)
    status=models.CharField(max_length=20,choices=PRODUCT_STATUS,default='available')

def __str__(self):
    return self.name


class productReview(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='reviews')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    review=models.TextField()
    rating=models.IntegerField()
    comment=models.TextField()
    created_at=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Product : {self.product.name} - User : {self.user.name} -Rating : {self.rating} -Comments : {self.comment}'
    
class Store(models.Model):
    name=models.CharField(max_length=100)
    products=models.CharField(max_length=100)
    product_varities=models.ManyToManyField(Product,related_name='stpres')
    def __str__(self):
        return self.name
class ProductCertificate(models.Model):
    product=models.OneToOneField(Product,on_delete=models.CASCADE)
    certificate_number=models.CharField(max_length=100)
    issued_date=models.DateTimeField(default=timezone.now)
    valid_until=models.DateTimeField()
    def __str__(self):
        return f'Certificate for {self.product.name}'