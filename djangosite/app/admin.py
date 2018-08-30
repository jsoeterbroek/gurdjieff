from django.contrib import admin

# Register your models here.
from .models import Rechtsgebied, Uitspraak

admin.site.register(Rechtsgebied)
admin.site.register(Uitspraak)
