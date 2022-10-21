from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.crypto import get_random_string


def get_name_file(instance, filename):
    return '/'.join([get_random_string(length=5) + '_' + filename])


class User(AbstractUser):
    name = models.CharField(max_length=254, verbose_name='Имя', blank=False)
    surname = models.CharField(max_length=254, verbose_name='Фамилия', blank=False)
    patronymic = models.CharField(max_length=254, verbose_name='Отчество', blank=True)
    username = models.CharField(max_length=254, verbose_name='Логин', unique=True, blank=True)
    email = models.CharField(max_length=254, verbose_name='Почта', blank=True)
    password = models.CharField(max_length=254, verbose_name='Пароль', blank=True)
    role = models.CharField(max_length=254, verbose_name='Роль',
                            choices=(('admin', 'Администратор'), ('user', 'Пользователь')), default='user')
    USERNAME_FIELD = 'username'

    def __str__(self):
        return str(self.name) + " " + str(self.surname)


class Product(models.Model):
    name = models.CharField(max_length=254, verbose_name='Имя', blank=False)
    date = models.DateTimeField(max_length=254, verbose_name='Дата добавления', blank=False)
    photo_file = models.ImageField(max_length=254, upload_to=get_name_file,
                                   blank=True, null=True,
                                   validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])
    year = models.IntegerField(max_length=254, verbose_name='Страна производства', blank=True)
    price = models.DecimalField(verbose_name='Стоимость', max_digits=10, decimal_places=2, blank=False,
                                default=0.00)
    count = models.IntegerField(verbose_name='Количество', blank=False, default=1)
    category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.CASCADE, blank=True)


class Category(models.Model):
    year = models.CharField(max_length=254, verbose_name='Наименование', blank=False)

    def __str__(self):
        return self.name
