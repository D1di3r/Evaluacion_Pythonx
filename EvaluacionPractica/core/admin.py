from django.contrib import admin
from .models import GamePosition, player, team,instructor, player



#admin.site.register(team)
#admin.site.register(player)

@admin.register(team)
class teamAdmin(admin.ModelAdmin):
    list_display= ["name", "Bandera", "Escudo"]
    search_fields=["name"]

@admin.register(player)
class teamAdmin(admin.ModelAdmin):
    list_display= ["name", "lastname", "Foto","birthdate","position","numTshirt","titled","teamp"]
    search_fields=["name","lastname"]
    list_filter =["teamp"] 

@admin.register(instructor)
class instAdmin(admin.ModelAdmin):
    list_display= ["name", "lastname","nationality"]
    search_fields=["name","lastname"]

@admin.register(GamePosition)
class gameAdmin(admin.ModelAdmin):
    list_display= ["name"]
    search_fields=["name"]
        

