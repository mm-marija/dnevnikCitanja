from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from .models import Zanr,Knjiga, Citat

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username','firstName', 'lastName', 'email']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Zanr)
admin.site.register(Knjiga)
admin.site.register(Citat)
