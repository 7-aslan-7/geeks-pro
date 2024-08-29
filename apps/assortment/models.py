from django.db import models
from django.contrib.auth.models import User
from datetime import date
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
        

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(
        max_length=13,  
        verbose_name='Номер телефона',
        help_text='Номер должен начинаться с +996 и содержать 9 цифр.',
        blank=True,  
        null=True,
    )
    date_of_birth = models.DateField(
        verbose_name='Дата рождения',
        blank=True,  
        null=True,
    )

    def calculate_age(self):
        if self.date_of_birth:
            today = date.today()
            return today.year - self.date_of_birth.year - (
                (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
            )
        return None

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'