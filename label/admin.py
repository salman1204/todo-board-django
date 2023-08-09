from django.contrib import admin

from .models import Label

# Register your models here.


class LabelAdmin(admin.ModelAdmin):
    search_fields = ["title"]


admin.site.register(Label, LabelAdmin)
