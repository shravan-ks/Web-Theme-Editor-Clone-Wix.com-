# Generated by Django 2.2.1 on 2019-05-05 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_restdb_brandimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restdb',
            name='brandimg',
            field=models.ImageField(blank=True, default='/static/restaurant/img/logo.png', null=True, upload_to='images/'),
        ),
    ]
