from django.db import models
from django.contrib.auth.models import User
from catatan.models import Catatan
class Bab(models.Model):
    bab_name = models.TextField(default="")
    forum_id = models.BigIntegerField(null=False)
    list_catatan = models.ForeignKey(Catatan,on_delete=models.CASCADE)
class Course(models.Model):
    # user_course_id = models.BigIntegerField(null=False)
    course_id = models.BigIntegerField(null=False)
    course_name = models.TextField(default="")
    list_bab = models.ForeignKey(Bab,on_delete=models.CASCADE)
class DaftarCourse(models.Model):
    list_course = models.ForeignKey(Course,on_delete=models.CASCADE)



    # @property
    # def user_course(self):
    #     user = User.objects.get(id=self.course_id)
    #     if user != None:
    #         return user.username
    #     return "Deleted account"




