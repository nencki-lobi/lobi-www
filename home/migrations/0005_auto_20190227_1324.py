# Generated by Django 2.1.5 on 2019-02-27 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190227_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='affiliated',
            field=models.BooleanField(default=False, verbose_name='Check for affiliated members'),
        ),
    ]
