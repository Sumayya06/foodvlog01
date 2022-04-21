from django.contrib import admin
from . models import *

# Register your models here.


# name enna fieldill enth type akkumbozum automatically slugill veraan vendiyann catadmin enna class create akiyittullath
class catadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}    
    # slug ill enthann display aaakandeth athann : itt idendath

admin.site.register(categ,catadmin)
# should call the class name while register

class prodadmin(admin.ModelAdmin):
    # price okke admin panel ill display avann use akunna variable ann list_display
    # avde thanne edit cheyaan um pattan list_editable use aakkum
    list_display=['name','slug','price','stock','img','available']
    list_editable=['price','stock','img','available']
    prepopulated_fields={'slug':('name',)}    

admin.site.register(products,prodadmin)