from django.contrib import admin
from account.models import *
from post.models import *

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
