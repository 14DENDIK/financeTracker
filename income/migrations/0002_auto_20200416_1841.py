# Generated by Django 3.0.5 on 2020-04-16 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='currency',
            field=models.CharField(choices=[('usd', '$')], default='usd', max_length=5),
        ),
    ]
