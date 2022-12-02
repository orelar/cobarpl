from django.db import models
from django.contrib.auth.models import User
from catatan.models import Catatan


class Course(models.Model):
    course_id = models.AutoField(null=False, primary_key=True)
    course_name = models.TextField(default="")
    user_id = models.TextField(default="")


class Bab(models.Model):
    bab_id = models.AutoField(null=False, primary_key=True)
    bab_name = models.TextField(default="")
    course_id = models.BigIntegerField(null=False, default=0)


