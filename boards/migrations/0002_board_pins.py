# Generated by Django 3.1.3 on 2021-01-11 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('boards', '0001_initial'),
        ('pins', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='pins',
            field=models.ManyToManyField(blank=True, to='pins.Pin'),
        ),
    ]
