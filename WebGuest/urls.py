from django.urls import path,include
from WebGuest import views

#from Administrator.views import admin

app_name = "WebGuest"

urlpatterns = [

path('Login/',views.Login,name="Login"),
path('index/',views.index,name="index"),

path('StudentRegistration/',views.StudentRegistration,name="StudentRegistration"),
path('AjaxCourse/',views.ajaxcourse,name="ajaxcourse"),
path('Notification/',views.notification_view,name="Notification"),

  path('ForgotPass/', views.ForgotPass,name="ForgotPass"),
  path('ValidateOTP/', views.ValidateOTP,name="ValidateOTP"),
  path('CreatePass/', views.CreatePass,name="CreatePass"),   
]
