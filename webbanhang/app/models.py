from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

# Create your models here.
class Category(models.Model):
    sub_category=models.ForeignKey('self',on_delete=models.CASCADE,related_name='sub_categories',null=True,blank=True)
    is_sub=models.BooleanField(default=False)
    name=models.CharField(max_length=200,null=True)
    slug= models.SlugField(max_length=200,unique=True)
    def __str__(self):
        return self.name
class CreateUserForm(UserCreationForm):
    class Meta:
        model =User
        fields= ['username','email','first_name','last_name','password1','password2']

class Product(models.Model):
    category=models.ManyToManyField(Category,related_name='product')
    name= models.CharField(max_length=200,null=True)
    price= models.FloatField()
    digital=models.BooleanField(default=False,null=True,blank=False)
    image=models.ImageField(null=True,blank=True)
    detail=models.TextField(null=True,blank=True)
    reviews = models.ManyToManyField('Review', related_name='products')

    def __str__(self) :
        return self.name
    @property
    def ImageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True,blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=False)
    rating = models.IntegerField(default=0, null=True, blank=True)
    comment = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} on {self.product.name}"
class ShippingAddress(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    ten = models.CharField(max_length=200, null=True)
    sodt = models.CharField(max_length=10, null=True)
    thanhpho = models.CharField(max_length=200, null=True)
    quan = models.CharField(max_length=200, null=True)
    huyen = models.CharField(max_length=200, null=True)
    def __str__(self):
        return str(self.thanhpho)
class Order(models.Model):
    customer = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    date_order=models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    complete=models.BooleanField(default=False,null=True,blank=False)
    transaction_id=models.CharField(max_length=200,null=True)
    customer_address = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.customer_address is None:
            return str(self.id)
        return str(self.id) + " - " + str(self.customer)+" - "+ str(self.customer_address.thanhpho)
    
    @property
    def get_cart_items(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.quantity for item in orderitems])
        return total

    def get_cart_total(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.get_total for item in orderitems])
        return total
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.product) + " - " + "Order: " + str(self.order_id)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


