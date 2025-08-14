from django.contrib import admin

from core.models import User, Patient


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ['username', 'created_at', 'updated_at', 'deleted_at', ]


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    pass
