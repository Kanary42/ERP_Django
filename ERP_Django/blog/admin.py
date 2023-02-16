from django.contrib import admin

from .models import Post, Order, WeldMaterial, WeldMaterialUse

admin.site.register(Post)
admin.site.register(Order)
admin.site.register(WeldMaterial)
admin.site.register(WeldMaterialUse)
