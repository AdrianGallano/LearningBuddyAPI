from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

@admin.register(User)
class NewUserAdmin(UserAdmin):
    readonly_fields = [
        "date_joined",
    ]

    # disable staff privelleges to edit username
    def get_form(self, request, object=None, **kwargs):
        form = super().get_form(request, object, **kwargs)

        if not request.user.is_superuser:
            form.base_fields["username"].disabled = True
            form.base_fields["email"].disabled = True
            form.base_fields["user_permissions"].disabled = True


        return form
