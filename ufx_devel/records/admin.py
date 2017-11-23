from django.contrib import admin
from .models import Record, BlackList
from django.utils.html import format_html
from decouple import config

class BlackListAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'is_blocked')
    search_fields = ('phone_number',)
    list_editable = ('is_blocked',)
    list_filter = ('is_blocked',)
    list_per_page = 10

class RecordAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'call_date', 'call_type', 'url_link', 'employee', 'is_recorded')
    search_fields = ('phone_number', 'call_date')
    list_filter = ('employee','call_date', 'call_type', 'is_recorded')
    list_per_page = 50

    def url_link(self, obj):
        ftp_url = config('FTP_URL_LINK')
        return format_html("<a href='{ftp}/{url}' target='_blank'>{url}</a>", ftp=ftp_url, url=obj.upload_to)

admin.site.register(Record, RecordAdmin)
admin.site.register(BlackList, BlackListAdmin)
