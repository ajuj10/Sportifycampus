from django.urls import path,include
from WebCoordinator import views
#from Administrator.views import admin
app_name = "WebCoordinator"

urlpatterns=[ 


path('HomePage/',views.LoadingHomePage,name="HomePage"),

path('myprofile/',views.coordinator_profile,name="myprofile"),
path('editprofile/',views.editprofile,name="editprofile"),
path('changepassword/',views.Coordinatorchangepassword,name="changepassword"),


path('participantListNew/',views.participantListNew,name="participantListNew"),
path('teammateListNew/<int:id>',views.teammateListNew,name="teammateListNew"),
path('acceptparticipant/<int:aid>',views.acceptparticipant,name="acceptparticipant"),
path('rejectparticipant/<int:rid>',views.rejectparticipant,name="rejectparticipant"),
path('ParticipantListAccepted/',views.ParticipantListAccepted,name="ParticipantListAccepted"),
path('ParticipantListRejected/',views.ParticipantListRejected,name="ParticipantListRejected"),

path('Addteamresults/',views.AddteamResults,name="Addteamresults"),
path('Addsoloresults/',views.AddsoloResults,name="Addsoloresults"),
path('ajaxstudent/',views.ajaxstudent,name="ajaxstudent"),

path('ViewDepartmentwiseResults/',views.deptresults,name="ViewDepartmentwiseResults"),
path('ViewAllresults/<int:id>',views.ViewAllresults,name="ViewAllresults"),


path('myevent/',views.myevent,name="myevent"),
]