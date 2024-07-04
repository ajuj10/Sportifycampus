from django.db import models
from Student.models import *
# Create your models here.
class tbl_results(models.Model):
    result_date=models.DateField(auto_now_add=True)
    participant_id=models.ForeignKey(tbl_participants, on_delete=models.CASCADE,null=True)
    department=models.ForeignKey(tbl_dept, on_delete=models.CASCADE,null=True)
    result_score=models.IntegerField()
    result_position=models.IntegerField()
    result_status=models.IntegerField(default="0")