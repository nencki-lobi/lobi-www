# Generated by Django 2.2.1 on 2019-06-13 21:46

from django.db import migrations, models
import home.validators


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20190613_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='github',
            field=models.CharField(blank=True, max_length=32, validators=[home.validators.validate_github], verbose_name='GitHub username'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='orcid',
            field=models.CharField(blank=True, help_text='0000-0000-0000-0000', max_length=32, validators=[home.validators.validate_orcid], verbose_name='Orcid ID'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='scholar',
            field=models.CharField(blank=True, help_text='Enter just the ID. This is part of an url, e.g. https://scholar.google.pl/citations?user=<strong>qTDPssQAAAAJ</strong>&hl=pl', max_length=32, validators=[home.validators.validate_scholar], verbose_name='Google scholar ID'),
        ),
    ]
