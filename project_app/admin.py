from django.contrib import admin
from .models import admin_data,admin_blog
# Register your models here.
admin.site.register(admin_data)
admin.site.register(admin_blog)