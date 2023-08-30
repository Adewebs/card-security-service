from django.contrib import admin
from .models import ChildParents, Pupil

# Register your models here.

class ChildParentAdmin(admin.ModelAdmin):
    list_display = ('title', 'first_name', 'last_name', 'phone_number','email',
                    'places_of_work','address','image', 'parentqr', 'picker')

admin.site.register(ChildParents, ChildParentAdmin)
admin.site.register(Pupil)