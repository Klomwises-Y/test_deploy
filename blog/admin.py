from django.contrib import admin
from .models import Post, Author
from django_summernote.admin import SummernoteInlineModelAdmin

# Register your models here.

admin.site.register(Author)
admin.site.register(Post)

# username: gift
# password: 1234