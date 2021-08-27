from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

# details of medicine
class Medicine(models.Model):
    name = models.CharField(max_length=1024, null=True, blank=True)
    batch_no = models.CharField(max_length=1024, null=True, blank=True)
    mnf_date = models.DateField()
    expire_date = models.DateField()
    type = models.CharField(max_length=20, null=True, blank=True)
    quantity_measurment = models.CharField(max_length=20, null=True, default='piece',choices=(('piece', 'piece'), ('ml', 'ml')))

# details of user
class Users(models.Model):
    first_name = models.CharField(max_length=1024, null=True, blank=True)
    last_name = models.CharField(max_length=1024, null=True, blank=True)
    age = models.IntegerField()
    address = models.CharField(max_length=1024, null=True, blank=True)
    contact = models.CharField(max_length=20, null=True, blank=True)

# Medicine intake schedule
class MedicineIntakeSchedule(models.Model):
    medicine = models.ForeignKey(Medicine, null=False, on_delete=CASCADE)
    user = models.ForeignKey(Users, null=False, on_delete=CASCADE)
    intake_time = models.CharField(max_length=20, choices=(('morning','morning'), ('night','night'), ('afternoon','afternoon')))
    no_of_times_a_day = models.IntegerField()
    intake_date = models.DateField()
    status = models.CharField(max_length=20, null=True, choices=(('taken', 'taken'),('not_taken', 'not_taken')), default='not_taken')
    quantity = models.CharField(max_length=20, null=True, default='1')

