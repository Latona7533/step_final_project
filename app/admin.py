from django.contrib import admin

# Register your models here.
from app.models import Profile, Portfolio, Comment, Blog

admin.site.register(Profile)
admin.site.register(Portfolio)
admin.site.register(Comment)
admin.site.register(Blog)