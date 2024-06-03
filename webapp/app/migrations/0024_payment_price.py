# Generated by Django 5.0.2 on 2024-02-20 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_payment_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]
