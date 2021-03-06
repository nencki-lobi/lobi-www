# Generated by Django 2.1.5 on 2019-02-13 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_alumni_course_photo_publication_research'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(blank=True, max_length=200, verbose_name='Position')),
                ('degree', models.CharField(blank=True, max_length=20, verbose_name='Academic degree')),
                ('affiliated', models.BooleanField(verbose_name='Check for affiliated members')),
                ('spoiler', models.ImageField(blank=True, upload_to='users', verbose_name='Email spoiler graphic')),
                ('priority', models.IntegerField(verbose_name='Priority (the more the higher at page)')),
                ('about', models.CharField(blank=True, max_length=2000, verbose_name='About (html allowed)')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Phone number')),
                ('research', models.CharField(blank=True, max_length=2000, verbose_name='Research interests (html allowed)')),
                ('publications', models.CharField(blank=True, max_length=12000, verbose_name='Selected publications (html allowed)')),
                ('funding', models.CharField(blank=True, max_length=2000, verbose_name='Funding (html allowed)')),
                ('image', models.ImageField(blank=True, upload_to='users', verbose_name='Face')),
                ('my_dish', models.CharField(blank=True, max_length=200, verbose_name='I can cook...')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
