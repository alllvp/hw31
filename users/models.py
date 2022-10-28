from django.contrib.auth.models import AbstractUser
from django.db import models

from users.validators import birth_date_validator, email_validator


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


class User(AbstractUser):
    role = models.CharField(choices=UserRoles.choises, default='member', max_length=12)
    location = models.ManyToManyField(Location)
    age = models.SmallIntegerField(null=True)
    birth_date = models.DateField(validators=[birth_date_validator], null=True)
    email = models.EmailField(validators=[email_validator])

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
