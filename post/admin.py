from django.contrib import admin
from account.models import *
from post.models import *

admin.site.register(Categories)
admin.site.register(Posts)
admin.site.register(Comments)
