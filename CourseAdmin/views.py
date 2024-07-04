from django.shortcuts import render,redirect
from CourseAdmin.models import *
# Create your views here.
def courseInsertSelect(request):
    data=tbl_newevent.objects.all()
    if request.method=="POST":
        coursename=request.POST.get("txtcoursename")
        courseduration=request.POST.get("txtduration")
        courseprice=request.POST.get("txtprice")
        coursedetails=request.POST.get("txtdetails")
        coursestartdate=request.POST.get("txtstartdate")
        coursenddate=request.POST.get("txtenddate")
        tbl_newevent.objects.create(course_name=coursename,course_duration=courseduration,course_price=courseprice,course_details=coursedetails,course_startdate=coursestartdate,course_enddate=coursenddate)
        return render(request,"CourseAdmin/Addcourses.html",{'data':data})
    else:
     return render(request,"CourseAdmin/Addcourses.html",{'data':data})
    
def coursedelete(request, id):
     tbl_newevent.objects.get(id=id).delete()     
     return redirect("CourseAdmin:Addcourses")   