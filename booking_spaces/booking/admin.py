from django.contrib import admin

from booking.models import Schedule, ParkingSpace


class ParkingSpaceAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'slug',
    )
    search_fields = ('title',)
    list_editable = ('title',)
    empty_value_display = '-empty-'


class ScheduleAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'space',
        'reserving_date',
        'is_reserved',
        'is_past',
        'booking_user',
    )
    search_fields = ('space', 'reserving_date', 'is_reserved',)
    list_filter = ('reserving_date',)
    list_editable = (
        'space',
        'reserving_date',
        'is_reserved',
        'booking_user',
    )
    empty_value_display = '-empty-'


admin.site.register(ParkingSpace, ParkingSpaceAdmin)
admin.site.register(Schedule, ScheduleAdmin)
