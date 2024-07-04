from django.shortcuts import render,redirect
from WebGuest.models import*
from WebAdmin.models import*
from Student.models import*
from django.conf import settings
from django.core.mail import send_mail
import random

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
          return redirect("WebCoordinator:HomePage")
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
    dept = tbl_dept.objects.all()
    ayear=tbl_acdemicyear.objects.all()
    sem=tbl_sem.objects.all()
    if request.method=="POST":
        ayearID= tbl_acdemicyear.objects.get(id=request.POST.get('selYear'))
        semID = tbl_sem.objects.get(id=request.POST.get('selSem'))
        courseID = tbl_course.objects.get(id=request.POST.get('selCourse'))
        tbl_student.objects.create(student_address=request.POST.get("txtadd"),student_name=request.POST.get("txtname"),student_gender=request.POST.get("gender"),student_contact=request.POST.get("txtcontact"),student_email=request.POST.get("txtemail"),student_photo=request.FILES.get("fileImage"),student_proof=request.FILES.get("fileProof"),student_password=request.POST.get("txtpwd"),acdemic=ayearID,course=courseID,sem=semID)
        return redirect("WebGuest:StudentRegistration")
    else:
        return render(request,"WebGuest/StudentRegistration.html",{"ayear":ayear,"sem":sem,"dept":dept})
    

def ajaxcourse(request):
    dept = tbl_dept.objects.get(id=request.GET.get("did"))
    course = tbl_course.objects.filter(dept=dept)
    return render(request,"WebGuest/AjaxCourse.html",{"course":course})


def notification_view(request):
    notifications = [
        "Notification 1: Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "Notification 2: Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "Notification 3: Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
    ]
    return render(request, 'AddNotifications.html', {'notifications': notifications})


def index(request):
    notify=Notification.objects.all()
    return render(request, "WebGuest/index.html",{'notify':notify})

def ForgotPass(request):
    if request.method=="POST":
        otp=(random.randint(100000,999999))
        request.session["otp"]=otp
        request.session["femail"]=request.POST.get('txt_email')
        send_mail(
            'Respected Sir/Madam '+" ",#subject
            "Your Otp is"+str(otp),#body
            settings.EMAIL_HOST_USER,
            [request.POST.get('txt_email')],
        )
        return redirect('WebGuest:ValidateOTP')
    else:
        return render(request,"WebGuest/ForgotPass.html")
    
def ValidateOTP(request):
    if request.method=="POST":
        otp=int(request.POST.get("txt_otp"))
        ce=request.session["otp"]
        print(otp,ce)
        if otp==ce:
            del request.session["otp"]
            return redirect("WebGuest:CreatePass")
    return render(request,"WebGuest/validateOTP.html")

def CreatePass(request):
    if request.method=="POST":
        if request.POST.get("txt_pass")==request.POST.get("txt_confirm"):
            usercount=tbl_student.objects.filter(student_email=request.session["femail"]).count()
            coordinatorcount=tbl_coordinator.objects.filter(coordinator_email=request.session["femail"]).count()
            admincount=tbl_adminreg.objects.filter(a_email=request.session["femail"]).count()
            if usercount>0:
                user=tbl_student.objects.get(student_email=request.session["femail"])
                user.user_password=request.POST.get("txt_pass")
                user.save()
                return redirect("WebGuest:Login")
            elif coordinatorcount>0:
                coordinator=tbl_coordinator.objects.get(coordinator_email=request.session["femail"])
                coordinator.coordinator_password=request.POST.get("txt_pass")
                coordinator.save()
                return redirect("WebGuest:Login")
            elif admincount>0:
                  admin=tbl_adminreg.objects.get(a_email=request.session["femail"])
                  admin.a_password=request.POST.get("txt_pass")
                  admin.save()
                  return redirect("WebGuest:Login")
        else:
            return render(request,"WebGuest/createpassword.html",{'msg':"Passwords not same"})
    else:
        return render(request,"WebGuest/createpassword.html")
