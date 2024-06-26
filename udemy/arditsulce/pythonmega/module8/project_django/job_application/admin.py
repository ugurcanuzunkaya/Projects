from django.contrib import admin
from .models import Form


class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "available_date", "occupation")
    search_fields = ("first_name", "last_name", "email", "available_date", "occupation")
    list_filter = ("first_name", "last_name", "email", "available_date", "occupation")
    ordering = ("first_name", "last_name")
    readonly_fields = ("occupation", )


admin.site.register(Form, FormAdmin)



