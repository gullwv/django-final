from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(UserCust)
admin.site.register(ItemType)
admin.site.register(PlaceType)
admin.site.register(Item)
admin.site.register(Place)