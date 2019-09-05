# Generated by Django 2.2.1 on 2019-05-13 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_notification_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=125)),
                ('email', models.EmailField(max_length=125)),
                ('first_name', models.CharField(max_length=125)),
                ('last_name', models.CharField(max_length=125)),
            ],
        ),
    ]
