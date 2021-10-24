# Generated by Django 3.2.8 on 2021-10-24 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='food-items', verbose_name='image')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('description', models.CharField(max_length=200, verbose_name='description')),
                ('food_class', models.CharField(choices=[('1', 'Entree'), ('2', 'Side'), ('3', 'Drink'), ('4', 'Dessert'), ('5', 'Misc.')], default='5', max_length=1, verbose_name='food class')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='restaurants', verbose_name='image')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('description', models.CharField(max_length=200, verbose_name='description')),
                ('price_rating', models.PositiveSmallIntegerField(verbose_name='price rating')),
                ('user_rating', models.PositiveSmallIntegerField(verbose_name='user rating')),
            ],
        ),
    ]
