from django.contrib import admin
from .models import Profile, PhoneNumber, Service, Category


admin.site.register(Profile)
admin.site.register(PhoneNumber)
admin.site.register(Service)
admin.site.register(Category)

