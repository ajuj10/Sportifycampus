from django.shortcuts import render,redirect,get_object_or_404

from WebCoordinator.models import *
from WebAdmin.models import *
from django.http import JsonResponse
from Student.models import*
# Create your views here.

def LoadingHomePage(request):
    return render (request,"WebCoordinator/HomePage.html")


def coordinator_profile(request):
    data=tbl_coordinator.objects.get(id=request.session["cid"])
    return render(request,"WebCoordinator/MyProfile.html",{'data':data})

def editprofile(request):
    coordinator_data=tbl_coordinator.objects.get(id=request.session["cid"])
    if request.method=="POST":
     coordinator_data.coordinator_name=request.POST.get('txtname')
     coordinator_data.coordinator_contact=request.POST.get('txtcontact')
     coordinator_data.coordinator_email=request.POST.get('txtemail')
     coordinator_data.save()
     return render(request,"WebCoordinator/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"WebCoordinator/EditProfile.html",{'coordinator_data':coordinator_data})

def Coordinatorchangepassword(request):
    if request.method=="POST":
        ccount=tbl_coordinator.objects.filter(id=request.session["cid"],user_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                coordinator_data=tbl_coordinator.objects.get(id=request.session.get["cid"],coordinator_password=request.POST.get('txtcurpass'))
                coordinator_data.coordinator_password=request.POST.get('txtnewpass')
                coordinator_data.save()
                return render(request,"WebCoordinator/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"WebCoordinator/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"WebCoordinator/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"WebCoordinator/ChangePassword.html")
    
def participantListNew(request):
    userdata = tbl_participants.objects.filter(participant_status=0,event_id__type_name='Team',event_id__coordinator=request.session["cid"])
    data= tbl_participants.objects.filter(participant_status=0,event_id__type_name='Solo',event_id__coordinator=request.session["cid"])
    return render(request,"WebCoordinator/participantListNew.html",{"userdata":userdata,"data":data})

def teammateListNew(request,id):
    userdata = tbl_teammates.objects.filter(participant_id=id)
    return render(request,"WebCoordinator/Viewteammates.html",{"userdata":userdata})


def acceptparticipant(request,aid):
    user = tbl_participants.objects.get(id=aid)
    user.participant_status = 1
    user.save()
    return redirect("WebCoordinator:HomePage")

def rejectparticipant(request,rid):
    user = tbl_participants.objects.get(id=rid)
    user.student_status = 2
    user.save()
    return redirect("WebCoordinator:HomePage")

def ParticipantListAccepted(request):
    userdata = tbl_participants.objects.filter(participant_status=1,event_id__type_name='Solo',event_id__coordinator=request.session["cid"])
    team = tbl_participants.objects.filter(participant_status=1,event_id__type_name='Team',event_id__coordinator=request.session["cid"])
    # print(userdata)
    return render(request,"WebCoordinator/ParticipantListAccepted.html",{"userdata":userdata,"team":team})

def ParticipantListRejected(request):
    userdata = tbl_participants.objects.filter(participant_status=2,event_id__type_name='Solo',event_id__coordinator=request.session["cid"])
    team = tbl_participants.objects.filter(participant_status=1,event_id__type_name='Team',event_id__coordinator=request.session["cid"])
    return render(request,"WebCoordinator/ParticipantListRejected.html",{"userdata":userdata,"team":team})

'''def ParticipantListRejected(request):
    userdata = tbl_participants.objects.filter(participant_status=2)
    team = tbl_participants.objects.filter(participant_status=1,event_id__type_name='Team')
    return render(request,"WebCoordinator/ParticipantListRejected.html",{"userdata":userdata,"team":team})'''

def AddteamResults(request):
     data=tbl_results.objects.filter(participant_id__participant_status=1, participant_id__event_id__type_name='Team', participant_id__event_id__coordinator=request.session["cid"]) 
     part = tbl_participants.objects.filter(participant_status=1,event_id__type_name='Team',event_id__coordinator=request.session["cid"])
     dept = tbl_dept.objects.all()
     if request.method == "POST":
         tbl_results.objects.create(participant_id=tbl_participants.objects.get(id=request.POST.get("sel_part")),
                                    department=tbl_dept.objects.get(id=request.POST.get("sel_depart")),
                                    result_score=request.POST.get("txt_score"),
                                    result_position=request.POST.get("sel_pos"))
         return render(request,"WebCoordinator/Addteamresults.html",{"msg":"Result Added"})
     else:
        return render(request,"WebCoordinator/Addteamresults.html",{'data':data,"part":part,"dept":dept})
     
def AddsoloResults(request):
    dept = tbl_dept.objects.all()
    part = tbl_participants.objects.filter(participant_status=1, event_id__type_name='Solo', event_id__coordinator=request.session["cid"])
    data = tbl_results.objects.filter(participant_id__participant_status=1, participant_id__event_id__type_name='Solo', participant_id__event_id__coordinator=request.session["cid"])
        
    if request.method == "POST":
        tbl_results.objects.create(
            participant_id=tbl_participants.objects.get(id=request.POST.get("sel_part")),
            department=tbl_dept.objects.get(id=request.POST.get("sel_depart")),
            result_score=request.POST.get("txt_score"),
            result_position=request.POST.get("sel_pos"),
        )
        return render(request, "WebCoordinator/Addsoloresults.html", {"msg": "Result Added"})
    else:
        return render(request, "WebCoordinator/Addsoloresults.html", {'data': data, "part": part, "dept": dept})
    

def deptresults(request):
    new=tbl_dept.objects.all()
    data = []
    for i in new:
        data.append({"dept":i,"total":getTotal(i.id)})
       
        data_sorted = sorted(data, key=lambda x: x['total'], reverse=True)
    
    return render(request, "WebCoordinator/ViewDepartmentwiseResults.html", {'new': data_sorted})

def getTotal(id):
    data = tbl_results.objects.filter(department=id)
    total = 0
    for i in data:
        total = total + int(i.result_score)
    return total

def ViewAllresults(request,id):
    result=tbl_results.objects.filter(department_id=id)
    return render(request,"WebCoordinator/ViewAllresults.html",{'result':result})

def ajaxstudent(request):
    par = tbl_participants.objects.get(id=request.GET.get("pid"))
    stu = tbl_student.objects.get(id=par.student_id.id)
    course = tbl_course.objects.get(id=stu.course.id)
    dept = tbl_dept.objects.get(id=course.dept.id)
    return JsonResponse({"dept":dept.dept_name,"id":dept.id})

def myevent(request):
    userdata = tbl_participants.objects.filter(participant_status=0,event_id__type_name='Team',event_id__coordinator=request.session["cid"])
    data= tbl_participants.objects.filter(participant_status=0,event_id__type_name='Solo',event_id__coordinator=request.session["cid"])
    return render(request,"WebCoordinator/myevent.html",{"userdata":userdata,"data":data})
