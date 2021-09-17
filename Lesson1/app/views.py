from django.http.response import HttpResponse
from django.http.request import HttpRequest

import random

def hello_view(request, name):
    return HttpResponse(f"Hello {name}")

def age_view(request, end, birthyear):
    age = (int(end) - int(birthyear))
    return HttpResponse(f"{age}")

def good_burger(request, burgers, fries, drinks):
    burger_cost = (burgers * 4.50)
    fries_cost = (fries * 1.5)
    drink_cost = (drinks * 1)
    total = int(burger_cost) + int(fries_cost) + int(drink_cost)
    return HttpResponse(f"Total Cost: ${total}")

def roll_die_view(request, sides):
    roll = random.randint(1, int(sides))
    return HttpResponse(roll)

def random_between_view(request, lo, hi):
    return HttpResponse (random.randint(lo, hi))