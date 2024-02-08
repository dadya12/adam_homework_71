from django.contrib import admin
from accounts.models import User
from webapp.models import Comment

admin.site.register(User)
admin.site.register(Comment)