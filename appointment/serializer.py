from rest_framework import serializers

from appointment.models import Appointment

class AppointmentSerializerForClient(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        exclude = (
            'created_at',
            'updated_at',
        )
        read_only_fields = ('real_time',)

class AppointmentSerializerForAdmin(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        exclude = (
            'created_at',
            'updated_at',
        )
        read_only_fields = ('required_time',)