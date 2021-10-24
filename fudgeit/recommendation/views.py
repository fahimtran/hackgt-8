from django.shortcuts import render
from recommendation.models import Restaurant, FoodItem
# Create your views here.


def home(request):
    return render(request, '../templates/home_page.html')


def questionnaire(request):
    return render(request, '../templates/questionnaire.html')


def recommendations(request):
    context = {'recommendations': [], 'food_items': []}
    print(request)
    restaurants = Restaurant.objects.all()
    food_items = FoodItem.objects.all()

    budget = request.GET['budget']
    min_price = request.GET['min']
    max_price = request.GET['max']
    food_class = request.GET['foodClass']
    print(str(min_price) + " " + str(max_price) + " " + str(budget))

    for restaurant in restaurants:
        if int(min_price) <= restaurant.price_rating <= int(max_price):
            context['recommendations'].append(restaurant)

    for food_item in food_items:
        if food_item.food_class == food_class and food_item.price <= float(budget):
            context['food_items'].append(food_item)

    for food_item in food_items:
        if food_item not in context['food_items']:
            context['food_items'].append(food_item)

    print(context)

    return render(request, '../templates/recommendations.html', context)


def confirmation(request):
    pass

