# Generated by Django 4.1.4 on 2023-04-01 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0009_odeme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sepet',
            name='adet',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='sepet',
            name='toplam',
            field=models.IntegerField(),
        ),
    ]