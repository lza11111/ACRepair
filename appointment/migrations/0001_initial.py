# Generated by Django 2.2.1 on 2019-06-14 02:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('phone_number', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=511)),
                ('required_time', models.DateTimeField()),
                ('real_time', models.DateTimeField()),
                ('status', models.IntegerField(choices=[(0, '已预约'), (1, '已确认'), (50, '维修中'), (100, '已完成'), (901, '用户取消'), (902, '商户取消')], default=0, verbose_name='预约状态')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('service_type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='services.Service')),
            ],
            options={
                'ordering': ['status', 'required_time'],
            },
        ),
    ]
