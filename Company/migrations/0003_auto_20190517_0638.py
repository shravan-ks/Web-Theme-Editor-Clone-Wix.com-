# Generated by Django 2.2.1 on 2019-05-17 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0002_auto_20190517_0619'),
    ]

    operations = [
        migrations.AddField(
            model_name='companydb',
            name='Accent_Color',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='companydb',
            name='Background_Color_Left_Column',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='companydb',
            name='Background_Color_Right_Column',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='companydb',
            name='Facebook',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='companydb',
            name='Instagram',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='companydb',
            name='Twitter',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
