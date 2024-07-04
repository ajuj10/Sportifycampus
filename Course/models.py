from django.db import models
from CourseAdmin .models import *
# Create your models here.
class tbl_userapply(models.Model):  
      u_name=models.CharField(max_length=30) 
      u_address=models.CharField(max_length=30)    
      u_qualification=models.CharField(max_length=30)    
      u_email=models.CharField(max_length=30) 
      course_id=models.ForeignKey(tbl_newevent, on_delete=models.CASCADE,null=True)
      application_status=models.IntegerField(default="0") 

