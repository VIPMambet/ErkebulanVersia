# Generated by Django 5.1.3 on 2024-11-19 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('born', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'verbose_name': 'Комната', 'verbose_name_plural': 'Комнаты'},
        ),
        migrations.AlterField(
            model_name='room',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img/', verbose_name='Фото комнаты'),
        ),
    ]