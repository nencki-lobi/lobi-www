# Generated by Django 2.2.1 on 2019-12-30 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_profile_researchgate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='research',
            name='about',
            field=models.TextField(blank=True, verbose_name='More information (html allowed)'),
        ),
    ]