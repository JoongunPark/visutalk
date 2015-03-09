from django.db import models

class UserKakaoAuth(models.Model):
    id = models.AutoField(primary_key=True, max_length=11)
    provider = models.CharField(max_length=32)
    uid = models.CharField(max_length=255,unique=True)
    user_id = models.IntegerField(max_length=11)
    extra_data = models.CharField(max_length=150)

