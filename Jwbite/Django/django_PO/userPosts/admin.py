from django.contrib import admin
from .models import Post

admin.site.register(Post)

# This controls what it seen at localhost:8000/admin. By adding in additional parameters, it adds in additional categories on the website.