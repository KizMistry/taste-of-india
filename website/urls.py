from . import views
from django.urls import path


urlpatterns = [
    path("", views.MealList.as_view(), name="home"),
    path("meal.html", views.MealList.as_view(), name="meal")
]
