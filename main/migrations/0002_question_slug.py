# Generated by Django 2.2.4 on 2019-08-19 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='slug',
            field=models.SlugField(default='question'),
            preserve_default=False,
        ),
    ]