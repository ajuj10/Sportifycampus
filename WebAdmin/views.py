from django.shortcuts import render,redirect
from Student.models import*
from WebGuest.models import *
from WebCoordinator.models import*
from WebAdmin.models import *
# Create your views here.

def HomePage(request):
    return render (request,"WebAdmin/HomePage.html")

def department(request):
      dept = tbl_dept.objects.all()
      if request.method=="POST":
        dept=request.POST.get("txtdepartment")
        tbl_dept.objects.create(dept_name=dept)
        return redirect("WebAdmin:department")
      else:
        return render (request,"WebAdmin/Department.html",{"department":dept}) 

def delete_department(request,id):  
    tbl_dept.objects.get(id=id).delete()
    return redirect("WebAdmin:department")

def edit_department(request,id):
    dept = tbl_dept.objects.get(id=id)
    if request.method == "POST":
        dept.dept_name = request.POST.get("txtdepartment")
        dept.save()
        return redirect("WebAdmin:department")
    else:
        return render(request,"WebAdmin/Department.html",{"edit":dept})
    

#
def AcademicYear(request):
      data = tbl_acdemicyear.objects.all()
      if request.method=="POST":
        dept=request.POST.get("txtAcademicYear")
        tbl_acdemicyear.objects.create(acdemic_year=dept)
        return redirect("WebAdmin:AcademicYear")
      else:
        return render (request,"WebAdmin/AcademicYear.html",{"data":data}) 

def delAcademicYear(request,id):  
    tbl_acdemicyear.objects.get(id=id).delete()
    return redirect("WebAdmin:AcademicYear")

def editAcademicYear(request,id):
    data = tbl_acdemicyear.objects.get(id=id)
    if request.method == "POST":
        data.acdemic_year = request.POST.get("txtAcademicYear")
        data.save()
        return redirect("WebAdmin:AcademicYear")
    else:
        return render(request,"WebAdmin/AcademicYear.html",{"edit":data})
    
#Views for category
def category(request):
     category= tbl_category.objects.all()
     if request.method=="POST":
        category=request.POST.get("txtcategory")
        tbl_category.objects.create(category_name=category)
        return redirect("WebAdmin:category")
     else:
        return render (request,"WebAdmin/category.html",{"category":category})

def delete_category(request,did):
    tbl_category.objects.get(id=did).delete()
    return redirect("WebAdmin:category")
def edit_category(request,eid):
    editcategory=tbl_category.objects.get(id=eid)
    if request.method=="POST":
        editcategory.category_name=request.POST.get("txtcategory")
        editcategory.save()
        return redirect("WebAdmin:category")
    else:
        return render(request,"WebAdmin/category.html",{"editcategory":editcategory})
    

#Subcategory
def Subcategory(request):
     cat= tbl_category.objects.all()
     sub_cat=tbl_subcategory.objects.all()
     if request.method=="POST":
        sub_cat=request.POST.get("txtsubcategory")
        cate= tbl_category.objects.get(id=request.POST.get("sel_category"))
        tbl_subcategory.objects.create(subcategory_name=sub_cat,category=cate)
        return redirect ("WebAdmin:Subcategory")
     else:
        return render (request,"WebAdmin/Subcategory.html",{"category":cat,"subcategory":sub_cat})
     
def delete_subcategory(request,id):
    tbl_subcategory.objects.get(id=id).delete()
    return redirect("WebAdmin:Subcategory")
def edit_subcategory(request,id):
    cat=tbl_category.objects.all()
    editsubcat=tbl_subcategory.objects.get(id=id)
    if request.method=="POST":
      editsubcat.subcategory_name=request.POST.get("txtsubcategory")
      cat=tbl_subcategory.objects.get(id=request.POST.get("sel_category"))
      editsubcat.category=cat
      editsubcat.save()
      return redirect("WebAdmin:Subcategory")
    else:
        return render(request,"WebAdmin/Subcategory.html",{"cat":cat,"subcat":editsubcat})   
    
def ajaxcategory(request):
    cat= tbl_category.objects.get(id=request.GET.get("did"))
    subcat= tbl_subcategory.objects.filter(category=cat)
    return render(request,"WebAdmin/ajaxcategory.html",{"subcat":subcat})



def semesterInsertSelect(request):
    sem = tbl_sem.objects.all()
    if request.method == "POST":
        sem= request.POST.get("txtsem")
        tbl_sem.objects.create(sem_no=sem)
        return redirect("WebAdmin:semesterInsertSelect")
    else:
        return render(request, "WebAdmin/Semester.html", {"semester": sem})
    
def delete_sem(request,id):
    tbl_sem.objects.get(id=id).delete()
    return redirect("WebAdmin:semesterInsertSelect")

