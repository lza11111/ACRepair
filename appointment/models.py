import uuid
from django.db import models
from django.utils import timezone

from services.models import Service
from appointment.constants import APPOINTMENT_TYPE_CHOICE, AppointmentType

# Create your models here.
class Appointment(models.Model):
    id              = models.UUIDField      (primary_key=True, default=uuid.uuid4, editable=False)
    service_type    = models.ForeignKey     (Service, verbose_name='服务类型', on_delete=models.SET_DEFAULT, null=False, default=1)
    phone_number    = models.CharField      (verbose_name='联系方式', max_length=255, null=False)
    address         = models.CharField      (verbose_name='地址', max_length=511, null=False)
    required_time   = models.DateTimeField  (verbose_name='预约时间', )
    real_time       = models.DateTimeField  (verbose_name='上门时间', )
    status          = models.IntegerField   (verbose_name='预约状态', choices=APPOINTMENT_TYPE_CHOICE, default=AppointmentType.STARTED)
    
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(default=timezone.now, db_index=True, editable=False)

    def __str__(self):
        return '%s %s %s' % (self.service_type.name, self.phone_number, self.status)
    
    class Meta:
        ordering = ['status', 'required_time', ]