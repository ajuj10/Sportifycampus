from django.urls import path,include
from Guest import *
from Student import views
app_name = "Student"

urlpatterns = [

   # path('Homepage/',views.homepage,name="Homepage"),
    path('myprofile/',views.my_pro,name="myprofile"),
    path('Editprofile/',views.editprofile,name="Editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),
    path('ViewsoloEvents/',views.ViewsoloEvents,name="ViewsoloEvents"),
    path('ViewteamEvents/',views.ViewteamEvents,name="ViewteamEvents"),
    path('logout/',views.logout,name="logout"),
 #Complaint 

     path('Complaint/',views.Complaint,name="Complaint"),
     path('feedback/',views.feedbackInsert,name="feedback"),

     path('ApplyEvent/<int:id>', views.ApplyEvent, name='ApplyEvent'),
     path('addteammates/<int:id>', views.Addteammates, name='addteammates'),
    
     path('EventSearch/', views.search_events, name='EventSearch'),

     path('ViewDepartmentResults/', views.deptresults, name='ViewDepartmentResults'),
     path('ViewAllResults/<int:id>', views.ViewAllResults, name='ViewAllResults'),
     path('ViewRules/', views.ViewRules, name='ViewRules'),
     path('ViewResults/', views.view_results, name='ViewResults'),
]


