# Generated by Django 4.0.4 on 2022-05-24 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0017_noticias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
    ]
