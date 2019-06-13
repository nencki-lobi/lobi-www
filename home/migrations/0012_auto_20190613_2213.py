# Generated by Django 2.2.1 on 2019-06-13 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20190612_2033'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Public',
        ),
        migrations.AddField(
            model_name='news',
            name='event_type',
            field=models.CharField(choices=[('NW', 'Generic news'), ('MD', 'Media release'), ('EV', 'Public event')], default='NW', help_text='All items will apear on the main page. Only media releases and events will display in the Public card.', max_length=2),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(help_text='New item will appear on the top. Re-edited and saved items are treated as new ones.', max_length=200, verbose_name='Title'),
        ),
    ]
