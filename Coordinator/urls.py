from django.urls import path,include
from Coordinator import views
#from Administrator.views import admin
app_name = "Coordinator"

urlpatterns=[ 


path('HomePage/',views.LoadingHomePage,name="LoadingHomePage"),


path('ajaxcategory/',views.ajaxcategory,name="ajaxcategory"),
path('Editevent/<int:id>/',views.edit_event,name="Editevent"),

path('NewsoloEvent/',views.NewsoloeventInsertSelect,name="NewsoloEvent"),
path('NewteamEvent/',views.NewteameventInsertSelect,name="NewteamEvent"),
path('myprofile/',views.coordinator_profile,name="myprofile"),
path('editprofile/',views.editprofile,name="editprofile"),
path('changepassword/',views.Coordinatorchangepassword,name="changepassword"),


path('ViewDepartmentwiseResults/',views.Coordinatorchangepassword,name="ViewDepartmentwiseResults"),

]