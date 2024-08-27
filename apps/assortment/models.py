from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Название',
        )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена',
        )
    image = models.ImageField(
        upload_to='products/',
        verbose_name='фото',
        )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
        )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Продукт' 
        verbose_name_plural = 'Продукты'
        
