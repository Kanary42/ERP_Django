from django.contrib import admin

from .models import Post, WeldMaterial, WeldMaterialUse

admin.site.register(Post)
admin.site.register(WeldMaterial)
admin.site.register(WeldMaterialUse)
