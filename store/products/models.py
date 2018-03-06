from django.db import models 
from django.urls import reverse

# Создаем базовую модель нашего продукта
class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000, blank=True)
    price= models.IntegerField(default='0',blank=True)
    image = models.ImageField(blank=True) # указываешь upload_to='media' если только в другой папке лежать будет
    category = models.ForeignKey('Category', on_delete='CASCADE', null=True,related_name="products") 

    def __str__(self):
        return self.title
    def get_absolute_url(self): 
        return reverse('product_detail', args=[str(self.id)])

class Category(models.Model): 
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000, blank=True)
    
    def __str__(self):
        return self.title

class Order(models.Model): 
    product = models.ForeignKey(Product, on_delete='CASCADE') 
    user = models.ForeignKey('auth.User', on_delete='CASCADE',blank=True,null=True)
    customer_name = models.CharField(max_length=200,blank=False )
    customer_phone = models.CharField(max_length=200,blank=False)
    customer_email = models.EmailField(max_length=254,blank=False,help_text='Пример: to1@example.com')