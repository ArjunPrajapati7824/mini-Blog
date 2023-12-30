from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(blog_post)
class admin_model(admin.ModelAdmin):
    list_display=['id','title','desc']

