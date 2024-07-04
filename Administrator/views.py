from django.shortcuts import render,redirect
from Administrator.models import *
from Guest.models import*
from Student.models import*
#Create your views here.
def LoadingHomePage(request):
    return render (request,"Administrator/HomePage.html")

#Event type and event name
def Eventtype(request):
    event=tbl_eventype.objects.all()
    if request.method=="POST":
        event=request.POST.get("txtevent")
        tbl_eventype.objects.create(event_name=event)
        return redirect("webadmin:Eventtype")
    else:
        return render (request,"Administrator/Eventtype.html",{"event":event})
   
def delete_event(request,id):
    tbl_eventype.objects.get(id=id).delete()
    return redirect("webadmin:Eventtype")
def edit_event(request,id):
    eventedit=tbl_eventype.objects.get(id=id)
    if request.method=="POST":
        eventedit.event_name=request.POST.get("txtevent")
        eventedit.save()
        return redirect("webadmin:Eventtype")
    else:
        return render (request,"Administrator/Eventtype.html",{"eventedit":eventedit})
    
#Adminregistration
def Adminregistration(request):
    admin=tbl_adminreg.objects.all
    if request.method=="POST":
        admin_name=request.POST.get("txtname")
        admin_contact=request.POST.get("txtcontact")
        admin_email=request.POST.get("txtemail")
        admin_password=request.POST.get("txtpass")
        tbl_adminreg.objects.create(a_name=admin_name,a_contact=admin_contact,a_email=admin_email,a_password=admin_password)
        
        return redirect("webadmin:Adminregistration")
    else:
        return render (request,"Administrator/AdminRegistration.html",{"adminregdata":admin})
def delete_admin(request,id):
  tbl_adminreg.objects.get(id=id).delete()
  return redirect("webadmin:Adminregistration") 
 
def edit_admin(request,id):
    adminedit=tbl_adminreg.objects.get(id=id)
    if request.method=="POST":
        adminedit.a_name=request.POST.get("txtname")
        adminedit.a_contact=request.POST.get("txtcontact")
        adminedit.a_email=request.POST.get("txtemail")
        adminedit.a_password=request.POST.get("txtpass")
        adminedit.save()
        return redirect("webadmin:Adminregistration")
    else:
        return render (request,"Administrator/AdminRegistration.html",{"adminedit":adminedit})
    



#Category
''''def category(request):
     category= tbl_category.objects.all()
     if request.method=="POST":
        category=request.POST.get("txtcategory")
        tbl_category.objects.create(category_name=category)
        return redirect("webadmin:category")
     else:
        return render (request,"Administrator/category.html",{"category":category})
    
def delete_category(request,did):
    tbl_category.objects.get(id=did).delete()
    return redirect("webadmin:category")
def edit_category(request,eid):
    editcategory=tbl_category.objects.get(id=eid)
    if request.method=="POST":
        editcategory.category_name=request.POST.get("txtcategory")
        editcategory.save()
        return redirect("webadmin:category")
    else:
        return render(request,"Administrator/category.html",{"editcategory":editcategory})
    


#Subcategory
def subcategory(request):
     cat= tbl_category.objects.all()
     sub_cat=tbl_subcategory.objects.all()
     if request.method=="POST":
        sub_cat=request.POST.get("txtsubcategory")
        cate= tbl_category.objects.get(id=request.POST.get("sel_category"))
        tbl_subcategory.objects.create(subcategory_name=sub_cat,category=cate)
        return redirect ("webadmin:subcategory")
     else:
        return render (request,"Administrator/subcategory.html",{"category":cat,"subcategory":sub_cat})
def delete_subcategory(request,id):
    tbl_subcategory.objects.get(id=id).delete()
    return redirect("webadmin:subcategory")
def edit_subcategory(request,id):
    cat=tbl_category.objects.all()
    editsubcat=tbl_subcategory.objects.get(id=id)
    if request.method=="POST":
      editsubcat.subcategory_name=request.POST.get("txtsubcategory")
      cat=tbl_subcategory.objects.get(id=request.POST.get("sel_category"))
      editsubcat.category=cat
      editsubcat.save()
      return redirect("webadmin:subcategory")
    else:
        return render(request,"Administrator/subcategory.html",{"cat":cat,"subcat":editsubcat})   '''
    

    
