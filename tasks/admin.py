from django.contrib import admin
from .models import Task

# para que se vean los campos de solo lectura en /admin el campo created
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created", )

# Register your models here.
#para que se vea en /admin
admin.site.register(Task, TaskAdmin)