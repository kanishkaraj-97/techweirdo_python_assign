# Generated by Django 3.2.6 on 2021-08-27 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mits_app', '0004_medicineintakeschedule_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicineintakeschedule',
            old_name='from_date',
            new_name='intake_date',
        ),
        migrations.RenameField(
            model_name='medicineintakeschedule',
            old_name='times_a_day',
            new_name='no_of_times_a_day',
        ),
        migrations.RemoveField(
            model_name='medicineintakeschedule',
            name='day_in_week',
        ),
        migrations.RemoveField(
            model_name='medicineintakeschedule',
            name='quantity_per_time',
        ),
        migrations.RemoveField(
            model_name='medicineintakeschedule',
            name='to_date',
        ),
        migrations.AddField(
            model_name='medicineintakeschedule',
            name='quantity',
            field=models.CharField(default='1', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='medicineintakeschedule',
            name='intake_time',
            field=models.CharField(choices=[('morning', 'morning'), ('night', 'night'), ('afternoon', 'afternoon')], max_length=20),
        ),
        migrations.AlterField(
            model_name='medicineintakeschedule',
            name='status',
            field=models.CharField(choices=[('taken', 'taken'), ('not_taken', 'not_taken')], default='not_taken', max_length=20, null=True),
        ),
    ]