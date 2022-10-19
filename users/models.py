from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = 'Местоположение'
        verbose_name_plural = 'Местоположения'
    def __str__(self):
        return self.name


class UserRoles:
    USER = 'member'
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    choises = (
        (USER, 'Пользователь'),
        (ADMIN, 'Админ'),
        (MODERATOR, 'Модератор'),
    )


# class User(models.Model):
#     first_name = models.CharField(verbose_name='Имя', max_length=60)
#     last_name = models.CharField(max_length=80)
#     username = models.CharField(max_length=20, unique=True)
#     password = models.CharField(max_length=30)
#     role = models.CharField(choices=UserRoles.choises, default='member', max_length=12)
#     location = models.ManyToManyField(Location)
#     age = models.SmallIntegerField(null=True)
#
#     class Meta:
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
class User(AbstractUser):
    role = models.CharField(choices=UserRoles.choises, default='member', max_length=12)
    location = models.ManyToManyField(Location)
    age = models.SmallIntegerField(null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