#district
def district(request):
      dis = tbl_district.objects.all()
      if request.method=="POST":
        dis=request.POST.get("txtdistrict")
        tbl_district.objects.create(district_name=dis)
        return redirect("webadmin:District")
      else:
        return render (request,"Administrator/District.html",{"district":district}) 

def delete_district(request,id):  
    tbl_district.objects.get(id=id).delete()
    return redirect("webadmin:District")

def edit_district(request,id):
    dis = tbl_district.objects.get(id=id)
    if request.method == "POST":
        dis.district_name = request.POST.get("txtdistrict")
        dis.save()
        return redirect("webadmin:District")
    else:
        return render(request,"Administrator/District.html",{"edit":dis})

#place 
def place(request):
    dis = tbl_district.objects.all()
    plc=tbl_place.objects.all()
    if request.method=="POST":
        plc=request.POST.get("txtplace")
        dis = tbl_district.objects.get(id=request.POST.get("sel_district"))
        tbl_place.objects.create(place_name=plc,district=dis)
        return redirect("webadmin:Place")
    else:
        return render (request,"Administrator/Place.html",{"district":dis,"plc":plc})
    
#views for semester
def semester(request):
    sem = tbl_sem.objects.all()
    if request.method == "POST":
        sem= request.POST.get("txtsem")
        tbl_sem.objects.create(sem_no=sem)
        return redirect("webadmin:Semester")
    else:
        return render(request, "Administrator/Semester.html", {"semester": sem})
def delete_sem(request,id):
    tbl_sem.objects.get(id=id).delete()
    return redirect("webadmin:Semester")
def edit_sem(request,id):
    semedit=tbl_sem.objects.get(id=id)
    if request.method=="POST":
        semedit.sem_no=request.POST.get("txtsem")
        semedit.save()
        return redirect("webadmin:Semester")
    else:
        return render(request,"Administrator/Semester.html",{"semedit":semedit})


#subject
def subject(request):
    sub = tbl_sub.objects.all()
    if request.method=="POST":
        sub=request.POST.get("txtsub")
        tbl_sub.objects.create(sub_name=sub)
        return redirect("webadmin:Subject")
    else:
        return render(request,"Administrator/Subject.html",{"subject":sub})
def delete_sub(request,id):
    tbl_sub.objects.get(id=id).delete()
    return redirect("webadmin:Subject")
def edit_sub(request,id):
    subedit=tbl_sub.objects.get(id=id)
    if request.method=="POST":
        subedit.sub=request.POST.get("txtsub")
        subedit.save()
        return redirect("webadmin:Subject")
    else:
        return render(request,"Administrator/Subject.html",{"subedit":subedit})
    
#admin views
def admin(request):
    if request.method == "POST":
        return render(request, "Administrator/admin.html")
    else:
        return render(request, "Administrator/admin.html")

