from django.db import models


# Create your models here.
class Restaurant(models.Model):
    image = models.ImageField('image', upload_to='restaurants')
    name = models.CharField('name', max_length=50)
    description = models.CharField('description', max_length=200)
    price_rating = models.PositiveSmallIntegerField('price rating')
    user_rating = models.DecimalField('user rating', max_digits=3, decimal_places=2)

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    FOOD_CLASS_CHOICES = [
        ('1', 'Entree'),
        ('2', 'Side'),
        ('3', 'Drink'),
        ('4', 'Dessert'),
        ('5', 'Misc.'),
    ]

    image = models.ImageField('image', upload_to='food-items')
    name = models.CharField('name', max_length=50)
    description = models.CharField('description', max_length=200)
    food_class = models.CharField('food class', max_length=1, choices=FOOD_CLASS_CHOICES, default='5')
    restaurant = models.ForeignKey('restaurant', Restaurant)

    def __str__(self):
        return self.name

