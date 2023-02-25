from django.contrib import admin

from .models import (Post,
                     WeldMaterial,
                     WeldMaterialUse,
                     Purchaser,
                     Worksite,
                     Order,
                     SerialNumber,
                     TechCard,
                     TechCardOperations,
                     DayTask,
                     DayTaskSheet,
                     ControlInput)

admin.site.register(Post)
admin.site.register(WeldMaterial)
admin.site.register(WeldMaterialUse)
admin.site.register(Purchaser)
admin.site.register(Worksite)
admin.site.register(Order)
admin.site.register(SerialNumber)
admin.site.register(TechCard)
admin.site.register(TechCardOperations)
admin.site.register(DayTask)
admin.site.register(DayTaskSheet)
admin.site.register(ControlInput)
