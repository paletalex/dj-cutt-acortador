from django.contrib import admin
from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ['url', 'key']

admin.site.register(Link, LinkAdmin)