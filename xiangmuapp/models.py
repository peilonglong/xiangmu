from django.contrib.auth.models import AbstractUser
from django.db import models
# from db.base_model import BaseModel
# Create your models here.
class User(AbstractUser):
    #用户模型
    class Meta:
        db_table='db_user'
        verbose_name='用户'
        verbose_name_plural=verbose_name




