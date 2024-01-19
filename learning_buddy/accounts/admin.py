from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

@admin.register(User)
class NewUser(UserAdmin):
    readonly_fields = [
        "date_joined",
    ]
    
    # disable staff privelleges to edit username
    def get_form(self, request, object=None, **kwargs):
        form = super().get_form(request, object, **kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            form.base_fields["username"].disabled = True
            form.base_fields["email"].disabled = True
            form.base_fields["user_permissions"].disabled = True
        
        return form
