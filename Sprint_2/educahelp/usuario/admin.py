from django.contrib import admin
from .models import Usuario, Permissoes


# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'nome']


@admin.register(Permissoes)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id']
