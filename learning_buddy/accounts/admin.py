from django.contrib import admin
from django.contrib.auth.models import User as AuthUser
from .models import User
from django.contrib.auth.admin import UserAdmin

admin.site.unregister(AuthUser)


@admin.register(User)
class UserAccountsAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email"]
    search_fields = ["email__startswith"]

@admin.register(AuthUser)
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
