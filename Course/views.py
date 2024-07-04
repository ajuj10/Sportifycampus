from django.shortcuts import render,redirect
from CourseAdmin.models import *
from Course.models import *
from django.conf import settings
from django.core.mail import send_mail
import random
import jinja2
import pdfkit
import os

'''path_to_wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)
html_path = 'Register.html'
output_pdf = 'out.pdf'''

try:
    pdfkit.from_file(html_path, output_pdf, configuration=config)
    print(f"PDF generated successfully: {output_pdf}")
except Exception as e:
    print(f"Error generating PDF: {e}")

#pdfkit.from_file('Register.html', 'out.pdf', configuration=config)
#pdfkit.from_file('Register.html', 'out.pdf') 
#Create your views here.

def ViewCourses(request):
    courses = tbl_newevent.objects.all()
    return render(request, "Course/ViewCourses.html", {'data': courses})

def view_selected(request,id):
    course = tbl_newevent.objects.filter(id=id)
    return render(request, "Course/Viewselected.html", {'data': course})

def Apply(request, id):
    course = tbl_newevent.objects.get(id=id)
    if request.method == "POST":
        username = request.POST.get("txtname")
        useraddress = request.POST.get("txtaddress")
        userqualification = request.POST.get("txtqualification")
        email = request.POST.get("txtemail")
        tbl_userapply.objects.create(u_name=username,u_qualification=userqualification,u_address=useraddress,u_email=email,course_id=course)
        return redirect("Course:ViewCourses")
    return render(request,"Course/Register.html",{'course': course})

def Booknow(request, id):
    course = tbl_newevent.objects.get(id=id)
    if request.method == "POST":
        username = request.POST.get("txtname")
        useraddress = request.POST.get("txtaddress")
        userqualification = request.POST.get("txtqualification")
        email = request.POST.get("txtemail")
        tbl_userapply.objects.create(u_name=username,u_qualification=userqualification,u_address=useraddress,u_email=email,course_id=course)
        return redirect("Course:ViewCourses")
    return render(request,"Course/bookNow.html",{'course': course})


def payment(request):
    if request.method == "POST":
        # Handle payment form submission
        # For example, process payment logic here
        # After processing payment, redirect with a success message
        return redirect("Course:payment", Msg="PAYMENT SUCCESSFUL")
    else:
        return render(request, "Course/payment.html")

def emailforotp(request):
    if request.method=="POST":
        otp=(random.randint(100000,999999))
        request.session["otp"]=otp
        request.session["femail"]=request.POST.get('txtemail')
        send_mail(
            'Respected Sir/Madam '+" ",#subject
            "Your Otp is"+str(otp),#body
            settings.EMAIL_HOST_USER,
            [request.POST.get('txtemail')],
        )
        return redirect('Course:Validateotp')
    else:
        return render(request,"Course/emailforotp.html")

def otpvalidate(request):
    if request.method=="POST":
        otp=int(request.POST.get("txt_otp"))
        ce=request.session["otp"]
        print(otp,ce)
        if otp==ce:
            del request.session["otp"]
            return redirect("Course:ViewCourses",{'Msg': "PAYMENT SUCCESFULL"})
    return render(request,"Course/Validateotp.html")

def ViewBill(request):
       userdata = tbl_userapply.objects.all()
       return render(request,"Course/viewbill.html",{"userdata":userdata})
       #return render(request,"Course/viewbill.html")


    #'''userdata = tbl_userapply.objects.get(course_id=id)
    #return render(request,"Course/viewbill.html",{"userdata":userdata})'''