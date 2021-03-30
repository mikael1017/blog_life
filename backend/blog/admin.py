from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import BlogPost


class SomeModelAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')


admin.site.register(BlogPost, BlogPostAdmin)

# Register your models here.
