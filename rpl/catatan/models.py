from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Catatan(models.Model):
    uploader_id = models.BigIntegerField(null=False)
    title = models.CharField(default="Untitled",max_length=100, null=True)

    @property
    def uploader(self):
        user = User.objects.get(id=self.uploader_id)
        if user != None:
            return user.username
        return "Deleted account"
