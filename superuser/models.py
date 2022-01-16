from django.db import models

# Create your models here.


class Superuser(models.Model):
    supername = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.supername


class Employee(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length=50)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=20)
    epoints = models.IntegerField(default=00)

    def __str__(self):
        return self.ename
