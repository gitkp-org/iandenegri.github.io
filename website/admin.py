from django.contrib import admin
from .models import Social, WebsiteSection, Project, Interest, Owner

# Register your models here.

admin.site.register(Owner)
admin.site.register(Social)
admin.site.register(WebsiteSection)
admin.site.register(Project)
admin.site.register(Interest)
