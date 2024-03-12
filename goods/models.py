from django.db import models


class GoodsCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Goods(models.Model):
    image = models.ImageField(upload_to='products_image')
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    category = models.ForeignKey(to=GoodsCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'Имя товара: {self.name} | Цена товара: {self.price}'
