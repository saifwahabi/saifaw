from django.contrib import admin
from .models import Project, Mockup, Contact, Site_data

# Register your models here.
admin.site.register(Project)
admin.site.register(Mockup)
admin.site.register(Contact)
admin.site.register(Site_data)


