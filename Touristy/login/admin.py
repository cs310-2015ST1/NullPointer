from django.contrib import admin

# Register your models here.
from login.models import UserProfile
from login.models import Favorite
admin.site.register(UserProfile)
admin.site.register(Favorite)
