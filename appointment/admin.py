from django.contrib import admin

from appointment.models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number', 'status')
    list_filter = ('status',)
    search_fields = ('phone_number', )
    ordering = ('-id', )

admin.site.register(Appointment, AppointmentAdmin)