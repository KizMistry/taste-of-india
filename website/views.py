from django.shortcuts import render
from django.views import generic
from .models import Meal, Booking


# Create your views here.
class MealList(generic.ListView):
    model = Meal
    queryset = Meal.objects.filter(status=1).order_by('created_on')
    template_name = 'meal.html'
    paginate_by = 6
