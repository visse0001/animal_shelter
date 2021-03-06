# Generated by Django 3.0.4 on 2020-05-12 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelter', '0004_animal_animal_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, null=True)),
                ('form', models.CharField(choices=[('dry', 'dry'), ('wet', 'wet')], max_length=128, null=True)),
                ('life_stage', models.CharField(choices=[('junior', 'junior'), ('adult', 'adult'), ('senior', 'senior')], max_length=128, null=True)),
                ('feature', models.CharField(choices=[('low fat', 'low fat'), ('bulk', 'bulk'), ('high protein', 'high protein')], max_length=128, null=True)),
                ('weight', models.FloatField(null=True)),
                ('price', models.FloatField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='animal_food',
            field=models.ManyToManyField(to='shelter.Food'),
        ),
    ]
