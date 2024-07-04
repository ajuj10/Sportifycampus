from django.db import models
from Administrator.models import *
from Student.models import *
from Guest.models import*

# Create your models here.
#table User
'''class tbl_student(models.Model):
    student_name=models.CharField(max_length=50)
    student_gender=models.CharField(max_length=50)
    student_contact=models.CharField(max_length=50)
    student_email=models.CharField(max_length=50)
    student_address=models.CharField(max_length=500)
    student_password=models.CharField(max_length=50)
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    student_photo = models.FileField(upload_to='Assets/StudentDocs/')
    student_proof = models.FileField(upload_to='Assets/StudentDocs/')
    student_status = models.IntegerField(default="0")
    student_doj=models.DateField(auto_now_add=True)
    dept = models.ForeignKey(tbl_dept, on_delete=models.CASCADE)'''
