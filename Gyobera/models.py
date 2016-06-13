from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Classification(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField()
    likes = models.IntegerField()
    slug = models.SlugField(default="")

    def save(self, *args, **kwargs):
        # Uncomment if you don't want the slug to change every time the name changes
        # if self.id is None:
        # self.slug = slugify(self.name)
        self.slug = slugify(self.name)
        super(Classification, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class List(models.Model):
    classification = models.ForeignKey(Classification)
    title = models.CharField(max_length=128)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')], default="")
    Custodian = models.CharField(max_length=25, blank=True)
    description = models.TextField(blank=True)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return '{} | {}'.format(self.title, self.title)


class Student(models.Model):
    Names = models.CharField(max_length=100, blank=False)
    Sex = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    Age = models.IntegerField(blank=False)
    Registration_Number = models.CharField(max_length=100, blank=False)
    Course = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return '{} | {} | {} | {} | {}'.format(self.Names, self.Sex, self.Age, self.Registration_Number, self.Course)


class Room(models.Model):
    Hostel = models.ForeignKey(List)
    Room_Number = models.CharField(max_length=50)
    Total_rooms = models.IntegerField(default=0, blank=True)
    Price_single = models.IntegerField(default=0, blank=True)
    Price_double = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return ' {}   |   {} '.format(self.Hostel, self.Room_Number)


class Booking(models.Model):
    Book_No = models.IntegerField(default=1)
    Gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')], default="--")
    Hostel = models.ForeignKey(List, null=True, blank=True)
    Room_Number = models.ForeignKey(Room)
    Room_capacity = models.CharField(max_length=1, choices=[('S', 'Single'), ('D', 'Double')], default="--")
    Booked_by = models.ForeignKey(Student, default='--')
    Booked_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}, {} booked a {} room in {} {} at {}'.format(
            self.Booked_by, self.Gender, self.Room_capacity, self.Hostel, self.Room_Number, self.Booked_on)


class MobilePayment(models.Model):
    Booked_by = models.ForeignKey(Student, default='--')
    Hostel = models.ForeignKey(List, null=True, blank=True)
    Amount_deposited = models.IntegerField(default=0)
    Balance = models.IntegerField
    Mobile_No = models.IntegerField(default='07')
    Pin_Number = models.IntegerField(default=00000)

    def __str__(self):
        return '{}, deposited {} for a room in {}'.format(
            self.Booked_by, self.Amount_deposited, self.Hostel)


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    About_me = models.CharField(max_length=200, blank=False)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.user
