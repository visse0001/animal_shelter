from django.shortcuts import render, redirect
from django.db.models import Sum
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Animal, Food
from .forms import AnimalForm, UserRegisterForm, FoodForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You are now able to login')
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {'form': form}

    return render(request, 'shelter/register.html', context)


@login_required(login_url='login')
def home(request):
    total_animals = Animal.objects.count()

    feed_ration = Animal.objects.aggregate(feed_ration_sum=Sum('daily_ration'))
    feed_ration_num = feed_ration['feed_ration_sum']

    only_cats = Animal.objects.filter(type='cat')
    total_cats = only_cats.count()

    only_dogs = Animal.objects.filter(type='dog')
    total_dogs = only_dogs.count()

    dogs_feed_ration = Animal.objects.filter(type="dog").aggregate(dogs_feed_ration_sum=Sum('daily_ration'))
    dogs_feed_ration_num = dogs_feed_ration['dogs_feed_ration_sum']

    cats_feed_ration = Animal.objects.filter(type="cat").aggregate(cats_feed_ration_sum=Sum('daily_ration'))
    cats_feed_ration_num = cats_feed_ration['cats_feed_ration_sum']

    animals = Animal.objects.all()

    context = {'feed_ration_num': feed_ration_num,
               'total_animals': total_animals,
               'total_cats': total_cats,
               'total_dogs': total_dogs,
               'animals': animals,
               'dogs_feed_ration_num': dogs_feed_ration_num,
               'cats_feed_ration_num': cats_feed_ration_num,
               }

    return render(request, 'shelter/dashboard.html', context)


@login_required(login_url='login')
def add_animal(request):
    if request.method == "POST":
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AnimalForm()

    context = {'form': form}

    return render(request, 'shelter/animal_form.html', context)


@login_required(login_url='login')
def update_animal(request, id):
    animal = Animal.objects.get(id=id)
    form = AnimalForm(instance=animal)

    if request.method == "POST":
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            messages.success(request, f'Update succeeded!')

            return redirect('home')

    context = {'form': form}

    return render(request, 'shelter/animal_form.html', context)


def delete_animal(request, id):
    animal = Animal.objects.get(id=id)
    if request.method == "POST":
        animal.delete()
        return redirect('home')

    context = {'animal': animal}

    return render(request, 'shelter/delete.html', context)


def animals_for_adoption(request):
    animals_for_adoption = Animal.objects.filter(status='for adoption')
    print(animals_for_adoption)
    context = {'animals_for_adoption': animals_for_adoption}

    return render(request, 'shelter/animals_for_adoption.html', context)


@login_required(login_url='login')
def add_food(request):
    if request.method == "POST":
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = FoodForm()

    context = {'form': form}

    return render(request, 'shelter/food_form.html', context)


@login_required(login_url='login')
def food(request):
    all_food = Food.objects.all()

    context = {'all_food': all_food}

    return render(request, 'shelter/food.html', context)
