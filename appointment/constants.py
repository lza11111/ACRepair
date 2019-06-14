
class AppointmentType:
    STARTED = 0
    CONIRMED = 1
    INPROGRESS = 50
    COMPLETED = 100
    CANCELED = 901
    ILLEGAL = 902


APPOINTMENT_TYPE_CHOICE = (
    (AppointmentType.STARTED, '已预约'),
    (AppointmentType.CONIRMED, '已确认'),
    (AppointmentType.INPROGRESS, '维修中'),
    (AppointmentType.COMPLETED, '已完成'),
    (AppointmentType.CANCELED, '用户取消'),
    (AppointmentType.ILLEGAL, '商户取消'),
)
