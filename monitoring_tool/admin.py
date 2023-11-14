from django.contrib import admin
from .models import Emission, EmissionCheck


@admin.register(Emission)
class EmissionAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on', 'last_checked')
    search_fields = ['title', 'description']
    summernote_fields = ('description',)


@admin.register(EmissionCheck)
class EmissionCheckAdmin(admin.ModelAdmin):

    list_display = ('id','title', 'date_checked', 'status',
                    'comments', 'checked_by')
    list_filter = ('checked_by', 'status')
    search_fields = ['checked_by', 'title']

