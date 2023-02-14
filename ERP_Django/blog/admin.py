from django.contrib import admin

from .models import Post, Order, WeldMat, WeldMatUse

admin.site.register(Post)
admin.site.register(Order)
admin.site.register(WeldMat)
admin.site.register(WeldMatUse)
