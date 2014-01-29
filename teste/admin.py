from django.contrib import admin
from teste.models import Jogador, Estrategia

# Register your models here.
admin.site.register(Jogador, admin.ModelAdmin)
admin.site.register(Estrategia, admin.ModelAdmin)