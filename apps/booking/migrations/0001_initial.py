# Generated by Django 4.2.3 on 2023-07-20 19:56

from django.db import migrations, models
import simple_history.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('deleted_date', models.DateTimeField(blank=True, null=True, verbose_name='Deleted Date')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('reservation_date', models.DateTimeField(auto_now_add=True, verbose_name='Reservation Date')),
                ('checkin_date', models.DateField(verbose_name='Check-In Date')),
                ('checkout_date', models.DateField(verbose_name='Check-Out Date')),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('PAID', 'Paid'), ('CANCELLED', 'Cancelled')], default='PENDING', max_length=20, verbose_name='Reservation State')),
            ],
            options={
                'verbose_name': 'Reservation',
                'verbose_name_plural': 'Reservations',
                'ordering': ['-reservation_date'],
            },
        ),
        migrations.CreateModel(
            name='HistoricalBooking',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_date', models.DateTimeField(blank=True, editable=False, verbose_name='Created Date')),
                ('modified_date', models.DateTimeField(blank=True, editable=False, verbose_name='Updated Date')),
                ('deleted_date', models.DateTimeField(blank=True, null=True, verbose_name='Deleted Date')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('reservation_date', models.DateTimeField(blank=True, editable=False, verbose_name='Reservation Date')),
                ('checkin_date', models.DateField(verbose_name='Check-In Date')),
                ('checkout_date', models.DateField(verbose_name='Check-Out Date')),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('PAID', 'Paid'), ('CANCELLED', 'Cancelled')], default='PENDING', max_length=20, verbose_name='Reservation State')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical Reservation',
                'verbose_name_plural': 'historical Reservations',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
