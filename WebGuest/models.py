from django.db import models
from WebAdmin.models import *
from Student.models import *
from WebGuest.models import *
# Create your models here.
#table User
class tbl_student(models.Model):
    student_name=models.CharField(max_length=50)
    student_gender=models.CharField(max_length=50)
    student_contact=models.CharField(max_length=50)
    student_email=models.CharField(max_length=50)
    student_address=models.CharField(max_length=500)
    student_password=models.CharField(max_length=50)
    student_photo = models.FileField(upload_to='Assets/StudentDocs/')
    student_proof = models.FileField(upload_to='Assets/StudentDocs/')
    student_status = models.IntegerField(default="0")
    student_doj=models.DateField(auto_now_add=True)
    course = models.ForeignKey(tbl_course,on_delete=models.CASCADE)
    acdemic = models.ForeignKey(tbl_acdemicyear,on_delete=models.CASCADE)
    sem = models.ForeignKey(tbl_sem,on_delete=models.CASCADE)

    