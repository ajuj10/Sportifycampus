from django.db import models

# Create your models here.

class tbl_dept(models.Model):
    dept_name=models.CharField(max_length=50)


class tbl_acdemicyear(models.Model):
    acdemic_year=models.CharField(max_length=50)


class tbl_sem(models.Model):
    sem_no = models.CharField(max_length=50)


class tbl_course(models.Model):
    course_name=models.CharField(max_length=30)
    dept=models.ForeignKey(tbl_dept,on_delete=models.CASCADE)  

class tbl_category(models.Model):
    category_name = models.CharField(max_length=50)

class tbl_subcategory(models.Model):
    subcategory_name=models.CharField(max_length=30)
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)

class tbl_coordinator(models.Model):
    coordinator_name=models.CharField(max_length=50)
    coordinator_gender=models.CharField(max_length=50)
    coordinator_contact=models.CharField(max_length=50)
    coordinator_email=models.CharField(max_length=50)
    coordinator_address=models.CharField(max_length=500)
    coordinator_password=models.CharField(max_length=50)
    coordinator_photo = models.FileField(upload_to='Assets/CoordinatorDocs/')
    coordinator_proof = models.FileField(upload_to='Assets/CoordinatorDocs/')
    coordinator_status = models.IntegerField(default="0")
    coordinator_doj=models.DateField(auto_now_add=True)
   

class tbl_adminreg(models.Model):
    a_name=models.CharField(max_length=30)
    a_contact=models.CharField(max_length=30)
    a_email=models.CharField(max_length=30)
    a_password=models.CharField(max_length=30)

class tbl_newevent(models.Model):  
      e_name=models.CharField(max_length=30) 
      e_gender=models.CharField(max_length=30)    
      category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)
      subcategory=models.ForeignKey(tbl_subcategory,on_delete=models.CASCADE)  
      e_date=models.DateField(auto_now_add=True)
      e_time=models.CharField(max_length=30)
      e_details=models.CharField(max_length=30)
      e_venue=models.CharField(max_length=30)
      e_poster=models.FileField(upload_to='eventphoto/')
      type_name=models.CharField(max_length=30)
      teammate_count=models.CharField(max_length=30)
      coordinator=models.ForeignKey(tbl_coordinator,on_delete=models.CASCADE)
      event_status=models.IntegerField(default="0") 
    

class Notification(models.Model):
    content = models.TextField()
    
class pointstable():
    department=models.CharField(max_length=30)
    total=models.CharField(max_length=30)


