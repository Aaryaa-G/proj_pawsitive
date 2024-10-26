from django.contrib import admin
from .models import Donation, Adoption, Volunteer

admin.site.register(Donation)
admin.site.register(Adoption)
admin.site.register(Volunteer)
