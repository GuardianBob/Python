# Generated by Django 2.2.13 on 2021-04-14 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginApp', '0002_auto_20210414_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
