from django.contrib import admin
from .models import *
from django.contrib.admin.decorators import register
# Register your models here.
@register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['full_name','phone','email' ,'services', 'date']
    list_filter = ['date']
    
    def full_name(self, obj):
        return '{} {}'.format(obj.fname, obj.lname)
# admin.site.register(Con)


@register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['type','title','organization','joining_date','end_year']
    list_filter = ['type','end_year']
    
    
    
# Projects Admin Class
@register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['name', 'link', 'image', 'upload_date']
    list_display_links = ['name', 'link', 'image', 'upload_date']
