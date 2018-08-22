# Generated by Django 2.0.7 on 2018-08-22 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0004_auto_20180821_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='additional_equipment',
            field=models.ManyToManyField(null=True, related_name='cars', to='car.AditionalEquipment'),
        ),
        migrations.AlterField(
            model_name='car',
            name='engine',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='car.Engine'),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='car.Model'),
        ),
    ]
