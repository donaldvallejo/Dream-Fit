# Generated by Django 2.2.6 on 2019-12-06 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0003_auto_20191206_0416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
