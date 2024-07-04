from django.shortcuts import render,redirect
from Guest.models import *
from WebAdmin.models import*


def Login(request):
    if request.method == "POST":
        studentcount = tbl_student.objects.filter(student_email=request.POST.get("txtemail"),student_password=request.POST.get("txtpassword")).count()
        coordinatorcount = tbl_coordinator.objects.filter(coordinator_email=request.POST.get("txtemail"),coordinator_password=request.POST.get("txtpassword")).count()
        admincount = tbl_adminreg.objects.filter(a_email=request.POST.get("txtemail"),a_password=request.POST.get("txtpassword")).count()
        if studentcount > 0:
            user = tbl_student.objects.get(student_email=request.POST.get("txtemail"), student_password=request.POST.get("txtpassword"))
            
            request.session["uid"] = user.id
            print(request.session["uid"])
            request.session["uname"] = user.student_name
            return redirect("Student:myprofile")
        elif coordinatorcount > 0:
          coordinator = tbl_coordinator.objects.get(coordinator_email=request.POST.get("txtemail"),coordinator_password=request.POST.get("txtpassword"))
          request.session["cid"] = coordinator.id
          request.session["cname"] = coordinator.coordinator_name
          return redirect("WebCoordinator:LoadingHomePage")
        elif admincount > 0:
          admin = tbl_adminreg.objects.get(a_email=request.POST.get("txtemail"),a_password=request.POST.get("txtpassword"))
          request.session["aid"] = admin.id
          request.session["aname"] = admin.a_name
          return redirect("WebAdmin:HomePage")
        else:
          return render(request,"WebGuest/Login.html",{"msg":"Invalid Email Or Password"})
    else:
          return render(request,"WebGuest/Login.html")


def StudentRegistration(request):
    district = tbl_district.objects.all()
    dept=tbl_dept.objects.all()
    if request.method=="POST":
        dept= tbl_dept.objects.get(id=request.POST.get('sel_dept'))
        place = tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_student.objects.create(student_address=request.POST.get("txtadd"),student_name=request.POST.get("txtname"),student_gender=request.POST.get("gender"),student_contact=request.POST.get("txtcontact"),student_email=request.POST.get("txtemail"),student_photo=request.FILES.get("fileImage"),student_proof=request.FILES.get("fileProof"),student_password=request.POST.get("txtpwd"),place=place,dept=dept)
        return redirect("WebGuest:StudentRegistration")
    else:
        return render(request,"WebGuest/StudentRegistration.html",{"districtdata":district,"deptdata":dept})
    

def ajaxplace(request):
    dis = tbl_district.objects.get(id=request.GET.get("did"))
    place = tbl_place.objects.filter(district=dis)
    return render(request,"WebGuest/AjaxPlace.html",{"placedata":place})



def index(request):
    if request.method == "POST":
        return render(request, "WebGuest/index.html")
    else:
        return render(request, "WebGuest/index.html")
