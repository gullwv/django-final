from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Commons(models.Model): #abstract base class for all name-description classes
    name = models.CharField(max_length=25)
    desc = models.CharField(max_length=100)
    
    class Meta:
        abstract = True

class PlaceType(Commons): #defines what kind of location
    dark = models.BooleanField(default=False)
    indoors = models.BooleanField(default=False)
    passable = models.BooleanField(default=True)
    can_wall = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class ItemType(Commons):
    heavy = models.BooleanField()
    swag = 'S'
    phone = 'P'
    pin = 'B'
    threads = 'T'
    food = 'F'
    types = (
        (phone, 'Phone'),
        (pin, 'Pin'),
        (threads, 'Threads'),
        (food, 'Food'),
        (swag, 'Miscellaneous'),
    )
    type = models.CharField(
        max_length = 1,
        choices = types,
        default = swag,
    )
    value = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.name

class Item(models.Model):
    item_type = models.ForeignKey(ItemType, default=1, on_delete=models.CASCADE)

class Place(Commons): #a location
    desc_alias = models.CharField(max_length=50)
    x = models.PositiveSmallIntegerField()
    y = models.PositiveSmallIntegerField()
    place_type = models.ForeignKey(PlaceType, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, blank=True)
    walled = models.BooleanField(default=False) #whether or not a wall is erected
    wall_clearance = models.PositiveSmallIntegerField(default=2) #rank you need to be in order to set up, take down, or pass through a wall at place
    def __str__(self):
        return self.name + " (" + str(self.x) + ", " + str(self.y) + ") (" + str(self.place_type) + ")"

class UserCust(AbstractUser): #user account
    current_location = models.ForeignKey(Place, default=1, on_delete=models.SET(1)) #where the user is
    clearance = models.PositiveSmallIntegerField(default=0) #user rank; 0 is Human, 1 is Player, 2 is Support, 3 is Harrier, 4 is Officer, 5 is GM, 6 is Conductor, 7 is Composer
    groups = related_name='+'
    user_permissions = related_name='+'