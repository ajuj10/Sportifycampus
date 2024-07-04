from django.urls import path,include
from Course import views

#from Administrator.views import admin

app_name = "Course"

urlpatterns = [

path('ViewCourses/',views.ViewCourses,name="ViewCourses"), 
path('Viewselected/<int:id>',views.view_selected,name="Viewselected"),
path('Register/<int:id>',views.Apply,name="Register"), 
path('bookNow/<int:id>',views.Booknow,name="bookNow"), 
path('emailforotp',views.emailforotp,name="emailforotp"),
path('Validateotp',views.otpvalidate,name="Validateotp"),
path('payment',views.payment,name="payment"),  
path('viewbill/',views.ViewBill,name="viewbill"),   
]
