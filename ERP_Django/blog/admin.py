from django.contrib import admin

from .models import Post, WeldMaterial, WeldMaterialUse, Purchaser, Worksite

admin.site.register(Post)
admin.site.register(WeldMaterial)
admin.site.register(WeldMaterialUse)
admin.site.register(Purchaser)
admin.site.register(Worksite)