def editprofile(request):
    userdata=tbl_adminreg.objects.get(id=request.session["uid"])
    if request.method=="POST":
     userdata.a_name=request.POST.get('txtname')
     userdata.a_contact=request.POST.get('txtcontact')
     userdata.a_email=request.POST.get('txtemail')
     userdata.save()
     return render(request,"Student/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"Student/EditProfile.html",{'userdata':userdata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_adminreg.objects.filter(id=request.session["uid"],student_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                userdata=tbl_student.objects.get(id=request.session["uid"],student_password=request.POST.get('txtcurpass'))
                userdata.student_password=request.POST.get('txtnewpass')
                userdata.save()
                return render(request,"Student/Userchangepassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"Student/Userchangepassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"Student/UserChangepassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"Student/UserChangepassword.html")


#Add coordinator

def CoOrdinatorRegistration(request):
    district = tbl_district.objects.all()
    if request.method=="POST":
        place = tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_coordinator.objects.create(coordinator_address=request.POST.get("txtadd"),coordinator_name=request.POST.get("txtname"),coordinator_gender=request.POST.get("gender"),coordinator_contact=request.POST.get("txtcontact"),coordinator_email=request.POST.get("txtemail"),coordinator_photo=request.FILES.get("fileImage"),coordinator_proof=request.FILES.get("fileProof"),coordinator_password=request.POST.get("txtpwd"),place=place)
        return redirect("webadmin:CoOrdinatorRegistration")
    else:
        return render(request,"Administrator/CoOrdinatorRegistration.html",{"districtdata":district})
    

def ajaxplace(request):
    dis = tbl_district.objects.get(id=request.GET.get("did"))
    place = tbl_place.objects.filter(district=dis)
    return render(request,"Administrator/AjaxPlace.html",{"placedata":place})


def CordinatorListNew(request):
    userdata = tbl_coordinator.objects.filter(coordinator_status=0)
    return render(request,"Administrator/CoordinatorListNew.html",{"userdata":userdata})

def acceptcordinator(request,aid):
    user = tbl_coordinator.objects.get(id=aid)
    user.coordinator_status = 1
    user.save()
    return redirect("Webadmin:LoadingHomePage")

def rejectcordinator(request,rid):
    user = tbl_coordinator.objects.get(id=rid)
    user.coordinator_status = 2
    user.save()
    return redirect("webadmin:LoadingHomePage")

def CordinatorListAccepted(request):
    userdata = tbl_coordinator.objects.filter(coordinator_status=1)
    return render(request,"webadmin/CoordinatorListAccepted.html",{"userdata":userdata})

def CordinatorListRejected(request):
    userdata = tbl_coordinator.objects.filter(coordinator_status=2)
    return render(request,"Administrator/CoordinatorListRejected.html",{"userdata":userdata})



#Student list view,accept,reject
def studentListNew(request):
    userdata = tbl_student.objects.filter(student_status=0)
    return render(request,"Administrator/StudentListNew.html",{"userdata":userdata})

def acceptstudent(request,aid):
    user = tbl_student.objects.get(id=aid)
    user.student_status = 1
    user.save()
    return redirect("webadmin:LoadingHomePage")

def rejectstudent(request,rid):
    user = tbl_student.objects.get(id=rid)
    user.student_status = 2
    user.save()
    return redirect("webadmin:LoadingHomePage")

def StudentListAccepted(request):
    userdata = tbl_student.objects.filter(student_status=1)
    return render(request,"Administrator/StudentListAccepted.html",{"userdata":userdata})

def studentListRejected(request):
    userdata = tbl_student.objects.filter(student_status=2)
    return render(request,"Administrator/StudentListRejected.html",{"userdata":userdata})

#complaint reply,view


'''def ComplaintReply(request,cid):
    complaint = tbl_complaint.objects.get(id=cid)
    if request.method=="POST":
        complaint.complaint_replydate = date.today()
        complaint.complaint_reply=request.POST.get('txtreply')
        complaint.complaint_status=1
        complaint.save()
        return redirect("webadmin:ComplaintReply")
    else:
        return render(request,"Administrator/ComplaintReply.html",{'complaint':complaint})
    
def complaintview(request):
    data=tbl_complaint.objects.filter(complaint_status=0)
    return render(request,"Administrator/ComplaintView.html",{'data':data})'''

def feedbackSelect(request):
    data=tbl_feedback.objects.all()
    return render(request,"Administrator/ViewFeedbacklList.html",{'data':data})

def feedbackDelete(request,did):
    tbl_feedback.objects.get(id=did).delete()
    return redirect("webadmin:ViewFeedbacklList")

#department
def department(request):
      dept = tbl_dept.objects.all()
      if request.method=="POST":
        dept=request.POST.get("txtdepartment")
        tbl_dept.objects.create(dept_name=dept)
        return redirect("webadmin:department")
      else:
        return render (request,"Administrator/Department.html",{"department":dept}) 

def delete_department(request,id):  
    tbl_dept.objects.get(id=id).delete()
    return redirect("webadmin:department")

def edit_department(request,id):
    dept = tbl_dept.objects.get(id=id)
    if request.method == "POST":
        dept.dept_name = request.POST.get("txtdepartment")
        dept.save()
        return redirect("webadmin:department")
    else:
        return render(request,"Administrator/Department.html",{"edit":dept})