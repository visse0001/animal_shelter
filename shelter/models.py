from django.db import models


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
    animal_pic = models.ImageField(null=True, blank=True)
    animal_food = models.ManyToManyField('Food')

    def __str__(self):
        return self.name


class Food(models.Model):
    FORM = (
        ('dry', 'dry'),
        ('wet', 'wet'),
    )

    LIFE_STAGE = (
        ('junior', 'junior'),
        ('adult', 'adult'),
        ('senior', 'senior'),
    )

    FEATURE = (
        ('low fat', 'low fat'),
        ('bulk', 'bulk'),
        ('high protein', 'high protein'),
    )

    name = models.CharField(max_length=128, null=True)
    form = models.CharField(max_length=128, null=True, choices=FORM)
    life_stage = models.CharField(max_length=128, null=True, choices=LIFE_STAGE)
    feature = models.CharField(max_length=128, null=True, choices=FEATURE)
    weight = models.FloatField(null=True)
    price = models.FloatField(null=True)
