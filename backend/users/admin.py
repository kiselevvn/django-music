from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group as BaseGroup
from django.utils.translation import gettext_lazy as _
from .models import ProxyGroup, User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "second_name",
                    "email",
                )
            },
        ),
        (
            _("Permissions Django"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )

    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "second_name",
    )
    list_readonly_not_superuser_fields = (
        "is_superuser",
        "is_staff",
        "last_login",
        "date_joined",
    )


admin.site.unregister(BaseGroup)
admin.site.register(ProxyGroup, GroupAdmin)
