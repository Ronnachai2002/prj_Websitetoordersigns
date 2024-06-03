# Generated by Django 5.0.2 on 2024-02-11 13:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=500)),
                ('description', models.TextField(default='No description', max_length=255)),
                ('material', models.CharField(default='No description', max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('is_available', models.BooleanField(blank=True, default=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='app.item')),
            ],
        ),
        migrations.CreateModel(
            name='Detailcart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('carts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cart')),
                ('itemImages', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.itemimage')),
            ],
        ),
    ]
