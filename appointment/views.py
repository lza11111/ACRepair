from rest_framework import viewsets

from appointment.models import Appointment
from appointment.serializer import (
    AppointmentSerializerForClient,
    AppointmentSerializerForAdmin,
)

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return AppointmentSerializerForAdmin
        
        return AppointmentSerializerForClient