from django.db import models
# Create your models here.
class tbl_newevent(models.Model):  
      course_name=models.CharField(max_length=30) 
      course_duration=models.CharField(max_length=30)    
      course_price=models.CharField(max_length=30)    
      course_details=models.CharField(max_length=300) 
      course_startdate=models.DateField()
      course_enddate=models.DateField()
      enrollment_status=models.IntegerField(default="0") 