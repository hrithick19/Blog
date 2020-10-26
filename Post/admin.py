from django.contrib import admin
from .models import  *

# Register your models here.

admin.site.site_header="Site Management"
admin.site.register(kadhai)
admin.site.register(kavithai)
admin.site.register(katturai)