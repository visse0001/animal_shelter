from django.db import models


# Create your models here.
class Animal(models.Model):
    SEX = (
        ('female', 'female'),
        ('male', 'male'),
    )

    TYPE = (
        ('cat', 'cat'),
        ('dog', 'dog'),
    )

    STATUS = (
        ('deceased', 'deceased'),
        ('for adoption', 'for adoption'),
        ('stay', 'stay'),
        ('adopted', 'adopted'),
    )

    name = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=100, null=True, choices=TYPE)
    sex = models.CharField(max_length=100, null=True, choices=SEX)
    daily_ration = models.IntegerField(null=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=100, null=True, choices=STATUS)

    def __str__(self):
        return self.name


# class Employee(models.Model):
#     name = models.CharField(max_length=200, null=True)
#     phone = models.CharField(max_length=200, null=True)
#     email = models.CharField(max_length=200, null=True)
#     date_created = models.DateTimeField(auto_now_add=True, null=True)
#
#     def __str__(self):
#         return self.name