def edit_sem(request,id):
    semedit=tbl_sem.objects.get(id=id)
    if request.method=="POST":
        semedit.sem_no=request.POST.get("txtsem")
        semedit.save()
        return redirect("WebAdmin:semesterInsertSelect")
    else:
        return render(request,"WebAdmin/Semester.html",{"semedit":semedit})
    

#


def courserInsertSelect(request):
    dept = tbl_dept.objects.all()
    course=tbl_course.objects.all()
    if request.method=="POST":
        courseName=request.POST.get("txtcourse")
        dept = tbl_dept.objects.get(id=request.POST.get("selDept"))
        tbl_course.objects.create(course_name=courseName,dept=dept)
        return redirect("WebAdmin:courserInsertSelect")
    else:
        return render (request,"WebAdmin/Course.html",{"dept":dept,"data":course})
    

def delCourse(request,id):
    tbl_course.objects.get(id=id).delete()
    return redirect("WebAdmin:courserInsertSelect")




#Student list view,accept,reject
def studentListNew(request):
    userdata = tbl_student.objects.filter(student_status=0)
    return render(request,"WebAdmin/StudentListNew.html",{"userdata":userdata})

def acceptstudent(request,aid):
    user = tbl_student.objects.get(id=aid)
    user.student_status = 1
    user.save()
    return redirect("WebAdmin:HomePage")

def rejectstudent(request,rid):
    user = tbl_student.objects.get(id=rid)
    user.student_status = 2
    user.save()
    return redirect("WebAdmin:HomePage")

def StudentListAccepted(request):
    userdata = tbl_student.objects.filter(student_status=1)
    return render(request,"WebAdmin/StudentAcceptedList.html",{"userdata":userdata})

def studentListRejected(request):
    userdata = tbl_student.objects.filter(student_status=2)
    return render(request,"WebAdmin/StudentRejectedList.html",{"userdata":userdata})



def CoOrdinatorRegistration(request):
    if request.method=="POST":
        tbl_coordinator.objects.create(coordinator_address=request.POST.get("txtadd"),coordinator_name=request.POST.get("txtname"),coordinator_gender=request.POST.get("gender"),coordinator_contact=request.POST.get("txtcontact"),coordinator_email=request.POST.get("txtemail"),coordinator_photo=request.FILES.get("fileImage"),coordinator_proof=request.FILES.get("fileProof"),coordinator_password=request.POST.get("txtpwd"))
        return redirect("WebAdmin:CoOrdinatorRegistration")
    else:
        return render(request,"WebAdmin/CoOrdinatorRegistration.html")
    



def CordinatorListNew(request):
    userdata = tbl_coordinator.objects.filter(coordinator_status=0)
    return render(request,"WebAdmin/CoordinatorListNew.html",{"userdata":userdata})

def acceptcordinator(request,aid):
    user = tbl_coordinator.objects.get(id=aid)
    user.coordinator_status = 1
    user.save()
    return redirect("WebAdmin:HomePage")

def rejectcordinator(request,rid):
    user = tbl_coordinator.objects.get(id=rid)
    user.coordinator_status = 2
    user.save()
    return redirect("WebAdmin:HomePage")

def CordinatorListAccepted(request):
    userdata = tbl_coordinator.objects.filter(coordinator_status=1)
    return render(request,"WebAdmin/CoordinatorListAccepted.html",{"userdata":userdata})

def CordinatorListRejected(request):
    userdata = tbl_coordinator.objects.filter(coordinator_status=2)
    return render(request,"WebAdmin/CoordinatorListRejected.html",{"userdata":userdata})


def Adminregistration(request):
    admin=tbl_adminreg.objects.all
    if request.method=="POST":
        admin_name=request.POST.get("txtname")
        admin_contact=request.POST.get("txtcontact")
        admin_email=request.POST.get("txtemail")
        admin_password=request.POST.get("txtpass")
        tbl_adminreg.objects.create(a_name=admin_name,a_contact=admin_contact,a_email=admin_email,a_password=admin_password)
        
        return redirect("WebAdmin:Adminregistration")
    else:
        return render (request,"WebAdmin/AdminRegistration.html",{"adminregdata":admin})
def delete_admin(request,id):
  tbl_adminreg.objects.get(id=id).delete()
  return redirect("WebAdmin:Adminregistration") 
 
def edit_admin(request,id):
    adminedit=tbl_adminreg.objects.get(id=id)
    if request.method=="POST":
        adminedit.a_name=request.POST.get("txtname")
        adminedit.a_contact=request.POST.get("txtcontact")
        adminedit.a_email=request.POST.get("txtemail")
        adminedit.a_password=request.POST.get("txtpass")
        adminedit.save()
        return redirect("WebAdmin:Adminregistration")
    else:
        return render (request,"WebAdmin/AdminRegistration.html",{"adminedit":adminedit})
    

