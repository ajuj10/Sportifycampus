from django.shortcuts import render,redirect
from Student.models import *
from WebGuest.models import *
from WebAdmin.models import *
from WebCoordinator.models import*
from datetime import date
# Create your views here.
#def homepage(request):
# return render(request,"Student/myprofile.html")

def my_pro(request):
    print(request.session["uid"])
    data=tbl_student.objects.get(id=request.session["uid"])
    return render(request,"Student/myprofile.html",{'data':data})

def editprofile(request):
    userdata=tbl_student.objects.get(id=request.session["uid"])
    if request.method=="POST":
     userdata.student_name=request.POST.get('txtname')
     userdata.student_contact=request.POST.get('txtcontact')
     userdata.student_email=request.POST.get('txtemail')
     userdata.save()
     return render(request,"Student/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"Student/EditProfile.html",{'userdata':userdata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_student.objects.filter(id=request.session["uid"],student_password=request.POST.get('txtcurpass')).count()
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
    
#Students can view  team and solo events seperately using these
'''def ViewsoloEvents(request):
    data=tbl_newsoloevent.objects.all()
    return render(request,"Student/ViewsoloEvents.html",{'data':data})

def ViewteamEvents(request):
    data=tbl_newteamevent.objects.all()
    return render(request,"Student/ViewteamEvents.html",{'data':data})'''


def ViewsoloEvents(request):
    solo_events = tbl_newevent.objects.filter(type_name='Solo')
    return render(request, "Student/ViewsoloEvents.html", {'data': solo_events})

def ViewteamEvents(request):
    team_events = tbl_newevent.objects.filter(type_name='Team')
    return render(request, "Student/ViewteamEvents.html", {'data': team_events})


#Add complaints
def Complaint(request):
    data=tbl_complaint.objects.filter(student=request.session["uid"])
    studentID=tbl_student.objects.get(id=request.session["uid"])
    if request.method=="POST":
        title=request.POST.get('txttitle')
        details=request.POST.get('txtcomplaint')
        tbl_complaint.objects.create(complaint_title=title,complaint_details=details,student=studentID)
        return redirect("Student:Complaint")
    else:
        return render(request,"Student/Complaint.html",{"data":data})

def ComplaintReply(request,cid):
    complaint = tbl_complaint.objects.get(id=cid)
    if request.method=="POST":
        complaint.complaint_replydate = date.today()
        complaint.complaint_reply=request.POST.get('txtreply')
        complaint.complaint_status=1
        complaint.save()
        return redirect("Administrator:complaintview")
    else:
        return render(request,"Administrator/replycomplaints.html",{'complaint':complaint})
#feedback
def feedbackInsert(request):
    if request.method=="POST":
        Subject=request.POST.get('txttitle')
        Content=request.POST.get('txtdetails')
        User=tbl_student.objects.get(id=request.session["uid"])
        tbl_feedback.objects.create(feedback_subject=Subject,feedback_details=Content,student=User)
        return render(request,"Student/feedback.html")
    else:
        return render(request,"Student/feedback.html")

# def paricipateEvent():
#     data=tbl_newevent.objects.get(id=request.session["uid"])
#     return render("Student/participateEvent.html",{'data':data})
    
'''def ApplysoloEvent(request,id):
    event = tbl_newsoloevent.objects.get(id=id)
    student = tbl_student.objects.get(id=request.session["uid"])
    tbl_participants.objects.create(soloevent_id=event, student_id=student) 
    return render(request, "Student/ViewsoloEvents.html", {'msg': "Application success"})

def ApplyteamEvent(request, id):
     event = tbl_newteamevent.objects.get(id=id)
     student = tbl_student.objects.get(id=request.session["uid"])
     data = tbl_participants.objects.create(teamevent_id=event, student_id=student)
     return redirect("Student:addteammates",data.id)'''


def ApplyEvent(request, id):
    event = tbl_newevent.objects.get(id=id)  # Assuming tbl_newevent contains both solo and team events
    event1=tbl_newevent.objects.filter(type_name="Solo")
    arr = []
    for i in event1:
        arr.append(i.id)
    print(arr)
    student = tbl_student.objects.get(id=request.session["uid"])
    participant=tbl_participants.objects.filter(event_id__in=arr,student_id=student).count()
    if participant>3:
         return render(request, "Student/ViewsoloEvents.html", {'msg': "You applied for 3 events already"})
    else:
        count = tbl_participants.objects.filter(event_id=event, student_id=student).count()
        if count > 0:
            return render(request, "Student/ViewsoloEvents.html", {'msg': "Already Applied"})
        else:
            if event.type_name == 'Solo':
                tbl_participants.objects.create(event_id=event, student_id=student) 
                return render(request, "Student/ViewsoloEvents.html", {'msg': "Application success"})
            elif event.type_name == 'Team':
                data = tbl_participants.objects.create(event_id=event, student_id=student)
                return redirect("Student:addteammates", data.id)
            else: return render(request, "Student/VIewteamevents.html", {'msg': "Application success"})
            
def Addteammates(request,id):
    participant=tbl_participants.objects.get(id=id)
    event_id=tbl_newevent.objects.get(id=participant.event_id.id)
    team_mate_count = event_id.teammate_count
    teammates=tbl_teammates.objects.filter(participant_id=id).count()
    print(team_mate_count,teammates)
    #student= tbl_student.objects.get(id=id)
    if request.method=="POST":
       if int(team_mate_count)<=teammates:
           return render(request, "Student/addteammates.html", {'msg': "limit exceeded"})
       else:  
           teammates=request.POST.get("txtteammate")
           tbl_teammates.objects.create(participant_id=participant,teammate_name=teammates)
           return render (request,"Student/addteammates.html")
    else:
        return render (request,"Student/addteammates.html")
    
def view_results(request):
    # Retrieve all existing result data from your model
    results = tbl_results.objects.filter(result_status=1)
    return render(request, "Student/ViewResults.html", {'results': results})

    
def ViewAllResults(request,id):
    result=tbl_results.objects.filter(department_id=id)
    return render(request,"WebAdmin/ViewAllResults.html",{'result':result})

def ViewRules(request):
    event=tbl_newevent.objects.all()
    return render(request,"Student/ViewRules.html",{'event':event})

def logout(request):
    if 'uid' in request.session:
        del request.session['uid']
        return redirect('WebGuest:index')
    else:
        return redirect('WebGuest:index')
    

def search_events(request):
    if request.method == 'GET':
        query = request.GET.get('q')

        if query:
            events = tbl_newevent.objects.filter(e_details__icontains=query)
        else:
            events = tbl_newevent.objects.all()

        return render(request, 'Student/EventSearch.html', {'events': events})
    else:
        return render(request, 'Student/EventSearch.html')
    
def deptresults(request):
    new=tbl_dept.objects.all()
    data = []
    for i in new:
        data.append({"dept":i,"total":getTotal(i.id)})
       
        data_sorted = sorted(data, key=lambda x: x['total'], reverse=True)
    
    return render(request, "Student/ViewDepartmentResults.html", {'new': data_sorted})

def getTotal(id):
    data = tbl_results.objects.filter(department=id,result_status=1)
    total = 0
    for i in data:
        total = total + int(i.result_score)
    return total