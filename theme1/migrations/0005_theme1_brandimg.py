# Generated by Django 2.2.1 on 2019-05-02 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theme1', '0004_theme1_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme1',
            name='brandimg',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
