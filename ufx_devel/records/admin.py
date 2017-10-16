from django.contrib import admin
from .models import Record, BlackList
# Register your models here.

class BlackListAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'is_blocked')
    search_fields = ('phone_number',)
    list_editable = ('is_blocked',)
    list_filter = ('is_blocked',)
    list_per_page = 50




class RecordAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'call_date', 'upload_to', 'call_type')
    search_fields = ('phone_number', 'call_date')
    list_filter = ('phone_number','call_date', 'call_type')
    list_per_page = 50





admin.site.register(Record, RecordAdmin)
admin.site.register(BlackList, BlackListAdmin)
