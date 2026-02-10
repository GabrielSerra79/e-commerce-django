from django.contrib import admin

from .models import Perfil

class PerfilAdmin(admin.ModelAdmin):
    readonly_fields = ('idade',)

admin.site.register(Perfil, PerfilAdmin)
