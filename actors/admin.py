from django.contrib import admin
from actors.models import Actor

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_of_birth', 'nationality')
    search_fields = ('name', 'date_of_birth', 'nationality')