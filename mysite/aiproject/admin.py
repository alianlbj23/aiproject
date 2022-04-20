from django.contrib import admin
from aiproject.models import *


class MemberAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Title', 'Expertise', 'Education']
admin.site.register(Member, MemberAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['Chi_title', 'Eng_title', 'Editor', 'Content','Data_url']
admin.site.register(Article, ArticleAdmin)
# Register your models here.
