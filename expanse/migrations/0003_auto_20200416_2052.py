# Generated by Django 3.0.5 on 2020-04-16 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expanse', '0002_auto_20200416_1841'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expanse',
            old_name='time',
            new_name='date',
        ),
    ]
