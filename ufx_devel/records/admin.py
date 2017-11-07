from django.contrib import admin
from .models import Record, BlackList

from django.utils.html import format_html

# Register your models here.

class BlackListAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'is_blocked')
    search_fields = ('phone_number',)
    list_editable = ('is_blocked',)
    list_filter = ('is_blocked',)
    list_per_page = 50




class RecordAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'call_date', 'upload_to', 'call_type', 'url_link')
    search_fields = ('phone_number', 'call_date')
    list_filter = ('phone_number','call_date', 'call_type')
    list_per_page = 50

    def url_link(self, obj):
        ftp_url = "ftp://yurika.gransy.com/media"
        return format_html("<a href='{ftp}/{url}' target='_blank'>{url}</a>", ftp=ftp_url, url=obj.upload_to)


admin.site.register(Record, RecordAdmin)
admin.site.register(BlackList, BlackListAdmin)
