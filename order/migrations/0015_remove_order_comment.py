# Generated by Django 2.0.7 on 2018-09-22 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_order_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='comment',
        ),
    ]
