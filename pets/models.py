from django.db import models
from datetime import date


class Animal(models.Model):
    name = models.CharField(max_length=100, verbose_name="Кличка")
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE, verbose_name="Порода")
    FAMILY_CHOICES = [('CAT', 'Кошка'), ('DOG', 'Собака'), ('PAR', 'Попугай')]
    family = models.CharField(max_length=3, choices=FAMILY_CHOICES, default='CAT', verbose_name="Семейство")
    SEX_CHOICES = [('M', 'Мальчик'), ('F', 'Девочка')]
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default='M', verbose_name="Пол")
    description = models.TextField(blank=True, verbose_name="Описание")
    date = models.DateField(default=date.today, verbose_name="Дата поступления")
    photo = models.ImageField(upload_to='photo', blank=True, verbose_name="Фото")

    def __str__(self):
        return "{} {} ({}, {})".format(self.get_family_display(), self.name, self.breed, self.get_sex_display())


class Breed(models.Model):
    name = models.CharField(max_length=100, verbose_name="Порода")

    def __str__(self):
        return self.name
