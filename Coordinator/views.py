from django.shortcuts import render,redirect,get_object_or_404

from Coordinator.models import *
from Administrator.models import *
# Create your views here.

def LoadingHomePage(request):
    return render (request,"Coordinator/HomePage.html")

def NewsoloeventInsertSelect(request):
    data=tbl_newsoloevent.objects.all()
    category=tbl_category.objects.all()
    subcategory=tbl_subcategory.objects.all()
    if request.method=="POST":
        gender=request.POST.get(("txtgender"))
        category=tbl_category.objects.get(id=request.POST.get("category"))
        subcategory=tbl_subcategory.objects.get(id=request.POST.get("subcategory"))
        date=request.POST.get("txtdate")
        time=request.POST.get("txttime")
        details=request.POST.get("txtdetails")
        venue=request.POST.get("txtvenue")  
        tbl_newsoloevent.objects.create(e_gender=gender,category=category,subcategory=subcategory,e_date=date,e_time=time,e_details=details,e_venue=venue)
        return render(request,"Coordinator/NewsoloEvent.html",{'data':data})
    else:
        return render(request,"Coordinator/NewsoloEvent.html",{'data':data,'type':type,'category':category,'subcategory':subcategory})
    
def edit_event(request, id):
    event = tbl_newsoloevent.objects.get(id=request.session["uid"])
    if request.method == 'POST':
        # Update the event with the submitted data
        event.type = request.POST.get('type')
        event.gender = request.POST.get('txtgender')
        event.category = request.POST.get('category')
        event.subcategory = request.POST.get('subcategory')
        event.date = request.POST.get('txtdate')
        event.time = request.POST.get('txttime')
        event.details = request.POST.get('txtdetails')
        event.venue = request.POST.get('txtvenue')
        event.save()
        return redirect('HomePage')  # Redirect to the home page or wherever you want

    return render(request, 'Editevent.html', {'event': event})

def NewteameventInsertSelect(request):
    data=tbl_newteamevent.objects.all()
    category=tbl_category.objects.all()
    subcategory=tbl_subcategory.objects.all()
    if request.method=="POST":
        gender=request.POST.get(("txtgender"))
        category=tbl_category.objects.get(id=request.POST.get("category"))
        subcategory=tbl_subcategory.objects.get(id=request.POST.get("subcategory"))
        date=request.POST.get("txtdate")
        time=request.POST.get("txttime")
        details=request.POST.get("txtdetails")
        venue=request.POST.get("txtvenue")  
        tbl_newteamevent.objects.create(e_gender=gender,category=category,subcategory=subcategory,e_date=date,e_time=time,e_details=details,e_venue=venue)
        return render(request,"Coordinator/NewteamEvent.html",{'data':data})
    else:
        return render(request,"Coordinator/NewteamEvent.html",{'data':data,'type':type,'category':category,'subcategory':subcategory})
    
def edit_event(request, id):
    event = tbl_newteamevent.objects.get(id=request.session["uid"])
    if request.method == 'POST':
        # Update the event with the submitted data
        event.gender = request.POST.get('txtgender')
        event.category = request.POST.get('category')
        event.subcategory = request.POST.get('subcategory')
        event.date = request.POST.get('txtdate')
        event.time = request.POST.get('txttime')
        event.details = request.POST.get('txtdetails')
        event.venue = request.POST.get('txtvenue')
        event.save()
        return redirect('Coordinator:Editevent')  # Redirect to the home page or wherever you want

    return render(request, 'Editevent.html', {'event': event})





    
def ajaxcategory(request):
    cat= tbl_category.objects.get(id=request.GET.get("did"))
    subcat= tbl_subcategory.objects.filter(category=cat)
    return render(request,"Coordinator/ajaxcategory.html",{"subcat":subcat})

def coordinator_profile(request):
    data=tbl_coordinator.objects.get(id=request.session["cid"])
    return render(request,"Coordinator/myprofile.html",{'data':data})

def editprofile(request):
    coordinator_data=tbl_coordinator.objects.get(id=request.session["cid"])
    if request.method=="POST":
     coordinator_data.coordinator_name=request.POST.get('txtname')
     coordinator_data.coordinator_contact=request.POST.get('txtcontact')
     coordinator_data.coordinator_email=request.POST.get('txtemail')
     coordinator_data.save()
     return render(request,"Coordinator/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"Coordinator/EditProfile.html",{'coordinator_data':coordinator_data})

def Coordinatorchangepassword(request):
    if request.method=="POST":
        ccount=tbl_coordinator.objects.filter(id=request.session["cid"],user_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                coordinator_data=tbl_coordinator.objects.get(id=request.session.get["cid"],coordinator_password=request.POST.get('txtcurpass'))
                coordinator_data.coordinator_password=request.POST.get('txtnewpass')
                coordinator_data.save()
                return render(request,"Coordinator/coordinatorchangepassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"Coordinator/coordinatorchangepassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"Coordinator/coordinatorchangepassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"Coordinator/coordinatorchangepassword.html")
