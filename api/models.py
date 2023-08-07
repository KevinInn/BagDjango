from django.db import models

class Member(models.Model):
    class Meta:
        managed = False
        db_table = 'Member'
    mId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    

# Create your models here.
class Product(models.Model):
    class Meta:
        managed = False
        db_table = 'Product'
    pId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    brand = models.CharField(max_length=255)
    age = models.IntegerField()
    size = models.CharField(max_length=100, default=' ')
    likes = models.IntegerField()
    def __str__(self):
        return self.name
    
class Picture(models.Model):
    class Meta:
        managed = False
        db_table = 'Picture'
    pId = models.ForeignKey(Product, on_delete=models.CASCADE, primary_key=True, db_column="pId")
    picture = models.CharField(max_length=255)

class Comment(models.Model):
    class Meta:
        managed = False
        db_table = 'Comment'
    pId = models.ForeignKey(Product, on_delete=models.CASCADE, db_column="pId")
    mId = models.ForeignKey(Member, on_delete=models.CASCADE, db_column="mId")
    cId = models.AutoField(primary_key=True)
    content = models.CharField(max_length=255)
    rank = models.IntegerField()

class Cart(models.Model):
    class Meta:
        managed = False
        db_table = 'Cart'
    pId = models.ForeignKey(Product, on_delete=models.CASCADE, db_column="pId")
    mId = models.ForeignKey(Member, on_delete=models.CASCADE, db_column="mId")
    cartTime = models.DateTimeField(db_column="cartTime")
    
class Orders(models.Model):
    class Meta:
        managed = False
        db_table = 'Orders'
    oId = models.AutoField(primary_key=True)
    pId = models.ForeignKey(Product, on_delete=models.CASCADE, db_column="pId")
    mId = models.ForeignKey(Member, on_delete=models.CASCADE, db_column="mId")
    payment = models.CharField(max_length=255)
    order_time = models.DateTimeField(db_column="order_time")
    duration = models.IntegerField()
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    startTime = models.DateField()
    endTime = models.DateField()