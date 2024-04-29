from django.db import models
# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    pwd = models.CharField(max_length=10)
    conf_pwd = models.CharField(max_length = 10)
    class Meta:
        db_table = "user"

class Classes(models.Model):
    student_id = models.IntegerField(max_length=10)
    student_name = models.CharField(max_length=20)
    attendance = models.CharField(max_length=50)
    class Meta:
        db_table = "Classes"
