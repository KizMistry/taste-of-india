from django.contrib import admin
from .models import Booking, Meal
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Meal)
class MealAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')
