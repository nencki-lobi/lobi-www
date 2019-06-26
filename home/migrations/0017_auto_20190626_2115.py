# Generated by Django 2.2.1 on 2019-06-26 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20190626_1916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='research',
            name='web',
        ),
        migrations.AlterField(
            model_name='meeting',
            name='link',
            field=models.URLField(blank=True, max_length=500, verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='link',
            field=models.URLField(blank=True, max_length=500, verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='research',
            name='link',
            field=models.URLField(blank=True, max_length=500, verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='research',
            name='recruitment',
            field=models.URLField(blank=True, max_length=500, verbose_name='Link to recruitment page eg. FB post'),
        ),
    ]
