from django.contrib import admin
from .models import Emission


@admin.register(Emission)
class EmissionAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'description']
    summernote_fields = ('description',)