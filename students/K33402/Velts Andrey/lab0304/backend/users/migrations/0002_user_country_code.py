# Generated by Django 3.1.4 on 2020-12-06 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='country_code',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Код Страны'),
        ),
    ]
