# Generated by Django 3.0.4 on 2020-05-12 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelter', '0005_auto_20200512_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='feature',
            field=models.CharField(choices=[('normal', 'normal'), ('low fat', 'low fat'), ('bulk', 'bulk'), ('high protein', 'high protein')], max_length=128, null=True),
        ),
    ]
