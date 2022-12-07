from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    description = models.TextField()
    status = models.CharField(max_length=15, choices=[('есть в наличии', 'in stock'), ('нет в наличии', 'out of stock'), ('ожидается', 'pending')])

    def __str__(self):
        return f'[{self.category}] -> {self.title}'