from django.db import models
from WebGuest.models import *
from Student.models import*
from Coordinator.models import*
from datetime import date

#Create your models here.

# Feedback and complaint

class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=500)
    complaint_details=models.CharField(max_length=500)
    complaint_postdate=models.DateField(auto_now_add=True)
    complaint_reply=models.CharField(max_length=500)
    complaint_replydate=models.DateField(null=True)
    complaint_status = models.IntegerField(default="0")
    student = models.ForeignKey(tbl_student,on_delete=models.CASCADE,null=True)
    coordinator=models.ForeignKey(tbl_coordinator, on_delete=models.CASCADE,null=True)
    

class tbl_feedback(models.Model):
    feedback_subject=models.CharField(max_length=500)
    feedback_details=models.CharField(max_length=500)
    feedback_postdate=models.DateField(auto_now_add=True)
    feedback_status = models.IntegerField(default="0")
    student = models.ForeignKey(tbl_student,on_delete=models.CASCADE)


class tbl_participants(models.Model):
    student_id=models.ForeignKey(tbl_student,on_delete=models.CASCADE,null=True)
    event_id=models.ForeignKey(tbl_newevent, on_delete=models.CASCADE,null=True)
    participant_date=models.DateField(auto_now_add=True)
    participant_status=models.IntegerField(default="0")
  
class tbl_teammates(models.Model):
    participant_id=models.ForeignKey(tbl_participants, on_delete=models.CASCADE,null=True)
    teammate_name=models.CharField(max_length=500)
    