#admin views
def admin(request):
    if request.method == "POST":
        return render(request, "WebAdmin/admin.html")
    else:
        return render(request, "WebAdmin/admin.html")\
        

def eventInsertSelect(request):
    data=tbl_newevent.objects.all()
    category=tbl_category.objects.all()
    subcategory=tbl_subcategory.objects.all()
    coordinator=tbl_coordinator.objects.all()
    if request.method=="POST":
        print(request.POST.get("subcategory"))
        eventname=request.POST.get("txteventname")
        gender=request.POST.get("gender")
        category=tbl_category.objects.get(id=request.POST.get("category"))
        subcategorydata=tbl_subcategory.objects.get(id=request.POST.get("subcategory"))
        date=request.POST.get("txtdate")
        time=request.POST.get("txttime")
        details=request.POST.get("txtdetails")
        venue=request.POST.get("txtvenue")  
        poster=request.FILES.get("fileImage")
        type=request.POST.get("type")
        teammatecount=request.POST.get("count")  
        venue=request.POST.get("txtvenue") 
        coordinator=tbl_coordinator.objects.get(id=request.POST.get("coordinator"))  
        tbl_newevent.objects.create(e_name=eventname,e_gender=gender,category=category,subcategory=subcategorydata,e_date=date,e_time=time,e_details=details,e_venue=venue,e_poster=poster,type_name=type,teammate_count=teammatecount,coordinator=coordinator)
        return render(request,"WebAdmin/NewEvent.html",{'data':data})
    else:
        return render(request,"WebAdmin/NewEvent.html",{'data':data,'category':category,'subcategory':subcategory,'coordinator':coordinator})
    
def eventdelete(request, id):
     tbl_newevent.objects.get(id=id).delete()     
     return redirect("WebAdmin:NewEvent")   
def ComplaintReply(request,cid):
    complaint = tbl_complaint.objects.get(id=cid)
    if request.method=="POST":
        complaint.complaint_replydate = date.today()
        complaint.complaint_reply=request.POST.get('txtreply')
        complaint.complaint_status=1
        complaint.save()
        return redirect("WebAdmin:ComplaintReply")
    else:
        return render(request,"WebAdmin/ComplaintReply.html",{'complaint':complaint})
    
def complaintview(request):
    data=tbl_complaint.objects.filter(complaint_status=0)
    return render(request,"WebAdmin/ComplaintView.html",{'data':data})



def Notifications(request):
    notify = Notification.objects.all()
    if request.method == "POST":
        notify = request.POST.get("txtnotification")
        Notification.objects.create(content=notify) 
        # Do something with notify_text, like saving it to the database
        return redirect("WebAdmin:Notifications")
    else:
        return render(request, "WebAdmin/Notification.html", {'notify': notify})
def delete_Notifications(request,id):  
    Notification.objects.get(id=id).delete()
    return redirect("WebAdmin:Notifications")

def logout(request):
    del request.session["aid"]
    return redirect("Guest:Login")

def ViewAllResults(request,id):
    result=tbl_results.objects.filter(department_id=id)
    return render(request,"WebAdmin/ViewAllResults.html",{'result':result})

def deptresults(request):
    new=tbl_dept.objects.all()
    data = []
    for i in new:
        data.append({"dept":i,"total":getTotal(i.id)})
       
        data_sorted = sorted(data, key=lambda x: x['total'], reverse=True)
    
    return render(request, "WebAdmin/DepartmentTotal.html", {'new': data_sorted})
def getTotal(id):
    data = tbl_results.objects.filter(department=id,result_status=1)
    total = 0
    for i in data:
        total = total + int(i.result_score)
    return total

def Publishresults(request):
    user = tbl_results.objects.all()
    data = []
    for result in user:
     result.result_status = 1
     result.save()   
    return redirect("WebAdmin:HomePage")

def feedbackSelect(request):
    data=tbl_feedback.objects.all()
    return render(request,"WebAdmin/ViewFeedbacklList.html",{'data':data})

def feedbackDelete(request,did):
    tbl_feedback.objects.get(id=did).delete()
    return redirect("WebAdmin:ViewFeedbacklList")


def PieReport(request):
    participant = tbl_newevent.objects.all()  
    data = []
    for jid in participant :
        total_quantity = tbl_participants.objects.filter(event_id=jid).count()
        data.append({'label': jid.e_name, 'value': total_quantity})
    return render(request, "WebAdmin/Report.html",{'data':data})
