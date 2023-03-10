from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
GUESTS = ((2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), ('More', '8+'))
STATUS = ((0, "Draft"), (1, "Published"))


class Meal(models.Model):
    title = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, unique=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='dish_likes', blank=True)

    class Meta:

        ordering = ['-created_on']


class Booking(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField()
    booking_time = models.DateTimeField()
    number_of_guests = models.IntegerField(choices=GUESTS, default=2)

    class Meta:

        ordering = ['-booking_time']

    def confirmation(self):
        return self.email, self.booking_time, self.number_of_guests


class Review(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=15)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=0)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
