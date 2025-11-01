from django.db import models

# Create your models here.
class usersInfo(models.Model):
    username=models.CharField(max_length=50,unique=True)
    password=models.CharField(max_length=20)
    Email=models.EmailField()
    mobile_number=models.IntegerField()
    


class product(models.Model):
    ProductName=models.CharField(max_length=100)
    ProductCatageries=models.CharField(max_length=100)
    ProductDescription=models.CharField(max_length=100)
    Price=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)

class orders(models.Model):
    userid=models.ForeignKey(usersInfo,on_delete=models.CASCADE)
    productid=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    totalamount=models.IntegerField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
