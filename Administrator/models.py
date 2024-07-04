from django.db import models 

# Create your models here.
''''class tbl_district(models.Model):
    district_name = models.CharField(max_length=30)

class tbl_sem(models.Model):
    sem_no = models.CharField(max_length=50)

class tbl_place(models.Model):
    place_name = models.CharField(max_length=30)
    district = models.ForeignKey(tbl_district,on_delete=models.CASCADE)

class tbl_category(models.Model):
    category_name = models.CharField(max_length=50)

class tbl_subcategory(models.Model):
    subcategory_name=models.CharField(max_length=30)
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)  


class tbl_adminreg(models.Model):
    a_name=models.CharField(max_length=30)
    a_contact=models.CharField(max_length=30)
    a_email=models.CharField(max_length=30)
    a_password=models.CharField(max_length=30)

class tbl_sub(models.Model):
    sub_name = models.CharField(max_length=30)



class tbl_coordinator(models.Model):
    coordinator_name=models.CharField(max_length=50)
    coordinator_gender=models.CharField(max_length=50)
    coordinator_contact=models.CharField(max_length=50)
    coordinator_email=models.CharField(max_length=50)
    coordinator_address=models.CharField(max_length=500)
    coordinator_password=models.CharField(max_length=50)
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    coordinator_photo = models.FileField(upload_to='Assets/CoordinatorDocs/')
    coordinator_proof = models.FileField(upload_to='Assets/CoordinatorDocs/')
    coordinator_status = models.IntegerField(default="0")
    coordinator_doj=models.DateField(auto_now_add=True)
    
class tbl_dept(models.Model):
    dept_name=models.CharField(max_length=50)'''
    